from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime
from typing import Dict, Any, List
import time
import os


class IccSpider:
    def __init__(self):
        self.url = 'https://www.icc-cpi.int/cases'

    def setup_driver(self):
        driver_path = os.path.join(os.path.dirname(__file__), "msedgedriver.exe")
        print(f"Utilisation du driver à: {driver_path}")

        service = Service(executable_path=driver_path)
        driver = webdriver.Edge(service=service)
        return driver

    def run(self) -> List[Dict[str, Any]]:
        driver = None
        try:
            print("Initialisation du driver Edge...")
            driver = self.setup_driver()
            print("Driver Edge initialisé")

            print(f"Chargement de la page: {self.url}")
            driver.get(self.url)
            time.sleep(5)

            print("Attente des éléments...")
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "card"))
            )

            print("Page chargée, extraction du contenu...")
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            cases = self.parse(soup)
            print(f"Nombre de cas extraits: {len(cases)}")
            return cases

        except Exception as e:
            print(f"Erreur lors du scraping: {e}")
            print(f"Type d'erreur: {type(e)}")
            print(f"Message d'erreur détaillé: {str(e)}")
            if driver and driver.page_source:
                print("Contenu de la page :")
                print(driver.page_source[:500])  # Affiche les 500 premiers caractères
            return []

        finally:
            if driver:
                try:
                    driver.quit()
                    print("Driver fermé")
                except:
                    pass

    def parse(self, soup: BeautifulSoup) -> List[Dict[str, Any]]:
        cases = []
        case_divs = soup.select('div.card')
        print(f"Nombre de cas trouvés: {len(case_divs)}")

        for case_div in case_divs:
            try:
                case_data = self._extract_case_data(case_div)
                if case_data:
                    cases.append(case_data)
                    print(f"Cas extrait: {case_data['input']['name']}")
            except Exception as e:
                print(f"Erreur lors du parsing d'un cas: {e}")

        return cases

    def _extract_case_data(self, case_div: BeautifulSoup) -> Dict[str, Any]:
        name = case_div.select_one('.card-header h5 a').text.strip()
        status = case_div.select_one('.defendant_status_button').text.strip()

        details = ' '.join([
            p.text.strip()
            for p in case_div.select('.aboutDefendant p')
            if p.text.strip()
        ])

        # Calculer les scores
        initial_score = self._calculate_initial_score(status, details)

        return {
            "input": {
                "name": name,
                "text": details,
                "status": status,
                "date_collected": datetime.now().isoformat(),
                "source": {
                    "type": "judicial_record",
                    "institution": "ICC",
                    "url": self.url
                }
            },
            "labels": self._generate_humanity_scores(status, details, initial_score)
        }

    def _calculate_initial_score(self, status: str, details: str) -> int:
        status_scores = {
            "Convicted": 20,
            "In ICC custody": 30,
            "At large": 40,
            "Case closed": 50,
            "Acquitted": 70
        }
        return status_scores.get(status, 50)

    def _generate_humanity_scores(self, status: str, details: str, initial_score: int) -> Dict[str, Any]:
        scores = {
            "dignity": initial_score,
            "non_violence": initial_score,
            "truth": initial_score,
            "justice": initial_score,
            "common_good": initial_score,
        }

        # Ajustements basés sur le texte
        details_lower = details.lower()
        if "crimes against humanity" in details_lower:
            scores["dignity"] = 10
            scores["non_violence"] = 10

        if "war crimes" in details_lower:
            scores["non_violence"] = 10
            scores["common_good"] = 20

        if "voluntary appearance" in details_lower:
            scores["truth"] += 10
            scores["justice"] += 10

        return {
            "scores": scores,
            "global_score": sum(scores.values()) // 5,
            "evaluation_date": datetime.now().isoformat(),
            "confidence": "high" if "convicted" in status.lower() or "in icc custody" in status.lower() else "medium"
        }