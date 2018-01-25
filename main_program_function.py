import ebaysdk,json
import statistics
import re
from ebaysdk.finding import Connection as finding
import csv
import os.path
import random
import pandas as pd
import numpy as np
from abhi import *
from pandas import DataFrame
from foil_test import*
from amount_of_cards import*
from condition_of_cards import*
from write_csv import*


def get_data(prefix, cardname, sets, language):

    key = '{} {} {} {}'.format(prefix, cardname, sets, language)
    cardname_for_fun_input = '{}'.format(cardname)
    edition_for_fun_input = '{}'.format(sets)

    api = finding(siteid='EBAY-US', appid='PeerRich-Snapcard-PRD-38ad16031-09f66a66', config_file=None)
    #print (key)

    options = {'keywords':key,
               'itemFilter': [{'name': 'Condition', 'value': 'Used'},
                              {'name': 'MinPrice', 'value': '0', 'paramName': 'Currency', 'paramValue': 'USD'},
                              {'name': 'MaxPrice', 'value': '25000', 'paramName': 'Currency', 'paramValue': 'USD'} ],

                'paginationInput': {'entriesPerPage': '25','pageNumber': '1'},
                'sortOrder': 'CurrentPriceHighest'
               }

    api.execute('findItemsByKeywords',options)

    dictstr = api.response.dict()  # creating a dictionary and storing in dictstr as keys and values
    #print (dictstr)
    data = []

    for item in dictstr['searchResult']['item']:

        d = {}
        d['itemID'] = item['itemId']
        d['title'] = item['title']
        d['categoryId'] = item['primaryCategory']['categoryId']
        d['offered_price'] = float(item['sellingStatus']['currentPrice']['value'])
        d['data_amt_cards'] = float( amount_of_cards(item['title']))
        d['avg_offered_card_price'] = d['offered_price'] /d['data_amt_cards']
        d['condition'] = get_condition(item['title'])
        d['foil'] = foil(item['title'])

        data.append(d)


    return data

def main():
    prefix = 'mtg'
    cardname = 'Orcish Bloodpainter'
    edition = 'Coldsnap'
    language = ''

    basic_details_offeredCards = {'Prefix':prefix, 'Cardname':cardname, 'Edition':edition}

    data_desc = get_data(prefix, cardname, edition, language)

    data_condition = get_condition_offered_cards(data_desc)

    data_foil = writing_foil (data_desc)
    #print (data_foil)

    data_analysis = analyze(data_desc)
    data_analysis_foil = foil_price_and_analysis (data_desc)

    overall_offeredCards = ('cardsoffered_xxx.csv', data_desc, basic_details_offeredCards, data_analysis)
    #print (overall_offeredCards)
    overall_offeredCardsfoil = ('cardsoffered_xxx.csv', data_desc, basic_details_offeredCards, data_analysis_foil)
    overall_write_2_csv (data_foil, overall_offeredCards, overall_offeredCardsfoil)

    

if __name__ == '__main__':
    main()
# Put all the hard core values on this page, whereas for all the functions there should not be any hard core values. They should be in variables. Make the functions smaller and use your brain.
