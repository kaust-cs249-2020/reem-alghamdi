"""
@BY: Reem Alghamdi
@DATE: 30-11-2020
"""
import numpy as np
from numpy.linalg import norm


def max_distance(data, centers):
    max_ = -np.inf
    point = None
    for datapoint in data:
        distance, p = d(datapoint, centers)
        if distance > max_:
            max_ = distance
            point = datapoint
    return max_, point
"""
Distortion(Data,Centers) = (1/n) ∑all points DataPoint in Datad(DataPoint, Centers)2 .
"""


def distortion(data, centers):
    return sum([d(datapoint, centers)[0] ** 2 for datapoint in data]) / len(data)


def d(datapoint, centers):
    min_ = np.inf
    point = None

    for x in centers:
        distance = norm(x - datapoint)
        if distance < min_:
            min_ = distance
            point = x
    return min_, point


if __name__ == "__main__":
    data = np.array([
        [1,6],
        [1,3],
        [3,4],
        [5,6],
        [5,2],
        [7,1],
        [8,7],
        [10,3]
    ], dtype=float)
    centers = np.array([
      [2, 4], [6, 7], [7, 3]
    ], dtype=float)
    print(max_distance(data, centers))
