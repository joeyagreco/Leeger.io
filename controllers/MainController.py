from services.DatabaseService import DatabaseService


class MainController:

    def __init__(self):
        self.__databaseService = DatabaseService()

    def getLeague(self, leagueId: int):
        return self.__databaseService.getLeague(leagueId)

    def addLeague(self):
        return self.__databaseService.addLeague()