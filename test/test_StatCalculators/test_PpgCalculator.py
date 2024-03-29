import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from packages.StatCalculators.PpgCalculator import PpgCalculator


class TestPpgCalculator(unittest.TestCase):

    def test_getPpg(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        yearDict = {"2020": year2020, "2021": year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        ppgTeam1_1 = PpgCalculator(1, leagueModel, [2020]).getPpg(throughWeek=1)
        ppgTeam1_2 = PpgCalculator(1, leagueModel, [2020]).getPpg(throughWeek=2)
        ppgTeam1_3 = PpgCalculator(1, leagueModel, [2020]).getPpg(throughWeek=3)
        ppgTeam1_vs2 = PpgCalculator(1, leagueModel, [2020]).getPpg(vsTeamIds=[2])
        ppgTeam1_vs3 = PpgCalculator(1, leagueModel, [2020]).getPpg(vsTeamIds=[3])
        ppgTeam1_only1 = PpgCalculator(1, leagueModel, [2020]).getPpg(onlyWeeks=[1])
        ppgTeam1_only1and3 = PpgCalculator(1, leagueModel, [2020]).getPpg(onlyWeeks=[1, 3])
        ppgTeam1_allParams = PpgCalculator(1, leagueModel, [2020]).getPpg(vsTeamIds=[2], throughWeek=1)
        ppgTeam1_default = PpgCalculator(1, leagueModel, [2020]).getPpg()
        ppgTeam1_2021 = PpgCalculator(1, leagueModel, [2021]).getPpg()
        ppgTeam1_bothYears = PpgCalculator(1, leagueModel, [2020, 2021]).getPpg()
        self.assertIsInstance(ppgTeam1_1, float)
        self.assertEqual(100, ppgTeam1_1)
        self.assertEqual(99.5, ppgTeam1_2)
        self.assertEqual(99.33, ppgTeam1_3)
        self.assertEqual(99.33, ppgTeam1_vs2)
        self.assertEqual(0, ppgTeam1_vs3)
        self.assertEqual(100, ppgTeam1_only1)
        self.assertEqual(99.5, ppgTeam1_only1and3)
        self.assertEqual(100, ppgTeam1_allParams)
        self.assertEqual(99.33, ppgTeam1_default)
        self.assertEqual(100.3, ppgTeam1_2021)
        self.assertEqual(99.72, ppgTeam1_bothYears)

    def test_getPpgAgainst(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 98, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        yearDict = {"2020": year2020, "2021": year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        ppgAgainstTeam1_1 = PpgCalculator(1, leagueModel, [2020]).getPpgAgainst(throughWeek=1)
        ppgAgainstTeam1_2 = PpgCalculator(1, leagueModel, [2020]).getPpgAgainst(throughWeek=2)
        ppgAgainstTeam1_3 = PpgCalculator(1, leagueModel, [2020]).getPpgAgainst(throughWeek=3)
        ppgAgainstTeam1_only1 = PpgCalculator(1, leagueModel, [2020]).getPpgAgainst(onlyWeeks=[1])
        ppgAgainstTeam1_only1and3 = PpgCalculator(1, leagueModel, [2020]).getPpgAgainst(onlyWeeks=[1, 3])
        ppgAgainstTeam1_default = PpgCalculator(1, leagueModel, [2020]).getPpgAgainst()
        ppgAgainstTeam1_2021 = PpgCalculator(1, leagueModel, [2021]).getPpgAgainst()
        ppgAgainstTeam1_bothYears = PpgCalculator(1, leagueModel, [2020, 2021]).getPpgAgainst()
        self.assertIsInstance(ppgAgainstTeam1_1, float)
        self.assertEqual(100.5, ppgAgainstTeam1_1)
        self.assertEqual(100.35, ppgAgainstTeam1_2)
        self.assertEqual(100.3, ppgAgainstTeam1_3)
        self.assertEqual(100.5, ppgAgainstTeam1_only1)
        self.assertEqual(100.35, ppgAgainstTeam1_only1and3)
        self.assertEqual(100.3, ppgAgainstTeam1_default)
        self.assertEqual(100.5, ppgAgainstTeam1_2021)
        self.assertEqual(100.38, ppgAgainstTeam1_bothYears)
