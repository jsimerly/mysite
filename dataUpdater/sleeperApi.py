import os
import requests
import json
from main.models import FantasyTeam
from .static import Static

class ApiEndpoint():
    static = Static()

    def jsonFetch(self, https):
        j = requests.get(https)
        j = json.loads(j.text)
        return j

    def getUsers(self):
        return self.jsonFetch(self.static.usersURL)

    def getRosters(self):
        return self.jsonFetch(self.static.rosterURL)
    
    def _getState(self):
        return self.jsonFetch(self.static.stateURL)

    def getMatchups(self):
        week = self.getWeek()
        url = self.static.matchupsURL(week)
        return self.jsonFetch(url)

    def getWeek(self):
        s = self._getState()
        return s['week']

    def getSeason(self):
        s = self._getState()
        return s['season']

    def getPlayers(self):
        return self.jsonFetch(Static.playersURL)
