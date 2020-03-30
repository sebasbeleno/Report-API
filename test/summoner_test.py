import unittest
import os

from .constants import SUMMONER_NAME

import sys

sys.path.append('../')
from report import print_basic_summoner_info


class TestSummoner(unittest.TestCase):
    def test_get_summoner_info(self):
        summoner = print_basic_summoner_info(name=SUMMONER_NAME, region="LAN")
        self.assertIsNotNone(summoner['accountId'])
        self.assertIsNotNone(summoner['level'])
        self.assertIsNotNone(summoner['ranked_flex_fives'])
        self.assertIsNotNone(summoner['ranked_solo_fives'])
        self.assertIsNotNone(summoner['uid'])


if __name__ == "__main__":
    unittest.main()