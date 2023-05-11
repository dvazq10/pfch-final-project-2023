import csv
import json

with open('doginpaintings.json', 'r') as f:
    wikidata = json.load(f)

output_data = []
for output in wikidata['results']['bindings']:
    row = {}
    if 'painting' in output:
        row['Painting QID'] = output['painting']['value']
    else:
        row['Painting QID'] = None

    if 'paintingLabel' in output:
        row['Painting Label'] = output['paintingLabel']['value']
    else:
        row['Painting Label'] = None

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

    if 'describedaturlLabel' in output:
        row['Described At URL'] = output['describedaturlLabel']['value']
    else:
        row['Described At URL'] = None

    if 'copyrightstatusLabel' in output:
        row['Copyright Status'] = output['copyrightstatusLabel']['value']
    else:
        row['Copyright Status'] = None

    if 'timeperiodLabel' in output:
        row['Time Period'] = output['timeperiodLabel']['value']
    else:
        row['Time Period'] = None

    if 'inceptionLabel' in output:
        row['Inception'] = output['inceptionLabel']['value']
    else:
        row['Inception'] = None

    if 'image' in output:
        row['Image'] = output['image']['value']
    else:
        row['Image'] = None

    if 'titleLabel' in output:
        row['Title of Artwork'] = output['titleLabel']['value']
    else:
        row['Title of Artwork'] = None

    output_data.append(row)

with open('doginpaintings.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=output_data[0].keys()
    writer.writeheader()
    for row in output_data:
        writer.writerow(row)

        