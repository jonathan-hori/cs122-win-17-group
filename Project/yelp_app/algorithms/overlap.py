import sqlite3
import pandas as pd
import json
import operator as op
import numpy as np
import scipy as sp
from math import sqrt, erf, log

# include function for sql calls
# include function that sends sqlcall to pandas database
# pandas db w/ column for each user where row is for a different rest.

# weighting functions to try out


#lognormal cdf function
#ended up not using because it makes all values the same 
def weighting(x, u, s):
    '''
    '''
    return  (1 / 2) * (1 + erf((x - u)/(log(s) * sqrt(2))))

# counts

def count_intersections(user_reviews):
    '''
    '''

    count_dict = {}
    for i_d in user_reviews["business_id"]:
        if i_d not in count_dict:
            count_dict[i_d] = 1
        else:
            count_dict[i_d] += 1

    # normalizes the scores so that they add to 1
    for key in count_dict:
        count_dict[key] = count_dict[key] / len(user_reviews["business_id"])
        #count_dict[key] = weighting(count_dict[key], 0 , .125)
    
    
    return count_dict
