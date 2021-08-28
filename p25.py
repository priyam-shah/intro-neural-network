# converting layers into objects

import numpy as np

# With the seed reset (every time), the same set of numbers will appear every time.
np.random.seed(0)

# input feature sets are denoted by X
X = [
    [1, 2, 3, 2.5],
    [2.0, 5.0, -1.0, 2.0],
    [-1.5, 2.7, 3.3, -0.8]
    ]

# initializeing a model ->
#   weights: random value b/w range of -1 & 1

class Layer_Dense:

    def __init__(self, n_inputs, n_neurons):
        # Initialize weights and biases
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        # Calculate output values from inputs, weights and biases
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 2)

layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)

'''
np.random.randn:
    + produces a Gaussian distribution with a mean of 0 and a variance of 1
    + which means that it’ll generate random numbers, positive and negative,
        centered at 0 and with the mean value close to 0
    + We’re going to multiply this Gaussian distribution for the weights by
        0.01 to generate numbers that are a couple of magnitudes smaller
    + np.random.randn function takes dimension sizes as parameters and creates
        the output array with this shape
    + The weights here will be the number of inputs for the first dimension
        and the number of neurons for the 2nd dimension

    ex:
        print(np.random.randn(2,5))
        >>>
            [[ 1.7640524 0.4001572 0.978738 2.2408931 1.867558 ]
            [-0.9772779 0.95008844 -0.1513572 -0.10321885 0.41059852]]

        function call has returned a 2x5 array (which we can also say is
        “with a shape of (2,5)”) with data randomly sampled from a Gaussian
        distribution with a mean of 0

np.zeros:
    np.zeros function takes a desired array shape as an argument and returns
    an array of that shape filled with zeros.

    ex:
        print(np.zeros((2,5)))
        >>>
            [[0. 0. 0. 0. 0.]
            [0. 0. 0. 0. 0.]]

    We’ll initialize the biases with the shape of (1, n_neurons),
    as a row vector, which will let us easily add it to the result
    of the dot product later, without additional operations like
    transposition