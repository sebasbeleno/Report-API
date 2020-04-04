"""
    Testea todos los metodos
    relacionados con el invocador.
"""
import unittest
import sys
from modules import summoner
from .constants import SUMMONER_NAME

sys.path.append('../')

class TestSummoner(unittest.TestCase):
    """
        Esta clase testa que la obtención de datos generales
        del invocador sea cottecta.
    """
    def test_get_summoner_info(self):
        """
            Esta función testa que la obtención de datos
            básicos de un invocador sea correcta.
        """
        summoner_result =  summoner.call_api_summoner(name=SUMMONER_NAME, region="LAN")
        self.assertIsNotNone(summoner_result.id)
        self.assertIsNotNone(summoner_result.level)
        self.assertIsNotNone(summoner_result.account_id)
        self.assertIsNotNone(summoner_result.match_history)
        self.assertIsNotNone(summoner_result.ranks)
        self.assertIsNotNone(summoner_result.level)
        self.assertIsNotNone(summoner_result.name)


if __name__ == "__main__":
    unittest.main()
