#!/usr/bin/env python3

rmseSum = 0
rmseCount = 0
openFiles = []

"""
    -input: list of one movie id followed by several cutomer ids
    -must predict that movie's rating for each customer.
"""

import json
import sys
from io      import StringIO
from functools import reduce
from math      import sqrt


def netflix_load_json (file_path) :
    """
    read  json file
    """
    jsonFile = open(file_path, 'r')
    jsonDict = json.loads(jsonFile.read())
    openFiles.append(jsonFile)
    return jsonDict
    #keyValue = jsonDict[key]
    #jsonFile.close()
    
    #return keyValue

customerAvgDic = netflix_load_json( 
"/u/mukund/netflix-tests/bryan-customer_cache.json")

movieAvgDic = netflix_load_json( 
"/u/mukund/netflix-tests/rbrooks-movie_average_rating.json")

customerAvgDecadeDic = netflix_load_json(
"/u/mukund/netflix-tests/ahsu-cust_by_decade.json")

movieDecadeDic = netflix_load_json(
"/u/mukund/netflix-tests/isabella-movie_decades_cache.json")

ansCacheDic = netflix_load_json(
"/u/mukund/netflix-tests/frankc-answer_cache.json")


def sqre_diff (x, y) :
    return (x - y) ** 2


def netflix_read (r) :
    """
    r is a reader, read a line containing 
    on int and return it. If movieID, 
    removes the ':' at the end.
    """
    s = r.readline()
    if s == "" :
        return []
    return s


# def netflix_is_movie (s) :
#     return s.endswith(':\n')


def netflix_write (w, v) :
    """
    write to json file
    """
    v = str(v)
    v = v.strip('\n ')
    w.write(str(v) + "\n") 

def netflix_eval (customer, movie) :
    """
    compute prediction for what a customer will
    rate a given movie
    """
    customerAvg = customerAvgDic[customer]
    movieAvg = movieAvgDic[movie]       
    movieDecade = movieDecadeDic[movie]     # made in 1993, return 1990
    customerAvgDecade = customerAvgDecadeDic[customer][movieDecade]

    predRating = round((2*customerAvg + 3*movieAvg + customerAvgDecade)/6, 1)    
    
    actualRating = ansCacheDic[movie][customer]
#    rmse(actualRating, predRating)   
    global rmseSum
    global rmseCount
    rmseElem = sqre_diff(predRating, actualRating)
    rmseSum += rmseElem
    rmseCount += 1

    return predRating

def netflix_solve (r, w) :
    """
    r is input file with movie ID, followed by customers
    that rated that movie.
    """
    movie = "5000:"
    customer = "1" 
    rating  = "1"
    while True : 

        a = netflix_read(r)
        if not a :
            w.write("RMSE: ")
            netflix_write(w, round(sqrt(rmseSum/rmseCount), 4) )
            s = len(openFiles)
            for i in range(s) :
                openFiles[i].close()
            # close files
            return
        #a = str(a)
        if a.endswith(':\n') :
            movie = a.strip(':\n ')
            netflix_write(w, a)
        else :
            customer = a.strip('\n')
            rating = netflix_eval (customer, movie)
            netflix_write(w, rating)


