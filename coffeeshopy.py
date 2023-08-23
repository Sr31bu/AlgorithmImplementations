#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:11:42 2023

@author: shashankramachandran
"""


#contributor : Alex Anuskevich

import sys

import numpy as np
import os


def parseInput(filename = None):
    if filename == None:
        try:
            weights = readIntList(sys.stdin)
        except:
            False, "Error parsing standard input as sequence of integers."
    else:
        try:
            with open(filename, 'r') as f:
                weights = readIntList(f)
        except:
            False, "Error parsing input file as sequence of integers."
    return True, weights

def readIntList(f):
    ints_list = []
    for line in f.readlines():
        if line != '\n':
            ints_list.append(int(line))
    return ints_list

def writeOutput(optset, filename = None):
    assert type(optset) == list
    if filename == None:
        writeIntList(optset, sys.stdout)
    else:
        with open(filename, 'w') as f:
            writeIntList(optset, f)


def writeIntList(optset, f):
    for x in optset:
        f.write(str(int(x)) + "\n")
    return




##################################################
# Coffee shop solution
##################################################


test_WTC_input = [5, 5, 9, 5, 5]
test_WTC_output = [0, 1, 3, 4]

def computeMaxValues(values):
    # values is a nonempty list of nonengative integers 
    # values[i] is the serving capacity of location i
    assert len(values) >= 3
    n = len(values)
    # Fill the table:
    # opt[i] is the value of the heaviest ok set 
    # among vertices 0,1,...,i.
    opt = [0] * n
    ########################################
    # Your code here.
    opt[0] = values[0]
    opt[1] = values[0] + values[1]
    length = len(opt)
    for i in range(2,length):
        if i == 2: # this is if we are on the first iteration so no negative indices 
            Case1 = values[i] + values[i-1] # considering only i and i-1
        else:
            Case1 = values[i] + values[i-1] + opt[i-3] # considering i,i-1,i-3
        Case2 = values[i] + opt[i-2] # considering i and i-2
        Case3 = opt[i-1] #not considering i-1
        opt[i] = max(Case1,Case2,Case3)
    ########################################
    return opt

def computeOptSet(values, opt):
    assert len(values) >= 3
    n = len(values)
    #Now compute the optimal set
    optset = []
    ########################################
    
    
    
# The idea behind this backtracking solutiion is two consider all possible cases. To prevent negative indices we consider 
# 2 cases : 
#           1) i < 3 ( i = 1 ,2 ,0 )
#           2) i>= 3
# we then consider all permuations in a brute force manner to find all soltions. 
    # Your code here.
    i = n - 1 # intialising the length  -1 to our counter 
    while i >=0: # iterating backwards over our optimal set 
        if i < 3:
            #CONSIDERING CASES BELOW 3 SINCE IT WOULD RESULT IN A NEGATIVE INDEX 
            if(i==0):
                optset.append(i) #if the optimla solution has 0 include it 
            elif(i==1):
                optset.append(i) # if it has 0 and 1 we shoudl include both of them 
                optset.append(i-1)
                i = i -2 # decreasing by 2 so that negative index ends the loop 
            else: # A SEPERARTE CASE for when i = 2 
                if values[i] + values[i-1] == opt[i]: # considering 2 and 1 
                    optset.append(i)
                    optset.append(i-1) 
                    i = i -2
                else:
                    optset.append(i) #CONSIDERING THE CASE where only 2 and 0 
                    optset.append(i-2)
                    i = i - 2
        else:
            if(values[i]+values[i-1]+opt[i-3] == opt[i]):  # CONSIDERING CASES where i is greater than equal to 3 
                optset.append(i) #CONSIDERING the case where i and i-1 are included byt not i-2 which is why be decrement by 2 to skip it 
                optset.append(i-1)
                i = i -2
            elif(values[i]+opt[i-2]==opt[i]): #considering where we dont consider i -1 
                optset.append(i)
                i = i -1
        i = i -1 #decrementing by 1 
                
    ########################################
    return optset

def main(args=[]):
    if len(args) != 2:
        print("Problem! There were {} arguments instead of 2.".format(len(args)))
        return 
    success, result = parseInput(filename = args[0])
    if success:
        values = result
        opt = computeMaxValues(values)
        optset = computeOptSet(values, opt)
        writeOutput(optset, filename = args[1])
    else:
        print(result)
    return

if __name__ == "__main__":
    main(sys.argv[1:])