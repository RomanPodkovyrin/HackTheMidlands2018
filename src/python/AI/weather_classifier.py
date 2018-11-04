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

    test = [[27.23,0.53,0,3.31]]
    print(test)
    test = scaler.transform(test)
    print(classifier.predict(test))


def train():
    # Creating Dataset and including the first row by setting no header as input
    dataset = pd.read_csv('data.csv', header=None)
    # Renaming the columns
    dataset.columns = ['temp', 'humi', 'preci', 'wind', 'f']
    print('Shape of the dataset: ' + str(dataset.shape))
    print(dataset.head())

    # Creating the dependent variable class
    factor = pd.factorize(dataset['f'])
    dataset.f = factor[0]
    definitions = factor[1]
    print("HELLO")
    print(dataset.f.head())
    print(definitions)
    print("HELLO")

    # Splitting the data into independent and dependent variables
    X = dataset.iloc[:, 0:4].values
    y = dataset.iloc[:, 4].values
    print('The independent features set: ')
    print(X[:5, :])
    print('The dependent variable: ')
    print(y[:5])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=21)

    # Feature Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    print("hello", X_test[0])
    X_test = scaler.transform(X_test)

    # Fitting Random Forest Classification to the Training set
    classifier = RandomForestClassifier(n_estimators=10, criterion='entropy', random_state=42)
    classifier.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(X_test)
    print("Heeeeeello", X_test, y_pred)

    # Reverse factorize (converting y_pred from 0s,1s and 2s ... to labels
    reversefactor = dict(zip(range(10), definitions))
    y_test = np.vectorize(reversefactor.get)(y_test)
    y_pred = np.vectorize(reversefactor.get)(y_pred)

    # Making the Confusion Matrix
    print(pd.crosstab(y_test, y_pred, rownames=['Actual feel'], colnames=['Predicted feel']))

    print(list(zip(dataset.columns[0:4], classifier.feature_importances_)))
    joblib.dump(classifier, 'randomforestmodel.pkl')


    return scaler, classifier

main()