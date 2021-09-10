#import http.client
from time import sleep 
import requests
import json
import pandas as pd

# conn = http.client.HTTPSConnection("api.sportradar.us")

# conn.request("GET", "http://api.sportradar.us/nfl/official/trial/v6/en/games/2021/REG/schedule.json?api_key=zmswx8wb4rqxypk9s6hp6gpx")

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

def NFL_Extract(list_objects, week_num):
    weekly_format = []
    for i in list_objects: 
        current_week = {} 
        current_week['Week'] = week_num
        current_week['Stadium'] = i['venue']['name']
        state = ''
        if i['venue']['city'] == 'London':
            state = 'none'
        else: 
            state = i['venue']['state']
        current_week['Location'] = i['venue']['city'] + ", " + state
        current_week['Date'] = i['scheduled'][:10]
        current_week['Home_Team'] = i['home']['name']
        current_week['Away_Team'] = i['away']['name']
        current_week['Time'] = i['scheduled'][14:19]
        if week_num < 15:
            current_week['Network']= i['broadcast']['network']
        else:
            current_week['Network']='TBA' 
        weekly_format.append(current_week)
        
    return weekly_format

     
NFL_DataFrame = pd.DataFrame()

for i in range (1,17):
    result = requests.get(f'http://api.sportradar.us/nfl/official/trial/v6/en/games/2021/REG/{i}/schedule.json?api_key=zmswx8wb4rqxypk9s6hp6gpx')
    current_week = NFL_Extract(result.json()["week"]["games"], i) 
    NFL_DataFrame = NFL_DataFrame.append(pd.DataFrame(current_week))
    sleep(2)
    
    print(NFL_DataFrame)
