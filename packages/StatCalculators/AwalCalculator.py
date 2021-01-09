from helpers.LeagueModelNavigator import LeagueModelNavigator
from helpers.Rounder import Rounder
from models.league_models.LeagueModel import LeagueModel
from models.league_models.WeekModel import WeekModel


class AwalCalculator:

    def __init__(self, teamId: int, leagueModel: LeagueModel, wins: int, ties: int):
        self.__teamId = teamId
        self.__leagueModel = leagueModel
        self.__wins = wins
        self.__ties = ties
        self.__rounder = Rounder()

    def getAwal(self, **params):
        """
        Returns a float that is the AWAL for the team with self.__teamId.
        WEEK: [int] Gives AWAL through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        return self.__rounder.normalRound(self.getAdjustment(week=weekNumber) + self.getWal(), 2)

    def getAwalVsTeam(self, opponentTeamId: int):
        """
        Returns a float that is the AWAL for the team with self.__teamId vs the team with opponentTeamId
        """
        return self.__rounder.normalRound(self.getAdjustmentVsTeam(opponentTeamId) + self.getWal(), 2)

    def getAdjustment(self, **params):
        """
        Returns a float that is the adjustment [A] for the team with self.__teamId
        A = W * (1/L) + T * (0.5/L) - WAL
        Where:
        WAL = Game outcome (1=win, 0=loss, 0.5=tie)
        W = Teams outscored
        T = Teams tied
        L = Opponents in league (league size - 1)
        WEEK: [int] Gives AWAL through that week.
        """
        leagueModelNavigator = LeagueModelNavigator()
        weekNumber = params.pop("week", leagueModelNavigator.getNumberOfWeeksInLeague(self.__leagueModel))
        totalAdjustment = 0
        L = self.__leagueModel.getNumberOfTeams() - 1
        for week in self.__leagueModel.getWeeks():
            if week.getWeekNumber() > weekNumber:
                break
            WAL = self.__getTeamOutcomeOfWeek(week)
            W = self.__getTeamsOutscoredOfWeek(week)
            T = self.__getTeamsTiedOfWeek(week)
            A = W * (1 / L) + T * (0.5 / L) - WAL
            totalAdjustment += A
        return self.__rounder.normalRound(totalAdjustment, 2)

    def getAdjustmentVsTeam(self, opponentTeamId: int):
        """
        Returns a float that is the adjustment [A] for the team with self.__teamId vs the team with opponentTeamId
        A = W * (1/L) + T * (0.5/L) - WAL
        Where:
        WAL = Game outcome (1=win, 0=loss, 0.5=tie)
        W = Teams outscored
        T = Teams tied
        L = Opponents in league (league size - 1)
        """
        leagueModelNavigator = LeagueModelNavigator()
        totalAdjustment = 0
        L = self.__leagueModel.getNumberOfTeams() - 1
        for week in self.__leagueModel.getWeeks():
            if leagueModelNavigator.teamsPlayInWeek(week, self.__teamId, opponentTeamId):
                # only count weeks where the this team plays the team with opponentTeamId
                WAL = self.__getTeamOutcomeOfWeek(week)
                W = self.__getTeamsOutscoredOfWeek(week)
                T = self.__getTeamsTiedOfWeek(week)
                A = W * (1 / L) + T * (0.5 / L) - WAL
                totalAdjustment += A
        return self.__rounder.normalRound(totalAdjustment, 2)

    def getWal(self):
        """
        Returns the total wins against the league for the team with self.__teamId [from class instance variables].
        """
        wal = self.__wins + (0.5 * self.__ties)
        return self.__rounder.normalRound(wal, 2)

    def __getTeamOutcomeOfWeek(self, week: WeekModel):
        """
        Returns the outcome in the given week for the team with self.__teamId
        (1=win, 0=loss, 0.5=tie)
        """
        for matchup in week.getMatchups():
            if matchup.getTeamA().getTeamId() == self.__teamId:
                # our target team is TeamA
                if matchup.getTeamAScore() > matchup.getTeamBScore():
                    # our target team won
                    return 1
                elif matchup.getTeamAScore() < matchup.getTeamBScore():
                    # our target team lost
                    return 0
                else:
                    # our target team tied
                    return 0.5
            elif matchup.getTeamB().getTeamId() == self.__teamId:
                # our target team is TeamB
                if matchup.getTeamBScore() > matchup.getTeamAScore():
                    # our target team won
                    return 1
                elif matchup.getTeamBScore() < matchup.getTeamAScore():
                    # our target team lost
                    return 0
                else:
                    # our target team tied
                    return 0.5

    def __getTeamsOutscoredOfWeek(self, week: WeekModel):
        """
        Returns the number of teams outscored in the given week for the team with self.__teamId
        """
        allScores = {}
        for matchup in week.getMatchups():
            allScores[matchup.getTeamA().getTeamId()] = matchup.getTeamAScore()
            allScores[matchup.getTeamB().getTeamId()] = matchup.getTeamBScore()
        allScoresList = []
        for teamId in allScores:
            allScoresList.append(allScores[teamId])
        targetTeamScore = allScores[self.__teamId]
        teamsOutscored = 0
        for score in allScoresList:
            if targetTeamScore > score:
                teamsOutscored += 1
        return teamsOutscored

    def __getTeamsTiedOfWeek(self, week: WeekModel):
        """
        Returns the number of teams tied in the given week for the team with self.__teamId
        """
        allScores = {}
        for matchup in week.getMatchups():
            allScores[matchup.getTeamA().getTeamId()] = matchup.getTeamAScore()
            allScores[matchup.getTeamB().getTeamId()] = matchup.getTeamBScore()
        allScoresList = []
        for teamId in allScores:
            if teamId != self.__teamId:
                allScoresList.append(allScores[teamId])
        targetTeamScore = allScores[self.__teamId]
        teamsTied = 0
        for score in allScoresList:
            if targetTeamScore == score:
                teamsTied += 1
        return teamsTied

