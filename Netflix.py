#!/usr/bin/env python3

"""
    -input: list of one movie id followed by several cutomer ids
    -must predict that movie's rating for each customer.
"""
import json, sys
from functools import reduce
from math      import sqrt
from sys       import version
from time      import clock

def sqre_diff (x, y) :
    return (x - y) ** 2


def netflix_read_json (key, file_path) :
    """
    read in one line.
    """
    jsonFile = open(file_path, 'r')
    customersDict = json.loads(jsonFile.read())
    customerRating = (customersDict[key])
    jsonFile.close()
    
    return customerRating

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
    #return s.strip(':')

def netflix_is_movie (s) :
    s = s[::-1]
    return s.startswith(':')


def netflix_write (w, v) :
    """
    write to json file
    
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile)
    outfile.close()
    """
    w.write(str(v) + "\n") 

def rmse_zip_reduce (a, p) :
    """
    compute root mean square deviation
    O(1) in space
    O(n) in time
    """
    assert(hasattr(a, "__len__"))
    assert(hasattr(p, "__len__"))
    assert(hasattr(a, "__iter__"))
    assert(hasattr(p, "__iter__"))
    assert(len(a) == len(p))
    s = len(a)
    v = sum(map(sqre_diff, a, p))
    return sqrt(v / s)


def netflix_eval (customer, movie) :
    """
    compute prediction for what a customer will
    rate a given movie
    """        
    customer_avg  = netflix_read_json(customer, 
    "/u/mukund/netflix-tests/bryan-customer_cache.json")
    movie_avg = netflix_read_json(movie, 
    "/u/mukund/netflix-tests/rbrooks-movie_average_rating.json")    
        

    p_movie_rating = int(customer_avg + movie_avg)/2
    
    return p_movie_rating


def netflix_solve (r, w) :
    """
    r is input file with movie ID, followed by customers
    that rated that movie.
    """
    movie = "1"
    customer = "1" 
    rating  = "1"
    while True : 
        a = netflix_read(r)
        if netflix_is_movie(a) :
            netflix_write(w, a)
            movie = a.strip(':')
        else :
            customer = a
            rating = netflix_eval (customer, movie)
            netflix_write (w, rating)


