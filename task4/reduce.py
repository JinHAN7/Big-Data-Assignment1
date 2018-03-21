#!/usr/bin/env python 
import sys

#countny=0
#countother=0
currentkey=None
count=0

for line in sys.stdin:
	line=line.strip()
#	key,value=line.split('\t',1)
	key=line.strip()
	if key==currentkey:
		count += 1
	else:
		if currentkey:
			print('%s\t%s'%(currentkey,count))
		currentkey=key
		count=1
if key==currentkey:
	print('%s\t%s'%(currentkey,count))

#	if key=='NY':
#		countny+=1
#	else:
#		countother+=1
#print ('NY\t%s'%(countny)) 
#print ('Other\t%s'%(countother))
