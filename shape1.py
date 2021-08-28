'''

Notes:

    so the concept of shape is that
        at each dimentions whats the size of that dimentiosn

             1
            list with 4 elements -> [1, 5, 6, 2]
            Type -> 1D array, Vector
            Shape -> (4)

            2
            lol -> [ [1, 5, 6, 2], [3, 2, 1, 3] ]
            Type -> 2D array , matrix (list of vectors)
            Shapr -> (2, 4)

            3
            lolol -> [ [ [1, 5, 6, 2],
                         [3, 2, 1, 3] ]
                       [ [5, 2, 1, 2],
                         [6, 4, 8, 4] ],
                       [ [2, 8, 5, 3],
                         [1, 1, 9, 4] ] ]
            Type -> 3D array Tensor
            Shape -> (3, 2, 4)

            Tensor: is an object that can be represented as an array

    what we want to do
        inputs * weights + bias
        vector * matrix of vectors + vector
            so we need dot product
                a=[1, 2, 3] b=[2, 3, 4]
                dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
                >>> 20 (scaler value)
