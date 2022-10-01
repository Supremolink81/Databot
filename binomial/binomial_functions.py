from builtins import bot
from combinatorics.combinatorics_functions import *
import math

def prob(n : int, r : int, p : int):
    return combinations(n, r) * (p**r) * ((1-p)**(n-r))

def stdev(n : int, p : int):
    return math.sqrt(n * p * (1 - p))