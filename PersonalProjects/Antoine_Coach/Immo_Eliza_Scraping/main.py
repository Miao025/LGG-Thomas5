import os
import numpy as np
import csv
from tqdm import tqdm
from scraper.scraper import get_links, get_property_dict

def main():

    y_n='y'

    links='data\\link_table.npy'
    csv_data='data\\raw_dataset.csv'

    if os.path.isfile(links):
        y_n=input("The links are already available, do you want to regenerate them (y/n)? ")

    #Load the link_table file or generate it
    if y_n=='y':
        print("Generating list...")
        link_table=get_links(min_page=1,max_page=10) #Default to 50 pages just for testing
        np.save(links,link_table)
    else:
        print("Loading list...")
        link_table=np.load(links)

    link_table = np.unique(link_table) #Eliminate repeated values

    y_n='y'

    if os.path.isfile('data\\raw_dataset.csv'):
        y_n=input("The raw dataset already exists, do you want to regenerate it (y/n)? ")
    
    if y_n=='y':
        print("Generating the data...")
        #Create the columns
        with open(csv_data,mode='w',newline='') as f:
            d=get_property_dict(link_table[0])
            writer=csv.writer(f)
            writer.writerow(key for  key in d.keys())
        
        print("Loading the data... you can check the CSV.")
        for link in tqdm(link_table):
            d=get_property_dict(link)
            if d=={} or d is None:
                continue
            with open(csv_data,mode='a',newline='') as f:
                d=get_property_dict(link)
                writer=csv.writer(f)
                writer.writerow(value for value in d.values())

if __name__=="__main__":
    main()