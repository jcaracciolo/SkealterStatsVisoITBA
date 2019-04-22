import json
from collections import defaultdict

file = open("matches.json", "r")
data = file.read().replace("'", "\"")
matches = json.loads(data)

array = matches["matches"]
# {'platformId': 'LA2', 'gameId': 323732824, 'champion': 98, 'queue': 410, 'season': 7, 'timestamp': 1462045096814, 'role': 'SOLO', 'lane': 'TOP'}
champions = defaultdict(lambda: 0, {})
queue = defaultdict(lambda: 0, {})
season = defaultdict(lambda: 0, {})
role = defaultdict(lambda: 0, {})
lane = defaultdict(lambda: 0, {})

for m in array:
    champions[m["champion"]] += 1
    queue[m["queue"]] += 1
    season[m["season"]] += 1
    role[m["role"]] += 1
    lane[m["lane"]] += 1


print(champions)
print(queue)
print(season)
print(role)
print(lane)

file.close()