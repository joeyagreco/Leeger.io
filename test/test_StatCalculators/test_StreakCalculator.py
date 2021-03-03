import unittest

from models.league_models.LeagueModel import LeagueModel
from models.league_models.MatchupModel import MatchupModel
from models.league_models.TeamModel import TeamModel
from models.league_models.WeekModel import WeekModel
from models.league_models.YearModel import YearModel
from packages.StatCalculators.PpgCalculator import PpgCalculator
from packages.StatCalculators.StreakCalculator import StreakCalculator


class TestStreakCalculator(unittest.TestCase):

    def test_getWinStreaks(self):
        team1 = TeamModel(1, "team1")
        team2 = TeamModel(2, "team2")
        team3 = TeamModel(3, "team3")
        team4 = TeamModel(4, "team4")
        team5 = TeamModel(5, "team5")
        team6 = TeamModel(6, "team6")
        teamList = [team1, team2, team3, team4, team5, team6]
        matchup1 = MatchupModel(1, team1, team2, 90.5, 100)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 99, 92)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 110.2, 100.2)
        matchup2 = MatchupModel(2, team3, team4, 0, 50.01)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week3 = WeekModel(3, matchupList)
        weekList = [week1, week2, week3]
        year2020 = YearModel(2020, teamList, weekList)

        matchup1 = MatchupModel(1, team1, team2, 102, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 0.0, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week1 = WeekModel(1, matchupList)
        matchup1 = MatchupModel(1, team1, team2, 100.5, 100.5)
        matchup2 = MatchupModel(2, team3, team4, 100.1, 100)
        matchup3 = MatchupModel(3, team5, team6, 104, 105)
        matchupList = [matchup1, matchup2, matchup3]
        week2 = WeekModel(2, matchupList)
        weekList = [week1, week2]
        year2021 = YearModel(2021, teamList, weekList)
        yearDict = {2020: year2020, 2021: year2021}
        leagueModel = LeagueModel(123456, "test", 6, yearDict)
        winStreaks_team1_2020 = StreakCalculator(leagueModel, 1, [2020]).getWinStreaks()
        winStreaks_team2_2020 = StreakCalculator(leagueModel, 2, [2020]).getWinStreaks()
        winStreaks_team1_bothYears = StreakCalculator(leagueModel, 1, [2020, 2021]).getWinStreaks()
        self.assertIsInstance(winStreaks_team1_2020, list)
        self.assertEqual(1, len(winStreaks_team1_2020))
        self.assertEqual(1, winStreaks_team1_2020[0].getOwnerId())
        self.assertEqual(2, winStreaks_team1_2020[0].getStreakNumber())
        self.assertEqual("Week 2 2020", winStreaks_team1_2020[0].getStartDate())
        self.assertEqual("team1", winStreaks_team1_2020[0].getStartTeam().getTeamName())
        self.assertEqual("Week 3 2020", winStreaks_team1_2020[0].getEndDate())
        self.assertEqual("team1", winStreaks_team1_2020[0].getEndTeam().getTeamName())
        self.assertIsInstance(winStreaks_team2_2020, list)
        self.assertEqual(0, len(winStreaks_team2_2020))
        self.assertIsInstance(winStreaks_team1_bothYears, list)
        self.assertEqual(1, len(winStreaks_team1_bothYears))
        self.assertEqual(1, winStreaks_team1_bothYears[0].getOwnerId())
        self.assertEqual(3, winStreaks_team1_bothYears[0].getStreakNumber())
        self.assertEqual("Week 2 2020", winStreaks_team1_bothYears[0].getStartDate())
        self.assertEqual("team1", winStreaks_team1_bothYears[0].getStartTeam().getTeamName())
        self.assertEqual("Week 1 2021", winStreaks_team1_bothYears[0].getEndDate())
        self.assertEqual("team1", winStreaks_team1_bothYears[0].getEndTeam().getTeamName())
