import numpy as np

arange_normal = np.arange(8) # Making array in range from 0 to 7 (according to parameters, the parameters is the stop number)
arange_antara = np.arange(1,8) # Making an array in range from the first to second params, example (1,8) then it will show 1,2,3...8
arange_interval = np.arange(1,24,2) # Same as before, but there is interval on third params (ex : 1,3,5 the second params is the interval)

#RESHAPE
example_array = np.array((np.arange(0,8,2), np.arange(1,8,2)))
normal_reshape = example_array.reshape((2,4)) #MAKING THE ARRAY TO 2 ROWS 4 COLS
reshape_channel = example_array.reshape((2,1,4))

#EMPTY ARRAY
array_zero = np.zeros((2,4)) # AN ARRAY CONTAIN 0 WITH 2 ROW 4 COLS
array_empty = np.empty((2,4)) # AN ARRAY CONTAINS RANDOM NUMBER
array_ones = np.ones((2,4)) # AN ARRAY CONTAIN 1 WITH 2 ROW 4 COLS

#EYE ARRAY
array_eye = np.eye(4) # AN ARRAY CONTAIN IDENTITY MATRIX, IF THE PARAMS WAS 3, THEN 3X3
array_eye[array_eye == 0] = 2 #CHANGE THE 0 ON THE IDENTITY / EYE MATRIX ARRAY TO 2
array_eye[1:] = 3 #CHANGE NUMBER IN (ROW AFTER 1) TO 3, IT MEANS ROW 2,3,4 ARE CHANGING
array_eye[:,3] = 2 #CHANGE NUMBER IN COLUMN 3 (FOURTH COLUMN) INTO TWO

#SORTING ARRAY
array_sorted_row = np.sort(array_eye) #SORTING THE ROWS, (ex : [2,9,3] to [2,3,9])
array_sorted_cols = np.sort(array_eye, axis=0) #SORTING THE COLS, (ex : [2,9,3],[1,2,4] to [1,2,3], [2,9,4])

print(array_sorted_row, "this is row")
print(array_sorted_cols, "this is col")
print(type(arange_normal))

