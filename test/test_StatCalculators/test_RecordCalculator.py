import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from packages.StatCalculators.RecordCalculator import RecordCalculator


class TestRecordCalculator(unittest.TestCase):

    def test_getWins(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
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
        winsTeam1_1 = RecordCalculator(1, leagueModel, [2020]).getWins(throughWeek=1)
        winsTeam1_2 = RecordCalculator(1, leagueModel, [2020]).getWins(throughWeek=2)
        winsTeam1_vs2 = RecordCalculator(1, leagueModel, [2020]).getWins(vsTeamIds=[2])
        winsTeam1_vs3 = RecordCalculator(1, leagueModel, [2020]).getWins(vsTeamIds=[3])
        winsTeam1_only2 = RecordCalculator(1, leagueModel, [2020]).getWins(onlyWeeks=[2])
        winsTeam1_only1and2 = RecordCalculator(1, leagueModel, [2020]).getWins(onlyWeeks=[1, 2])
        winsTeam1_allParams = RecordCalculator(1, leagueModel, [2020]).getWins(throughWeek=2, vsTeamIds=[2])
        winsTeam1_default = RecordCalculator(1, leagueModel, [2020]).getWins()
        winsTeam1_2021 = RecordCalculator(1, leagueModel, [2021]).getWins()
        winsTeam1_bothYears = RecordCalculator(1, leagueModel, [2020, 2021]).getWins()
        self.assertIsInstance(winsTeam1_1, int)
        self.assertEqual(0, winsTeam1_1)
        self.assertEqual(1, winsTeam1_2)
        self.assertEqual(1, winsTeam1_vs2)
        self.assertEqual(0, winsTeam1_vs3)
        self.assertEqual(1, winsTeam1_only2)
        self.assertEqual(1, winsTeam1_only1and2)
        self.assertEqual(1, winsTeam1_allParams)
        self.assertEqual(1, winsTeam1_default)
        self.assertEqual(1, winsTeam1_2021)
        self.assertEqual(2, winsTeam1_bothYears)

    def test_getLosses(self):
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
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
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
        lossesTeam1_1 = RecordCalculator(1, leagueModel, [2020]).getLosses(throughWeek=1)
        lossesTeam1_2 = RecordCalculator(1, leagueModel, [2020]).getLosses(throughWeek=2)
        lossesTeam1_vs2 = RecordCalculator(1, leagueModel, [2020]).getLosses(vsTeamIds=[2])
        lossesTeam1_vs3 = RecordCalculator(1, leagueModel, [2020]).getLosses(vsTeamIds=[3])
        lossesTeam1_only2 = RecordCalculator(1, leagueModel, [2020]).getLosses(onlyWeeks=[2])
        lossesTeam1_only1and2 = RecordCalculator(1, leagueModel, [2020]).getLosses(onlyWeeks=[1, 2])
        lossesTeam1_allParams = RecordCalculator(1, leagueModel, [2020]).getLosses(throughWeek=1, vsTeamIds=[2])
        lossesTeam1_default = RecordCalculator(1, leagueModel, [2020]).getLosses()
        lossesTeam1_2021 = RecordCalculator(1, leagueModel, [2021]).getLosses()
        lossesTeam1_bothYears = RecordCalculator(1, leagueModel, [2020, 2021]).getLosses()
        self.assertIsInstance(lossesTeam1_1, int)
        self.assertEqual(1, lossesTeam1_1)
        self.assertEqual(1, lossesTeam1_2)
        self.assertEqual(1, lossesTeam1_vs2)
        self.assertEqual(0, lossesTeam1_vs3)
        self.assertEqual(0, lossesTeam1_only2)
        self.assertEqual(1, lossesTeam1_only1and2)
        self.assertEqual(1, lossesTeam1_allParams)
        self.assertEqual(1, lossesTeam1_default)
        self.assertEqual(1, lossesTeam1_2021)
        self.assertEqual(2, lossesTeam1_bothYears)

    def test_getTies(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100.1, 100.00)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.6, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
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
        tiesTeam1_1 = RecordCalculator(1, leagueModel, [2020]).getTies(throughWeek=1)
        tiesTeam1_2 = RecordCalculator(1, leagueModel, [2020]).getTies(throughWeek=2)
        tiesTeam1_vs2 = RecordCalculator(1, leagueModel, [2020]).getTies(vsTeamIds=[2])
        tiesTeam1_vs3 = RecordCalculator(1, leagueModel, [2020]).getTies(vsTeamIds=[3])
        tiesTeam1_only2 = RecordCalculator(1, leagueModel, [2020]).getTies(onlyWeeks=[2])
        tiesTeam1_only1and2 = RecordCalculator(1, leagueModel, [2020]).getTies(onlyWeeks=[1, 2])
        tiesTeam1_allParams = RecordCalculator(1, leagueModel, [2020]).getTies(throughWeek=1, vsTeamIds=[2])
        tiesTeam1_default = RecordCalculator(1, leagueModel, [2020]).getTies()
        tiesTeam1_2021 = RecordCalculator(1, leagueModel, [2021]).getTies()
        tiesTeam1_bothYears = RecordCalculator(1, leagueModel, [2020, 2021]).getTies()
        self.assertIsInstance(tiesTeam1_1, int)
        self.assertEqual(0, tiesTeam1_1)
        self.assertEqual(1, tiesTeam1_2)
        self.assertEqual(1, tiesTeam1_vs2)
        self.assertEqual(0, tiesTeam1_vs3)
        self.assertEqual(1, tiesTeam1_only2)
        self.assertEqual(1, tiesTeam1_only1and2)
        self.assertEqual(0, tiesTeam1_allParams)
        self.assertEqual(1, tiesTeam1_default)
        self.assertEqual(1, tiesTeam1_2021)
        self.assertEqual(2, tiesTeam1_bothYears)

    def test_getWinPercentage(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100.00)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.6)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 104)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        year2020 = YearModel(2020, teamList, weekList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
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
        winPercentageTeam1_1 = RecordCalculator(1, leagueModel, [2020]).getWinPercentage(throughWeek=1)
        winPercentageTeam1_2 = RecordCalculator(1, leagueModel, [2020]).getWinPercentage(throughWeek=2)
        winPercentageTeam1_3 = RecordCalculator(1, leagueModel, [2020]).getWinPercentage(throughWeek=3)
        winPercentageTeam1_vs2 = RecordCalculator(1, leagueModel, [2020]).getWinPercentage(vsTeamIds=[2])
        winPercentageTeam1_vs3 = RecordCalculator(1, leagueModel, [2020]).getWinPercentage(vsTeamIds=[3])
        winPercentageTeam1_only2 = RecordCalculator(1, leagueModel, [2020]).getWinPercentage(onlyWeeks=[2])
        winPercentageTeam1_only1and3 = RecordCalculator(1, leagueModel, [2020]).getWinPercentage(onlyWeeks=[1, 3])
        winPercentageTeam1_allParams = RecordCalculator(1, leagueModel, [2020]).getWinPercentage(throughWeek=1,
                                                                                                 vsTeamIds=[2])
        winPercentageTeam1_default = RecordCalculator(1, leagueModel, [2020]).getWinPercentage()
        winPercentageTeam1_2021 = RecordCalculator(1, leagueModel, [2021]).getWinPercentage()
        winPercentageTeam1_bothYears = RecordCalculator(1, leagueModel, [2020, 2021]).getWinPercentage()
        self.assertIsInstance(winPercentageTeam1_1, float)
        self.assertEqual(0.5, winPercentageTeam1_1)
        self.assertEqual(0.25, winPercentageTeam1_2)
        self.assertEqual(0.167, winPercentageTeam1_3)
        self.assertEqual(0.167, winPercentageTeam1_vs2)
        self.assertEqual(0.0, winPercentageTeam1_vs3)
        self.assertEqual(0.0, winPercentageTeam1_only2)
        self.assertEqual(0.25, winPercentageTeam1_only1and3)
        self.assertEqual(0.5, winPercentageTeam1_allParams)
        self.assertEqual(0.167, winPercentageTeam1_default)
        self.assertEqual(0.75, winPercentageTeam1_2021)
        self.assertEqual(0.4, winPercentageTeam1_bothYears)
