import requests

import json

url = "https://query.wikidata.org/sparql"

sparql ="""

SELECT ?painting ?paintingLabel ?image ?location ?locationLabel ?collection ?collectionLabel ?ownedby ?ownedbyLabel ?creator ?creatorLabel ?madefrommaterial ?madefrommaterialLabel ?country ?countryLabel ?genre ?genreLabel ?describedaturl ?describedaturlLabel ?copyrightstatus ?copyrightstatusLabel ?timeperiod ?timeperiodLabel ?movement ?movementLabel ?inception ?inceptionLabel ?title ?titleLabel 
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

with open('doginpaintings.json', 'w') as f:
    json.dump(wikidata, f)

    for output in wikidata['results']['bindings']:
        row = {}
        if 'painting' in output:
            row['painting QID'] = output['painting']['value']
        else:
            row['painting QID'] = None

        if 'locationLabel' in output:
            row['Location'] = output['locationLabel']['value']
        else:
            row['Location'] = None

        if 'movementLabel' in output:
            row['Movement'] = output['movementLabel']['value']
        else:
            row['Movement'] = None

        if 'collectionLabel' in output:
            row['Collection'] = output['collectionLabel']['value']
        else:
            row['Collection'] = None

        if 'ownedbyLabel' in output:
            row['Owned By'] = output['ownedbyLabel']['value']
        else:
            row['Owned By'] = None

        if 'creatorLabel' in output:
            row['Creator'] = output['creatorLabel']['value']
        else:
            row['Creator'] = None

        if 'madefrommaterialLabel' in output:
            row['Made From Material'] = output['madefrommaterialLabel']['value']
        else:
            row['Made From Material'] = None

        if 'countryLabel' in output:
            row['Country'] = output['countryLabel']['value']
        else:
            row['Country'] = None

        if 'describedaturl' in output:
            row['Described At URL'] = output['describedaturlLabel']['value']
        else:
            row['Described At URL'] = None

        if 'copyrightstatusLabel ' in output:
            row['Copyright Status'] = output['copyrightstatusLabel ']['value']
        else:
            row['Copyright Status'] = None

        if 'timeperiodLabel' in output:
            row['Time Period'] = output['timeperiodLabel']['value']
        else:
            row['Time Period'] = None

        if 'inceptionLabel ' in output:
            row['Inception'] = output['inceptionLabel']['value']
        else:
            row['Inception'] = None

        if 'image' in output:
            row['Image'] = output['image']['value']
        else:
            row['Image'] = None

        if 'title' in output:
            row['Title'] = output['titleLabel']['value']
        else:
            row['Title'] = None
