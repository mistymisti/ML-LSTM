import pandas as pd 
import pickle

dataset = pd.read_csv('./traindata_final.csv')
X = dataset.iloc[:, [6,7,8,9,10,11,12]].values
y = dataset.iloc[:, 13].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

pickle.dump(classifier,open("./MLModel.sav",'wb'))