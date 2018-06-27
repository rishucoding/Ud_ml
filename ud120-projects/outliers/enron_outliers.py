#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
print len(data)
print "salary: ", data[0][0]
print "bonus: ",data[0][1]




### your code below

max0 = 0
max1 = 0
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    if max0 < salary:
    	max0 = salary
    if max1 < bonus:
    	max1 = bonus
print max0
print max1
print type(data_dict)
for x in data_dict.items():
	print type(x)
	#print x
	if x["salary"] == max0:
		print 
        print type(x)
        #print x
        print len(x[0])

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

