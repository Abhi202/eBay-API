import ebaysdk,json
import statistics
import re
from ebaysdk.finding import Connection as finding
import csv
import random
import os.path
import pandas as pd
from pandas import DataFrame
from abhi import *
from condition_of_cards import *
#----------------- funtion for writing csv----------------------

def write_csv_on_condition (filepath, data, initials, analysis, foil):

    condition_of_cards = list((object['condition'] for object in data))
    prefix = initials['Prefix']
    cardname = initials['Cardname']
    edition = initials['Edition']

    number_of_searchResults = analysis['Number of Search Results for Offered Price']
    eBayHigh = analysis['eBay High']
    eBayMedian = analysis['eBay Median']
    eBayLow = analysis['eBay Low']
    eBayAverage = analysis['eBay Average']

    source = filepath, cardname, edition, number_of_searchResults, eBayHigh, eBayMedian, eBayLow, eBayAverage, foil

    for item in condition_of_cards:

        if item == 'Not Defined':
            if check_if_already_exists (source) == False:
                writing_all_cards(source)

        elif item == 'Played':
            if check_if_already_exists (source) == False:
                writing_all_cards(source)

        elif item == 'Near Mint':
            if check_if_already_exists (source) == False:
                writing_all_cards(source)

        elif item == 'Good':
            if check_if_already_exists (source) == False:
                writing_all_cards(source)

        elif item == 'Excellent':
            if check_if_already_exists (source) == False:
                writing_all_cards(source)

        else:
            item = 'Damaged'
            if check_if_already_exists (source) == False:
                writing_all_cards(source)



#------------------ cheacking if the file haveing the same data exits

def check_if_already_exists (source_data):
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

    dict_cards = {'iD':str(b), 'Cardname':str(cardname),'Edition':str(edition),'No. of Search Results':str(number_of_searchResults),'eBay High':str(eBayHigh),'eBay Median':str(eBayMedian),'eBay Low':str(eBayLow),'eBay Average':str(eBayAverage),'eBay Foil':str(eBayFoil)}

    with open (filepath,'r') as file_read:

        headers = ['iD', 'Cardname', 'Edition', 'No. of Search Results', 'eBay High', 'eBay Median', 'eBay Low', 'eBay Average', 'eBay Foil']
        reader = csv.DictReader(file_read, delimiter=',', lineterminator='\n',fieldnames=headers)

        for row in reader:

            if row == dict_cards:
                return True

        return False
