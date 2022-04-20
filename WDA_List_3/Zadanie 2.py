from Node_and_List import *
import random
from matplotlib import pyplot as plt


def counting_operations(office, queue):

    time = 0
    type_index = 0
    complexity_index = 1

    while True:

        only_zeros = True

        for window in office:

            if window[complexity_index] != 0:
                window[complexity_index] -= 1
                only_zeros = False

            else:
                if queue.length() != 0:
                    if window[type_index] == "E":
                        next_task = queue.first_item()
                        if next_task is None:
                            continue
                        else:
                            window[complexity_index] = next_task[1]
                            queue.remove(0)
                    else:
                        values = queue.correct_type(window[type_index])
                        if values is not None:
                            window[complexity_index] = values[0]
                            queue.remove(int(values[1]))
                        else:
                            continue
                else:
                    continue

        if only_zeros and queue.length() == 0:
            return time

        time += 1


def creating_queues():
    possible_tasks = ["A", "B", "C"]
    list_with_tasks = []
    for t in range(30):
        list_with_tasks.append([random.choice(possible_tasks), random.randint(1, 10)])
    new_first_queue = List()
    new_second_queue = List()
    for customer in list_with_tasks:
        new_first_queue.appending(customer)
        new_second_queue.appending(customer)
    return new_first_queue, new_second_queue


nine_windows_office = [["A"], ["A"], ["A"], ["B"], ["B"], ["B"], ["C"], ["C"], ["C"]]
eight_windows_office = [["A"], ["A"], ["B"], ["B"], ["C"], ["C"], ["E"], ["E"]]

for w1 in nine_windows_office:
    w1.append(0)

for w2 in eight_windows_office:
    w2.append(0)

first_queue = List()
second_queue = List()
additional_list = []
tasks = ["A", "B", "C"]

for task in range(30):
    additional_list.append([random.choice(tasks), random.randint(1, 10)])

for client in additional_list:
    first_queue.appending(client)
    second_queue.appending(client)

print(f'First customer service lasted {counting_operations(nine_windows_office, first_queue)} iterations.')
print(f'Second customer service lasted {counting_operations(eight_windows_office, second_queue)} iterations.')
print()

first_office_times = []
second_office_times = []

for case in range(100):
    queues = creating_queues()
    first = queues[0]
    second = queues[1]
    first_office_times.append(counting_operations(nine_windows_office, first))
    second_office_times.append(counting_operations(eight_windows_office, second))


first_average = sum(first_office_times)/100
second_average = sum(second_office_times)/100

print(f"First office's average time equals {first_average} iterations. ")
print(f"Second office's average time equals {second_average} iterations. ")

bins = [15, 20, 25, 30, 35, 40, 45, 50]
plt.style.use("seaborn-whitegrid")

plt.hist(first_office_times, bins=bins, edgecolor='black', color="#FFA07A")

plt.axvline(first_average, color="blue", label='Average time')   # why is label not working
plt.title("Nine windows in office")
plt.xlabel("How did it last to do all tasks")
plt.ylabel("Total number of iterations")

plt.show()

plt.hist(second_office_times, bins=bins, edgecolor='black', color="#7FFFD4")

plt.axvline(second_average, color="red", label='Average time')  # why is label not working
plt.title("Eight windows in office")
plt.xlabel("How did it last to do all tasks")
plt.ylabel("Total number of iterations")

plt.show()
'''
First office's time average is a little bit higher than second office's time average and we can't forget about
the fact that first office has one window more than second office. To conclude, it can be seen clearly, that having
special window 'E' which can operate each type of task is more effective and faster.

W tym zadaniu modyfikacja jak w pierwszym zadaniu mogłaby mieć sens gdybyśmy za każdym razem tworzyli nowy urząd,
po usunięciu wszystkich okienek z urzędu, trzeba by je z powrotem dodać, czyli stworzyć nowy urząd.
Jednak dobrym usprawnieniem mogłoby być wyszukiwanie okienka o dopasowanym typie zadania, dla oczekującego klienta,
w dodatku można by przeskakiwać od razu o 3 okienka gdy pierwsze danego typu nie pasuje.
'''


