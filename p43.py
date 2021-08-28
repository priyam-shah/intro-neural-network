import numpy as np

layer_output = [[4.8, 1.21, 2.385],
                [8.9, -1.81, 0.2],
                [1.41, 1.051, 0.026]]

# exponentiation

'''
exponentiation quickly makes values massive
    np.exp(10) -> 22026.46
    np.exp(100) -> 2.6881171e+43
    np.exp(1000) -> overflow

therefore: we subtract every no from the largest no

{ this is implemented in p44 }
'''

exp_values = np.exp(layer_output)

# normalization

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)
'''
    axis = None (sum of all 9 values)
    axis = 0 (sum column wise)
    axis = 1 (sum row wise)

    keepdims=True prevers the shape
        so it will be the matrix of exact same dimentions
'''

print(norm_values)