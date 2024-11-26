from pathlib import Path
import importlib
import json
from datetime import datetime
from typing import Dict, Any, List


class SpiderManager:
    def __init__(self):
        self.data_dir = Path("data")
        self.data_dir.mkdir(exist_ok=True)

    def run_spider(self, spider_name: str) -> Dict[str, Any]:
        try:
            spider_module = importlib.import_module(f'spiders.{spider_name}_spider')
            spider_class = getattr(spider_module, f'IccSpider')

            spider = spider_class()
            raw_data = spider.run()

            # Formater les données dans la structure attendue
            formatted_data = {
                "metadata": {
                    "version": "1.0",
                    "source": spider_name.upper(),
                    "date_collected": datetime.now().isoformat(),
                    "total_entries": len(raw_data)
                },
                "training_examples": raw_data
            }

            # Sauvegarder les données
            self.save_data(spider_name, formatted_data)

            return formatted_data

        except Exception as e:
            print(f"Erreur lors de l'exécution du spider {spider_name}: {e}")
            return {"metadata": {}, "training_examples": []}

    def save_data(self, spider_name: str, data: Dict[str, Any]):
        output_file = self.data_dir / f"{spider_name}_{datetime.now().strftime('%Y%m%d')}.json"

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Données sauvegardées dans: {output_file}")

    def analyze_data(self, data: Dict[str, Any]):
        if not data or not data.get('training_examples'):
            print("Pas de données à analyser")
            return

        examples = data['training_examples']

        print("\nAnalyse des données:")
        print(f"Nombre total d'entrées: {len(examples)}")

        if examples and 'input' in examples[0]:
            self._analyze_case_data(examples)

    def _analyze_case_data(self, examples: List[Dict[str, Any]]):
        """
        Analyse spécifique pour les cas ICC
        """
        statuses = {}
        avg_scores = {
            "dignity": 0,
            "non_violence": 0,
            "truth": 0,
            "justice": 0,
            "common_good": 0
        }
        total_cases = len(examples)

        for case in examples:
            # Compter les statuts
            if 'input' in case and 'status' in case['input']:
                status = case['input']['status']
                statuses[status] = statuses.get(status, 0) + 1

            # Calculer les moyennes des scores
            if 'labels' in case and 'scores' in case['labels']:
                for key, value in case['labels']['scores'].items():
                    avg_scores[key] += value

        # Calculer les moyennes finales
        if total_cases > 0:
            for key in avg_scores:
                avg_scores[key] = round(avg_scores[key] / total_cases, 2)

        print("\nDistribution des statuts:")
        for status, count in statuses.items():
            print(f"- {status}: {count}")

        print("\nScores moyens d'humanité:")
        for key, value in avg_scores.items():
            print(f"- {key}: {value}")


def main():
    manager = SpiderManager()

    # Liste des spiders à exécuter
    spiders = ['icc']  # Ajouter d'autres spiders ici

    for spider_name in spiders:
        print(f"\nExécution du spider: {spider_name}")
        data = manager.run_spider(spider_name)
        manager.analyze_data(data)


if __name__ == "__main__":
    main()