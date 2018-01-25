# calculating the number of cards in a pcak
import ebaysdk,json
import statistics
import re
from ebaysdk.finding import Connection as finding
import csv

def amount_of_cards(test_str):
    quantityregex = re.compile("(\d)x|x(\d)|(playset)", re.IGNORECASE)
    res = quantityregex.findall(test_str)
    qty = 1
    for item in res:
        temp = item[0] * 1
        if temp:
            qty = temp
        temp = item[1] * 1
        if temp:
            qty = temp
        temp = item[2]
        if temp != "":
            qty = 4

    return qty
