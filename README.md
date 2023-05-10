# pfch-final-project-2023

<h2><b>"<i>Wikidata Project: Human's best friend portrayed in paintings</i>"</b>

An exploration of  dogs painted by artists found on wikidata's open data repository.</h2>

<h3><b>Introduction</b></h3>

The inspiration for my project came to me while visiting the Metropolitan Museum of Art. I came across an exhibition called "In Praise of Painting: Dutch Masterpieces at The Met". As a dog owner, I found myself spotting all the dogs in the various domestic paintins on view while I perused the gallery. Later on when I started my project, I elected to explore the various items in wikidata and narrow my query down to depictions of dogs in all instances of paintings. My main goal was to extract as much information as I could, and explore the data.

<h3><b>Dataset</b></h3>

The main source of the data came from Wikidata, an open data repository. 
I used the Wikidata Query Service to construct a SPARQL query to explore the data I wanted in Wikidata.

<h3><b>Method</b></h3>

Step I: Wikidata Query Service

My first step was to construct a query using Wikidata Query Service and test it with their visual interface for errors, and then review results. 

The query was built with the intention of gathering QID's which have the property "instance of" with a the value of "painting" <b>and</b> also "depicts" with the value "dog". In addition, the query includes these optional properties that I thought would be most informative:

<i>image | location | collection | owned by | creator | made from material | country | genre | described at URL | copyright status | time period | movement | inception | title </i>
   
 You can run the query I built with this link: https://w.wiki/6g6t


<b>Step II:</b> 2_output_from_wikidata.py

The next step uses python's requests and json module. The objective of this script was to receive the data back with json headers and view the printed output in the terminal.

<b>Step III:</b> 3_output_to_json_from_wikidata.py

This file includes the script to write the data recieved from wikidata's endpoint to a JSON file with the chosen key values. The file that was created with this is doginpaintings.json 

<b>Step IV:</b> 4_json_to_csv_wikidata.py

This script was created to transfrom the json file I created previously to a CSV file. 
The output of this script is this file: doginpaintings.csv

<b>Step V:</b> wikidata_clean_doginpaintings.csv
This file was the dataset used to create visualizations. It was cleaned with a combination of OpenRefine and Microsoft Excel. 

<h3><b>Visualization</b></h3>
Visit ...... to view findings and visualizations.

<h3><b>Conclusion</b></h3>

The data exported from wikidata's endpoint ended up including multiple repetitive records, leading to an over estimate of results at first glance. After hours of cleaning the data for duplicates, the total went from about ~11k to ~2k rows of data. I think in the future I would need to create a script that fixes this problem becuause it was time consuming to go through every single row in Microsoft Excel. OpenRefine was used for simple transformations. Ultimately, I think there was still a decent amount of results to interpret!






   
  









