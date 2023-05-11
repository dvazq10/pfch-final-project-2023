import requests

import json

url = "https://query.wikidata.org/sparql"

sparql ="""

SELECT ?painting ?paintingLabel ?title ?titleLabel ?image ?location ?locationLabel ?collection ?collectionLabel ?ownedby ?ownedbyLabel ?creator ?creatorLabel ?madefrommaterial ?madefrommaterialLabel ?country ?countryLabel ?genre ?genreLabel ?describedaturl ?describedaturlLabel ?copyrightstatus ?copyrightstatusLabel ?timeperiod ?timeperiodLabel ?movement ?movementLabel ?inception ?inceptionLabel 
WHERE {
  ?painting wdt:P31 wd:Q3305213 .
  ?painting wdt:P180 wd:Q144 .
  
  OPTIONAL { ?painting wdt:P18 ?image . }
  OPTIONAL { ?painting wdt:P276 ?location . }
  OPTIONAL { ?painting wdt:P195 ?collection . }
  OPTIONAL { ?painting wdt:P127 ?ownedby . }
  OPTIONAL { ?painting wdt:P170 ?creator . }
  OPTIONAL { ?painting wdt:P186 ?madefrommaterial . }
  OPTIONAL { ?painting wdt:P17 ?country . }
  OPTIONAL { ?painting wdt:P136 ?genre . }
  OPTIONAL { ?painting wdt:P973 ?describedaturl . }
  OPTIONAL { ?painting wdt:P6216 ?copyrightstatus  . }
  OPTIONAL { ?painting wdt:P2348 ?timeperiod . }
  OPTIONAL { ?painting wdt:P135 ?movement . }
  OPTIONAL { ?painting wdt:P571 ?inception . }
  OPTIONAL { ?painting wdt:P1476 ?title . }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
        }
"""
params = {
    'query' : sparql

}

headers = {
    'Accept' : 'application/json'
}

r = requests.get(url, params=params, headers=headers)


wikidata = json.loads(r.text)

print(wikidata)
