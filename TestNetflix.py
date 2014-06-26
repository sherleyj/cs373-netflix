#!/usr/bin/env python3

# not sure if we can use io to test with json files
import json
import sys
from io       import StringIO
from unittest import main, TestCase
from Netflix  import netflix_load_json, netflix_write, netflix_read, netflix_eval, netflix_solve

class TestNetflix (TestCase) :

    # ----
    # read
    # ----

    def test_load_json (self) :
        file_path = "/u/mukund/netflix-tests/bryan-customer_cache.json"
        j = netflix_load_json(file_path)
        jsonFile = open(file_path, 'r')
        jsonDict = json.loads(jsonFile.read())
        self.assertEqual(j, jsonDict)
    
    def test_load_json_1 (self) :
        file_path = "/u/mukund/netflix-tests/eros-movie_cache.json"
        j = netflix_load_json(file_path)
        jsonFile = open(file_path, 'r')
        jsonDict = json.loads(jsonFile.read())
        self.assertEqual(j, jsonDict)
 
    def test_load_json_2 (self) :
        file_path = "/u/mukund/netflix-tests/rbrooks-movie_average_rating.json"
        j = netflix_load_json(file_path)
        jsonFile = open(file_path, 'r')
        jsonDict = json.loads(jsonFile.read())
        self.assertEqual(j,jsonDict)

    # -----
    # write
    # -----
   
    def test_write (self) :
        w = StringIO()
        data = "4590:"
        netflix_write(w, data)
        self.assertEqual(w.getvalue(), "4590:\n")

    def test_write_1 (self) :
        w = StringIO()
        data = "3290"
        netflix_write(w, data)
        self.assertEqual(w.getvalue(), "3290\n")

    def test_write_2 (self) :
        w = StringIO() 
        data = "1:"
        netflix_write(w, data)
        self.assertEqual(w.getvalue(), "1:\n")   
 
    # ----
    # read
    # ----
    
    def test_read (self) :
        r = StringIO("4590:\n1\n2\n")
        i = netflix_read(r)
        self.assertEqual(i, "4590:\n")

    def test_read_1 (self) :
        r = StringIO("\n")
        i = netflix_read(r)
        self.assertEqual(i,"\n")

    def test_read_2 (self) :
        r = StringIO("67\n")
        i =netflix_read(r)
        self.assertEqual(i, "67\n")

    # ----
    # eval
    # ----
    
    def test_eval (self) :
        customer = "30878"
        movie = "1"
        j = netflix_eval(customer, movie)
        self.assertEqual(j, 3.7)

    def test_eval_1 (self) :  
        customer = "43671"
        movie = "2877"
        j = netflix_eval(customer,movie)
        self.assertEqual(j, 3.3)
    
    def test_eval_2 (self) :
        customer = "1573433"
        movie = "9960"
        j = netflix_eval(customer, movie)
        self.assertEqual(j, 4.0)

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("2043:\n1417435\n2312054\n462685\n1:\n30878\n2647871")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "2043:\n3.7\n4.0\n3.8\n1:\n3.7\n3.4\nRMSE: 1.2124\n")

    def test_solve_1 (self) :
        r = StringIO("10:\n1952305\n1531863\n2043:\n1417435\n2312054\n462685\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "10:\n3.3\n3.2\n2043:\n3.7\n4.0\n3.8\nRMSE: 1.2836\n")



main()

