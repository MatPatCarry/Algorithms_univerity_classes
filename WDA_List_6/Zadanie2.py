from Zadanie1 import creating_graph

print('\n-------------------Zad2_dijkstra_algorithm------------------------\n')


def dijkstra_algorithm(graph, start, goal):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph.copy()
    infinity = float("inf")
    path = []
    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes.keys():
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, distance in graph[min_node].items():
            if distance + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = distance + shortest_distance[min_node]
                predecessor[child_node] = min_node

        unseen_nodes.pop(min_node)

    current_node = goal
    while current_node != start:
        try:
            path.insert(0, current_node)
            current_node = predecessor[current_node]
        except KeyError:
            print('Path not reachable')
            break
    path.insert(0, start)

    if shortest_distance[goal] != infinity:
        print(f'Shortest distance between {start} and {goal} is ' + str(int(shortest_distance[goal])))

        result = "The path is: "
        for item_index in range(len(path)):
            if item_index != len(path) - 1:
                result += str(path[item_index]) + " ---- (" + str(int(graph[path[item_index]][path[item_index + 1]])) \
                          + ") ----> "
            else:
                result += str(path[item_index])
        print(result)


def output(matrix, n):
    alphabet = 'abcdefghij'
    to_show = '_ '
    for top_number in range(n - 1):
        to_show += alphabet[top_number] + " "
    to_show = to_show + "\n"
    for w in range(1, n):
        to_show += alphabet[w - 1] + " "
        for k in range(1, n):
            if matrix[w][k] >= 1:
                to_show += str(int(matrix[w][k])) + " "
            elif w == k:
                to_show += "0 "
            else:
                to_show += '- '
        to_show = to_show + "\n"
    print(to_show)


def creating_dict(matrix, n):
    alp = 'abcdefghij'
    graph = {}
    for r in range(1, n):
        graph[alp[r - 1]] = {}
        for c in range(1, n):
            if matrix[r][c] != 0 and r != c:
                graph[alp[r - 1]][alp[c - 1]] = matrix[r][c]
            elif r == c:
                graph[alp[r - 1]][alp[c - 1]] = 0

    return graph


dimension = 8
graph_matrix = creating_graph(dimension, True, False)
output(graph_matrix, dimension)
dijkstra_algorithm(creating_dict(graph_matrix, dimension), "a", "c")



