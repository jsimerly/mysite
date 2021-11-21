import json
import requests

class sleeperEndpoint():
    def __init__(self) -> None:
        pass

    def jsonFetch(https):
        j = requests.get(https)
        j = json.loads(j.text)
        return j

    def getUsers(self, userUrl):
        return self.jsonFetch(userUrl)

    def getRosters(self, rosterURL):
        return self.jsonFetch(rosterURL)
    
    def getState(self, stateURL):
        return self.jsonFetch(stateURL)

    def getWeek(state):
        return state['week']

    def getSeason(state):
        return state['season']

    def getPlayers(self, playerUrl):
        return self.jsonFetch(playerUrl)

    

    
            

