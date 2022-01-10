import pandas as pd # library for data analysis
import requests # library to handle requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup # library to parse HTML documents
import unicodedata as normalize
import statistics as stat
import numpy as np
import sys
import getopt

def get_state(state):
  table_state = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population#State_and_territory_rankings')
  df = table_state[0]
  retstat = None
  retpop  = None
  for i in range(0,len(df.index)):
     if df['State or territory'].values[i] == state:
        retstat = df['State or territory'].values[i]
        retpop = df['Census population[7][8][a]']['April 1, 2020'].values[i]
  return retstat, retpop 

def summarize():
   pop_data_list = []
   table_state = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population#State_and_territory_rankings')
   df = table_state[0]
   for i in range(0,len(df.index)):  
      pop_data_list.append(df['Census population[7][8][a]']['April 1, 2020'].values[i])
   pop_data_list.sort()
   median_ret = stat.median(pop_data_list)
   mean_ret = stat.mean(pop_data_list)
   stdev = stat.stdev(pop_data_list)
   return median_ret, mean_ret, stdev

if __name__ == '__main__':
   argument_list = sys.argv[1:]
   options = "x:sh"
   long_options = ["state=", "summary", "help"]
   try:
    # Parsing argument
    arguments, values = getopt.getopt(argument_list, options, long_options)
    # checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-h", "--help"):
            print ("python3 statepop.py blank --summary --state='state' --help")
            print ("python3 statepop.py blank -x state -h -s")
        elif currentArgument in ("-s", "--summary"):
            median, mean, stdev = summarize()
            print("Statistics Summary")
            print("Standard Deviaton = {:10.2f}".format(stdev))
            print("Median = ", median)
            print("Mean = ", mean)           
        elif currentArgument in ("-x", "--state"):
            state, pop = get_state(currentValue)
            print("State            Population")
            print(state, pop)
             
   except getopt.error as err:
     print (str(err))
