class OwnerComparisonModel:

    def __init__(self, **stats):
        self.__ownerId = stats["ownerId"]
        self.__ownerName = stats["ownerName"]
        self.__wins = stats["wins"]
        self.__losses = stats["losses"]
        self.__ties = stats["ties"]
        self.__winPercentage = stats["winPercentage"]
        self.__ppg = stats["ppg"]
        self.__ppgAgainst = stats["ppgAgainst"]
        self.__plusMinus = stats["plusMinus"]
        self.__stddev = stats["stddev"]
        self.__maxScore = stats["maxScore"]
        self.__minScore = stats["minScore"]
        self.__awal = stats["awal"]
        self.__teamScore = stats["teamScore"]
        self.__teamSuccess = stats["teamSuccess"]
        self.__teamLuck = stats["teamLuck"]
        self.__smartWins = stats["smartWins"]
        self.__percentageOfLeagueScoring = stats["percentageOfLeagueScoring"]
        self.__strengthOfSchedule = stats["strengthOfSchedule"]
        self.__wal = stats["wal"]

    def getOwnerId(self):
        return self.__ownerId

    def getOwnerName(self):
        return self.__ownerName

    def getMaxScore(self):
        return self.__maxScore

    def getMinScore(self):
        return self.__minScore

    def getPpg(self):
        return self.__ppg

    def getPpgAgainst(self):
        return self.__ppgAgainst

    def getPlusMinus(self):
        return self.__plusMinus

    def getStddev(self):
        return self.__stddev

    def getWins(self):
        return self.__wins

    def getLosses(self):
        return self.__losses

    def getTies(self):
        return self.__ties

    def getWinPercentage(self):
        return self.__winPercentage

    def getAwal(self):
        return self.__awal

    def getTeamScore(self):
        return self.__teamScore

    def getTeamSuccess(self):
        return self.__teamSuccess

    def getTeamLuck(self):
        return self.__teamLuck

    def getSmartWins(self):
        return self.__smartWins

    def getPercentageOfLeagueScoring(self):
        return self.__percentageOfLeagueScoring

    def getStrengthOfSchedule(self):
        return self.__strengthOfSchedule

    def getWal(self):
        return self.__wal


