"""
@BY: Reem Alghamdi
@DATE: 30-10-2020
"""
import numpy as np


def limb_length(n, j, d):
    minimum = float("inf")
    # print(j)
    for i in range(n):
        for k in range(i + 1, n):
            if i != j and k != j:
                value = (d[i][j] + d[k][j] - d[i][k]) // 2
                # print(j, i, k, d[i][j], d[k][j], d[i][k], value)
                if value < minimum:
                    minimum = value

    return minimum


def solve_limb_length(n, j, string):

    matrix = format_matrix(n, string)

    print(limb_length(n, j, matrix))


def format_matrix(n, string):
    matrix = np.zeros((n, n), dtype=int)
    rows = string.split("\n")
    for i, elements in enumerate(rows):
        for k, element in enumerate(elements.split()):
            matrix[i][k] = int(element)
    return matrix


if __name__ == "__main__":
    string = """0	13	21	22
13	0	12	13
21	12	0	13
22	13	13	0"""
    solve_limb_length(4, 1, string)

    # with open("../data/dataset_369349_11.txt") as file:
    #     solve_limb_length(27, 13, file.read())
