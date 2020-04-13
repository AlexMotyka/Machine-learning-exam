import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# stores iterations and costs for the Cost vs. Iterations graph
# first array stores iterations
# second array stores costs
cumulative_cost_data = [[],[]]

train_data = []
correct_outputs = []
"""----------Activation Functions----------"""
def relu_backward(deriv_activation, activation_cache):
    return deriv_activation * 1. * (activation_cache> 0)


def sigmoid_backward(deriv_activation, activation_cache):
    return deriv_activation * (1 / (1 + np.exp(-activation_cache))) * (1 - (1 / (1 + np.exp(-activation_cache))))


def sigmoid(weighted_sum):
    return (1 / (1 + np.exp(-weighted_sum))), weighted_sum


def relu(weighted_sum):
    return weighted_sum * (weighted_sum > 0), weighted_sum
"""----------------------------------------"""

"""
Init the parameters
"""
def initialize_parameters_deep(layer_dims):
    np.random.seed(3)
    parameters_ = {}
    layer_dim_len = len(layer_dims)
    for l in range(1, layer_dim_len):
        parameters_['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l - 1]) * 0.01
        parameters_['b' + str(l)] = np.zeros((layer_dims[l], 1))
    return parameters_

"""
linear_forward
*no activation*
"""
def linear_forward(activation, weight, bias):
    weighted_sum = np.dot(weight, activation) + bias
    cache = (activation, weight, bias)
    return weighted_sum, cache

"""
linear_activation_forward
This function is a linear_forward *with* activation in the network
activation_prev - the previous network output
activation - the output of the network
"""
def linear_activation_forward(activation_prev, weight, bias, activation):
    if activation == "sigmoid":
        weighted_sum, linear_cache_ = linear_forward(activation_prev, weight, bias)
        activation, activation_cache = sigmoid(weighted_sum)

    elif activation == "relu":
        weighted_sum, linear_cache_ = linear_forward(activation_prev, weight, bias)
        activation, activation_cache = relu(weighted_sum)

    cache = (linear_cache_, activation_cache)

    return activation, cache

"""
forward propagation
- move forward for all hidden layers, then one final output layer
- hidden layers are relu activation
- output layer is sigmoid
"""
def layer_model_forward(x_, parameters_):
    caches = []
    activation = x_
    param_length = len(parameters_) // 2
    for l in range(1, param_length):
        activation_prev = activation
        activation, cache = linear_activation_forward(activation_prev, parameters_['W' + str(l)], parameters_['b' + str(l)], "relu")
        caches.append(cache)
    activation_linear, cache = linear_activation_forward(activation, parameters_['W' + str(param_length)], parameters_['b' + str(param_length)], "sigmoid")
    caches.append(cache)
    return activation_linear, caches

"""
compute_cost
This function calculates cost with the Sum of Squares Deviation formula
y_ - the true output
activation_layer - is the output of the network (the value)
sse/ssd - the sum of squared deviations/error between the two
"""
def compute_cost(activation_layer, y_):
    true_output_std = np.std(y_)
    network_output_std = np.std(activation_layer)
    sse = np.sum(np.square(true_output_std - network_output_std)) * 100.0
    return sse

def linear_backward(deriv_weighted_sum, cache):
    activation_prev, weight, bias = cache
    m = activation_prev.shape[1]
    deriv_weight = (1 / m) * np.dot(deriv_weighted_sum, activation_prev.T)
    deriv_bias = (1 / m) * np.sum(deriv_weighted_sum, axis=1, keepdims=True)
    deriv_activation_prev = np.dot(weight.T, deriv_weighted_sum)
    return deriv_activation_prev, deriv_weight, deriv_bias

"""
linear backwards uses the derivatives of the activation functions instead
"""
def linear_activation_backward(deriv_activation, cache, activation):
    linear_cache_, activation_cache = cache

    # if activation was on a hidden layer, do relu activation
    if activation == "relu":
        deriv_weighted_sum = relu_backward(deriv_activation, activation_cache)
        deriv_activation_prev, deriv_weight, deriv_bias = linear_backward(deriv_weighted_sum, linear_cache_)

    # if the activation is on output layer, do sigmoid
    elif activation == "sigmoid":
        deriv_weighted_sum = sigmoid_backward(deriv_activation, activation_cache)
        deriv_activation_prev, deriv_weight, deriv_bias = linear_backward(deriv_weighted_sum, linear_cache_)
    return deriv_activation_prev, deriv_weight, deriv_bias


# back propogation
def layered_model_backward(activation_layer, y_, caches):
    grads = {}
    cache_length = len(caches)
    deriv_activation_layer = - (np.divide(y_, activation_layer) - np.divide(1 - y_, 1 - activation_layer))

    current_cache = caches[cache_length - 1]
    grads["dA" + str(cache_length - 1)], grads["dW" + str(cache_length)], grads["db" + str(cache_length)] = linear_activation_backward(deriv_activation_layer,
                                                                                                      current_cache,
                                                                                                      "sigmoid")
    for l in reversed(range(cache_length - 1)):
        current_cache = caches[l]
        deriv_activation_prev_temp, deriv_weight_temp, deriv_bias_temp = linear_activation_backward(grads["dA" + str(l + 1)], current_cache, "relu")
        grads["dA" + str(l)] = deriv_activation_prev_temp
        grads["dW" + str(l + 1)] = deriv_weight_temp
        grads["db" + str(l + 1)] = deriv_bias_temp
    return grads


# update the parameters
def update_parameters(parameters_, grads, learning_rate):
    param_length = len(parameters_) // 2
    for l in range(param_length):
        parameters_["W" + str(l + 1)] = parameters_["W" + str(l + 1)] - learning_rate * grads["dW" + str(l + 1)]
        parameters_["b" + str(l + 1)] = parameters_["b" + str(l + 1)] - learning_rate * grads["db" + str(l + 1)]
    return parameters_

def layered_network_layer_model(x_, y_, layers_dims_, learning_rate=0.00042, num_iterations=3000, print_cost=False):
    np.random.seed(1244)
    costs = []
    parameters_ = initialize_parameters_deep(layers_dims_)
    for j in range(0, num_iterations):
        activation_layer, caches = layer_model_forward(x_, parameters_)
        sse = compute_cost(activation_layer, y_)
        grads = layered_model_backward(activation_layer, y_, caches)
        parameters_ = update_parameters(parameters_, grads, learning_rate)
        if print_cost and j % 500 == 0:
            print("Cost at iteration %i: %f SSE" % (j, sse))
            costs.append(sse)
            cumulative_cost_data[0].append(j)
            cumulative_cost_data[1].append(sse)

    return parameters_

def predict_layered_network_layer(x_, parameters_, results=False):
    a_l, caches = layer_model_forward(x_, parameters_)
    if results:
        return a_l.reshape(1, a_l.shape[0]), np.argmax(a_l, axis=0)
    prediction_ = np.argmax(a_l, axis=0)
    return prediction_.reshape(1, prediction_.shape[0]), prediction_

'''----- main code starts here ------'''
file_list = ['Master.csv']
answers_arr = []
input_arr = []
# Get the data from the csv file
for filename in file_list:
    with open(filename) as csvf:
        csvf_read = csv.reader(csvf, delimiter=',')

        for row in csvf_read:
            input_arr.append([int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12]), int(row[13]), int(row[14]), int(row[15]), int(row[16]), int(row[17]), int(row[18]), int(row[19]), int(row[20]), int(row[21]), int(row[22]), int(row[23]), int(row[24]), int(row[25]), int(row[26]), int(row[27]), int(row[28]), int(row[29]), int(row[30]), int(row[31]), int(row[32]), int(row[33]), int(row[34]), int(row[35]), int(row[36]), int(row[37]), int(row[38]), int(row[39]), int(row[40]), int(row[41]), int(row[42]), int(row[43]), int(row[44])])
            answers_arr.append(int(row[45]))


# convert the lists to numpy array for performance, and then zip them together
train_data = np.asanyarray(input_arr)
correct_outputs = np.asanyarray(answers_arr)
data_and_labels = list(zip(train_data, correct_outputs))

# Define variables
n_samples = len(train_data)
print("number of samples: " + str(n_samples))

x = train_data.reshape((n_samples, -1))
print("train data shape: " + str(x.shape))

y = correct_outputs
print("answers data shape: " + str(y.shape))

# split the set and use 30 percent as test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
# # scale the features
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
print(x_test)
print(y_test)
x_test = sc.transform(x_test)

x_train = x_train.T
x_test = x_test.T
y_train = y_train.reshape(y_train.shape[0], 1)
y_test = y_test.reshape(y_test.shape[0], 1)
y_train = y_train.T
y_test = y_test.T

# generate weight matrix
Y_train_ = np.zeros((10, y_train.shape[1]))
for i in range(y_train.shape[1]):
    Y_train_[y_train[0, i], i] = 1

Y_test_ = np.zeros((10, y_test.shape[1]))
for i in range(y_test.shape[1]):
    Y_test_[y_test[0, i], i] = 1

n_x = x_train.shape[0]
n_h = 60
n_y = Y_train_.shape[0]

layers_dims = [n_x, n_h, n_y]
parameters = layered_network_layer_model(x_train, Y_train_, layers_dims, num_iterations=70000, print_cost=True)
predictions_train_L, raw_prediction_list_train = predict_layered_network_layer(x_train, parameters)

# Creates a scatter plot that visualizes the cost over time
plt.plot(cumulative_cost_data[0], cumulative_cost_data[1], 'ro')
plt.grid(True)
plt.title('Cost vs Iterations during Training')
plt.xlabel('# of Iterations')
plt.ylabel('Cost')



predictions_test_L, raw_prediction_list_test = predict_layered_network_layer(x_test, parameters)

expected_results = y_test[0].tolist()
predicted_results = list(np.array(raw_prediction_list_test))
print(expected_results)
print(predicted_results)
# calculate the confusion matrix
actual_y_predict_y = 0
actual_n_predict_y = 0
actual_y_predict_n = 0
actual_n_predict_n = 0
count = 0
for value in predicted_results:
    temp_val = value.astype(np.int32)
    if temp_val == expected_results[count]:
        actual_y_predict_y = actual_y_predict_y + 1
    count = count + 1
#
print("# predictions correct " + str(actual_y_predict_y/count) + " - " + str(actual_y_predict_y) + "/" + str(count) + '\n')
# print("A YES : P NO - " + str(actual_y_predict_n) + '\n')
# print("A NO : P NO - " + str(actual_n_predict_n) + '\n')
# print("A NO : P YES - " + str(actual_n_predict_y) + '\n')

plt.show()
