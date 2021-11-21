
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

    
            
