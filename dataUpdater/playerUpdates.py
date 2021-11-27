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
                        print('nflTaem - error with {}'.format(playerId))

                    
                player.save()

    def updateMatchups(self):
        js = self.getMatchups()
        teams = FantasyTeam.objects.all()
        matchups = Matchup()

        for i in js:
            rosterId = i['roster_id']
            matchupId = i['matchup_id']

            team = FantasyTeam.objects.get(rosterId=rosterId)
            team.matchup = matchupId
            team.save()
        
        matchup1 = []
        matchup2 = []
        matchup3 = []
        matchup4 = []
        matchup5 = []


        for team in teams:
            if team.matchup == 1:
                matchup1.append(team)
            elif team.matchup ==2:
                matchup2.append(team)
            elif team.matchup == 3:
                matchup3.append(team)
            elif team.matchup == 4:
                matchup4.append(team)
            elif team.matchup == 5:
                matchup5.append(team)
            else:
                print('Team Matchup Id did not matchup')

        matchupList = [matchup1,matchup2,matchup3,matchup4,matchup5]

        for i in range(0,5):
            try:
                matchup = Matchup.objects.get(matchupId=i+1)                
            except:
                matchup = Matchup(matchupId=i+1)

            matchup.team1 = matchupList[i][0]
            matchup.team2 = matchupList[i][1]
            
            print(matchup.team1)
            print(matchup.team2)
            matchup.save()
            
