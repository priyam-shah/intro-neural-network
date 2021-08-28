import numpy as np

def spiral_data(points, classes):

    X = np.zeros((points*classes, 2))
    '''
    calling as (100, 3) -> X = np.zeros(300, 2)
        [
         [0, 0],
         [0, 0],
         ... 300 times
        ]
    '''
    y = np.zeros(points*classes, dtype='uint8') # Data type of returned array
    ''' [0, 0, 0 ... 300 times] '''

    for class_number in range(classes):

        ix = range(points*class_number, points*(class_number+1))
        ''' nos b/w | 0-100 | 100-200 | 200-300 | '''

        r = np.linspace(0.0, 1, points)  # radius
        ''' 100 nos equally distributed b/w 0.0 & 1 '''

        t = np.linspace(class_number*4, (class_number+1)*4, points) + np.random.randn(points)*0.2
        ''' t = 100 nos equally distributed b/w | 0-4 |  4-8 | 8-12 |
                added with a random number
        '''

        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
        # print(X)
        # print(y)
    return X, y


class Layer_Dense:

    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.01 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU: # Rectified Linear Unit

    def forward(self, inputs):
        # Calculate output values from input
        self.output = np.maximum(0, inputs)

X, y = spiral_data(100, 3)

# Create Dense layer with 2 input features and 3 output values
layer1 = Layer_Dense(2,3)

# Create Dense layer with 2 input features and 3 output value
activation1 = Activation_ReLU()

# Make a forward pass of our training data through this layer
layer1.forward(X)

# Forward pass through activation func.
# Takes in output from previous layer
activation1.forward(layer1.output)

print(activation1.output)

'''

np.linspace(start, stop, num):
    Return evenly spaced numbers over a specified interval.
    start: The starting value of the sequence.
    stop: The end value of the sequence (stop is excluded)
    num: Number of samples to generate
        ie num evenly distributed numbers will be generated b/w start and stop
    ex:
        print(np.linspace(2, 3))
        print(np.linspace(2, 3, 5))

np.random.randn():
    Return a sample (or samples) from the “standard normal” (Gaussian)
        distribution of mean 0 and variance 1.

    ex:
        np.random.randn(6)
        will create a 1-D array with 6 random items

np.c_[]:
    adds along second (horizontal ) axis
    
    ex:
        np.c_[np.array([1,2,3]), np.array([4,5,6])]
            { shape of both array becomes (3,1) }
            { resultant shape would be (3,1+1) which is (3,2) }
        
        array([[1, 4],
               [2, 5],
               [3, 6]])

'''