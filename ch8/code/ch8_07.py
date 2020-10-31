"""
@BY: Reem Alghamdi
@DATE: 31-10-2020
"""
import pandas as pd
import numpy as np

from ch8.code.ch8_03 import format_matrix
from ch8.code.ch8_06 import closest_clusters
from ch8.code.ch8_extra import Tree


def total_distance(d):
    """return vector of sum of rows"""

    return {k: sum(d[k]) for k in d.keys()}


def d_star(d, t_d, n):
    d_s = d.copy(deep=True)
    for i in d.keys():
        for j in d.keys():
            if j > i:
                d_s[i][j] = d_s[j][i] = (n - 2) * d[i][j] - t_d[i] - t_d[j]
    return d_s


def neighbour_joining(d, nodes):
    # print("INNER", inner)
    n = np.shape(d)[0]
    if n == 2:
        k = list(d.keys())
        tree = Tree()
        tree.link(k[0], k[1], d[k[0]][k[1]])
        return tree
    t_d = total_distance(d)
    # print(t_d)
    d_s = d_star(d, t_d, n)
    # print(d_s)
    i, j = closest_clusters(d_s)
    # print(i, j)
    delta = (t_d[i] - t_d[j]) / (n - 2)
    limb_length_i = 0.5 * (d[i][j] + delta)
    limb_length_j = 0.5 * (d[i][j] - delta)
    # print(d)
    m = {}
    inner = nodes[-1] + 1
    nodes.append(inner)
    for k in d.keys():
        m[k] = 0.5 * (d[k][i] + d[k][j] - d[i][j])
    # print("m", m)
    d[inner] = pd.Series(m)
    # print("d1", d)
    m[inner] = 0
    # d = d.append(m, ignore_index=True)
    d.loc[inner] = m
    # print("d2\n", d)
    d = d.drop([i, j])
    d = d.drop([i, j], axis=1)
    # print(d)
    t = neighbour_joining(d, nodes)

    t.link(inner, i, limb_length_i)
    t.link(inner, j, limb_length_j)

    return t


def solve_neighbour_joining(n, string):
    matrix = format_matrix(n, string)
    # print(matrix)
    d = pd.DataFrame(matrix)
    d.columns = list(range(n))
    d.index = list(range(n))
    neighbour_joining(d, list(range(n))).AdjList(is_float=True)


if __name__ == "__main__":
    # string = """0	13	21	22
    # 13	0	12	13
    # 21	12	0	13
    # 22	13	13	0"""
    # string = """0	3	4	3
    # 3	0	4	5
    # 4	4	0	2
    # 3	5	2	0"""
#     string = """0	23	27	20
# 23	0	30	28
# 27	30	0	30
# 20	28	30	0"""
#     solve_neighbour_joining(4, string)

    # with open("../data/dataset_369353_7.txt") as file:
    #     solve_neighbour_joining(32, file.read())

    string = """0	295	300	524	1077	1080	978	941	940
295	0	314	487	1071	1088	1010	963	966
300	314	0	472	1085	1088	1025	965	956
524	487	472	0	1101	1099	1021	962	965
1076	1070	1085	1101	0	818	1053	1057	1054
1082	1088	1088	1098	818	0	1070	1085	1080
976	1011	1025	1021	1053	1070	0	963	961
941	963	965	962	1057	1085	963	0	16
940	966	956	965	1054	1080	961	16	0"""
    solve_neighbour_joining(9, string)

