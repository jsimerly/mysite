import os
import requests
import json
from main.models import FantasyTeam
from .static import Static

class ApiEndpoint():

    def jsonFetch(self, https):
        j = requests.get(https)
        j = json.loads(j.text)
        return j

    def getUsers(self):
        return self.jsonFetch(Static.usersURL)

    def getRosters(self):
        return self.jsonFetch(Static.rosterURL)
    
    def _getState(self):
        return self.jsonFetch(Static.stateURL)

    def getMatchups(self):
        return self.jsonFetch(Static.matchupsURL(self.getWeek))

    def getWeek(self):
        s = self._getState()
        return s['week']

    def getSeason(self):
        s = self._getState()
        return s['season']

    def getPlayers(self):
        return self.jsonFetch(Static.playersURL)
