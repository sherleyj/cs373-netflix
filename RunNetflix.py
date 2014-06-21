#!/usr/bin/env python3

import sys

# -------
# Imports
# -------

from Netflix import netflix_solve

# ----
# Main
# ----

netflix_solve(sys.stdin, sys.stdout)

"""
% coverage3 run --branch RunNetflix.py < RunNetflix.in > RunNetflix.out
% coverage3 report -m

% pydoc -w Collatz

"""

