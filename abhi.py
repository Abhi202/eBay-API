import ebaysdk,json
from ebaysdk.finding import Connection as finding
import csv
import os.path
import pandas as pd
from pandas import DataFrame


def writing_all_cards(source_data):

    filepath = source_data[0]
    cardname = source_data[1]
    edition = source_data[2]
    number_of_searchResults = source_data[3]
    eBayHigh = source_data[4]
    eBayMedian = source_data[5]
    eBayLow = source_data[6]
    eBayAverage = source_data[7]
    eBayFoil = source_data[8]

    df = pd.read_csv('cards.csv',index_col='id')
    b = (df.index[(df['englishName']  == '{}'.format(cardname)) & (df['edition'] == '{}'.format(edition))].tolist())
    dict_csv = {'iD':b, 'Cardname':cardname,'Edition':edition,'No. of Search Results':number_of_searchResults,'eBay High':eBayHigh,'eBay Median':eBayMedian,'eBay Low':eBayLow,'eBay Average':eBayAverage ,'eBay Foil':eBayFoil}
    keys = dict_csv.keys()

    with open(filepath, "a") as csvfile:

        fileEmpty = os.stat(filepath).st_size == 0
        headers = ['iD', 'Cardname', 'Edition', 'No. of Search Results', 'eBay High', 'eBay Median', 'eBay Low', 'eBay Average', 'eBay Foil']
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)

        if fileEmpty:
            writer.writeheader()

        writer.writerow(dict_csv)
