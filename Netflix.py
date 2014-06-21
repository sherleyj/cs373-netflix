#!/usr/bin/env python3

"""
    -input: list of one movie id followed by several cutomer ids
    -must predict that movie's rating for each customer.
"""
import json, sys


"""
    read in one line.
"""
def collatz_read () :
    jsonFile = open("/u/sj8346/cs373/netflix-tests/mwham-probeRatings.json", 'r')
    customersDict = json.loads(jsonFile.read())
    customerRating = (customersDict["1024"])
    jsonFile.close()
    
    return customerRating

"""
    compute root mean Root Mean Square Deviation
"""
def rmsr (a, p) :
    return 1

"""
    compute prediction for what a cutomer will
    rate a given movie
"""
def netflix_eval (customer, movie) :
    return 1

"""
    r is reader
    w is writer
"""
def netflix_solve (r, w) :
    return 1


print( collatz_read())
