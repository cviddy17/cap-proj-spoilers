import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

f = open('./data/train.txt', 'r')
X = f.readlines()
g = open('./data/labels.txt', 'r')
y = g.readlines()
y = [int(i) for i in y]

#vectorizing words, performing Tfidf, elimnating stop_words
crunch = TfidfVectorizer(stop_words='english')
X_vec = crunch.fit_transform(X)

#performing split for testing
X_train, X_test, y_train, y_test = train_test_split(X_vec,y)

#Choosing Random Forest Model, this is optimal model (given time) from notebook.
clf = RandomForestClassifier(n_jobs=500, max_depth=8, n_estimators=1000)
clf.fit(X_train, y_train)

#Cross-Validation
scores = cross_val_score(clf, X_train, y_train, cv=5)
print "Train Crossval Accuracy: " + str(scores)
print "Predicted Accuracy: "+ str(sum(scores)/5)

#Testing
preds = clf.predict(X_test)
score = clf.score(X_test,y_test)
print 'Test Accuracy: ' + str(score)
