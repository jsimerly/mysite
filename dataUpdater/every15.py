import os
import requests
import json
from main.models import FantasyTeam
from .static import Static

class SleeperEndpoint():
    static = Static()
   
    def _jsonFetch(self, https):
        j = requests.get(https)
        j = json.loads(j.text)
        return j

    def _getUsers(self, userUrl):
        return self._jsonFetch(userUrl)

    def _getRosters(self, rosterURL):
        return self._jsonFetch(rosterURL)

    def updateUserInfo(self):
        js = self._getUsers(Static.usersURL)

        for i in range(10):
            user = js[i]
            if user is not None:
                print(user['user_id'])
                print(i)
                
                try:
                    team = FantasyTeam.objects.get(sleeperId=user['user_id'])
                except:
                    team = FantasyTeam(sleeperId=user['user_id'])
                
                team.sleeperName = user['display_name']

                try:
                    team.funName = user['metadata']['team_name']
                except:
                    team.funName = user['display_name']

                team.save()
                

    