#!/usr/bin/env python
# coding: utf-8

# # Getting Started With Python
# 
# ## Defining Variables
# 

# In[23]:


# Python supports four data types : Integer, String, Boolean and float

var1=2
var2=5.0
var3=False
var4="Machine Learning"

print("Value of var1: ",var1)
print("Value of var2: ",var2)
print("Value of var3: ",var3)
print("Value of var4: ",var4)


## Checking the type of each variable: Python has a method type()

print('\n')
print("Type of var1:",type(var1))
print("Type of var2:",type(var2))
print("Type of var3:",type(var3))
print("Type of var4:",type(var4))



# ## Conditional Statements

# In[41]:


# Simple condition 1

##Redefine Var1 to check the implementation of the code
##The input function by default inputs a string value. Its important to convert it to string first

var1=int(input("Enter the value of var1"))

if var1 >1:
    print("\n Bigger than 1")
elif var1==1:
    print("\n equal to 1")
else:
    print("\n smaller than 1")
    
# Ternary operators as conditional statement     

isgreater= True if var1>1 else False

print("\n",isgreater)


# ## Generating Sequence of Numbers

# In[46]:


## Initializing the sequence of numbers with [a,b)
numbers= range(1,6)
print(numbers)
print(len(numbers))
print(type(numbers))

#Range is a variable type in python, its similar to a list and it's elements can also be accessed through
#list operations

print(numbers[0])


# ## Control Flow Statement

# In[57]:


## For loop

for i in numbers: # numbers is supposed to be a range
    print(i)
    
## While loop

## Initialize value of i
i=1 
while i<7:
    print(i)
    i=i+1

print("final value of i is", i)
    


# ## Functions Define

# In[55]:


# Returning only one value

def addelements(a,b):
    return a+b

## Returning 2 values
def addelements_v2(a,b):
    total=a+b
    prod=a*b
    return total,prod

add1=addelements(1,4)
add2=addelements_v2(1,4)

print(add1,"\n",add2)
print(type(add1),"\n",type(add2))

## If multiple values are returned from function, they are stored in a tuple


# ## Working with Collections : List, Tuple, Dictionary & Sets

# In[92]:


## Lists are like C++ Arrays but can contain heterogenous elements as well. A list can have float, character or objects
## Lists are mutable

## Creating an empty list

empty_list =[]

batsmen = ["Rohit","Dhawan","Kohli","Rahane","Rayudu","Dhoni"]

## Indexing starts from '0'
print(batsmen[0])
print(batsmen[1])
print(batsmen[-1])

## Slicing a list
openers=batsmen[0:2] ## Notice that the last element is not included i.e. [0:2] means [0,2)
print(sliced_list)

## Elements count in the list
print(len(batsmen))

bowler=["Bumrah","Jadeja","Shami","Bhuvi","Chahal"]

## Adding two list = concatinating them

team=batsmen+bowler
print(team)

#finding the element in list
a="Bumrah" in team
print(a)

## Finding the index of the item

print(team.index("Bumrah"))

## This doesn't work as reverse just reverses the list but doesn't create another list

x= team.reverse()
print(x)

## Used reversed list

print("\n\n",team )

y= list(reversed(team)) ## list() changes the type of the object 

print (y)


## Tuples are similar to list but are immutable data types

tuple_1 = tuple(team)
#tuple_1[1]="Sahil" # This statement throws an error

## Sets are collection of unique elements and are unordered

set_1 = {1,2,3,4,5,6,7,1,2,3,4}

print("\n\n",set_1,"   Notice duplicate elements are removed from the initialization")

multiple_2 = {2,4,6,8,10,12,14,16,18,20}

multiple_5 = {5,10,15,20}

## Taking union

multiple_2_or_5 = multiple_2.union(multiple_5)

multiple_2_and_5 = multiple_2.intersection(multiple_5)

multiple_2_not_5 = multiple_2.difference(multiple_5)

print(multiple_2_and_5,multiple_2_not_5,multiple_2_or_5)


## Dictionaries are the Key:Value pairs. The values can be accessed by passing the key as the input parameter.

wc_winners = { 1975: "West Indies",
               1979: "West Indies",
               1983: "India",
               1987: "Australia",
               1991: "Pakistan"}

## Printing the value based on the key
print(wc_winners[1975])

## Extracting all the values of the dictionary

print(wc_winners.values())


# ## Playing with Strings in Python

# In[109]:


string0="python"
string1="machine learning"
string2="this is a multiline string"

list_strings=[string0,string1,string2]

for i in range(0,3):
    print(list_strings[i])


## Convert a string to either upper/lower case 
x=string0.upper()

print(string0)
print(x)

## Separating a string for web scrapping like requirements

## It splits it and creates a list out of it :P Awesome!!!
y= string2.split(" ")

print("\n\n", type(y),"     ",y, "   ",y[4])


### Cleaning the space of the string

spaced_string = "    this is spaced string   "

print("length of spaced string is ", len(spaced_string))

unspaced_string =spaced_string.strip()

print("length of spaced string is ", len(unspaced_string))


# ## Defining the Anonymous functions in Python

# In[108]:


## Lambda functios are called anonymous functions and are not stored somewhere. These functions are used once only.

anonymous_function= lambda a,b: a*b

print(anonymous_function(2,3))

## Labda functions are mostly used within another function

## A function that will multiply the number input with a certain number based on function

### Here a function is returning another function
def multiplier(n):
    x= lambda a: a*n
    return x

twice_multi = multiplier(2) ## Twice multi is a function that is being created from the function multiplier
thrice_multi=multiplier(3)

print(twice_multi(5))
print(thrice_multi(5))


# ## Functional Programming : Here we use Map and filter functions which are called higher order functions bcoz they take a function as an input

# In[130]:


## Functions can be passed to other functions as variables. They can be used as an alternative to looping.
### Example1: Mapping

# Defining an integer list
int_list = [1,2,3,4,5,6,7,8,9]
## Get square of the list

##Method 1: Using loops

sqr_list=[] 

### Now sqr_list is an empty list: It will not add any element coz its empty: Below code will throw error
"""
i=1
while i<(len(int_list)-1):
    sqr_list[i]=int_list[i]
    i=i+1
"""
print(sqr_list)

for i in int_list:
    sqr_list.append(i*i)


print("This is step 1 way :    ",sqr_list)

## Function Define

def square_me(x):
    return pow(x,2)

## Use map function to by default iterate over each element of the list 

sqr_list_v2 =list(map(square_me,int_list))

print("Using map function:   ",sqr_list_v2)
##########################################################################################
## Another way is to define lambda function in map function

sqr_list_v3= list(map(lambda x: x*x , int_list))

print("Using map and Lambda function:   ",sqr_list_v3)


## Example2: Using filter function

## filter function takes function as an input and applies that filter on the list 

numbers=[1,2,3,4,5,6,7,8,9,10]

even_numbers= list(filter(lambda x: x%2==0, numbers))

                   
print("Even numbers in the list are :   ",even_numbers)                   


# ## Importing and using liabraries

# In[138]:


## Taking square root of a number
import math
print("square root is:  ",math.sqrt(16))

## Generating random numbers within a range
import random
print(random.sample(range(1,10),3))

## Median and mean calculation
from statistics import mean,median

def get_stats(x):
    return(mean(x),median(x))


stats=get_stats([1,2,3,40,5,6,7,8,9])

print("\n\n",stats)

