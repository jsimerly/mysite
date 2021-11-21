import requests
from bs4 import BeautifulSoup
import time


class FantasyProScrapper():
    def __init__(self) -> None:
        pass

    def getSoup(url):
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')
        return soup

    def getHtmlRows(soup):
        return soup.findAll('tr')

    def stripPlayerStats(contents):
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

        return allData

    def fetchPosStats(self, posUrl):
        return self.stripPlayerStats(posUrl)

            



