import altair as alt
from vega_datasets import data
import csv
import json
from enum import Enum
import datetime
import pandas as pd

class GameMode(str, Enum):
    CLASSIC = "CLASSIC"
    ARAM = "ARAM"
    ONEFORALL = "ONEFORALL"
    SNOWURF = "SNOWURF"
    STARGUARDIAN = "STARGUARDIAN"
    ASSASSINATE = "ASSASSINATE"
    ASCENSION = "ASCENSION"

class Side(int, Enum):
    BLUE = 100
    RED = 200

class K(str, Enum):
    playerId = "playerId"
    seasonId = "seasonId"
    queueId = "queueId"
    gameId = "gameId"
    gameMode = "gameMode"
    gameDuration = "gameDuration"
    gameCreation = "gameCreation"
    win = "win"
    teamId = "teamId"
    firstBlood = "firstBlood"
    firstTower = "firstTower"
    firstDragon = "firstDragon"
    firstInhibitor = "firstInhibitor"
    firstBaron = "firstBaron"
    myTeamKills = "myTeamKills"
    myTeamtowerKills = "myTeamtowerKills"
    myTeamdragonKills = "myTeamdragonKills"
    myTeaminhibitorKills = "myTeaminhibitorKills"
    myTeambaronKills = "myTeambaronKills"
    enemyTeamKills = "enemyTeamKills"
    enemyTeamtowerKills = "enemyTeamtowerKills"
    enemyTeamdragonKills = "enemyTeamdragonKills"
    enemyTeaminhibitorKills = "enemyTeaminhibitorKills"
    enemyTeambaronKills = "enemyTeambaronKills"
    participantId = "participantId"
    spell1Id = "spell1Id"
    spell2Id = "spell2Id"
    championId = "championId"
    magicDamageDealtToChampions = "magicDamageDealtToChampions"
    physicalDamageDealtToChampions = "physicalDamageDealtToChampions"
    physicalDamageTaken = "physicalDamageTaken"
    magicalDamageTaken = "magicalDamageTaken"
    totalTimeCrowdControlDealt = "totalTimeCrowdControlDealt"
    damageDealtToTurrets = "damageDealtToTurrets"
    largestKillingSpree = "largestKillingSpree"
    pentaKills = "pentaKills"
    quadraKills = "quadraKills"
    tripleKills = "tripleKills"
    doubleKills = "doubleKills"
    kills = "kills"
    deaths = "deaths"
    assits = "assits"
    totalMinionsKilled = "totalMinionsKilled"
    goldSpent = "goldSpent"
    wardsPlaced = "wardsPlace"




def match_to_object(line, SummonerSpells, Champions):
    match = {}
    column = 1
    match[K.playerId.value] = int(line[column]);    column += 1
    match[K.seasonId.value] = int(line[column]);    column += 1
    match[K.queueId.value] = int(line[column]);    column += 1
    match[K.gameId.value] = int(line[column]);    column += 1
    match[K.gameMode.value] = GameMode(line[column]);    column += 1
    match[K.gameDuration.value] = int(line[column])/60.0;    column += 1
    match[K.gameCreation.value] = datetime.datetime.fromtimestamp(int(line[column]) / 1000);    column += 1
    match[K.win.value] = 1 if line[column] == "Win" else 0;    column += 1
    match[K.teamId.value] = Side.BLUE if line[column] == Side.BLUE else Side.RED;    column += 1
    match[K.firstBlood.value] = bool(line[column]);    column += 1
    match[K.firstTower.value] = bool(line[column]);    column += 1
    match[K.firstDragon.value] = bool(line[column]);    column += 1
    match[K.firstInhibitor.value] = bool(line[column]);    column += 1
    match[K.firstBaron.value] = bool(line[column]);    column += 1
    match[K.myTeamKills.value] = int(line[column]);    column += 1
    match[K.myTeamtowerKills.value] = int(line[column]);    column += 1
    match[K.myTeamdragonKills.value] = int(line[column]);    column += 1
    match[K.myTeaminhibitorKills.value] = int(line[column]);    column += 1
    match[K.myTeambaronKills.value] = int(line[column]);    column += 1
    match[K.enemyTeamKills.value] = int(line[column]);    column += 1
    match[K.enemyTeamtowerKills.value] = int(line[column]);    column += 1
    match[K.enemyTeamdragonKills.value] = int(line[column]);    column += 1
    match[K.enemyTeaminhibitorKills.value] = int(line[column]);    column += 1
    match[K.enemyTeambaronKills.value] = int(line[column]);    column += 1
    match[K.teamId.value] = Side.BLUE.value if int(line[column]) == 100 else Side.RED.value;    column += 1
    match[K.participantId.value] = int(line[column]);    column += 1
    match[K.spell1Id.value] = SummonerSpells[int(line[column])];    column += 1
    match[K.spell2Id.value] = SummonerSpells[int(line[column])];    column += 1
    match[K.championId.value] = Champions[int(line[column])]['name'];    column += 1
    match[K.magicDamageDealtToChampions.value] = int(line[column]);    column += 1
    match[K.physicalDamageDealtToChampions.value] = int(line[column]);    column += 1
    match[K.physicalDamageTaken.value] = int(line[column]);    column += 1
    match[K.magicalDamageTaken.value] = int(line[column]);    column += 1
    match[K.totalTimeCrowdControlDealt.value] = int(line[column]);    column += 1
    match[K.damageDealtToTurrets.value] = int(line[column]);    column += 1
    match[K.largestKillingSpree.value] = int(line[column]);    column += 1
    match[K.pentaKills.value] = int(line[column]);    column += 1
    match[K.quadraKills.value] = int(line[column]);    column += 1
    match[K.tripleKills.value] = int(line[column]);    column += 1
    match[K.doubleKills.value] = int(line[column]);    column += 1
    match[K.kills.value] = int(line[column]);    column += 1
    match[K.deaths.value] = int(line[column]);    column += 1
    match[K.assits.value] = int(line[column]);    column += 1
    match[K.totalMinionsKilled.value] = int(line[column]);    column += 1
    match[K.goldSpent.value] = int(line[column]);    column += 1
    match[K.wardsPlaced.value] = int(line[column]);    column += 1
    return match


def parse_data():
    SummonerSpells = {}
    with open('SumonerSpells.json', 'r') as file:
        data = file.read()
        dataJson = json.loads(data)
        for spell in dataJson["data"]:
            spellO = dataJson["data"][spell]
            SummonerSpells[int(spellO["key"])] = spellO

    Champions = {}
    with open('champions.json', 'r') as file:
        data = file.read()
        dataJson = json.loads(data)
        for champ in dataJson["data"]:
            champO = dataJson["data"][champ]
            Champions[int(champO["key"])] = champO

    with open('SkealterStats.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        matches = []
        first = True
        for row in spamreader:
            if first:
                first = False
                continue
            matches.append(match_to_object(row, SummonerSpells, Champions))

    result_data = pd.DataFrame(matches)
    result_data['month'] = result_data[K.gameCreation.value].dt.strftime('%Y-%m')

    return result_data

def expanding_sum(s):
    return s.expanding().size()
