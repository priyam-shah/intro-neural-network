# 3 neurons with 4 inputs v2

inputs = [1, 2, 3, 2.5]

weights = [
    [0.2, 0.8, -0.5, 1.0],
    [0.5, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
    ]

biases = [2, 3, 0.5]

layer_output = [] # output for current layer


for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # output for given neuron

    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight

    neuron_output += neuron_bias
    layer_output.append(neuron_output)

print(layer_output)


'''
keys:
 1. zip combines two lists into list of lists element wise
 2. bias is sort of ofset
 3. weight is changing the magnitude

'''