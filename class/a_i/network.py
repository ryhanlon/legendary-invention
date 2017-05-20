"""
Deep learning in class

"""

import pickle
import tflearn
# from data_format import equation
import tflearn.datasets.mnist as mnist

def equation(w, x, y, z):

    first = x * y
    second = w + first + z
    return second/2

#train_x, train_y, test_x, test_y = pickle.load(open('data_set.pickle', 'rb'))
train_x, train_y, test_x, test_y = mnist.load_data(one_hot=True)

number_nodes = 500

network = tflearn.input_data(shape=[None, 784])
network = tflearn.fully_connected(network, number_nodes)
network = tflearn.fully_connected(network, number_nodes)
network = tflearn.fully_connected(network, 10, activation='softmax')

network = tflearn.regression(network)

model = tflearn.DNN(network, tensorboard_verbose=0)
model.fit(train_x, train_y, n_epoch=20, batch_size=100000, show_metric=True, validation_set=(test_x, test_y))

def format_pred(prediction):
    pred = prediction[0]
    index = 0
    max = pred[0]

    for i in range(len(pred)):
        if pred[i] > max:
            max = pred[i]
            index = i
    return index



print(test_y[0])
print(format_pred(model.predict([test_x[0]])))

