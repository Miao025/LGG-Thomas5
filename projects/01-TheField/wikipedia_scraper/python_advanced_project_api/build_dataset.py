
import requests
from collections import defaultdict
from pprint import pprint
from wikidata.client import Client
import json

wikidata_client = Client()

countries_language = {
    "fr": "fr",
    "be": "nl",
    "us": "en",
    "ru": "ru",
    "ma": "ar"
}

countries_position_wikidata = {
    "fr": "Q191954",
    "be": "Q213107",
    "us": "Q11696",
    "ru": "Q218295",
    "ma": "Q14566719"
}

results = defaultdict(list)
for country, position in countries_position_wikidata.items():
    query = """
        SELECT ?uri ?label  WHERE {
            ?uri wdt:P39 wd:%s.
            ?uri wdt:P31 wd:Q5;
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
        }
    """ % (position)
    r = requests.get("https://query.wikidata.org/sparql", params = {'format': 'json', 'query': query})
    for elm in r.json()["results"]["bindings"]:
        results[country].append(elm["uri"]["value"].split("/")[-1])

for country, presidents in results.items():
    wikilanguage = countries_language[country]
    president_list = []
    for president_id in presidents:
        
        entity = wikidata_client.get(president_id, load=True)

        try:
            birth_date = entity[wikidata_client.get("P569")].strftime("%Y-%m-%d")
        except:
            birth_date = None
            
        try:
            death_date = entity.get(wikidata_client.get("P570")).strftime("%Y-%m-%d")
        except:
            death_date = None
       
        try:
            first_name = entity[wikidata_client.get("P735")].label
        except:
            first_name = None
            
        try:
            last_name = entity[wikidata_client.get("P734")].label
        except:
            last_name = None
            
        try:
            place_of_birth = entity[wikidata_client.get("P19")].label
        except:
            place_of_birth = None
        
        
        r = requests.get(f"https://www.wikidata.org/wiki/Special:EntityData/{president_id}.json").json()["entities"][president_id]
        
        wikipedia_url = r["sitelinks"][f"{wikilanguage}wiki"]["url"]
        
        start_mandate = None
        end_mandate = None
        for claim in r["claims"]["P39"]:
            if claim["mainsnak"]["datavalue"]["value"]["id"] == countries_position_wikidata[country]:
                try:
                    start_mandate = claim["qualifiers"]["P580"][0]["datavalue"]["value"]["time"][1:11]
                except:
                    start_mandate = None
                try:
                    end_mandate = claim["qualifiers"]["P582"][0]["datavalue"]["value"]["time"][1:11]
                except:
                    end_mandate = None
        
        
        president_list.append({
            "id": president_id,
            "first_name": str(first_name),
            "last_name": str(last_name),
            "birth_date": birth_date,
            "death_date": death_date,
            "place_of_birth": str(place_of_birth),
            "wikipedia_url": wikipedia_url,
            "start_mandate": start_mandate,
            "end_mandate": end_mandate
        })
        
        
    pprint(president_list)
    with open(f'{country}.json', 'w') as outfile:
        json.dump(president_list, outfile, indent=4)
