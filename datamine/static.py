
class Static():
    leagueID = "730630605066371072"
    usersURL = 'https://api.sleeper.app/v1/league/{}/users'.format(leagueID)
    stateURL = 'https://api.sleeper.app/v1/state/nfl'

    defenceDict = {
        #AFC North
        'BAL': 'Baltimore Ravens',
        'CIN': 'Cincintti Bengals',
        'PIT': 'Pittsburg Steelers',
        'CLE': 'Cleveland Browns',
        
        #AFC East
        'BUF': 'Buffalo Bills',
        'NE': 'New England Patriots',
        'MIA': 'Miami Dolphins',
        'NYJ': 'New York Jets',
        
        #AFC South
        'IND': 'Indianapolis Colts',
        'TEN': 'Tennesee Titans',
        'JAX': 'Jacksonville Jaguars',
        'HOU': 'Houston Texans',
        
        #AFC West
        'LAC':'Los Angeles Charges',
        'DEN': 'Denver Bronocos',
        'KC': 'Kansas City Chiefs',
        'LV': 'Las Vegas Raiders',
        
        #NFC North
        'GB':'Green Bay Packers',
        'CHI':'Chicago Bears',
        'MIN':'Minnesota Vikings',
        #DET
        
        #NFC East
        'DAL': 'Dallas Cowboys',
        'WAS': 'Washington Redskins',
        'NYG': 'New York Giants',
        'PHI': 'Philidelphia Eagles',
        
        #NFC South
        'TB': 'Tampa Bay Buccaneers',
        'NO': 'New Orleans Saints',
        'ATL': 'Atlanta Falcons',
        'CAR': 'Carolina Panthers',
        
        #NFC West
        'ARI': 'Arizona Cardinals',
        'SF': 'Sanfrancisco 49ers',
        'LAR': 'Los Angeles Rams',
        'SEA': 'Seattle Seahawks'  
    }

    rbURL = 'https://www.fantasypros.com/nfl/projections/rb.php?scoring=HALF'
    wrURL = 'https://www.fantasypros.com/nfl/projections/wr.php?scoring=HALF'
    teURL = 'https://www.fantasypros.com/nfl/projections/te.php?scoring=HALF'
    qbURL = 'https://www.fantasypros.com/nfl/projections/qb.php'
    kURL = 'https://www.fantasypros.com/nfl/projections/k.php'
    defURL = 'https://www.fantasypros.com/nfl/projections/dst.php'

    rbColumns=['Player','Rushing:Att','Rushing:Yds','Rushing:TDs','Recieving:Rec','Recieving:Yds','Recieving:TDs','Misc:FL','FPP']
    wrColumns=['Player','Recieving:Rec','Recieving:Yds','Recieving:TDs','Rushing:Att','Rushing:Yds','Rushing:TDs','Misc:FL','FPP']
    teColumns=['Player','Recieving:Rec','Recieving:Yds','Recieving:TDs','Misc:FL','FPP']
    qbColumns=['Player', 'Passing:Att','Passing:Cmp','Passing:Yds','Passing:TDs','Passing:Int','Rushing:Att','Rushing:Yds','Rushing:Tds','Misc:FL','FPP']
    kColumns=['Player', 'FG','FGA','XPT','FPP']
    defColumns=['Player','Sack','Int','FR','FF','TD','Saftey','PA','Yds Against','FPP']

    flexDtype={'Player':'object','Rushing:Att':'float','Rushing:Yds':'float','Rushing:TDs':'float','Recieving:Rec':'float',
                'Recieving:Yds':'float','Recieving:TDs':'float','Misc:FL':'float','FPP':'float'}
    teDtype= {'Player':'object','Recieving:Yds':'float','Recieving:TDs':'float','Recieving:Rec':'float','Misc:FL':'float'}
    qbDtype={'Player':'object', 'Passing:Att':'float','Passing:Cmp':'float','Passing:Yds':'float','Passing:TDs':'float',
                'Passing:Int':'float','Rushing:Att':'float','Rushing:Yds':'float','Rushing:Tds':'float','Misc:FL':'float'
                ,'FPP':'float'}
    kDtype={'Player':'object', 'FG':'float','FGA':'float','XPT':'float','FPP':'float'}
    defDtype={'Player':'object','Sack':'float','Int':'float','FR':'float','FF':'float','TD':'float','Saftey':'float','PA':'float',
                        'Yds Against':'float','FPP':'float'}

    renameDict = {'Patrick Mahomes II':'Patrick Mahomes'}

    posScoringDict = {"rb":{"rushYds":.1,
                            "rushTds":6,
                            "recYds":.1,
                            "rec":.5,
                            "recTds":6,
                            "fum":-2},
                    "wr":{"rushYds":.1,
                            "rushTds":6,
                            "recYds":.1,
                            "rec":.5,
                            "recTds":6,
                            "fum":-2},
                    "te":{"recYds":.1,
                            "recTds":6,
                            "rec":1,
                            "fum":-2},
                    "qb":{"paYds":.04,
                            "paTds":4,
                            "ints":-2,
                            "rushYds":.1,
                            "rushTds":6,
                            "fum":-2},
                    "k":{"fg3":3,
                            "fg4":4,
                            "fg5":5,
                            "xp":1}}