import json
import yaml

with open("myfile.json", "r") as json_file:
    ourjson = json.load(json_file)
print(ourjson)
print("Su token de acceso es: {}".format(ourjson["access_token"]))
print("Su token de expira en {} Segundos".format(ourjson["expires_in"]))
