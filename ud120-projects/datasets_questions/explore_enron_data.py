#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import math

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#print len(enron_data)
list1 = enron_data.items()
count = 0
#print len(list1[0][1])
for x in list1:
	if x[1]['poi'] == True:
		count +=1
#print count
#print enron_data["PRENTICE JAMES"].items()
#print enron_data["PRENTICE JAMES"]["salary"]
#print enron_data["PRENTICE JAMES"]["total_stock_value"]
#print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
#print enron_data["COLWELL WESLEY"]['poi']
#print enron_data["SKILLING JEFFREY K"].items()
#for x in list1:
#	if x[1]['poi'] == 1:
#		print x[0]
boii = max(enron_data["SKILLING JEFFREY K"]['total_payments'],enron_data["LAY KENNETH L"]['total_payments'],enron_data["FASTOW ANDREW S"]['total_payments'])
#print "SKILLING " ,enron_data["SKILLING JEFFREY K"]['total_payments'],"LAY KENNETH L "
#print enron_data["LAY KENNETH L"]['total_payments'],enron_data["FASTOW ANDREW S"]['total_payments']
#print enron_data["LAY KENNETH L"]['total_payments']
#print boii
#35 poi in total but only 18 are present in the dataset

# quantified salary
file = 'features.txt'
flag = 0
for x in list1:
	if flag:
		continue
	for i in x[1]:
		print i
	flag = 1

count = 0
for x in list1:
	if x[1]["salary"] == "NaN":
		continue
	count +=1
print "quantified salary", count
count  = 0
for x in list1:
	if x[1]["email_address"] == "NaN":
		continue
	count +=1
print "known email addresses", count

count = 0
for x in list1:
	if x[1]["total_payments"] == "NaN" :
		count += 1 
print "/// Count is ", count
print len(list1)
print (1-float(count)/len(list1))*100.0