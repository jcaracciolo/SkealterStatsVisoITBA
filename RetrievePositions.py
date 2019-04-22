import csv
import urllib
import json

positionFile = open("positionsFile.json", "a")
# positionFile.write("{")
with open('SkealterStats.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    c = 0
    for l in reader:
        c+=1
        if c < 396:
            continue
        id = int(l[1]) + 1
        # matchId = 646526418
        matchId = l[4]
        success = False
        contents = None

        while not success:
            try:
                print("Calling for match {match}".format(match=matchId))
                contents = urllib.request.urlopen(
                    "https://la2.api.riotgames.com/lol/match/v4/timelines/by-match/{matchId}?api_key=RGAPI-8e5628d4-7a37-42f1-9557-ac80af2f911b"
                        .format(matchId=matchId)).read()
                success = True
            except Exception as e:
                print("Failed Calling for match {match}, retrying".format(match=matchId))
                success = True

        parsed = json.loads(contents)
        positions = []
        frames = parsed["frames"]
        for i in range(0, len(frames)-1):
            positions.append([frames[i]["timestamp"], frames[i]["participantFrames"][str(id)]["position"]["x"], frames[i]["participantFrames"][str(id)]["position"]["y"]])


        positionFile.write("\""+str(matchId)+"\": [" )

        first = True
        for p in positions:
            if not first:
                positionFile.write(",")

            first = False
            positionFile.write("{\"timestamp\":" + str(p[0]) + ", \"x\": " + str(p[1]) + ", \"y\": " + str(p[2]) + "}")

        positionFile.write("],")
        positionFile.flush()

positionFile.write("}")
