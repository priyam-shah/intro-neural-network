import math

E = math.e

layer_output = [4.8, 1.21, 2.385]

# exponentiation

exp_values = []

for output in layer_output:
    exp_values.append(E**output)
    
# normalization

norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value / norm_base)

# print(sum(norm_values)) # add upto 1