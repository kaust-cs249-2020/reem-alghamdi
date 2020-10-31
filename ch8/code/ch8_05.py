"""
@BY: Reem Alghamdi
@DATE: 31-10-2020
"""
import numpy as np
import pandas as pd

from ch8.code.ch8_03 import format_matrix


def closest_clusters(d, n):
    min_dist = float("inf")
    index = ()
    for i in d.keys():
        for j in d.keys():
            if i != j:
                if d[i][j] < min_dist:
                    min_dist = d[i][j]
                    index = (i, j)
    return index


def upgma(d, n):
    inner = n
    clusters = {i: 1 for i in range(n)}
    age = {i: 0 for i in range(n)}
    adj_list = {i: [] for i in range(n)}
    weights = {}
    d = pd.DataFrame(d)
    d.columns = list(range(n))
    d.index = list(range(n))
    # print(d)
    # print(clusters, age, adj_list)
    while len(clusters) > 1:
        # print("NEW")
        # print(d)
        i, j = closest_clusters(d, np.shape(d)[0])
        c_i = clusters[i]
        c_j = clusters[j]
        elements_count = c_i + c_j
        # print(i, j, c_i, c_j, elements_count, d[i][j])
        adj_list[inner] = [i, j]
        adj_list[i].append(inner)
        adj_list[j].append(inner)

        weights[(inner, i)] = 0
        weights[(inner, j)] = 0
        weights[(i, inner)] = 0
        weights[(j, inner)] = 0

        # print(adj_list, weights)
        age[inner] = d[i][j] / 2
        # print(age)
        # print(d)
        del clusters[i]
        del clusters[j]
        # print(clusters)
        new_addition = []
        for m in clusters.keys():
            # print(m)
            # print("C", d[i][c_m], c_i[1], d[j][c_m], c_j[1], elements_count)
            new_di = (d[i][m] * c_i + d[j][m] * c_j) / elements_count
            new_addition.append(new_di)

        # print(d, (i, j))
        # print(new_addition)
        # d = np.delete(d, (j, i), axis=0)
        # d = np.delete(d, (i, j), axis=1)

        d = d.drop([i, j])
        d = d.drop([i, j], axis=1)
        d[inner] = new_addition

        # print(d)
        # d = np.append(d, [new_addition], axis=0)
        # print(d)
        new_addition.append(0)
        d.loc[inner] = new_addition
        # d = np.append(d, np.reshape(new_addition, (np.shape(d)[0], 1)), axis=1)

        # print(d)
        clusters[inner] = elements_count

        inner += 1

    for edge, weight in weights.items():
        if weight == 0:
            v = edge[0]
            w = edge[1]
            # print(edge, weight, age[v], age[w])
            weights[(v, w)] = abs(age[v] - age[w])
            weights[(w, v)] = abs(age[v] - age[w])

    return adj_list, weights


def solve_upgma(n, string):
    matrix = format_matrix(n, string)
    # print(matrix)
    weights = upgma(matrix, n)[1]
    for edge, w in weights.items():
        print(f"{edge[0]}->{edge[1]}:{w:.3f}")


if __name__ == "__main__":
#     string = """0	20	17	11
# 20	0	20	13
# 17	20	0	10
# 11	13	10	0"""
#     string = """0	3	4	3
#     3	0	4	5
#     4	4	0	2
#     3	5	2	0"""
#     solve_upgma(4, string)

    with open("../data/dataset_369352_8.txt") as file:
        solve_upgma(30, file.read())
