import requests
import json
from dataUpdater.sleeperApi import ApiEndpoint
from main.models import FantasyTeam, Player
from .static import Static

class UsersRosters(ApiEndpoint):
   
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
                team.rosterId = user['']

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
            print(team.funName)

            for playerId in rosterTeam['players']:
                player = Player.objects.get(sleeperId=playerId)
                print(player.sleeperId)

                if player not in team.player_set.all():
                    
                    player.currentTeam_id = team.pk
                    print('{} added to team {}'.format(player.name, team.pk))
                    player.save()

            for dbPlayer in team.player_set.all():
                player = Player.objects.get(sleeperId = dbPlayer.sleeperId)
                if dbPlayer.sleeperId not in rosterTeam['players']:
                    
                    player.currentTeam_id = 11
                    print('{} removed from team {}'.format(player.name, team.pk))

                    player.save()      





        
    

                

    