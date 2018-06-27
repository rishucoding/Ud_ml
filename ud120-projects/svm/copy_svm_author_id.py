#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess



### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
labels_train = labels_train[:len(labels_train)/100]
features_train = features_train[:len(features_train)/100]



#########################################################
### your code goes here ###
clf = SVC(10000, 'rbf')
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
accuracy = accuracy_score(pred, labels_test)
print pred[10], pred[26], pred[50]
print len(pred)
count = 0
for x in pred:
	if x == 1:
		count = count + 1
print count
print accuracy

#########################################################


