# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 09:53:23 2021

@author: Dell
"""

x = 10

print (x)

2**5

# find method-----------------------------

x="this is the right way,right?"
type(x)

print(x)

x[0]

x[26]

x.find("right",0,26)

x.find("right",11,30)

x.find("bbbb",0,30)

x.find("right",0)

x.find("right")


#capitalize method(capitalize the first letter of a string)

x.capitalize()

##saves the new output continually-------------------------
x_2=x.capitalize()

##count argument--------------------
x.count("is")

x.count(" ")

"The length of the string is "+ str(len(x))


#upperCase--------------------
x.upper()

x2=x.upper()

#lowerCase----------------------
x.lower()

x2.lower()



#replacement arguement------------

x.replace("right", "correct")          

x.replace("right", "correct",1)  

x.replace("right?", "correct?")  

x.replace( "","*", 3)


#to get the key word in a statement eg 'this'-----------

x[0:4]

x[6:9]

x[17:27]

x[17:27].replace( "right", "correct")

x[0:16] + x[17:27].replace( "right", "correct")

#----------------------------------

s="Tareq"
s="Lisa"

names=["Lisa", "grace","zein"]

len(names)
type(names)

#-----------------------------
x="this is a right way,right?"

#split function----------------

x.split(" ")

x.split() 

x.split(" ") -------the input is a string,the output is a list

x.split(",")

words=x.split(" ")

type(words)

len(words)

words

words[5]

#joins function----------------

"*".join(x)

words

" ".join(words)


#string slicing--------------------------
x
x[0]
x[25]
x[0:3] #0,1,2
x[0:4] #0,1,2,3

len(x)
x[27] #error;out of range
x[20:27]  #20-26

x= "this is a right way,right?"
x=[0:-7]


#print function---  (bakslash) \n ,\t-------------

print("The author of the PDA book is 'James'")
print('the author of the PDA book is James')
print('the author of the PDA book is \'James\'')
print('the author of \nthe PDA book is \nJames')
print('the author of \nthe PDA book is \nJames') #\n it creates a new line char
print('the author of \tthe PDA book is \tJames')
print('the author of \tthe PDA book is \tJames') #t it creates a tab space
print('the author of \rthe PDA book is James')
print('the author of \rthe PDA book is James') #r it removes the previous str

# importing operationg system-----------------
import os

os.getcwd()


#DATE and TIME------------(construction)

---#import package----

from datetime import date, datetime, time, timedelta

d1=datetime(2017,6,5, 6,13,20)
print(d1)
type(d1)

d1.year
d1.month
d1.day

t1=datetime.strptime("05 Nov 01", "%d %b %y")
print(t1)

t1.strftime("%d %b %y") #display function

print(t1.strftime("%d %b %y"))

print(datetime.today())
print(t1)

x=datetime.now()
x.year
x.day

#-----------
d2=date(2017,6,5)
print(d2)
d2.day
d2.year
'i moved to canada on'  + str(d2)

d3=d1.replace(hour=0,minute=0,second=0)
print(d3)


#Maths package

import math

math.exp(1) #e**1

math.factorial(4)  #4*3*2*1

#---------------------------

name="Tareq"

city="Oakville"

print("My name is %s,and i live in %s" % (name,city))

age=18


print("My name is %s,and i live in %s" % (name,age))

#---------
#MISSING VALUES-----------------
import numpy as np

np.array([2,4,6])

y=np.array([1, 0,np.NaN,0,np.NaN,0,9])
type(y)
print(y)
len(y)

np.isnan(y)

z=np.isnan(y) #save Z in the 
print(z)
type(z)


z.sum() #sum of the true values =2== the total of missing values

np.mean(z)

2/7 #similar to np.mean(z) or z.mean

#.........................

import pandas as pd

range(1-10) #1-9 we stop at (end-1)
range(10)
list(range(10))

x = pd.Series(range(11,18), index=range(1,8))
x
type(x)
x=[1]


y=x[::2]
y

x
x.reindex([4,6,5,7,3,2,1])

a=x.reindex([2,1,12,3],fill_value=0)

a
 
b=x.reindex([15,2,1,12,3])
b

b.shape
len(b)

b.count()    #number of non-missing values
len(b)-b.count()  #number of missing values

pd.isnull(b)  #isnan in numpy

b.isnull()

pd.notnull(b)

