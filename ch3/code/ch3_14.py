"""
@BY: Reem Alghamdi
@DATE: 17-10-2020
"""
from ch3.code.ch3_08 import format_adjacency_list
from ch3.code.ch3_10 import graph_degrees


def maximal_non_branching_paths(adj_list):

    paths = []
    degrees = graph_degrees(adj_list)
    # print(adj_list)
    # print(degrees)
    visited = []
    for v in degrees.keys():
        if degrees[v] != [1, 1]:
            if degrees[v][1] > 0:
                visited.append(v)
                try:
                    for w in adj_list[v]:
                        non_branching_path = [v, w]
                        # print(v, w, degrees[v], degrees[w])

                        # print(v, w, degrees[v], degrees[w])
                        while degrees[w] == [1, 1]:
                            visited.append(w)
                            u = adj_list[w][0]
                            non_branching_path.append(u)
                            # print(v, w, u, degrees[v], degrees[w], degrees[u])
                            # print(v, w, u, degrees[v], degrees[w], degrees[u])
                            w = u
                        paths.append(' -> '.join(non_branching_path))
                        # print(paths[-1])
                except:
                    pass
    # print(adj_list)
    # print(degrees)
    # print(paths)

    for v in degrees.keys():
        if degrees[v] == [1, 1] and v not in visited:
            visited.append(v)
            # print(v, degrees[v])
            isolated = [v]
            w = adj_list[v][0]
            while degrees[w] == [1, 1]:
                isolated.append(w)
                visited.append(w)
                if v == w:
                    break
                # print(v, w, degrees[v], degrees[w])
                w = adj_list[w][0]

            paths.append(" -> ".join(isolated))
            # print(paths[-1])
    # print(adj_list)
    # print(degrees)

    return paths


if __name__ == "__main__":
    with open("../data/ch3_14") as file:
        print('\n'.join(maximal_non_branching_paths(format_adjacency_list(file.read()))))
#
#     print('\n'.join(maximal_non_branching_paths(format_adjacency_list("""1 -> 2
# 2 -> 3
# 3 -> 4,5
# 6 -> 7
# 7 -> 6"""))))

#     print('\n'.join(maximal_non_branching_paths(format_adjacency_list("""0 -> 1
# 1 -> 2
# 2 -> 3,4"""))))

#     print('\n'.join(maximal_non_branching_paths(format_adjacency_list("""5 -> 3
# 3 -> 4
# 1 -> 2
# 6 -> 1
# 2 -> 6"""))))

#     print('\n'.join(maximal_non_branching_paths(format_adjacency_list("""1 -> 2
# 2 -> 3,4,5
# 4 -> 6,10
# 5 -> 7
# 6 -> 10"""))))
#
#     print('\n'.join(maximal_non_branching_paths(format_adjacency_list("""7 -> 10
# 10 -> 14
# 14 -> 3,5,18
# 5 -> 4
# 52 -> 13
# 4 -> 8
# 8 -> 14
# 18 -> 19
# 19 -> 31
# 31 -> 52"""))))

#     print('\n'.join(maximal_non_branching_paths(format_adjacency_list("""7 -> 3
# 3 -> 4
# 4 -> 8
# 8 -> 9
# 9 -> 7
# 1 -> 2
# 2 -> 5
# 5 -> 10
# 10 -> 2
# 16 -> 111
# 111 -> 16"""))))