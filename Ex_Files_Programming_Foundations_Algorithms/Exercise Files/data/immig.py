import shellsort
import linearsearch
import random
from datetime import date
approve = 0
reject = 0
def add_person(person,output):
    appid = get_appid()
    perid = get_perid() 
    today = str(date.today())
    output.write('{} {} {} {} {} {} {}\n'.format(perid, appid, person[0], person[1], person[2], "Approved" , today ))
    output.close()
    output=open("hist.txt", "r+")
    lines=output.readlines()
    mydata = [tuple(line.strip().split()) for line in lines]
    for item in mydata:
       print(item)
def add_appid(person, perid, output):
    appid = get_appid()
    today = str(date.today())
    print('{} {} {} {} {} {} {}\n'.format(perid, appid, person[0], person[1], person[2], "Approved" , today ))
    output.write('{} {} {} {} {} {} {}\n'.format(perid, appid, person[0], person[1], person[2], "Approved" , today ))
    output.close()
    output=open("hist.txt", "r+")
    lines=output.readlines()
    mydata = [tuple(line.strip().split()) for line in lines]
    for item in mydata:
       print(item)
def get_perid():
    perid = random.randint(0,99999)
    return perid
def get_appid():
    appid= random.randint(0,999999)
    return appid
def decision_count(data):
    global approve
    global reject
    if data[5] == "Approved":
     approve = approve + 1
    else:
     reject = reject + 1
#open hist data files

histfile=open("hist.txt", "r+")
lines=histfile.readlines()
data=[tuple(line.strip().split()) for line in lines]
#open input data files

inputfile=open("input.txt", "r")
lines=inputfile.readlines()
inputdata=[tuple(line.strip().split()) for line in lines]

#sort data file

shellsort.shellSort(data)

#read in input file

for inputitem in inputdata:
   j=linearsearch.LinearSearch(data,inputitem[2],4)
   if len(j):
       for item in j:
          if item[2] == inputitem[0] and item[3] == inputitem[1]:
            print("ok")
       add_appid(inputitem,item[0],histfile)
   else:
      add_person(inputitem, histfile)
