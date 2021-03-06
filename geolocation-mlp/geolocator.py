# encoding: utf-8
from random import seed
from random import randrange
from random import random
from csv import reader
from math import exp
 
def load_csv(filename):
	dataset = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file)
		for row in csv_reader:
			if not row:
				continue
			dataset.append(row)
	return dataset 

def load_csv_comma(filename):
	locations = list()
	with open(filename, 'r') as file:
		csv_reader = reader(file, delimiter=';')
		for row in csv_reader:
			if not row:
				continue
			locations.append(row)
	return locations

def appendLocation(dataset, locations):
    for i in range(len(locations)):
        dataset[i].pop()
        dataset[i].pop()
        dataset[i].append(locations[i][0])
    return dataset

def appendLocationDic(dataset, dic, locations):
    for i in range(len(locations)):
        dataset[i].pop()
        dataset[i].pop()
        dataset[i].append(dic[locations[i][0]])
    return dataset

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
 
# Split a dataset into k folds
def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split
 
# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] < predicted[i] + 0.25 and actual[i] > predicted[i] - 0.25:
			correct += 1
	return correct / float(len(actual)) * 100.0
 
# Evaluate an algorithm using a cross validation split
def evaluate_algorithm(dataset, back_propagation, n_folds, *args):
	folds = cross_validation_split(dataset, n_folds)
	scores = list()
	for fold in folds:
		train_set = list(folds)
		train_set.remove(fold)
		train_set = sum(train_set, [])
		test_set = list()
		for row in fold:
			row_copy = list(row)
			test_set.append(row_copy)
			row_copy[-1] = None
		predicted = back_propagation(train_set, test_set, *args)
		actual = [row[-1] for row in fold]
		accuracy = accuracy_metric(actual, predicted)
		scores.append(accuracy)
	return scores
 
# Calculate neuron activation for an input
def activate(weights, inputs):
	activation = weights[-1]
	for i in range(len(weights)-1):
		activation += weights[i] * inputs[i]
	return activation
 
# Transfer neuron activation
def transfer(activation):
	return 1.0 / (1.0 + exp(-activation))
 
# Forward propagate input to a network output
def forward_propagate(network, row):
	inputs = row
	#print inputs
    #ok
	for layer in network:
		new_inputs = []
		for neuron in layer:
			activation = activate(neuron['weights'], inputs)
			#print activation
            #ok
			neuron['output'] = transfer(activation)
			new_inputs.append(neuron['output'])
		inputs = new_inputs
		#print inputs
        #ok
	return inputs
 
# Calculate the derivative of an neuron output
def transfer_derivative(output):
	return output * (1.0 - output)
 
# Backpropagate error and store in neurons
def backward_propagate_error(network, expected):
	for i in reversed(range(len(network))):
		layer = network[i]
		errors = list()
		if i != len(network)-1:
			for j in range(len(layer)):
				error = 0.0
				for neuron in network[i + 1]:
					error += (neuron['weights'][j] * neuron['delta'])
				errors.append(error)
		else:
			for j in range(len(layer)):
				neuron = layer[j]
				errors.append(expected[j] - neuron['output'])
		for j in range(len(layer)):
			neuron = layer[j]
			neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
 
# Update network weights with error
def update_weights(network, row, l_rate):
	for i in range(len(network)):
		inputs = row[:-1]
		if i != 0:
			inputs = [neuron['output'] for neuron in network[i - 1]]
		for neuron in network[i]:
			for j in range(len(inputs)):
				neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
			neuron['weights'][-1] += l_rate * neuron['delta']
 
# Train a network for a fixed number of epochs
def train_network(network, train, l_rate, n_epoch, n_outputs):
	for epoch in range(n_epoch):
		for row in train:
			outputs = forward_propagate(network, row)
			#print outputs
			#ok
			expected = [i for i in range(1, n_outputs + 1)]
			#expected[0] = 1.0
			backward_propagate_error(network, expected)
			update_weights(network, row, l_rate)
 
# Initialize a network
def initialize_network(n_inputs, n_hidden, n_outputs):
	network = list()
	hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
	network.append(hidden_layer)
	output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
	network.append(output_layer)
	return network
 
# Make a prediction with a network
def predict(network, row):
	outputs = forward_propagate(network, row)
	return outputs.index(max(outputs))
 
# Backpropagation Algorithm With Stochastic Gradient Descent
def back_propagation(train, test, l_rate, n_epoch, n_hidden):
	n_inputs = len(train[0]) - 1
	n_outputs = 33
	network = initialize_network(n_inputs, n_hidden, n_outputs)
	train_network(network, train, l_rate, n_epoch, n_outputs)
	predictions = list()
	for row in test:
		prediction = predict(network, row)
		predictions.append(prediction)
	return(predictions)

dataset = load_csv('default_features_1059_tracks.txt')
locations = load_csv_comma('locationsUTF.csv')

#print len(dataset[0])
#print len(locations)
listLoc = []
for i in range(len(locations)):
    listLoc.append(locations[i][0])

locationsSet = list(set(listLoc))
#print locationsSet

dicLocations = {}
for i in range(len(locationsSet)):
    dicLocations[locationsSet[i]] = i

songs = appendLocationDic(dataset, dicLocations, locations)

for i in range(len(songs[0])-1):
	str_column_to_float(songs, i)

n_folds = [3, 5]
l_rate = [ 0.5, 0.8]
n_epoch = [ 1000, 10000]
n_hidden = [1,2]
aux_id = 1
for h in n_hidden:
	for e in n_epoch:
		for l in l_rate:
			for f in n_folds:
				scores = evaluate_algorithm(dataset, back_propagation, f, l, e, h)
				a =  (sum(scores)/float(len(scores)))
				print('%d %d %d %0.1f %d %.3f%%' %(aux_id, h, e, l, f, a))
				aux_id += 1
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
