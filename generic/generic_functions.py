from builtins import bot
import pandas as pd
from io import StringIO
import requests

#GENERAL DATAFRAME
def make_df(items1,lab1,items2=None,lab2=None):
    return pd.DataFrame({lab1 : items1, lab2 : items2}) if items2 is not None and lab2 is not None else pd.DataFrame({lab1 : items1})

#CSV
def make_df_file(ctx):
    """
    Creates a dataframe from a csv or xsls file.
    """

    attachments = ctx.message.attachments

    # No attached files
    if len(attachments) == 0:
        raise RuntimeError
    
    file = attachments[0].url

    # Not csv or xsls file
    if not file.endswith("csv") and not file.endswith("xsls"):
        raise RuntimeError
    
    s = requests.get(file).text
    return pd.read_csv(StringIO(s))

def HELP():
    """
    String with descriptions of each command.
    """
    return ("""COMMANDS:

    FILE
    [p_q_file] plot 1-var quantitative data from csv or xsls file
    [a_q_file] analyze 1-var quantitative data from csv or xsls file
    [p_2q_file] plot 2-var quantitative data from csv or xsls file
    [a_2q_file] analyze 2-var quantitative data from csv or xsls file
    [p_c_file] plot categorical data from csv or xsls file
    [a_c_file] analyze categorical data from csv or xsls file
    QUANTITATIVE DATA
    [p_q_d] plot 1-var quantitative data
    [a_q_d] analyze 1-var quantitative data
    [p_2q_d] plot 2-var quantitative data
    [a_2q_d] analyze 2-var quantitative data
    CATEGORICAL DATA
    [p_c_d] plot categorical data
    [a_c_d] analyze categorical data
    NORMAL DISTRIBUTIONS
    [norm_prob_before] get probability a value is less than a value plugged in
    [norm_prob_between] get probability a value is between two values
    [norm_prob_after] get probability a value is greater than a value plugged in
    COMBINATORICS
    [nPr] get permutations of n choose r
    [nCr] get combinations of n choose r
    
""")