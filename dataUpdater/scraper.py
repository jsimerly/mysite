import requests
from bs4 import BeautifulSoup
from .static import Static

class Scraper():
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

            playerTeams = content.findAll('td', class_='player-label')
            for result in playerTeams:
                text = result.get_text(strip=True)
                team = text.replace(playerData[0],'')
                playerData.append(team)

            allData.append(playerData)
        cleanData = [x for x in allData if x != []]
        return cleanData

    def fetchPosStats(self, posUrl):
        soup = self.getSoup(posUrl)
        return self.stripPlayerStats(soup)

    def fetchRbProj(self):
        stats = self.fetchPosStats(Static.rbURL)
        return stats
            
    def fetchWrProj(self):
        stats = self.fetchPosStats(Static.wrURL)
        return stats

    def fetchTeProj(self):
        stats = self.fetchPosStats(Static.teURL)
        return stats

    def fetchQbProj(self):
        stats = self.fetchPosStats(Static.qbURL)
        return stats

    def fetchKProj(self):
        stats = self.fetchPosStats(Static.kURL)
        return stats

    def fetchDstProj(self):
        stats = self.fetchPosStats(Static.defURL)
        return stats