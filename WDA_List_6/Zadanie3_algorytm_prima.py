from Zadanie1 import creating_graph
from Zadanie2 import output, creating_dict
import random
import heapq
print("\n----------------Zad3_prim_algorithm-------------------\n")

n = 6

matrix = creating_graph(n, False, True)
output(matrix, n)
graph = creating_dict(matrix, n)

possible_distances = []

for key, value in graph.items():
    for neigh, distance in value.items():
        if distance != 0:
            possible_distances.append([int(distance), key, neigh])

possible_distances.sort(key=lambda y: y[0])

for index, item in enumerate(possible_distances):
    possible_distances[index] = set(item)

used_tops = []
pdc = possible_distances.copy()
for item_index in range(len(pdc)):
    for tup_index in range(len(pdc)):
        if (pdc[item_index] == pdc[tup_index]) and (item_index != tup_index) and (pdc[item_index] not in used_tops):
            possible_distances.remove(pdc[tup_index])

    used_tops.append(pdc[item_index])


result = []
for f, s, t in possible_distances:
    if type(f) is int:
        result.append([f, s, t])
    elif type(s) is int:
        result.append([s, f, t])
    elif type(t) is int:
        result.append([t, s, f])


possible_start = ["a", "b", "c", "d", "e"]
start = random.choice(possible_start)
print(start)
visited_tops = []
possible_tops = []
p_distances = []
pairs = []
current = start

for _ in range(n-2):
    for item in result:
        if current in item:
            possible_tops.append(item)
    print(possible_tops)
    if current not in visited_tops:
        visited_tops.append(current)

    if len(possible_tops) == 0:
        break

    heapq.heapify(possible_tops)

    condition = True
    while condition:
        chosen = heapq.heappop(possible_tops)
        if chosen[1] in visited_tops and chosen[2] in visited_tops:
            continue
        else:
            result.remove(chosen)
            dist = chosen[0]
            first = chosen[1]
            second = chosen[2]
            condition = False

            if first == current or second == current:
                if first != current:
                    pairs.append((current, first))
                    current = first
                elif second != current:
                    pairs.append((current, second))
                    current = second
            else:
                pairs.append((first, second))
                if first not in visited_tops:
                    current = first
                elif second not in visited_tops:
                    current = second
            p_distances.append(dist)
    print(current)

    if _ == n-3:
        visited_tops.append(current)


print(visited_tops)
print(p_distances)
for x in range(len(pairs)):
    print(f'{pairs[x][0]} ---- ({p_distances[x]}) ---- {pairs[x][1]}')


