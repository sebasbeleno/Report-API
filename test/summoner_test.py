"""
    Testea todos los metodos
    relacionados con el invocador.
"""
import unittest
import sys
from report import print_basic_summoner_info
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
        summoner = print_basic_summoner_info(name=SUMMONER_NAME, region="LAN")
        self.assertIsNotNone(summoner['accountId'])
        self.assertIsNotNone(summoner['level'])
        self.assertIsNotNone(summoner['ranked_flex_fives'])
        self.assertIsNotNone(summoner['ranked_solo_fives'])
        self.assertIsNotNone(summoner['uid'])


if __name__ == "__main__":
    unittest.main()
