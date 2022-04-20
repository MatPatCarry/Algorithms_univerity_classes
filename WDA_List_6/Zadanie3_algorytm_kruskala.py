from Zadanie1 import creating_graph
from Zadanie2 import output, creating_dict

print("\n----------------Zad3_kruskal_algorithm-------------------\n")


gh = {"a": {"a": 0, "b": 2, "c": 4, "e": 1}, "b": {"a": 2, "b": 0, "c": 8, "d": 1},
      "c": {"a": 4, "b": 8, "c": 0, "d": 3},
      "d": {"b": 1, "c": 3, "d": 0, "e": 2 }, "e": {"a": 1, "d": 2, "e": 0 }}

possible_distances = []
print(gh)
for key, value in gh.items():
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


final = []
for f, s, t in possible_distances:
    if type(f) is int:
        final.append([f, s, t])
    elif type(s) is int:
        final.append([s, f, t])
    elif type(t) is int:
        final.append([t, s, f])


visited_tops = []
path_distances = []
path = []

for index, (dist, start, goal) in enumerate(final):
    any_operation = False
    if index == 0:
        visited_tops.append(start)
    if goal not in visited_tops:
        visited_tops.append(goal)
        path.append((start, goal))
        any_operation = True
    elif start not in visited_tops:
        visited_tops.append(start)
        path.append((start, goal))
        any_operation = True
    if any_operation:
        path_distances.append(dist)

for x in range(len(path)):
    print(f'{path[x][0]} ---- ({path_distances[x]}) ---- {path[x][1]}')

