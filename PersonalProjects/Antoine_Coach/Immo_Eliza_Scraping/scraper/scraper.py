from bs4 import BeautifulSoup
import requests
import cloudscraper
import numpy as np
import json
import os

scraper = cloudscraper.create_scraper()


def get_links(min_page=1,max_page=333,base_string="https://www.immoweb.be/en/search/house/for-sale?countries=BE&page="):

    link_table=[]

    #Loop through the pages
    for i in range(min_page,max_page):

        r = scraper.get("https://www.immoweb.be/en/search/house/for-sale?countries=BE&page="+str(i))
        soup = BeautifulSoup(r.content,"html.parser")

        elems=soup.find_all("a", class_="card__title-link")

        for elem in elems: # Get the links
            link_table.append(elem['href'])
    
    return link_table

def nested_dict_get(d,key_list):
    for key in key_list:
        d=d.get(key,None)
        if d is None:
            return d
    return d

def get_property_dict(link):

    #Placeholder for dictionary from the page
    d={}
    r=scraper.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    elems=soup.find_all("script")

    for elem in elems:
        to_analyse = elem.text

        if 'window.classified' in to_analyse:#Load the dictionary by taking the substring which represents it
            start=to_analyse.index('{"id":')
            end=to_analyse.index('}};')+2
            try:
                d=json.loads(to_analyse[start:end])
            except:
                print("Error with dictionary\n\n", to_analyse[start:end+10])
                return {}

    final_dict = {}

    final_dict['property-id'] = nested_dict_get(d, ['id'])
    final_dict['locality_name'] = nested_dict_get(d, ['property', 'location', 'district'])
    final_dict['postal_code'] = nested_dict_get(d, ['property', 'location', 'postalCode'])
    final_dict['price'] = nested_dict_get(d, ['transaction', 'sale', 'price'])
    final_dict['type_prop'] = nested_dict_get(d, ['property', 'type'])
    final_dict['subtype_prop'] = nested_dict_get(d, ['property', 'subtype'])
    final_dict['type_sale'] = nested_dict_get(d, ['transaction', 'type'])
    final_dict['room_count'] = nested_dict_get(d, ['property', 'bedroomCount'])
    final_dict['living_area'] = nested_dict_get(d, ['property', 'netHabitableSurface'])
    final_dict['kitchen'] = nested_dict_get(d, ['property', 'kitchen', 'type'])
    final_dict['furnished'] = nested_dict_get(d, ['transaction', 'sale', 'isFurnished'])
    final_dict['open_fire'] = nested_dict_get(d, ['property', 'fireplaceExists'])
    final_dict['terrace'] = nested_dict_get(d, ['property', 'terraceSurface'])
    final_dict['garden'] = nested_dict_get(d, ['property', 'gardenSurface'])
    final_dict['surface_of_good'] = nested_dict_get(d, ['property', 'land', 'surface'])
    final_dict['facade_count'] = nested_dict_get(d, ['property', 'building', 'facadeCount'])
    final_dict['swimming_pool'] = nested_dict_get(d, ['property', 'hasSwimmingPool'])
    final_dict['state_building'] = nested_dict_get(d, ['property', 'building', 'condition'])

    return final_dict