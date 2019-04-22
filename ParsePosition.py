import json
import pandas as pd
from ParseData import parse_data, K, GameMode, Side

def parse_positions():
    with open('positionsFile.json', 'r') as file:
        data = file.read()
        dataJson = json.loads(data)
        matches = []
        for k in dataJson:
            match = dataJson[k]
            for m in match:
                val = { K.gameId.value: int(k),
                       'timestamp': int(m['timestamp']),
                       'x': int(m['x']),
                       'y': int(m['y'])
                       }
                matches.append(val)

        df = parse_data()

        return pd.merge(df, pd.DataFrame(matches), on=K.gameId.value)


# df = parse_data()
# classic = df.loc[df[K.gameMode.value] == GameMode.CLASSIC.value]
# blue = classic.loc[classic[K.teamId.value] == Side.RED.value]
#
# dataP=parse_positions()
# # print(list(blue[K.gameId.value]))
# # dataP=dataP.loc[dataP['match'].isin(blue[K.gameId.value])]
#
#
# print()