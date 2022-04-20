import numpy as np
import math
import sys

try:
    rows = int(input("How many rows? : "))
    columns = int(input("How many columns? : "))
except ValueError:
    print("Data Type Exception!")
else:
    if (rows or columns) < 1:
        print("Matrix can't have less than one row or column!")
        sys.exit(0)
    else:
        first_array = np.random.randint(-100, 100, size=(rows, columns))
        second_array = np.random.randint(-100, 100, size=(rows, columns))
        symmetric_difference = 0

        for i in range(rows):
            for j in range(columns):
                symmetric_difference += (first_array[i, j] - second_array[i, j])

        to_show = math.fabs(symmetric_difference)
        print(to_show)
