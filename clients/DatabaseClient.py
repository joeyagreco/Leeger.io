import os
import random

from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime

from helpers.Error import Error

load_dotenv()


class DatabaseClient:
    """
    This class is used to connect directly to the Mongo Database.
    """

    def __init__(self):
        self.__cluster = MongoClient(os.getenv("DATABASE_CLUSTER"))
        self.__database = self.__cluster[os.getenv("DATABASE_DATABASE")]
        self.__collection = self.__database[os.getenv("DATABASE_COLLECTION")]

    def __generateLeagueId(self) -> int:
        """
        Returns a new and unused random league id
        Will be between 100000-999999 [always 6 digits]
        """
        newLeagueId = random.randint(100000, 999999)
        while self.__collection.find_one({"_id": newLeagueId}):
            newLeagueId = random.randint(100000, 999999)
        return newLeagueId

    def getLeague(self, leagueId: int):
        """
        Returns a dictionary object of the league or an Error object if not inserted
        https://docs.mongodb.com/manual/reference/method/db.collection.findOne/
        """
        response = self.__collection.find_one({"_id": leagueId})
        # response will be None if not found
        if response:
            return response
        else:
            return Error(f"Could not find a league with ID: {leagueId}")

    def addLeague(self, leagueName: str, numberOfTeams: int, teams: list):
        """
        Adds a league with a new generated ID to the database
        Returns the new league's ID or an Error object if not inserted
        https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/
        """
        # set "year 0", which will be the "all time" year selection
        owners = []
        for i in range(1, len(teams)+1):
            owners.append({"teamId": i, "teamName": f"Owner {i}"})
        year0 = {"year": 0, "teams": owners, "weeks": None}
        # get the current year and set it as default
        currentYear = datetime.now().year
        # construct default year object
        year = {"year": currentYear, "teams": teams, "weeks": []}
        league = {"_id": self.__generateLeagueId(),
                  "leagueName": leagueName,
                  "numberOfTeams": numberOfTeams,
                  "years": {"0": year0,
                            str(currentYear): year}}
        response = self.__collection.insert_one(league)
        if response.acknowledged:
            return response.inserted_id
        else:
            return Error("Could not insert into database.")

    def updateLeague(self, leagueId: int, leagueName: str, years):
        """
        Updates a league with given parameters
        Returns a Document object or an Error object if not updated
        https://docs.mongodb.com/manual/reference/method/db.collection.update/
        https://specify.io/how-tos/mongodb-update-documents
        """
        league = self.getLeague(leagueId)
        if isinstance(league, Error):
            return league
        else:
            league["leagueName"] = leagueName
            league["years"] = years
            response = self.__collection.update({"_id": leagueId}, league)
            if response:
                return response
            else:
                return Error("Could not update league.")

    def deleteLeague(self, leagueId: int):
        """
        Deletes the league with the given ID
        Returns None if successfully deleted or an Error if not.
        https://docs.mongodb.com/manual/reference/method/db.collection.remove/
        """
        response = self.__collection.remove({"_id": leagueId})
        if response["n"] == 1:
            # successfully deleted 1 league
            return None
        else:
            # could not delete the league
            return Error("Could not delete league.")

    def deleteWeek(self, leagueId: int, year: int):
        """
        Deletes the most recent week of the year in the league with the given ID
        Returns league if successfully deleted or an Error if not.
        https://docs.mongodb.com/manual/reference/method/db.collection.update/
        https://specify.io/how-tos/mongodb-update-documents
        """
        league = self.getLeague(leagueId)
        if isinstance(league, Error):
            return league
        else:
            league["years"][str(year)]["weeks"] = league["years"][str(year)]["weeks"][:-1]
            response = self.__collection.update({"_id": leagueId}, league)
            if response:
                league = self.getLeague(leagueId)
                return league
            else:
                return Error("Could not delete week.")
