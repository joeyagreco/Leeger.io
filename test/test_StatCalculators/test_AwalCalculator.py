import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from packages.StatCalculators.AwalCalculator import AwalCalculator


class TestAwalCalculator(unittest.TestCase):

    def test_getAwalNormal(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        awalTeam1_1 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal(throughWeek=1)
        awalTeam1_2 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal(throughWeek=2)
        awalTeam1_vs2 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal(vsTeamIds=[2])
        awalTeam1_vs3 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal(vsTeamIds=[3])
        awalTeam1_only2 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal(onlyWeeks=[2])
        awalTeam1_only1and2 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal(onlyWeeks=[1, 2])
        awalTeam1_allParams = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal(throughWeek=1, vsTeamIds=[2])
        awalTeam1_default = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal()
        self.assertIsInstance(awalTeam1_1, float)
        self.assertEqual(0.2, awalTeam1_1)
        self.assertEqual(0.4, awalTeam1_2)
        self.assertEqual(0.4, awalTeam1_vs2)
        self.assertEqual(0, awalTeam1_vs3)
        self.assertEqual(0.2, awalTeam1_only2)
        self.assertEqual(0.4, awalTeam1_only1and2)
        self.assertEqual(0.2, awalTeam1_allParams)
        self.assertEqual(0.4, awalTeam1_default)

    def test_getAwalOneTiedMatchup(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        awalTeam1 = AwalCalculator(1, leagueModel, [2020], 0, 1).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel, [2020], 0, 1).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel, [2020], 0, 0).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel, [2020], 1, 0).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel, [2020], 0, 0).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel, [2020], 1, 0).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.30, awalTeam1)
        self.assertEqual(0.30, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(0.60, awalTeam4)
        self.assertEqual(0.80, awalTeam5)
        self.assertEqual(1.00, awalTeam6)

    def test_getAwalOneTieNotMatchup(self):
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
        weekList = [week1]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        awalTeam1 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel, [2020], 1, 0).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel, [2020], 0, 0).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel, [2020], 1, 0).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel, [2020], 0, 0).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel, [2020], 1, 0).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.30, awalTeam1)
        self.assertEqual(0.60, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(0.30, awalTeam4)
        self.assertEqual(0.80, awalTeam5)
        self.assertEqual(1.00, awalTeam6)

    def test_getAwalOneTiedMatchupOneTieNotMatchup(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        awalTeam1 = AwalCalculator(1, leagueModel, [2020], 0, 1).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel, [2020], 0, 1).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel, [2020], 0, 0).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel, [2020], 1, 0).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel, [2020], 0, 0).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel, [2020], 1, 0).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.40, awalTeam1)
        self.assertEqual(0.40, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(0.40, awalTeam4)
        self.assertEqual(0.80, awalTeam5)
        self.assertEqual(1.00, awalTeam6)

    def test_getAwalAllTies(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 100, 100)
        matchup3 = MatchupModel(3, team5, team6, 100, 100)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        awalTeam1 = AwalCalculator(1, leagueModel, [2020], 0, 1).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel, [2020], 0, 1).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel, [2020], 0, 1).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel, [2020], 0, 1).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel, [2020], 0, 1).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel, [2020], 0, 1).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.50, awalTeam1)
        self.assertEqual(0.50, awalTeam2)
        self.assertEqual(0.50, awalTeam3)
        self.assertEqual(0.50, awalTeam4)
        self.assertEqual(0.50, awalTeam5)
        self.assertEqual(0.50, awalTeam6)

    def test_getAwalNormalTwoWeeks(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 101)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        awalTeam1 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel, [2020], 2, 0).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel, [2020], 0, 0).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel, [2020], 2, 0).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel, [2020], 0, 0).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel, [2020], 2, 0).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.40, awalTeam1)
        self.assertEqual(0.80, awalTeam2)
        self.assertEqual(0.00, awalTeam3)
        self.assertEqual(1.20, awalTeam4)
        self.assertEqual(1.60, awalTeam5)
        self.assertEqual(2.00, awalTeam6)

    def test_getAwalNormalSixteenTeams(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        team7 = TeamModel(7, "team7")
        team8 = TeamModel(8, "team8")
        team9 = TeamModel(9, "team9")
        team10 = TeamModel(10, "team10")
        team11 = TeamModel(11, "team11")
        team12 = TeamModel(12, "team12")
        team13 = TeamModel(13, "team13")
        team14 = TeamModel(14, "team14")
        team15 = TeamModel(15, "team15")
        team16 = TeamModel(16, "team16")
        teamList = [team1, team2, team3, team4, team5, team6, team7, team8,
                    team9, team10, team11, team12, team13, team14, team15, team16]
        matchup1 = MatchupModel(1, team1, team2, 100, 101)
        matchup2 = MatchupModel(2, team3, team4, 102, 103)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchup4 = MatchupModel(4, team7, team8, 106, 107)
        matchup5 = MatchupModel(5, team9, team10, 108, 109)
        matchup6 = MatchupModel(6, team11, team12, 110, 111)
        matchup7 = MatchupModel(7, team13, team14, 112, 113)
        matchup8 = MatchupModel(8, team15, team16, 114, 115)
        matchupList = [matchup1, matchup2, matchup3, matchup4, matchup5, matchup6, matchup7, matchup8]
        week1 = WeekModel(1, matchupList)
        weekList = [week1]
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 16, yearDict)
        awalTeam1 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAwal()
        awalTeam2 = AwalCalculator(2, leagueModel, [2020], 1, 0).getAwal()
        awalTeam3 = AwalCalculator(3, leagueModel, [2020], 0, 0).getAwal()
        awalTeam4 = AwalCalculator(4, leagueModel, [2020], 1, 0).getAwal()
        awalTeam5 = AwalCalculator(5, leagueModel, [2020], 0, 0).getAwal()
        awalTeam6 = AwalCalculator(6, leagueModel, [2020], 1, 0).getAwal()
        awalTeam7 = AwalCalculator(7, leagueModel, [2020], 0, 0).getAwal()
        awalTeam8 = AwalCalculator(8, leagueModel, [2020], 1, 0).getAwal()
        awalTeam9 = AwalCalculator(9, leagueModel, [2020], 0, 0).getAwal()
        awalTeam10 = AwalCalculator(10, leagueModel, [2020], 1, 0).getAwal()
        awalTeam11 = AwalCalculator(11, leagueModel, [2020], 0, 0).getAwal()
        awalTeam12 = AwalCalculator(12, leagueModel, [2020], 1, 0).getAwal()
        awalTeam13 = AwalCalculator(13, leagueModel, [2020], 0, 0).getAwal()
        awalTeam14 = AwalCalculator(14, leagueModel, [2020], 1, 0).getAwal()
        awalTeam15 = AwalCalculator(15, leagueModel, [2020], 0, 0).getAwal()
        awalTeam16 = AwalCalculator(16, leagueModel, [2020], 1, 0).getAwal()
        self.assertIsInstance(awalTeam1, float)
        self.assertEqual(0.00, awalTeam1)
        self.assertEqual(0.07, awalTeam2)
        self.assertEqual(0.13, awalTeam3)
        self.assertEqual(0.20, awalTeam4)
        self.assertEqual(0.27, awalTeam5)
        self.assertEqual(0.33, awalTeam6)
        self.assertEqual(0.40, awalTeam7)
        self.assertEqual(0.47, awalTeam8)
        self.assertEqual(0.53, awalTeam9)
        self.assertEqual(0.60, awalTeam10)
        self.assertEqual(0.67, awalTeam11)
        self.assertEqual(0.73, awalTeam12)
        self.assertEqual(0.80, awalTeam13)
        self.assertEqual(0.87, awalTeam14)
        self.assertEqual(0.93, awalTeam15)
        self.assertEqual(1.00, awalTeam16)

    def test_getWal(self):
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
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        walTeam1 = AwalCalculator(1, leagueModel, [2020], 0, 0).getWal()
        walTeam2 = AwalCalculator(2, leagueModel, [2020], 1, 0).getWal()
        walTeam3 = AwalCalculator(3, leagueModel, [2020], 0, 0).getWal()
        walTeam4 = AwalCalculator(4, leagueModel, [2020], 1, 0).getWal()
        walTeam5 = AwalCalculator(5, leagueModel, [2020], 0, 0).getWal()
        walTeam6 = AwalCalculator(6, leagueModel, [2020], 1, 0).getWal()
        self.assertIsInstance(walTeam1, float)
        self.assertEqual(0.00, walTeam1)
        self.assertEqual(1.00, walTeam2)
        self.assertEqual(0.00, walTeam3)
        self.assertEqual(1.00, walTeam4)
        self.assertEqual(0.00, walTeam5)
        self.assertEqual(1.00, walTeam6)

    def test_getAdjustment(self):
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
        year = YearModel(2020, teamList, weekList)
        yearDict = {2020: year}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        adjustmentTeam1 = AwalCalculator(1, leagueModel, [2020], 0, 0).getAdjustment()
        adjustmentTeam2 = AwalCalculator(2, leagueModel, [2020], 1, 0).getAdjustment()
        adjustmentTeam3 = AwalCalculator(3, leagueModel, [2020], 0, 0).getAdjustment()
        adjustmentTeam4 = AwalCalculator(4, leagueModel, [2020], 1, 0).getAdjustment()
        adjustmentTeam5 = AwalCalculator(5, leagueModel, [2020], 0, 0).getAdjustment()
        adjustmentTeam6 = AwalCalculator(6, leagueModel, [2020], 1, 0).getAdjustment()
        self.assertIsInstance(adjustmentTeam1, float)
        self.assertEqual(0.20, adjustmentTeam1)
        self.assertEqual(-0.60, adjustmentTeam2)
        self.assertEqual(0.00, adjustmentTeam3)
        self.assertEqual(-0.40, adjustmentTeam4)
        self.assertEqual(0.80, adjustmentTeam5)
        self.assertEqual(0.00, adjustmentTeam6)
