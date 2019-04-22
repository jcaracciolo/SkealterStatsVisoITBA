import json
files = ["0-99.json", "100-199.json", "200-299.json", "300-399.json", "400-499.json", "500-503.json"]

matches = []
for f_name in files:
    file = open(f_name, "r")
    data = file.read()


    formattedData = "{ 'matches': " + data + "}"
    array = json.loads(formattedData.replace("'","\""))
    matches.extend(array["matches"])
    file.close()


formattedData = "{ 'matches': " + str(matches) + "}".replace("'","\"")
file = open("matches.json", "w")
file.write(formattedData)
file.close()