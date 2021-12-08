from dataUpdater.sleeperApi import ApiEndpoint
from dataUpdater.scraper import Scraper
from main.models import FantasyTeam, Player
from .static import Static

class UsersRosters(ApiEndpoint, Scraper):
    projDict = Static.posScoringDict
    nameDict = Static.multipleNames

    def updateUserInfo(self):
        js = self.getUsers()

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
                # team.rosterId = user['roster_id']

                try:
                    team.funName = user['metadata']['team_name']
                except:
                    team.funName = user['display_name']

                team.save()

    def updateRoster(self):
        rosterJS = self.getRosters()
        teams = FantasyTeam.objects.all()

        for team in teams:
            for i in rosterJS:
                if team.sleeperId == i['owner_id']:
                    team.rosterId = i['roster_id']
                    
                    team.save()

        for rosterTeam in rosterJS:
            
            team = FantasyTeam.objects.get(rosterId=rosterTeam['roster_id'])

            for playerId in rosterTeam['players']:
                player = Player.objects.get(sleeperId=playerId)

                if player not in team.player_set.all():
                    
                    player.currentTeam_id = team.pk
                    print('{} added to team {}'.format(player.name, team.funName))
                    player.save()

            for dbPlayer in team.player_set.all():
                player = Player.objects.get(sleeperId = dbPlayer.sleeperId)
                if dbPlayer.sleeperId not in rosterTeam['players']:
                    
                    player.currentTeam_id = 11
                    print('{} removed from team {}'.format(player.name, team.funName))

                    player.save()

    def _cleanName(self, playerName):
        name = playerName.replace(' Jr.', "")
        name = name.replace(" Sr.", "")
        name = name.replace(' IV', "")
        name = name.replace(' III', "")
        name = name.replace(' II', "")
        return name

    def _findPlayer(self, playerName, posStr, nflTeam):

        def lookForPlayer(playerObj, playerName):
            try:
                return playerObj.get(name=playerName)
            except:
                try:
                    playerName = self._cleanName(playerName)
                    return playerObj.get(name=playerName)
                except:
                    try:
                        return playerObj.get(name=playerName, nflTeam = nflTeam)
                    except:
                        try:                    
                            playerId = self.nameDict[posStr][playerName]
                            return playerObj.get(sleeperId=playerId)
                        except:
                            pass
                        
        
        posQuery = Player.objects.filter(pos=posStr)
        player = lookForPlayer(posQuery, playerName)
        
        if player == None:
            allQuery = Player.objects.all()
            player =lookForPlayer(allQuery, playerName)
            if player == None:
                print('!! Player not found: ' + playerName + ' !!')
        
        return player     
        
    def updateAllProject(self):
        Player.objects.all().update(currentProj=0)
        self._rbProjection()
        self._wrProjection()
        self._qbProjection()
        self._teProjection()
        self._kProjection()
        self._dstProjection()

    def _rbProjection(self):
        projectionData = self.fetchRbProj()
        ratio = self.projDict['rb']

        for playerList in projectionData:
            playerName = playerList[0]
            rushYds = float(playerList[2])
            rushTds = float(playerList[3])
            rec = float(playerList[4])
            recYds = float(playerList[5])
            recTds = float(playerList[6])
            fum = float(playerList[7])
            nflTeam = playerList[9]

            proj = (rushYds * ratio["rushYds"] 
                    + rushTds * ratio['rushTds']
                    + recYds * ratio['recYds']
                    + recTds * ratio['recTds']
                    + rec * ratio['rec']
                    + fum * ratio['fum'])

            player = self._findPlayer(playerName, 'RB', nflTeam)
            player.currentProj = proj
            player.save()


    def _wrProjection(self):
        projectionData = self.fetchWrProj()
        ratio = self.projDict['wr']

        for playerList in projectionData:
            playerName = playerList[0]
            rec = float(playerList[1])
            recYds = float(playerList[2])
            recTds = float(playerList[3])
            rushYds = float(playerList[5])
            rushTds = float(playerList[6])
            fum = float(playerList[7])
            nflTeam = playerList[9]

            ratio = self.projDict['wr']
            proj = (rushYds * ratio["rushYds"] 
                    + rushTds * ratio['rushTds']
                    + recYds * ratio['recYds']
                    + recTds * ratio['recTds']
                    + rec * ratio['rec']
                    + fum * ratio['fum'])
            
            player = self._findPlayer(playerName,'WR', nflTeam)

            player.currentProj = proj
            player.save()           

    def _teProjection(self):
        projectionData = self.fetchTeProj()
        ratio = self.projDict['te']

        for playerList in projectionData:
            playerName = playerList[0]
            rec = float(playerList[1])
            recYds = float(playerList[2])
            recTds = float(playerList[3])
            fum = float(playerList[4])
            nflTeam = playerList[6]

            proj = (recYds * ratio['recYds']
                    + recTds * ratio['recTds']
                    + rec * ratio['rec']
                    + fum * ratio['fum'])
            
            player = self._findPlayer(playerName, 'TE', nflTeam)

            player.currentProj = proj
            player.save()
            
    
    def _qbProjection(self):
        projectionData = self.fetchQbProj()
        ratio = self.projDict['qb']
        
        for playerList in projectionData:
            playerName = playerList[0]
            paYds = float(playerList[3])
            paTds = float(playerList[4])
            ints = float(playerList[5])
            rushYds = float(playerList[7])
            rushTds = float(playerList[8])
            fum = float(playerList[9])
            nflTeam = playerList[11]

            proj = (paYds * ratio['paYds']
                    + paTds * ratio['paTds']
                    + ints * ratio['ints']
                    + rushYds * ratio['rushYds']
                    + rushTds * ratio['rushTds']
                    + fum * ratio['fum'])

            player = self._findPlayer(playerName, 'QB', nflTeam)
            player.currentProj = proj
            player.save()

    def _kProjection(self):
        projectionData = self.fetchKProj()
        
        for playerList in projectionData:
            playerName = playerList[0]
            nflTeam = playerList[5]
            proj = playerList[4]

            player = self._findPlayer(playerName, 'K', nflTeam)
            player.currentProj = proj
            player.save()


    def _dstProjection(self):
        projectionData = self.fetchDstProj()

        for playerList in projectionData:
            playerName = playerList[0]
            nflTeam = 'null'
            proj = playerList[9]

            player = self._findPlayer(playerName, 'DEF', nflTeam)
            player.currentProj = proj
            player.save()


            
        
