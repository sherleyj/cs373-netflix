#!/usr/bin/env python3

# not sure if we can use io to test with json files
from io       import StringIO
from unittest import main, TestCase
from Netflix  import netflix_read_json, netflix_write, netflix_eval, netflix_is_movie, netflix_solve

class TestNetflix (TestCase) :

    # ----
    # read
    # ----

    def test_read_json (self) :
        key = "291"
        file_path = "/u/mukund/netflix-tests/bryan-customer_cache.json"
        j = netflix_read_json(key, file_path)
        self.assertEqual(j, 3.48)
    
    def test_read_json_1 (self) :
        key = "3926"
        file_path = "/u/mukund/netflix-tests/eros-movie_cache.json"
        j = netflix_read_json(key, file_path)
        self.assertEqual(j,["2.5", "0.69"])
 
    def test_read_json_2 (self) :
        key = "2043"
        file_path = "/u/mukund/netflix-tests/rbrooks-movie_average_rating.json"
        j = netflix_read_json(key, file_path)
        self.assertEqual(j, 3.7776648456358783)


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

    # ----
    # eval
    # ----
    
    def test_eval (self) :
        customer = "6"
        movie = "3926"
        j = netflix_eval(customer, movie)
        #self.assertEqual(j, 3.42)


    def test_is_movie (self) :
        s = "4:\n"
        j = netflix_is_movie(s)
        self.assertEqual(j, True)

    def test_is_movie_1 (self) :
        s = "24\n"
        j = netflix_is_movie(s)
        self.assertEqual(j, False)

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("2043:\n1417435\n2312054\n462685\n")
        #10851:\n1417435\n2312054\n462685")
        w = StringIO("")
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "2043:\n3.4\n4.1\n1.9\n")

#        10851:\n4.3\n1.4\n2.8")

main()

