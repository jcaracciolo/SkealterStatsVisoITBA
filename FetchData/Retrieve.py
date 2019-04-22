import urllib.request
import json


# Retrieves all games
endIndex = 500
player = "Skealter"
secretId = "0rOkHXo-Y3_Rc8eh51fvqXBvAhK_5Y2XayXBxPRiqJ0"
for i in range(0,int(endIndex/100) + 1):
    contents = urllib.request\
        .urlopen("https://la2.api.riotgames.com/lol/match/v4/matchlists/by-account/{secretId}?beginIndex={beginIndex}&api_key=RGAPI-a3dd6f50-45b2-4b22-91ee-6c004db24796"
         .format(beginIndex=i*100, secretId = secretId)).read()

    data = json.loads(contents)
    print(data["startIndex"])
    print(" - ")
    print(data["endIndex"])
    print("\n")

    file = open(player + "{startIndex}-{endIndex}.json".format(startIndex=data["startIndex"], endIndex=data["endIndex"]-1), "w")
    file.write(str(data["matches"]))
    file.close()

