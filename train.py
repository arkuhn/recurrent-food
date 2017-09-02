from dataset import *

import tensorflow as tf


#Learning rate
learning_rate = 0.001

#Total iterations we train
training_iterations = 20000

#How much is getting trained per iteration
batch_size = 100

#N number of most common words in dictionary
vocabulary_size = 10000

#sequence length
num_steps = 150

#Hidden units in RNN
n_hidden = 512


weights = {
    'out': tf.Variable(tf.random_normal([n_hidden, vocabulary_size]))
}
biases = {
    'out': tf.Variable(tf.random_normal(vocabulary_size))
}

#Get the data
data, count, dictionary, reversed_dictionary = build_dataset(get_words(), vocabulary_size)

for i in data[0:400]:
    print(reversed_dictionary[i])

"""
def RNN(weights, biases):


#Placeholders

#Input data
x = tf.placeholder(tf.int32, [batch_size, num_steps, vocabulary_size ], name='input_placeholder')

# data
y = tf.placeholder(tf.int32, [batch_size, num_steps, vocabulary_size], name='labels_placeholder')


init_state = tf.zeros([batch_size, state_size])
"""