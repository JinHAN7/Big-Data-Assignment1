#!/usr/bin/env python 
import sys
max_key=None
max_count=0
current_count=0
current_key=None
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
		if current_count >max_count:
			max_count=current_count
			max_key=current_key
		current_count=count
		current_key=key
if current_count >max_count:
			max_count=current_count
			max_key=current_key
print ('%s\t%s'%(max_key,max_count))
