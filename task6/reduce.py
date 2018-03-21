#!/usr/bin/env python 
import sys
from csv import reader
key=None
current_key=None
current_count=0
ls=[]
for line in sys.stdin:
	line=line.strip()
	key,count=line.split('\t')
	try:
		count=int(count)
	except ValueError:
		continue
	if current_key==key:
		current_count+=count
	else:
		if current_key:
			ls.append([current_key,current_count])
		current_key=key
		current_count=count
if current_key==key:
	ls.append([current_key, current_count])
sortls=sorted(ls,key=lambda x: x[0])
sortls=sorted(sortls, key=lambda x: x[1],reverse=True)
for i in range(20):
	print ('%s\t%s'%(sortls[i][0], sortls[i][1]))

