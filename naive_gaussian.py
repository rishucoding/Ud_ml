# link is http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html
import numpy as np 
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]]) # features
Y = np.array([1, 1, 1, 2, 2, 2]) # labelling as clases
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB() # classifier which makes prediction
clf.fit(X, Y) # passing the data via which it learns to make a decision curve
print(clf.predict([[-0.8, -1]]))
