from builtins import bot
from combinatorics.combinatorics_functions import *
import math

def prob(n : int, r : int, p : int):
    """
    Returns the binomial probability of N trials with R successes, each success
    having a probability of P (0 <= P <= 1, 0 <= R <= N, N > 0).
    """
    return combinations(n, r) * (p**r) * ((1-p)**(n-r))

def stdev(n : int, p : int):
    """
    Returns the standard deviation of a binomail distribution
    given N events and a probability of success p (0 <= p <= 1)
    """
    return math.sqrt(n * p * (1 - p))