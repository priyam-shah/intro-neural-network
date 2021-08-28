'''
In our ReLU function any -ve no will just become 0 { wether it is -9 or -9000 }

In softmax we would use:
    
    y = e^x (e = 2.7182) to get rid of -ve values
    
    ex: 
        x = -10 -> y = 0.00005
        x = -3.25 -> y = 0.038
        x = 6.68 -> y = 796.31

Input -> Exponentiation -> Normalization -> Output
Input -> Softmax -> Output

ex:

Dog - 1 - e^1 - e^1 / (e^1 + e^2 + e^3) - 0.09
Cat - 2 - e^2 - e^2 / (e^1 + e^2 + e^3) - 0.24
Hum - 3 - e^3 - e^3 / (e^1 + e^2 + e^3) - 0.67

'''