import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from packages.StatCalculators.ScoresCalculator import ScoresCalculator


class TestScoresCalculator(unittest.TestCase):

    def test_getMaxScore(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 98, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.1)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100, 100.2)
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
        maxScoreTeam1_1 = ScoresCalculator(1, leagueModel, [2020]).getMaxScore(throughWeek=1)
        maxScoreTeam1_2 = ScoresCalculator(1, leagueModel, [2020]).getMaxScore(throughWeek=2)
        maxScoreTeam1_3 = ScoresCalculator(1, leagueModel, [2020]).getMaxScore(throughWeek=3)
        maxScoreTeam1_vs2 = ScoresCalculator(1, leagueModel, [2020]).getMaxScore(vsTeamIds=[2])
        maxScoreTeam1_vs3 = ScoresCalculator(1, leagueModel, [2020]).getMaxScore(vsTeamIds=[3])
        maxScoreTeam1_only1 = ScoresCalculator(1, leagueModel, [2020]).getMaxScore(onlyWeeks=[1])
        maxScoreTeam1_only1and3 = ScoresCalculator(1, leagueModel, [2020]).getMaxScore(onlyWeeks=[1, 3])
        maxScoreTeam1_allParams = ScoresCalculator(1, leagueModel, [2020]).getMaxScore(throughWeek=2, vsTeamIds=[2])
        maxScoreTeam1_default = ScoresCalculator(1, leagueModel, [2020]).getMaxScore()
        maxScoreTeam1_2021 = ScoresCalculator(1, leagueModel, [2021]).getMaxScore()
        maxScoreTeam1_bothYears = ScoresCalculator(1, leagueModel, [2020, 2021]).getMaxScore()
        self.assertEqual(98, maxScoreTeam1_1)
        self.assertEqual(99, maxScoreTeam1_2)
        self.assertEqual(100, maxScoreTeam1_3)
        self.assertEqual(100, maxScoreTeam1_vs2)
        self.assertEqual(0, maxScoreTeam1_vs3)
        self.assertEqual(98, maxScoreTeam1_only1)
        self.assertEqual(100, maxScoreTeam1_only1and3)
        self.assertEqual(99, maxScoreTeam1_allParams)
        self.assertEqual(100, maxScoreTeam1_default)
        self.assertEqual(100.6, maxScoreTeam1_2021)
        self.assertEqual(100.6, maxScoreTeam1_bothYears)

    def test_getMinScore(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.1)
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
        minScoreTeam1_1 = ScoresCalculator(1, leagueModel, [2020]).getMinScore(throughWeek=1)
        minScoreTeam1_2 = ScoresCalculator(1, leagueModel, [2020]).getMinScore(throughWeek=2)
        minScoreTeam1_3 = ScoresCalculator(1, leagueModel, [2020]).getMinScore(throughWeek=3)
        minScoreTeam1_vs2 = ScoresCalculator(1, leagueModel, [2020]).getMinScore(vsTeamIds=[2])
        minScoreTeam1_vs3 = ScoresCalculator(1, leagueModel, [2020]).getMinScore(vsTeamIds=[3])
        minScoreTeam1_only1 = ScoresCalculator(1, leagueModel, [2020]).getMinScore(onlyWeeks=[1])
        minScoreTeam1_only1and3 = ScoresCalculator(1, leagueModel, [2020]).getMinScore(onlyWeeks=[1, 3])
        minScoreTeam1_allParams = ScoresCalculator(1, leagueModel, [2020]).getMinScore(throughWeek=1, vsTeamIds=[2])
        minScoreTeam1_default = ScoresCalculator(1, leagueModel, [2020]).getMinScore()
        minScoreTeam1_2021 = ScoresCalculator(1, leagueModel, [2021]).getMinScore()
        minScoreTeam1_bothYears = ScoresCalculator(1, leagueModel, [2020, 2021]).getMinScore()
        self.assertEqual(100, minScoreTeam1_1)
        self.assertEqual(99, minScoreTeam1_2)
        self.assertEqual(98, minScoreTeam1_3)
        self.assertEqual(98, minScoreTeam1_vs2)
        self.assertEqual(0, minScoreTeam1_vs3)
        self.assertEqual(100, minScoreTeam1_only1)
        self.assertEqual(98, minScoreTeam1_only1and3)
        self.assertEqual(100, minScoreTeam1_allParams)
        self.assertEqual(98, minScoreTeam1_default)
        self.assertEqual(100, minScoreTeam1_2021)
        self.assertEqual(98, minScoreTeam1_bothYears)

    def test_getPlusMinus(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.1)
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
        plusMinusTeam1_1 = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus(throughWeek=1)
        plusMinusTeam1_2 = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus(throughWeek=2)
        plusMinusTeam1_3 = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus(throughWeek=3)
        plusMinusTeam1_vs2 = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus(vsTeamIds=[2])
        plusMinusTeam1_vs3 = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus(vsTeamIds=[3])
        plusMinusTeam1_only1 = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus(onlyWeeks=[1])
        plusMinusTeam1_only1and3 = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus(onlyWeeks=[1, 3])
        plusMinusTeam1_allParams = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus(throughWeek=2, vsTeamIds=[2])
        plusMinusTeam1_default = ScoresCalculator(1, leagueModel, [2020]).getPlusMinus()
        plusMinusTeam1_2021 = ScoresCalculator(1, leagueModel, [2021]).getPlusMinus()
        plusMinusTeam1_bothYears = ScoresCalculator(1, leagueModel, [2020, 2021]).getPlusMinus()
        self.assertIsInstance(plusMinusTeam1_1, float)
        self.assertEqual(0, plusMinusTeam1_1)
        self.assertEqual(-1.1, plusMinusTeam1_2)
        self.assertEqual(-2.3, plusMinusTeam1_3)
        self.assertEqual(-2.3, plusMinusTeam1_vs2)
        self.assertEqual(0, plusMinusTeam1_vs3)
        self.assertEqual(0, plusMinusTeam1_only1)
        self.assertEqual(-1.2, plusMinusTeam1_only1and3)
        self.assertEqual(-1.1, plusMinusTeam1_allParams)
        self.assertEqual(-2.3, plusMinusTeam1_default)
        self.assertEqual(-0.4, plusMinusTeam1_2021)
        self.assertEqual(-2.7, plusMinusTeam1_bothYears)

    def test_getStandardDeviation(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 100.1)
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
        standardDeviationTeam1_1 = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation(throughWeek=1)
        standardDeviationTeam1_2 = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation(throughWeek=2)
        standardDeviationTeam1_3 = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation(throughWeek=3)
        standardDeviationTeam1_vs2 = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation(vsTeamIds=[2])
        standardDeviationTeam1_vs3 = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation(vsTeamIds=[3])
        standardDeviationTeam1_only1 = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation(onlyWeeks=[1])
        standardDeviationTeam1_only1and3 = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation(
            onlyWeeks=[1, 3])
        standardDeviationTeam1_allParams = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation(throughWeek=1,
                                                                                                         vsTeamIds=[2])
        standardDeviationTeam1_default = ScoresCalculator(1, leagueModel, [2020]).getStandardDeviation()
        standardDeviationTeam1_2021 = ScoresCalculator(1, leagueModel, [2021]).getStandardDeviation()
        standardDeviationTeam1_bothYears = ScoresCalculator(1, leagueModel, [2020, 2021]).getStandardDeviation()
        self.assertIsInstance(standardDeviationTeam1_1, float)
        self.assertEqual(0, standardDeviationTeam1_1)
        self.assertEqual(0.5, standardDeviationTeam1_2)
        self.assertEqual(0.47, standardDeviationTeam1_3)
        self.assertEqual(0.47, standardDeviationTeam1_vs2)
        self.assertEqual(0, standardDeviationTeam1_vs3)
        self.assertEqual(0, standardDeviationTeam1_only1)
        self.assertEqual(0.5, standardDeviationTeam1_only1and3)
        self.assertEqual(0, standardDeviationTeam1_allParams)
        self.assertEqual(0.47, standardDeviationTeam1_default)
        self.assertEqual(0.3, standardDeviationTeam1_2021)
        self.assertEqual(0.63, standardDeviationTeam1_bothYears)

    def test_getScoringShare(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 101, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
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
        percentageTeam1_1 = ScoresCalculator(1, leagueModel, [2020]).getScoringShare(throughWeek=1)
        percentageTeam1_2 = ScoresCalculator(1, leagueModel, [2020]).getScoringShare(throughWeek=2)
        percentageTeam1_vs2 = ScoresCalculator(1, leagueModel, [2020]).getScoringShare(vsTeamIds=[2])
        percentageTeam1_vs3 = ScoresCalculator(1, leagueModel, [2020]).getScoringShare(vsTeamIds=[3])
        percentageTeam1_only2 = ScoresCalculator(1, leagueModel, [2020]).getScoringShare(onlyWeeks=[2])
        percentageTeam1_only1and2 = ScoresCalculator(1, leagueModel, [2020]).getScoringShare(onlyWeeks=[1, 2])
        percentageTeam1_allParams = ScoresCalculator(1, leagueModel, [2020]).getScoringShare(throughWeek=1,
                                                                                             vsTeamIds=[2])
        percentageTeam1_default = ScoresCalculator(1, leagueModel, [2020]).getScoringShare()
        percentageTeam1_2021 = ScoresCalculator(1, leagueModel, [2021]).getScoringShare()
        percentageTeam1_bothYears = ScoresCalculator(1, leagueModel, [2020, 2021]).getScoringShare()
        self.assertIsInstance(percentageTeam1_1, float)
        self.assertEqual(23.87, percentageTeam1_1)
        self.assertEqual(23.96, percentageTeam1_2)
        self.assertEqual(23.96, percentageTeam1_vs2)
        self.assertEqual(0, percentageTeam1_vs3)
        self.assertEqual(24.05, percentageTeam1_only2)
        self.assertEqual(23.96, percentageTeam1_only1and2)
        self.assertEqual(23.87, percentageTeam1_allParams)
        self.assertEqual(23.96, percentageTeam1_default)
        self.assertEqual(17.92, percentageTeam1_2021)
        self.assertEqual(20.5, percentageTeam1_bothYears)

    def test_getScoringShareAgainst(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 100, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 101, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 10.01)
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
        percentageTeam1_1 = ScoresCalculator(1, leagueModel, [2020]).getScoringShareAgainst(throughWeek=1)
        percentageTeam1_2 = ScoresCalculator(1, leagueModel, [2020]).getScoringShareAgainst(throughWeek=2)
        percentageTeam1_vs2 = ScoresCalculator(1, leagueModel, [2020]).getScoringShareAgainst(vsTeamIds=[2])
        percentageTeam1_vs3 = ScoresCalculator(1, leagueModel, [2020]).getScoringShareAgainst(vsTeamIds=[3])
        percentageTeam1_only2 = ScoresCalculator(1, leagueModel, [2020]).getScoringShareAgainst(onlyWeeks=[2])
        percentageTeam1_only1and2 = ScoresCalculator(1, leagueModel, [2020]).getScoringShareAgainst(onlyWeeks=[1, 2])
        percentageTeam1_allParams = ScoresCalculator(1, leagueModel, [2020]).getScoringShareAgainst(throughWeek=1,
                                                                                                    vsTeamIds=[2])
        percentageTeam1_default = ScoresCalculator(1, leagueModel, [2020]).getScoringShareAgainst()
        percentageTeam1_2021 = ScoresCalculator(1, leagueModel, [2021]).getScoringShareAgainst()
        percentageTeam1_bothYears = ScoresCalculator(1, leagueModel, [2020, 2021]).getScoringShareAgainst()
        self.assertIsInstance(percentageTeam1_1, float)
        self.assertEqual(23.87, percentageTeam1_1)
        self.assertEqual(23.84, percentageTeam1_2)
        self.assertEqual(23.84, percentageTeam1_vs2)
        self.assertEqual(0, percentageTeam1_vs3)
        self.assertEqual(23.81, percentageTeam1_only2)
        self.assertEqual(23.84, percentageTeam1_only1and2)
        self.assertEqual(23.87, percentageTeam1_allParams)
        self.assertEqual(23.84, percentageTeam1_default)
        self.assertEqual(17.95, percentageTeam1_2021)
        self.assertEqual(20.47, percentageTeam1_bothYears)
