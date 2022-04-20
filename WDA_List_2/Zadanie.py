import random
import time
from matplotlib import pyplot as plt


# Bubble Sort
def bubble_sort(x):
    for i in range(len(x)):
        for j in range(0, len(x) - 1):
            if x[j] > x[j + 1]:
                temp_b = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp_b
    return x


# Insertion Sort
def insertion_sort(y):
    for i in range(len(y)):
        for j in range(0, i):
            if y[i] < y[j]:
                temp_i = y[i]
                y[i] = y[j]
                y[j] = temp_i
    return y


# Selection Sort
def selection_sort(z):
    for i in range(len(z)):
        for j in range(i + 1, len(z)):
            if z[i] > z[j]:
                temp_s = z[i]
                z[i] = z[j]
                z[j] = temp_s
    return z


def filling_in(numbers):
    filled_list = []
    for n in range(numbers):
        filled_list.append(random.randint(-10000, 10000))
    return filled_list


def counting_time(fn, tab):
    start = time.time()
    fn(tab)
    end = time.time()
    return end - start


bubble_times1 = []
insertion_times1 = []
selection_times1 = []

for x in range(10):
    how_many_numbers = random.randint(100, 1000)
    base_list1 = filling_in(how_many_numbers)
    bubble_sort_list = base_list1.copy()
    insertion_sort_list = base_list1.copy()
    selection_sort_list = base_list1.copy()
    bubble_times1.append(counting_time(bubble_sort, bubble_sort_list))
    insertion_times1.append(counting_time(insertion_sort, insertion_sort_list))
    selection_times1.append(counting_time(selection_sort, selection_sort_list))

print(f"Average bubble sort's time equals {sum(bubble_times1) / 10} seconds,"
      f" maximum time equals {max(bubble_times1)} seconds.\n"
      f"Average insertion sort's time equals {sum(insertion_times1) / 10} seconds,"
      f" maximum time equals {max(insertion_times1)} seconds.\n"
      f"Average selection sort's time equals {sum(selection_times1) / 10} seconds,"
      f" maximum time equals {max(selection_times1)} seconds.")

values = ['10', '20', '50', '100', '200', '500', '1000']
bubble_max = []
bubble_average = []
insertion_max = []
insertion_average = []
selection_max = []
selection_average = []


for value in values:

    base_list2 = filling_in(int(value))
    bubble_sort_list2 = base_list2.copy()
    insertion_sort_list2 = base_list2.copy()
    selection_sort_list2 = base_list2.copy()

    bubble_times2 = []
    insertion_times2 = []
    selection_times2 = []

    for y in range(10):
        bubble_times2.append(counting_time(bubble_sort, bubble_sort_list2))
        insertion_times2.append(counting_time(insertion_sort, insertion_sort_list2))
        selection_times2.append(counting_time(selection_sort, selection_sort_list2))

    bubble_max.append(max(bubble_times2))
    bubble_average.append(sum(bubble_times2) / int(value))

    insertion_max.append(max(insertion_times2))
    insertion_average.append(sum(insertion_times2) / int(value))

    selection_max.append(max(selection_times2))
    selection_average.append(sum(selection_times2) / int(value))

    base_list2.clear()


print(bubble_average)
print(insertion_average)
print(selection_average)

plt.style.use("bmh")

plt.title("Maximum times")
plt.xlabel("How many times sorting was carried out")
plt.ylabel("How long did it last to execute [s]")

plt.plot(values, bubble_max, color="#8A2BE2", linestyle=":", marker='.', linewidth=1, label='bubble sort')
plt.plot(values, insertion_max, color="red", linestyle=":", marker='.', linewidth=1, label='insertion sort')
plt.plot(values, selection_max, color="green", linestyle=":", marker='.', linewidth=1, label='selection sort')

plt.legend()
plt.show()

plt.style.use("bmh")

plt.title("Average times")
plt.xlabel("How many times sorting was carried out")
plt.ylabel("How long did it last to execute [s]")

plt.plot(values, bubble_average, color="#8A2BE2", linestyle=":", marker='.', linewidth=1, label='bubble sort')
plt.plot(values, insertion_average, color='red', linestyle=':', marker='.', linewidth=1, label='insertion sort')
plt.plot(values, selection_average, color='blue', linestyle=':', marker='.', linewidth=1, label='selection sort')

plt.legend()
plt.show()

