import unittest

from helpers.LeagueModelNavigator import LeagueModelNavigator
from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel


class TestLeagueModelNavigator(unittest.TestCase):

    def test_getTeamById(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        leagueModel = LeagueModel(123456, "test", 6, teamList, weekList)

        leagueModelNavigator = LeagueModelNavigator()
        team1 = leagueModelNavigator.getTeamById(leagueModel, 1)
        self.assertEqual("team1", team1.getTeamName())
        self.assertEqual(1, team1.getTeamId())
        self.assertRaises(Exception, leagueModelNavigator.getTeamById, leagueModel, 7)




