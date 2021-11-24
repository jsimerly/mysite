import os
import requests
import json
from main.models import FantasyTeam
from .static import Static

class SleeperEndpoint():
   
    def _jsonFetch(self, https):
        j = requests.get(https)
        j = json.loads(j.text)
        return j

    def _getUsers(self, userUrl):
        return self.jsonFetch(userUrl)

    def _getRosters(self, rosterURL):
        return self.jsonFetch(rosterURL)
    
    def _getState(self, stateURL):
        return self.jsonFetch(stateURL)

    def _getWeek(self, state):
        s = self.getState
        return s['week']

    def _getSeason(self, state):
        s = self.getState
        return s['season']

    def _getPlayers(self, playerUrl):
        return self.jsonFetch(playerUrl)
