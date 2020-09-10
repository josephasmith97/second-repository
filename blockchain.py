#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 11:09:23 2018

@author: josephsmith
"""
"""
import numpy as np
import scipy as sc

"""

import random as rnd

miner1 = 0
miner2 = 100
hacker = 0
x = 0
miner1list = []
miner2list = []
hackerlist = []

honestblockchain = 0
fakeblockchain = 0


hashcode = rnd.randint(0,100)

for x in range(0,1000):
    
    for i in range(0,100):
        
        miner1 = miner1 + rnd.randint((0-miner1),(100-miner1))
        miner2 = miner2 - rnd.randint((miner2-100),(0+miner2))
                                          
        
        if miner1 == hashcode :
            #print "miner1 is winner, hashcode was ",  (miner1)
            #print "number of iterations was", (i)
            miner1list.append(hashcode)
            hackerlist = hackerlist[:-1]
            break
        if miner2 == hashcode :
            #print "miner2 is winner, hashcode was ",  (miner2)
            #print "number of iterations was", (i)
            miner2list.append(hashcode)
            hackerlist = hackerlist[:-1]
            break
        
        
    
    if miner1list.__len__() + miner2list.__len__() == 20:
        print "The network is safe"
        break
    
    if hackerlist.__len__() == 20:
        print "The network has been hacked"
        break

def networkhacker(hacker):
    if hacker == rnd.randint(0,40):
            #print "hacker has entered blockchain!"
            hackerlist.append(hacker)
    return;
        
print("hello world")   




        

        
     
        



    

        
