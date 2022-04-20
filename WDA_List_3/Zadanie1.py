from Node_and_List import *
import numpy as np
import random

office = [["A"], ["A"], ["A"], ["B"], ["B"], ["B"], ["C"], ["C"], ["C"], ["E"]]

for w in range(len(office)):
    (office[w]).append(random.randint(1, 10))
    (office[w]).append(0)
print(office)

queue = List()
tasks = ["A", "B", "C"]
for x in range(30):
    queue.appending([random.choice(tasks), random.randint(1, 10)])

time = 0
times_index = 2
complexity_index = 1
type_index = 0

while True:

    only_zeros = True

    for window in office:

        if window[complexity_index] != 0:
            window[complexity_index] -= 1
            window[times_index] += 1
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
        number = 1
        print(f'Completed iterations: {time}')
        print(f'How many operations has each window done: ')
        for win in office:
            print(f'{number}. window has done {win[times_index]} operations.')
            number += 1
        break

    time += 1

'''
W tym zadaniu okienka A, B, C, które stają się wolne wyszukuje w kolejce zadanie swojego typu. Usprawnieniem
w tym przypadku może być "zamykanie" okienka, wtedy gdy w kolejce nie ma już typu zadań danego okienka, a wykonało
one już swoje zadania, wtedy można by usuwać takie okienko z urzędu, co spowoduje krótszą iteracje w przyszłosci.
'''