#!/usr/bin/env python
import sys
#from csv import reader
currentkey=None
currentvalue = None 
count=0
list1=[]
maker_list=[]
color_list=[]

for line in sys.stdin:
	line=line.strip()
#	print(line)
	key,value=line.split(',',1)

	if key==currentkey:#deal with one column
		if value==currentvalue:
			count+=1
		else:
			if currentvalue:
				list1.append([currentkey,currentvalue,count])
			currentvalue=value
			count=1

	else:#deal with another column
		if value==currentvalue:
			count+=1
		else:
			if currentvalue:
				list1.append([currentkey,currentvalue,count])
			currentvalue=value
			count=1

		currentkey=key

if key==currentkey:
	list1.append([currentkey,currentvalue,count])
for i in  range(len(list1)):
	if list1[i][0]=='vehicle_make':
		maker_list.append([list1[i][0], list1[i][1],list1[i][2]])
	else:
		color_list.append([list1[i][0],list1[i][1],list1[i][2]])
maker_list=sorted(maker_list,key=lambda x:x[1])
color_list=sorted(color_list,key=lambda x:x[1])
for i in range(len(maker_list)):
	print ('%s\t%s, %s'%(maker_list[i][0],maker_list[i][1],maker_list[i][2]))
for i in range(len(color_list)):
	print ('%s\t%s, %s'%(color_list[i][0],color_list[i][1],color_list[i][2] ))
