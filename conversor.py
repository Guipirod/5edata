
import sys
import json

FILE_NAME = sys.argv[1]
URL_BASE = "https://raw.githubusercontent.com/Guipirod/5edata/master/"
IMAGES = "images"
TOKENS = "tokens"
true = True
false = False


with open(FILE_NAME, 'r') as json_file:
    json_data = json.load(json_file)
    for index in range(len(json_data["monster"])):
        # change token path
        print(">>> NAME", json_data["monster"][index]["name"])
        if "tokenUrl" in json_data["monster"][index].keys():
            token_url = json_data["monster"][index]["tokenUrl"]
            token_name = token_url.split("/")[-1]
            json_data["monster"][index]["tokenUrl"] = URL_BASE+TOKENS+'/'+token_name
            print("TOKEN", token_url, "-->", URL_BASE+TOKENS+'/'+token_name)
        # change image path
        if "fluff" in json_data["monster"][index].keys():
            for index2 in range(len(json_data["monster"][index]["fluff"]["images"])):
                image_url = json_data["monster"][index]["fluff"]["images"][index2]["href"]["url"]
                image_name = image_url.split("/")[-1]
                json_data["monster"][index]["fluff"]["images"][index2]["href"]["url"] = URL_BASE+IMAGES+'/'+image_name
                print("IMAGE", token_url, "-->", URL_BASE+IMAGES+'/'+image_name)

new_name = '.'.join(FILE_NAME.split('.')[:-1])
with open(new_name+'_Online.json', 'w') as new_file:
    json.dump(json_data, new_file)
