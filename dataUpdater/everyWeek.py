from dataUpdater.sleeperApi import ApiEndpoint
from main.models import Player
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




                
