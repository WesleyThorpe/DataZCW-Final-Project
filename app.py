#1/usr/bin/env python
import urllib
import _json
import json


api = '3fcdf7812ded2ec328589bdd3e923933'
url = ('https://api.themoviedb.org/3/search/keyword?api_key=3fcdf7812ded2ec328589bdd3e923933&query=baseball')
json_obj = urllib.urlopen(url)
data = json.load(json_obj)

