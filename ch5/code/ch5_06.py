"""
@BY: Reem Alghamdi
@DATE: 02-10-2020
"""
import numpy as np


def manhattan_tourist(n, m, down, right):
    """
    n×m are rectangle dimensions
    n × (m + 1) matrix Down
    (n + 1) × m matrix Right

    return The length of a longest path from source (0, 0) to sink (n, m)
    """
    s = np.zeros((n + 1, m + 1), dtype=int)

    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i - 1][0]
    for j in range(1, m + 1):
        s[0][j] = s[0][j - 1] + right[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1])
    return s[n, m]


if __name__ == "__main__":
    with open("../data/dataset_369314_10.txt") as file:
        n = 6
        m = 4
        d = np.zeros((n, m + 1), dtype=int)
        r = np.zeros((n + 1, m), dtype=int)
        print(np.shape(d), np.shape(r))
        data = file.read().split("-")
        for k, matrix in enumerate(data):
            rows = matrix.split("\n")
            rows.remove("")
            for i, elements in enumerate(rows):
                for j, element in enumerate(elements.split()):
                    if k == 0:
                        d[i][j] = int(element)
                    else:
                        r[i][j] = int(element)

    print(manhattan_tourist(n, m, d, r))