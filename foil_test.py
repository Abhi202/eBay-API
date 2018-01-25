import ebaysdk,json
import statistics
import re
from ebaysdk.finding import Connection as finding
from condition_of_cards import*
import csv
import pandas as pd
from pandas import DataFrame
#--------------------- testing a card to be foil or not foil -----------------------------
def foil(test_str):

    foil_regex = re.compile("(foil)", re.IGNORECASE)
    foil_res = foil_regex.findall(test_str)
    condition = 'No'
    for item in foil_res:
        temp = item[0]
        if item:
            condition = 'Foil'
    return condition

def writing_csv (filename,data):
    myFile = open( filename, 'a')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows([data])

#------------------------- analyzing the data --------------------------------------------

def analyze (data):

    offered_price_depending_upon_cards = [x.get('avg_offered_card_price') for x in data[:]]
    offered_price_condition = [x.get('foil') for x in data[:]]
    offeredCards_dict = {'Price of Offered Cards':offered_price_depending_upon_cards, 'Foil':offered_price_condition }
    df = pd.DataFrame (offeredCards_dict)
    price_offeredCards = df[df.Foil == 'No']
    list_of_offeredCard_prices = price_offeredCards['Price of Offered Cards'].tolist()

    eBay_low_offeredPrice = round(min(list_of_offeredCard_prices),2)
    eBay_high_offeredPrice = round(max(list_of_offeredCard_prices),2)
    eBay_median_offeredPrice = round(statistics.median(list_of_offeredCard_prices),2)
    eBay_mean_offeredPrice = round(statistics.mean(list_of_offeredCard_prices),2)
    num_of_searchResults_offered = len(offered_price_depending_upon_cards)

    analyzed_data = {'eBay High':eBay_high_offeredPrice, 'eBay Low':eBay_low_offeredPrice, 'eBay Median':eBay_median_offeredPrice,'eBay Average':eBay_mean_offeredPrice, 'Number of Search Results for Offered Price':num_of_searchResults_offered
                    }
    #print (analyzed_data)
    return analyzed_data

#------------------------- computing the condition of cards --------------------------------

def get_condition_offered_cards(data):

    title_offered = [x.get('title') for x in data[:]]
    #print (title_offered)

    d = []
    #d_foil = []
    for item in title_offered:

        condition = get_condition (item)

        d.append(condition)

        #condition_foil = foil (item)
        #d_foil.append(condition_foil)

    return {'Condition of the Offered Cards':d}#, 'Foil Y/N':d_foil}

#-------------------------------------- computing foil testing ------------------------------

def writing_foil (data):
    title_offered = [x.get('title') for x in data[:]]
    #print (title_offered)
    d_foil = []
    #is_foil = False
    for item in title_offered:
        if foil(item) == 'Foil':   ## ask latet ----
            is_foil = 'Yes'
            d_foil.append (is_foil)
        else:
            is_foil = 'No'
            d_foil.append (is_foil)

    return d_foil


def foil_price_and_analysis (data):
    price_of_articles = [x.get('avg_offered_card_price') for x in data[:]]
    #print (price_of_articles)
    foil_condition = [x.get('foil') for x in data[:]]
    #print (foil_condition)
    foil_keys = {'Price of Foil Cards':price_of_articles, 'Foil':foil_condition}
    #print (foil_keys)

    df = pd.DataFrame (foil_keys)
    price_foil_cards = df[df.Foil == 'Foil']
    list_of_foilcard_prices = price_foil_cards['Price of Foil Cards'].tolist()
    #print(list_of_foilcard_prices)
    num_of_searchResults_offered = len(price_of_articles)
    #print (num_of_searchResults_offered)
    eBayHigh = round(max(list_of_foilcard_prices),2)

    eBayLow = round(min(list_of_foilcard_prices),2)
    eBayMedian = round(statistics.median(list_of_foilcard_prices),2)
    eBayAverage = round(statistics.mean(list_of_foilcard_prices),2)

    data_foil_analysis = {'Number of Search Results for Offered Price':num_of_searchResults_offered, 'eBay High':eBayHigh, 'eBay Median': eBayMedian, 'eBay Low':eBayLow, 'eBay Average':eBayAverage}

    return data_foil_analysis
