
import ebaysdk,json
import statistics
import re
from ebaysdk.finding import Connection as finding
import csv


#-------------this function gets the condition of cards---------------------------


def get_condition(title_str):
        condition_regex= re.compile("(Near Mint)|(NM)|(Excellent)|(EXC)|(light played)|(lightly played)|(Good)|(GD)|(moderately played)|(MP)|(Played)|(heavily played)|(HP)|(damage)|(damaged)|"
        , re.IGNORECASE)
        condition_res = condition_regex.findall(title_str)
        condition = 'Not Defined'
        for item in condition_res:
            #Near Mint
            temp = item[0]
            if temp:
                condition = 'Near Mint'
            temp = item[1]
            if temp:
                condition = 'Near Mint'
            #Excellent
            temp = item[2]
            if temp:
                condition = 'Excellent'
            temp = item[3]
            if temp:
                condition = 'Excellent'
            temp = item[4]
            if temp:
                condition = 'Excellent'
            temp = item[5]
            if temp:
                condition = 'Excellent'
            temp = item[6]
            if temp:
                condition = 'Good'
            temp = item[7]
            if temp:
                condition = 'Good'
            temp = item[8]
            if temp:
                condition = 'Good'
            temp = item[9]
            if temp:
                condition = 'Good'
            #played
            temp = item[10]
            if temp:
                condition = 'Played'
            temp = item[11]
            if temp:
                condition = 'Played'
            temp = item[12]
            if temp:
                condition = 'Played'
            #damaged
            temp = item[13]
            if temp:
                condition = 'Damaged'
            temp = item[14]
            if temp:
                condition = 'Damaged'
        return condition
