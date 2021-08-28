import math
import numpy as np

E = math.e

layer_output = [4.8, 1.21, 2.385]

# exponentiation

exp_values = np.exp(layer_output)
    
# normalization

norm_values = exp_values / np.sum(exp_values)

print(sum(norm_values)) # add upto 1