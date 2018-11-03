import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline


X = ""
Y = ""

def main():
    # ensures that the stochastic process of training a neural network can be reproduced
    seed = 7
    numpy.random.seed(seed)
    loadDataSet()


# change
def loadDataSet():
    dataframe = pandas.read_csv("iris.csv", header= None)
    dataset = dataframe.values
    global X
    global Y
    X = dataset[:, 0:4].astype(float) # says what columns it is ant their type
    Y = dataset[:, 4]

def encodeTheOutputVariable():
    # encode class values as integers
    encoder = LabelEncoder()
    encoder.fit(Y)
    encoded_Y = encoder.transform(Y)
    # convert integers to dummy variables (i.e. one hot encoded)
    dummy_y = np_utils.to_categorical(encoded_Y)


def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(8, input_dim=4), activation = 'relu')
    model.add(Dense(3, activation='softmax'))

    # compile model
    model.compile(loss = 'categorical-crossentropy', optimizer='adam', metrics=['accuracy'])
    return model
def evaluate():
    kford = KFold(n_splits=10, shuffle=True, random_state = seed)
main()