from django.db.models.fields import NullBooleanField
from main.models import FantasyTeam

class CreateLines():
    allTeams = FantasyTeam.objects.all()
    noFA = allTeams.exclude(sleeperName='FreeAgent')

    def createSpread(self):
        teams = self.noFA

        for matchup in teams.values('matchup'):
            print(matchup['matchup'])
            
        
        
        for team in teams:
            print(team.funName)


    def createLineUp(self):

        teams = self.noFA

        for team in teams:
            qb = []
            rb = []
            wr = []
            te = []
            k = []
            dst = []

            for player in team.player_set.all():
                if player.pos == 'QB':
                    qb.append(player.currentProj)
                elif player.pos == 'RB':
                    rb.append(player.currentProj)
                elif player.pos == 'WR':
                    wr.append(player.currentProj)
                elif player.pos == 'TE':
                    te.append(player.currentProj)
                elif player.pos == 'K':
                    k.append(player.currentProj)
                elif player.pos == 'DEF':
                    dst.append(player.currentProj)
                else:
                    print('position not recognized')

            qb1 = max(qb)
            qb.remove(qb1)

            rb1 = max(rb)
            rb.remove(rb1)
            rb2 = max(rb)
            rb.remove(rb2)

            wr1 = max(wr)
            wr.remove(wr1)
            wr2 = max(wr)
            wr.remove(wr2)

            te1 = max(te)
            te.remove(te1)

            k1 = max(k)

            dst1 = max(dst)

            flex = rb + wr + te
            flex1 = max(flex)
            flex.remove(flex1)

            superFlex = flex + qb
            superFlex1 = max(superFlex)

            total = qb1 + rb1 + rb2 + wr1 + wr2 + te1 + k1 + dst1 + flex1 + superFlex1
            
            team.currentProj = total
            team.save()

