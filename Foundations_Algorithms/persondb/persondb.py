# From work
import quicksort
import shellsort
import linearsearch
import random
import time

from datetime import date
approve = 0
reject = 0

def add_person(person,output):
    appid = get_appid()
    perid = get_perid() 
    today = str(date.today())
    output.write('{} {} {} {} {} {} {}\n'.format(perid, appid, person[0], person[1], person[2], "Approved" , today ))

def add_appid(person, perid, output):
    appid = get_appid()
    today = str(date.today())
    output.write('{} {} {} {} {} {} {}\n'.format(perid, appid, person[0], person[1], person[2], "Approved" , today ))

def get_perid():
    perid = random.randint(0,99999)
    return perid

def get_appid():
    appid= random.randint(0,999999)
    return appid

start = time.time()

#open hist data files
histfile=open("hist.txt", "r+")
lines=histfile.readlines()
data=[tuple(line.strip().split()) for line in lines]

#open input data files
inputfile=open("input.txt", "r")
lines=inputfile.readlines()
inputdata=[tuple(line.strip().split()) for line in lines]

#sort data file

quicksort.quickSort(data,0,len(data)-1)

#read in input file

for inputitem in inputdata:
   j=linearsearch.LinearSearch(data,inputitem[2],4)
   approve = 0
   reject = 0
   if len(j):
       for item in j:
          if item[2] == inputitem[0] and item[3] == inputitem[1]:
            if item[5] == "Approved":
               approve = approve + 1
            else: 
               reject = reject + 1            
       add_appid(inputitem,item[0],histfile)
       print("Persons name",inputitem[0],inputitem[1])
       print("Number of current Approvals = ",approve)
       print("Number of currentRejections = ",reject)
   else:
      add_person(inputitem, histfile)
      print("Added ",inputitem[0],inputitem[1])

end = time.time()
print("\nRunning time",end - start)
