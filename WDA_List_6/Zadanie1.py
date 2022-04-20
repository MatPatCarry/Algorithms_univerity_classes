import numpy as np
import random


def creating_graph(n, dijkstra=False, kruskal_or_prim=False):
    matrix_graph = np.zeros((n, n))
    matrix_graph[0] = [x for x in range(n)]
    for r in range(n):
        matrix_graph[r][0] = r

    for row_index in range(1, n):
        for column_index in range(1, n):
            if dijkstra:
                d = random.randint(0, 1)
                if d == 1:
                    matrix_graph[row_index][column_index] = random.randint(1, 9)
                else:
                    matrix_graph[row_index][column_index] = 0
            elif kruskal_or_prim:
                matrix_graph[row_index][column_index] = random.randint(0, 9)
            else:
                matrix_graph[row_index][column_index] = random.randint(0, 1)

    # test
    '''
    for r_i in range(1, 3):
        for c_i in range(1, n):
            if c_i >= 3:
                matrix_graph[r_i][c_i] = 0
            else:
                matrix_graph[r_i][c_i] = 1
    '''
    for diagonal in range(1, n):
        matrix_graph[diagonal][diagonal] = 0

    column_indexes = [x + 1 for x in range(n - 1)]

    for row_index_2 in range(1, n):
        for column_index_2 in column_indexes:
            if matrix_graph[row_index_2][column_index_2] == matrix_graph[column_index_2][row_index_2]:
                continue
            else:
                matrix_graph[column_index_2][row_index_2] = matrix_graph[row_index_2][column_index_2]

    return matrix_graph


n = random.randint(4, 10)

matrix_graph = creating_graph(n)
print(matrix_graph)
list_of_sets = []
current_list = []
for i in range(1, n):
    current_set = set()
    current_set.add(i)
    current_list.append(i)
    while len(current_list) != 0:
        current_element = int(current_list.pop())
        for j in range(1, n):
            if matrix_graph[j][current_element] == 1 and current_element != j:
                if j in current_set:
                    continue
                else:
                    current_set.add(j)
                    current_list.append(j)
            else:
                continue
    current_set = frozenset(current_set)
    list_of_sets.append(current_set)

result = list(set(list_of_sets))
for item_index in range(len(result)):
    result[item_index] = list(set(result[item_index]))

print()
number = 1
for c_c in result:
    graph = '\ '
    for top_number in c_c:
        graph += str(int(matrix_graph[0][top_number])) + " "
    graph = graph + "\n"
    for w in c_c:
        graph += str(int(matrix_graph[w][0])) + " "
        for k in c_c:
            if matrix_graph[w][k] == 1:
                graph += "+ "
            elif w == k:
                graph += "\ "
            else:
                graph += '- '
        graph = graph + "\n"
    print(f'{number}. Connected component: \n\n{graph}')
    number += 1
