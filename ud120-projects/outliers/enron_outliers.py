#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
del data_dict["TOTAL"]
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
#print max0
#print max1
#print type(data_dict)
count = 0
print len(data_dict.items())
for x in data_dict.items():
    #print x[1]["salary"]
    
    if (x[1]["bonus"] >= 5000000 and x[1]["bonus"]!= "NaN") and (x[1]["salary"] >=1000000 and x[1]["salary"] !="NaN") :
        print x[0]
#print data_dict["LAVORATO JOHN J"]

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

