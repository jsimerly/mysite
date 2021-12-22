from re import match
from typing import Match
from dataUpdater.sleeperApi import ApiEndpoint
from main.models import FantasyTeam, Player, Matchup
from .static import Static

class AllPlayers(ApiEndpoint):
    defDict = Static.defenceDict

    def updatePlayers(self):
        js = self.getPlayers()

        for playerId in js:
            if playerId is not None:

                try:
                    player = Player.objects.get(sleeperId=playerId)
                except:
                    player = Player(sleeperId=playerId)

                if js[playerId]['position'] == 'DEF':
                    try:
                        player.name = self.defDict[playerId]
                    except:
                        print('def name - error with {}'.format(playerId))

                    try:
                        player.pos = js[playerId]['position']
                    except:
                        print('def pos - error with {}'.format(playerId))
                else:
                    try:
                        player.name = js[playerId]['full_name']
                    except:
                        print("name - error with {}".format(playerId))

                    try:
                        player.age = js[playerId]['age']
                    except:
                        print('age - error with {}'.format(playerId))

                    try :
                        player.pos = js[playerId]['position']
                    except:
                        print('pos - error with {}'.format(playerId))

                    try:
                        player.nflTeam = js[playerId]['team']
                    except:
                        print('nflTeam - error with {}'.format(playerId))

                player.save()

    def updateMatchups(self):
        js = self.getMatchups()
        team = FantasyTeam.objects.all()
        
        matchingDict = {}
        matchCounter = 0
        for i in js:
            rosterId = i['roster_id']
            matchupId = i['matchup_id']

            team = FantasyTeam.objects.get(rosterId=rosterId)

            team.pk
            team.matchup = matchupId

            if matchupId != None:
                if matchupId not in matchingDict:
                    matchingDict[matchupId] = team
                else:
                    matchCounter += 1
                    versusTeam = matchingDict[matchupId]
                    matchup = Matchup.objects.get(matchupId=matchCounter)
                    matchup.team1 = team
                    matchup.team2 = versusTeam
                    print(team.funName + ' vs. ' + versusTeam.funName)

                    matchup.save()

            team.save()

        hTeams = len(js)/2
        if matchCounter != hTeams:
            nByes = hTeams-matchCounter
            nNoMatchup = range(matchCounter+1,matchCounter+int(nByes)+1)
            for i in nNoMatchup:
                matchup = Matchup.objects.get(matchupId=i)
                matchup.setBye()
            

            
