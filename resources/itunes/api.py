import requests
import json

T='song'
TERM='2017'
country='us'
LIMIT=200
ENTITY='musicTrack'

URL='https://itunes.apple.com/search?term=%s&limit=%d&country=%s&entity=%s&releaseYearTerm=%s&attribute=artistTerm' %(T,LIMIT,country,ENTITY,TERM)
res = requests.get(URL)
res2=json.loads(res.text)
with open('songUS.text', 'w') as outfile:
    json.dump(res2, outfile)

#with open('res2.json') as f:
#    data = json.load(f)

#df = json_normalize(data)

#df.to_csv('Output.csv')

#print (res2)