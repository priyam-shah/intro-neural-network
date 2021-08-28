# Step Activation Function:
#     mimic a neuron “firing” or “not firing”
#     based on input information

inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]

output = []

# rectified linear activation function

for i in inputs:
    if i > 0:
        output.append(i)
    elif i <= 0:
        output.append(0)

print(output)