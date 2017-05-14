import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

def split_data(df, col):
	train, test = train_test_split(df, test_size = 0.25)
	y_train = train[col]
	train = train.drop(col, axis=1)
	y_test = test[col]
	test = test.drop(col, axis=1)
	return train, y_train, test, y_test

def preprocess(df):
	old_columns = df.columns
	if style == "normilization":
		new_df = preprocessing.MinMaxScaler().fit_transform(df)
		new_df = pd.DataFrame(new_df)
		new_df.columns = old_columns

def neural_network(layers, neurons, epochs, batch_size, x_train, y_train, x_test, y_test):
	model = Sequential()
	model.add(Dense(neurons[0], input_dim = x_train.shape[1], activation = layers[0]))
	
	for layer,neuron in zip(layers[1:], neurons[1:]):
		model.add(Dense(neurons, activation = layer))
	
	model.compile(loss = 'binary_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])
	history = model.fit(x_train.as_matrix(), y_train.as_matrix(), epochs = epochs,
		batch_size = batch_size, verbose=1, validation_data = (x_test.as_matrix(), y_test.as_matrix()))
	
	plt.plot(history.history['loss'], label="Training Loss")
	plt.plot(history.history['val_loss'], label="Test Loss")
	plt.xlabel("Iterations")
	plt.ylabel("Cross Entropy")
	plt.legend(loc='upper right')
	plt.show()


def main():
	df = pd.read_pickle("/home/...")
	x_train, y_train, x_test, y_test = split_data(df)
	x_train = preprocess(x_train)
	x_test = preprocess(y_test)
	layers = ["relu", "relu", "sigmoid"]
	neurons = [64, 32, 1]
	neural_network(layers, neurons, 2000, 512, x_train, y_train, x_test, y_test)