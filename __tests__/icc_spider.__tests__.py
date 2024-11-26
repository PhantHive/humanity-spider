import unittest
from spiders.icc_spider import IccSpider


class TestIccSpiderScoring(unittest.TestCase):
    def setUp(self):
        self.spider = IccSpider()

    def test_score_calculations(self):
        test_cases = [
            {
                # Case test #1: Case with no keywords
                "name": "Convicted case",
                "status": "Convicted",
                "details": "The defendant was found guilty of basic charges.",
                "expected_scores": {
                    "dignity": 20,
                    "non_violence": 20,
                    "truth": 20,
                    "justice": 20,
                    "common_good": 20
                },
                "expected_global": 20
            },
            {
                # Case test #2: Case with crimes against humanity keyword
                "name": "Crimes against humanity case",
                "status": "Convicted",
                "details": "Found guilty of crimes against humanity including systematic attacks against civilians.",
                "expected_scores": {
                    "dignity": 10,
                    "non_violence": 10,
                    "truth": 20,
                    "justice": 20,
                    "common_good": 20
                },
                "expected_global": 16
            },
            {
                # Case test #3: with war crimes keyword
                "name": "War crimes case",
                "status": "In ICC custody",
                "details": "Accused of war crimes and destruction of cultural heritage.",
                "expected_scores": {
                    "dignity": 30,
                    "non_violence": 10,
                    "justice": 30,
                    "truth": 30,
                    "common_good": 20
                },
                "expected_global": 24
            },
            {
                # Case test #4: Case with voluntary appearance but war crimes keywords
                "name": "Voluntary surrender case",
                "status": "In ICC custody",
                "details": "The suspect made a voluntary appearance before the court after war crimes accusations.",
                "expected_scores": {
                    "dignity": 30,
                    "non_violence": 10,
                    "justice": 40,
                    "truth": 40,
                    "common_good": 20
                },
                "expected_global": 28
            },
            {
                # Case test #5: Complex case with multiple keywords (crimes against humanity, war crimes, voluntary appearance)
                "name": "Complex case",
                "status": "Convicted",
                "details": """The accused was convicted of crimes against humanity and war crimes. 
                However, they made a voluntary appearance and provided crucial testimony.
                The crimes included systematic attacks on civilians and destruction of cultural sites.""",
                "expected_scores": {
                    "dignity": 10,
                    "non_violence": 10,
                    "truth": 30,
                    "justice": 30,
                    "common_good": 20
                },
                "expected_global": 20
            },
            {
                # Case test #6: Acquitted case with no keywords
                "name": "Acquitted case",
                "status": "Acquitted",
                "details": "The defendant was acquitted of all charges after trial.",
                "expected_scores": {
                    "dignity": 70,
                    "non_violence": 70,
                    "truth": 70,
                    "justice": 70,
                    "common_good": 70
                },
                "expected_global": 70
            }
        ]

        for test_case in test_cases:
            with self.subTest(name=test_case["name"]):
                initial_score = self.spider._calculate_initial_score(
                    test_case["status"],
                    test_case["details"]
                )

                result = self.spider._generate_humanity_scores(
                    test_case["status"],
                    test_case["details"],
                    initial_score
                )

                # Check individual scores
                for score_type, expected_score in test_case["expected_scores"].items():
                    self.assertEqual(
                        result["scores"][score_type],
                        expected_score,
                        f"Score {score_type} incorrect pour {test_case['name']}"
                    )

                # Check global score
                self.assertEqual(
                    result["global_score"],
                    test_case["expected_global"],
                    f"Score global incorrect pour {test_case['name']}"
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)