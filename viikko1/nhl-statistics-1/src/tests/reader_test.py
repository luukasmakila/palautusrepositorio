import unittest
from statistics import Statistics
from player import Player
from enum import Enum
from statistics import sort_by_assists, sort_by_goals, sort_by_points

class SortBy(Enum):
    POINTS = sort_by_points
    GOALS = sort_by_goals
    ASSISTS = sort_by_assists

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_sort_by_default(self):
        players = self.statistics.top(0)
        self.assertEqual(len(players), 1)

        for player in players:
            self.assertEqual(player.name, 'Gretzky')

    def test_top_sort_by_goals(self):
        players = self.statistics.top(0, SortBy.GOALS)
        self.assertEqual(len(players), 1)

        for player in players:
            self.assertEqual(player.name, 'Lemieux')
    
    def test_sort_by_assists(self):
        players = self.statistics.top(0, SortBy.ASSISTS)
        self.assertEqual(len(players), 1)

        for player in players:
            self.assertEqual(player.name, 'Gretzky')

    def test_team(self):
        players = self.statistics.team('EDM')
        self.assertEqual(len(players), 3)

        for player in players:
            self.assertEqual(player.team, 'EDM')
    
    def test_search(self):
        player = self.statistics.search('Semenko')
        self.assertEqual(player.name, 'Semenko')
    
    def test_player_not_found(self):
        player = self.statistics.search('Luke')
        self.assertEqual(player, None)