from dataset import *
import tensorflow as tf


#Learning rate
learning_rate = 0.001

#Total iterations we train
training_iterations = 20000

#How much is getting trained per iteration
batch_size = 100

#How often do we print to terminal
display_step = 100

#N number of most common words in dictionary, n_classes
vocabulary_size = 10000

#sequence length
num_steps = 150

#Hidden units in RNN
n_hidden = 512

#layers???
n_layers = 2


"""
Placeholders
"""
#Input data
x = tf.placeholder(tf.int32, [batch_size, num_steps, vocabulary_size ], name='input_placeholder')

# data
y = tf.placeholder(tf.int32, [batch_size, num_steps, vocabulary_size], name='labels_placeholder')


def rnn_model(x):
    layer = {
        'weights': tf.Variable(tf.random_normal([n_hidden, vocabulary_size]))
        'biases': tf.Variable(tf.random_normal(vocabulary_size))
    }

    lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden,forget_bias=1.0,state_is_tuple=True)
    #cells = tf.nn.rnn_cell.MultiRNNCell([lstm_cell]*n_layers, state_is_tuple=True)
    
    outputs, states = tf.nn.static_rnn(lstm_cell, x, dtype=tf.float32) 

    output = tf.matmul(outputs[-1], layer['weights']) + layer['biases']
    return output


def train():
    prediction = rnn_model(x)
    cost = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(prediction, y))
    optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost) #its MY optimizer

    with tf.Session() as sess:

        sess.run(tf.initialize_all_variables())

        #Training loop
        for i in training_iterations:

            #Get batch
            

        
            if (i % display_step == 0):
                print("Completed #" + i + "of" training_iterations ", loss")
        




#Get the data
#data, count, dictionary, reversed_dictionary = build_dataset(get_words(), vocabulary_size)



rnn_model(x)