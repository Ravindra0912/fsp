import operator
from collections import Counter

##  OPEN THE FILE AND READ
handle = open('file.txt', 'r')
readList = handle.read().split() # split each word of the file in a list
######################################

######## SORT the dict to the values of the 
a = dict(Counter(readList))
sorted_lst = sorted(a.items(), key=lambda x: x[1])			



print(sorted_lst)