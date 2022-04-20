import numpy as np


def levenshtein_distance(first, second):
    n = len(first)
    k = len(second)

    needed_array = np.zeros((n + 1, k + 1))
    column_values = [x for x in range(k + 1)]
    needed_array[0] = column_values

    for row in range(n + 1):
        needed_array[row][0] = row

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if first[i - 1] == second[j - 1]:
                cost = 0
            else:
                cost = 1
            needed_array[i][j] = min(needed_array[i - 1][j] + 1,
                                     needed_array[i][j - 1] + 1,
                                     needed_array[i - 1][j - 1] + cost)
    return needed_array[-1][-1]


while True:
    result = levenshtein_distance(input("Please, pass first string: "), input("Please, pass second string: "))
    print(f"Levenshtein distance equals: {result}")
    once_again = input("One more time?: \n[1] Yes\n[2] No\n ")
    if once_again == 1:
        continue
    else:
        break


'Złozonosc czasowa to n*k'