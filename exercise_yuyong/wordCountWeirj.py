# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 22:52:07 2017
@author: weirj
"""
import sys
from collections import Counter

def isChineseStr(string):
    return all(0x4e00<=ord(ch)<=0x9fff for ch in string)

filename = sys.argv[1]
file = open(filename)
txtlist = file.read().split(' ')
bin_word_list = []
for i in range(1, len(txtlist)):
    if isChineseStr(txtlist[i-1]) and len(txtlist[i-1])==2 and isChineseStr(txtlist[i]) and len(txtlist[i])==2:
        bin_word_list.append(' '.join((txtlist[i-1],txtlist[i])))

c = Counter(bin_word_list)

print(c.most_common(10))