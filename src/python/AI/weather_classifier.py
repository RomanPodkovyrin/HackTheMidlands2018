#Importing Libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib
print('Libraries Imported')


def main():

    scaler, classifier = train()

    """test = [[27.23,0.53,0,3.31]]
    print(test)
    test = scaler.transform(test)
    print(classifier.predict(test))"""

    predict(scaler, classifier, [[27.23, 0.53, 0, 3.31]])


def train():
    # Creating Dataset and including the first row by setting no header as input
    dataset = pd.read_csv('data.csv', header=None)
    # naming the columns
    dataset.columns = ['temp', 'humi', 'preci', 'wind', 'feel']
    print('Dataset shape: ' + str(dataset.shape))
    print(dataset.head())

    # Converts classes to numerical values
    factor = pd.factorize(dataset['feel'])
    dataset.feel = factor[0]
    definitions = factor[1]
    print(dataset.feel.head())
    print("Definitions: ",definitions)

    # Splitting the data into independent and dependent variables
    X = dataset.iloc[:, 0:4].values # first four columns are input values
    y = dataset.iloc[:, 4].values # last columns are the classes of the data
    print('The independent features set: ')
    print(X[:5, :])
    print('The dependent variable: ')
    print(y[:5])

    # splits data into training and test data
    # if have enough data set test_size to 0.1
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=21)

    # Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    print( X_test[0])
    # scales the input datas
    X_test = scaler.transform(X_test)

    # Fitting Random Forest Classification to the Training set
    classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=42)
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)
    print( X_test, y_pred)

    # Reverse factorize (converting y_pred from 0s,1s and 2s ... to labels  )
    reversefactor = dict(zip(range(10), definitions))
    y_test = np.vectorize(reversefactor.get)(y_test)
    y_pred = np.vectorize(reversefactor.get)(y_pred)

    # Making the Confusion Matrix
    print(pd.crosstab(y_test, y_pred, rownames=['Actual feel'], colnames=['Predicted feel']))

    print(list(zip(dataset.columns[0:4], classifier.feature_importances_)))
    # dumps classifier to a file
    joblib.dump(classifier, 'randomforestmodel.pkl')
    # dumps scaler to a file
    joblib.dump(classifier, 'scaler.pkl')


    return scaler, classifier
def predict(scaler,classifier, data):
    #data = [[27.23, 0.53, 0, 3.31]]
    print(data)
    data = scaler.transform(data)
    print(classifier.predict(data))

main()