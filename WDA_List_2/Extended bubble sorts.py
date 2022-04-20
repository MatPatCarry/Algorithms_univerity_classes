from Zadanie import bubble_sort
import time
import random


def faster_bubble_sort(x):

    for i in range(len(x)):
        any_change = False
        for j in range(0, len(x) - 1):

            if x[j] > x[j + 1]:
                any_change = True
                temp_b = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp_b

        if any_change is False:
            return x
    return x


def slower_bubble_sort(x):

    for i in range(len(x)):
        j = 0

        for g in range(0, len(x) - 1):
            if x[j] > x[j + 1]:
                temp_b = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp_b
            j += 1

    return x


test = []
for x in range(500):
    test.append(random.randint(-10000, 10000))

normal_bubble = test.copy()
extended_bubble = test.copy()
slower_bubble = test.copy()

n_start = time.time()
bubble_sort(normal_bubble)
n_end = time.time()

f_start = time.time()
faster_bubble_sort(extended_bubble)
f_end = time.time()

s_start = time.time()
slower_bubble_sort(slower_bubble)
s_end = time.time()

print(f"Normal bubble sort's time equals {n_end - n_start} seconds.\n"
      f"Faster bubble sort's time equals {f_end - f_start} seconds.\n"
      f"Slower bubble sort's time equals {s_end - s_start} seconds for this dataset,"
      f" so the second is the most effective.")
