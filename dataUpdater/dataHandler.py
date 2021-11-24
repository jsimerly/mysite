import requests
from bs4 import BeautifulSoup, FeatureNotFound
from .static import Static
import json
import requests

class SleeperEndpoint():
    def __init__(self) -> None:
        pass

    def jsonFetch(self, https):
        j = requests.get(https)
        j = json.loads(j.text)
        return j

    def getUsers(self, userUrl):
        return self.jsonFetch(userUrl)

    def getRosters(self, rosterURL):
        return self.jsonFetch(rosterURL)
    
    def getState(self, stateURL):
        return self.jsonFetch(stateURL)

    def getWeek(self, state):
        s = self.getState
        return s['week']

    def getSeason(self, state):
        s = self.getState
        return s['season']

    def getPlayers(self, playerUrl):
        return self.jsonFetch(playerUrl)

class DataHandler():
    def __init__(self) -> None:
        pass

    def rostersToUsernames(rosters, users):
            userNames = {}

            for roster in rosters:
                for user in users:
                    if user['user_id'] == roster['owner_id']:
                        userNames[roster['owner_id']]=user['display_name']
            
            return userNames

    def rosterIds(rosters, userNames):
        rosterIds = {}

        for roster in rosters:
            rosterIds[roster['roster_id']]=userNames['owner_id']
        
        return rosterIds
    
    def createMatchups(rosterIds, matchups):
        allMatches = [[],[],[],[],[]]

        for matchup in matchups:
            print(matchup['matchup_id'])
            if matchup['matchup_id'] == 1:
                allMatches[0].append(rosterIds[matchup['roster_id']])
                continue
            if matchup['matchup_id'] == 2:
                allMatches[1].append(rosterIds[matchup['roster_id']])
                continue
            if matchup['matchup_id'] == 3:
                allMatches[2].append(rosterIds[matchup['roster_id']])
                continue
            if matchup['matchup_id'] == 4:
                print('here')
                allMatches[3].append(rosterIds[matchup['roster_id']])
                continue
            if matchup['matchup_id'] == 5:
                allMatches[4].append(rosterIds[matchup['roster_id']])
                continue
                
        return allMatches


class Projections(): 
    projDict = Static.posScoringDict

    def rbProjection(self, rushYds, rushTds, recYds, recTds, rec, fum):
        ratio = self.projDict['rb']
        proj = (rushYds * ratio["rushYds"] 
                + rushTds * ratio['rushTds']
                + recYds * ratio['recYds']
                + recTds * ratio['recTds']
                + rec * ratio['rec']
                + fum * ratio['fum'])
        return  proj

    def wrProjection(self, rushYds, rushTds, recYds, recTds, rec, fum):
        ratio = self.projDict['wr']
        proj = (rushYds * ratio["rushYds"] 
                + rushTds * ratio['rushTds']
                + recYds * ratio['recYds']
                + recTds * ratio['recTds']
                + rec * ratio['rec']
                + fum * ratio['fum'])
        return  proj

    def teProjection(self, recYds, recTds, rec, fum):
        ratio = self.projDict['te']
        proj = (recYds * ratio['recYds']
                + recTds * ratio['recTds']
                + rec * ratio['rec']
                + fum * ratio['fum'])
        return  proj
    
    def qbProjection(self, paYds, paTds, ints, rushYds, rushTds, fum):
        ratio = self.projDict['qb']
        proj = (paYds * ratio['paYds']
                + paTds * ratio['paTds']
                + ints * ratio['ints']
                + rushYds * ratio['rushYds']
                + rushTds * ratio['rushTds']
                + fum * ratio['fum'])
    def kProjection(kproj):
        return kproj

    def kProjection(dproj):
        return dproj


class FantasyProScrapper():
    def __init__(self):
        pass

    def getSoup(self, url):
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup

    def stripPlayerStats(self, soup):
        contents = soup.findAll('tr')
        allData = []

        for content in contents:
            playerData = []

            namesResults = content.findAll('a', class_='player-name')
            for result in namesResults:
                playerData.append(result.get_text(strip=True))

            statsResults = content.findAll('td', class_='center')
            for result in statsResults:
                playerData.append(result.get_text(strip=True))

            allData.append(playerData)
        cleanData = [x for x in allData if x != []]
        return cleanData

    def fetchPosStats(self, posUrl):
        return self.stripPlayerStats(posUrl)

    def fetchRbProj(self, url):
        stats = self.fetchPosStats(Static.rbURL)
        return stats
            
    def fetchWrProj(self, url):
        stats = self.fetchPosStats(Static.wrURL)
        return stats

    def fetchTeProj(self, url):
        stats = self.fetchPosStats(Static.teURL)
        return stats

    def fetchQbProj(self, url):
        stats = self.fetchPosStats(Static.qbURL)
        return stats

    def fetchKProj(self, url):
        stats = self.fetchPosStats(Static.kURL)
        return stats

    def fetchDstProj(self, url):
        stats = self.fetchPosStats(Static.defURL)
        return stats