import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = raw_input()
    counts = dict()
    #counts_sorted = dict()
    for i in s :
        counts[i] = counts.get(i,0)+1

    counts = sorted(counts.items(),key = lambda kv: (-kv[1],kv[0]))
    
    for k,v in counts[:3]:
        print (''.join("{} {}".format(k,v)))  
