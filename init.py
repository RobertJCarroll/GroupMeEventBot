import json
from gm_bot_listener import GMBotHandler,GMBotServer

with open('my_creds.json') as json_creds: creds = json.load(json_creds)

s = GMBotServer(creds.get('port'),creds.get('msg_dump_dir'))
