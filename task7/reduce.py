#!/usr/bin/env python 
import sys 
current_word = None
num_weekend=0
num_weekday=0
word=None
weekends=[5,6,12,13,19,20,26,27]
for line in sys.stdin:
	line.strip()
	word, value=line.split('\t',1)
	day=value.strip().split('-')
	try:
		
		day=int(day[2])
	except ValueError:
		continue
	if current_word==word:
		if day in weekends:
			num_weekend+=1
		else:
			num_weekday+=1
	else: 
		if current_word:
			weekend_average=float(num_weekend/8)
			weekday_average=float(num_weekday/23)
			print ('%s\t%0.2f, %0.2f'%(current_word,weekend_average, weekday_average))
		current_word=word
		num_weekend=0
		num_weekday=0
		if day in weekends:
			num_weekend+=1
		else:
			num_weekday+=1
weekend_average=float(num_weekend/8)
weekday_average=float(num_weekday/23)
print ('%s\t%0.2f, %0.2f'%(current_word,weekend_average, weekday_average))
