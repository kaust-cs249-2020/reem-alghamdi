"""
@BY: Reem Alghamdi
@DATE: 01-12-2020
"""
from random import choices
import numpy as np
from ch12.code.ch12_05 import d
from ch12.code.ch12_06 import format_matrix
from ch12.code.ch12_07 import squared_error_distortion


def center_of_gravity(data):
    center = np.zeros(len(data[0]), dtype=np.float)
    for datapoint in data:
        center += datapoint
    center /= len(data)
    return center


def lloyd_algorithm_k_means(k, data):
    """
    The Lloyd algorithm is one of the most popular clustering heuristics for the k-Means Clustering Problem.
    It first chooses k arbitrary distinct points Centers from Data as centers and then iteratively performs the following
    two steps (see figure below):

    Centers to Clusters: After centers have been selected, assign each data point to the cluster corresponding to
    its nearest center; ties are broken arbitrarily.

    Clusters to Centers: After data points have been assigned to clusters, assign each cluster’s center of gravity
    to be the cluster’s new center.
    """

    # random k centers:
    centers = list([list(x) for x in data[:k]])

    # CENTERS TO CLUSTERS:
    clusters = {i: [] for i in range(k)}
    for datapoint in data:
        clusters[centers.index(list(d(datapoint, centers)[1]))].append(datapoint)

    # CLUSTERS TO CENTERS
    centers_new = [list(center_of_gravity(v)) for v in clusters.values()]
    clusters_new = {i: [] for i in range(k)}
    for datapoint in data:
        clusters_new[centers_new.index(d(datapoint, centers_new)[1])].append(datapoint)

    i = 0
    while set(map(tuple, centers)) != set(map(tuple, centers_new)):
        i += 1
        clusters = clusters_new
        centers = centers_new

        centers_new = [list(center_of_gravity(v)) for v in clusters.values()]
        clusters_new = {i: [] for i in range(k)}
        for datapoint in data:
            clusters_new[centers_new.index(d(datapoint, centers_new)[1])].append(datapoint)

    return centers


if __name__ == "__main__":
#     data = """1.3 1.1
# 1.3 0.2
# 0.6 2.8
# 3.0 3.2
# 1.2 0.7
# 1.4 1.6
# 1.2 1.0
# 1.2 1.1
# 0.6 1.5
# 1.8 2.6
# 1.2 1.3
# 1.2 1.0
# 0.0 1.9"""

    data = """13.5 13.5 0.3 14.2 16.8
0.8 2.4 6.4 9.6 18.1
12.8 12.2 10.5 3.1 9.8
3.2 1.9 4.2 6.4 8.0
4.4 14.7 8.6 4.7 5.1
5.6 12.9 6.0 6.6 5.6
22.0 10.8 16.5 4.4 8.2
19.5 3.1 0.3 2.5 10.5
12.1 3.6 7.3 9.0 16.0
7.8 12.3 4.2 5.6 4.8
2.9 7.9 5.3 5.4 1.2
10.0 1.3 4.4 12.1 5.9
9.8 11.9 0.1 4.7 3.9
1.2 13.5 14.3 13.9 11.6
16.3 3.6 6.1 21.5 3.6
14.2 4.8 12.7 22.4 10.6
7.5 3.8 3.8 8.9 10.5
9.0 2.8 2.3 8.0 20.2
4.8 4.9 14.0 16.1 12.4
8.8 7.2 1.0 2.9 0.1
0.7 1.6 5.8 9.7 3.1
8.0 4.8 10.9 6.5 2.2
16.5 13.9 11.4 4.7 8.8
10.1 6.3 2.2 1.4 3.3
3.9 5.7 9.6 17.7 13.4
4.1 10.6 11.1 8.0 9.5
9.5 5.7 16.3 2.3 11.5
6.4 12.4 11.9 11.6 14.9
2.9 5.6 12.2 12.9 1.9
2.6 4.5 3.2 2.2 5.9
5.7 0.3 9.5 10.2 7.7
3.6 0.3 2.7 20.3 8.0
16.9 12.3 9.1 10.8 5.1
6.5 11.0 8.5 14.5 8.2
12.2 0.2 8.3 3.5 2.9
8.7 20.2 2.8 6.9 10.0
6.2 13.4 10.5 3.0 5.2
0.3 5.9 14.8 17.0 2.1
4.8 4.2 8.4 2.5 11.5
5.8 2.8 9.1 17.6 9.3
5.9 2.1 14.2 5.6 4.8
6.2 1.5 12.7 13.6 0.1
24.9 12.7 11.9 1.0 29.2
18.7 4.2 21.5 11.7 17.4
1.0 16.9 3.2 8.5 2.2
15.7 2.3 1.9 3.4 6.3
12.8 7.8 5.4 5.0 7.2
0.6 7.0 2.9 6.3 16.1
4.7 6.2 8.1 3.3 4.1
9.6 13.0 12.0 19.3 3.7
1.5 15.4 0.6 6.9 15.5
6.0 4.9 5.1 11.1 23.0
14.0 8.5 7.4 15.2 1.9
15.9 7.5 4.6 2.3 7.4
7.9 10.5 8.6 25.8 10.2
5.4 5.0 10.7 13.1 2.8
2.1 6.7 2.9 17.6 2.2
4.3 7.9 6.2 12.2 5.3
9.6 7.2 0.9 10.3 8.6
4.9 6.6 9.6 0.4 21.0
4.1 4.3 0.4 0.4 24.7
11.8 1.2 4.3 7.6 7.8
7.3 0.2 3.7 0.2 3.0
6.8 8.3 14.4 6.5 21.3
0.6 3.6 3.8 6.5 1.6
2.8 13.3 4.8 9.4 3.6
3.0 0.3 1.0 6.6 8.4
10.7 11.2 0.1 6.3 5.0
11.2 13.1 5.8 8.5 11.2
25.6 6.4 13.9 0.7 12.8
20.4 3.9 11.3 0.6 1.0
10.2 15.4 9.1 7.7 16.4
4.7 10.5 3.4 14.8 4.4
19.5 12.6 11.0 7.1 18.6
0.8 0.5 25.1 14.9 7.5
3.9 9.0 15.4 3.1 5.5
11.4 7.8 5.2 2.5 11.2
9.8 26.5 10.8 7.6 8.4
16.0 4.3 0.7 1.8 1.4
16.1 7.9 17.3 0.8 28.9
0.3 6.6 4.0 2.4 9.3
8.9 9.5 9.9 4.9 7.4
16.0 8.8 3.1 9.1 2.6
2.7 0.3 4.1 7.4 2.7
6.9 5.6 8.3 3.8 13.1
3.6 1.7 7.4 10.7 5.4
0.9 6.9 7.3 8.8 7.4
2.7 10.7 1.7 13.7 24.0
6.3 9.2 7.5 2.4 0.2
16.6 1.8 9.5 9.6 2.5
8.6 12.5 3.7 6.5 2.5
11.6 13.3 11.6 11.4 9.0
1.2 1.8 6.7 3.5 6.0
4.7 0.3 14.8 7.3 14.3
8.8 16.3 1.9 8.7 7.7
11.2 16.7 16.7 9.3 16.7
1.5 1.4 3.9 10.2 8.1
10.1 1.3 2.5 7.8 31.2
14.5 15.5 16.9 2.7 22.9
17.7 2.9 3.8 9.1 3.5
5.5 12.1 13.0 4.1 1.9
10.1 15.6 12.1 11.0 16.0
8.4 8.1 3.8 19.0 7.2
3.0 1.1 4.6 3.3 4.7
1.7 0.3 4.5 19.8 23.3
2.0 22.0 15.2 3.1 1.7
19.1 5.1 1.9 22.3 1.0
9.6 1.1 0.2 24.8 4.8
23.0 6.8 16.8 13.2 16.5
0.1 7.2 0.2 16.5 7.0
25.0 9.9 8.4 17.9 4.7
9.7 10.6 20.8 10.9 12.3
7.7 11.9 11.4 4.3 3.4
3.2 5.3 3.6 4.0 1.1
4.3 3.3 2.3 8.7 5.2
3.8 3.6 17.6 10.6 6.8
10.7 12.9 10.3 5.5 0.7
1.8 0.9 14.2 0.9 1.3
19.9 7.3 2.9 0.9 1.8
2.0 11.3 0.2 9.2 14.0
1.1 13.2 12.0 10.4 2.8
23.1 30.9 11.0 5.9 14.6
3.5 6.2 5.9 9.9 10.8
1.1 5.0 9.4 1.6 1.1
13.6 8.1 5.6 10.5 10.6
10.7 3.0 9.4 8.2 9.6
4.2 1.6 9.8 13.3 0.1
7.7 0.9 6.3 2.3 2.7
6.6 10.0 10.0 5.3 7.4
11.7 0.3 4.1 1.4 2.1
15.4 1.0 12.9 10.3 3.5
15.4 17.1 5.2 0.9 3.2
5.0 0.1 8.5 8.1 0.1
10.9 18.8 6.1 8.8 6.9
23.8 11.3 1.1 6.9 13.9
3.9 1.7 7.4 2.9 12.0
8.1 5.5 18.5 0.1 17.0
5.0 11.5 6.1 5.3 7.8
0.2 6.3 9.8 16.4 8.2
0.0 1.7 9.0 0.4 4.5
1.6 7.1 2.0 2.5 4.7
19.0 4.4 2.2 5.6 9.4
7.0 10.8 13.5 11.7 13.8
7.6 8.3 10.8 14.3 6.1
7.7 8.9 2.3 14.5 7.1
0.2 5.0 13.8 0.5 5.0
10.6 19.6 5.6 12.9 1.1
9.2 7.6 4.3 11.3 5.2
6.6 15.8 0.6 3.3 10.7
17.8 16.7 4.1 10.6 15.7
3.3 13.4 9.5 0.4 17.9
9.6 5.5 8.0 17.2 1.4
0.7 1.5 17.5 1.6 6.3
0.5 14.4 1.9 13.7 5.2
0.3 4.1 8.3 13.5 4.2
20.2 11.7 1.4 8.3 17.5
22.6 10.0 5.5 0.4 13.2
3.8 10.1 35.8 9.7 1.9
10.5 11.8 14.4 6.7 0.2
17.4 16.1 14.6 17.5 16.9
4.4 1.5 4.3 12.9 1.2
19.5 11.8 5.3 10.5 13.8
7.5 12.7 10.2 17.3 3.4
3.6 3.3 1.0 5.9 17.1
2.4 10.9 1.8 3.4 8.0
16.0 7.3 4.6 9.3 9.1
5.6 1.1 14.0 9.0 1.3
0.2 8.4 11.9 1.8 24.2
6.4 2.9 7.2 15.4 5.0
0.8 11.1 17.6 10.1 9.9
8.2 4.0 19.0 7.3 19.4
5.4 2.4 12.7 1.9 7.6
4.2 3.5 2.7 4.1 1.0
6.2 2.1 6.4 8.1 9.9
20.4 15.1 1.2 2.6 12.8
13.0 3.0 10.4 3.7 9.3
6.8 5.7 17.1 1.1 2.0
6.7 12.7 14.6 7.7 0.9
17.9 8.8 14.9 1.6 5.2
10.4 9.7 8.9 6.0 16.4
17.8 16.0 14.4 14.4 2.6
4.4 1.8 24.7 15.6 7.4
10.7 11.7 6.7 19.1 0.7
6.6 6.5 21.3 2.9 15.4
8.9 11.1 8.5 8.6 0.1
0.4 0.8 15.6 18.0 7.0
18.4 22.3 5.8 11.7 6.1
0.7 19.6 25.5 7.5 0.7
5.2 13.1 3.6 6.8 9.3
5.0 1.4 4.5 11.2 14.9
2.2 6.2 8.4 16.6 4.5
12.8 9.4 8.5 4.9 7.8
9.5 7.8 9.2 0.9 21.0
7.7 15.8 4.9 8.0 0.4
2.6 4.5 0.5 3.0 10.8
7.4 14.1 8.1 1.6 7.8
0.7 1.3 6.5 8.4 16.2
16.7 0.4 18.6 4.9 1.1
15.5 0.2 9.0 4.3 10.5
0.7 11.0 20.2 1.5 10.1
3.6 7.6 5.0 1.0 2.0
16.0 2.9 12.4 12.4 26.5
13.2 7.8 2.7 7.8 0.3
4.7 5.3 0.0 16.3 5.9
17.3 4.0 10.2 3.0 5.7
16.4 12.7 7.8 9.3 0.8
6.2 4.2 13.7 6.3 5.7
14.1 21.8 3.3 4.9 10.4
5.3 7.1 17.1 6.3 13.0
6.3 0.3 15.8 0.9 0.8
5.8 13.1 0.5 13.7 4.9
17.7 13.1 12.7 13.1 17.9
19.6 8.9 4.4 17.7 20.6
14.1 4.4 5.4 1.1 5.7
7.0 1.4 5.5 3.3 16.7
18.3 5.5 17.4 1.7 23.9
11.4 15.4 7.7 5.9 4.2
0.8 2.5 1.7 1.6 4.8
1.7 4.9 0.3 19.1 11.4
1.3 13.9 8.9 3.2 11.4
24.8 1.0 8.7 25.1 12.3
0.6 5.4 8.6 4.9 12.2
8.4 14.8 9.1 6.7 13.9
0.9 8.0 1.6 16.2 10.6
6.6 13.7 11.8 8.5 9.1
15.6 8.1 10.3 1.7 16.1
0.8 8.1 4.8 1.1 5.0
14.0 6.0 26.2 14.0 2.4
7.3 5.7 1.5 4.2 10.8
12.4 21.4 1.2 2.4 4.8
5.8 4.5 8.5 4.6 6.5
6.8 1.1 10.5 5.4 1.8
7.8 5.5 5.3 3.1 4.8
10.6 1.7 0.5 0.4 15.8
8.1 1.0 6.1 5.9 2.4
19.2 10.3 10.9 2.6 4.3
12.4 13.9 6.6 7.5 9.7
16.4 8.8 10.3 0.6 5.3
13.4 6.7 10.0 0.3 11.3
0.0 7.9 4.9 0.4 8.0
0.4 4.5 8.6 27.2 7.5
11.2 5.8 1.1 6.7 5.8
15.8 11.8 14.5 3.4 10.2
1.4 15.8 1.9 3.6 22.3
8.3 9.6 0.6 2.4 4.0
4.1 14.3 9.7 12.9 6.4
9.0 7.6 0.1 10.8 15.2
21.6 7.2 15.8 2.4 18.1
2.4 1.1 16.9 8.5 0.9
16.2 5.4 16.8 0.4 1.4
4.2 1.0 2.9 0.6 3.3
1.2 2.4 2.5 10.1 22.8
12.5 0.2 15.0 2.0 8.3
5.1 1.6 8.3 11.2 0.3
19.2 5.8 2.2 6.5 9.4
3.9 7.2 16.5 1.0 11.2
1.4 14.6 9.2 7.5 3.3
3.9 3.2 5.1 12.6 7.5
3.7 21.1 11.3 10.1 2.9
1.9 14.6 1.7 4.6 16.5
2.6 0.6 15.6 7.5 1.2
2.2 2.5 7.2 8.9 17.6
6.9 6.5 13.3 17.1 8.3
2.5 9.2 15.0 3.8 18.3
8.0 2.6 3.4 2.9 5.0
2.5 0.0 7.2 0.4 24.7
2.0 7.8 1.6 4.3 3.9
12.3 2.2 1.1 4.6 0.4
9.7 13.8 14.7 5.8 5.0
9.4 12.8 14.7 4.9 7.6
10.3 0.0 12.1 2.1 8.9
15.1 20.1 7.8 18.8 14.2
12.9 7.6 0.1 3.7 2.2
0.7 4.5 13.9 5.9 6.4
4.8 0.8 7.1 2.2 5.6
4.9 1.8 16.8 2.3 7.0
16.1 0.1 8.7 6.9 1.8
4.0 5.1 15.6 23.3 1.5
8.4 1.2 13.7 22.5 12.5
8.7 16.3 6.5 6.4 1.3
4.5 0.8 4.4 2.2 5.6
24.0 2.7 9.5 16.6 18.7
9.9 2.3 6.6 9.9 16.5
12.3 10.4 8.4 1.3 0.2
12.0 5.4 5.2 6.8 2.2
5.6 0.1 0.9 18.1 6.3
7.3 15.9 28.1 7.2 0.1
1.8 0.8 3.0 15.9 2.7
3.8 7.7 4.5 12.4 11.9
8.6 6.2 3.0 8.2 5.7
10.1 7.5 17.1 7.5 12.1
3.2 0.5 9.9 0.4 15.6
5.1 2.3 3.6 3.6 6.3
0.7 15.4 8.9 7.8 11.8
6.7 8.3 4.3 10.1 2.3
15.2 5.0 3.8 11.9 6.3
6.5 5.3 3.6 6.0 2.9
0.3 6.2 2.9 0.9 0.3
11.8 1.5 8.3 0.7 0.5
5.3 12.5 13.3 16.1 5.4
14.0 1.6 4.5 1.9 16.0
2.8 11.8 20.3 7.8 5.4
21.5 8.7 0.8 9.9 24.5
9.2 5.7 13.7 22.1 1.1
4.3 19.0 12.5 23.1 5.1
4.1 3.6 5.4 9.1 1.7
7.0 1.5 5.3 0.1 0.2
2.2 9.2 6.3 16.1 5.9
5.2 7.5 15.6 0.3 4.3
4.8 2.8 0.5 10.7 8.7
10.2 13.2 12.6 10.5 4.5
12.2 11.9 0.6 4.7 1.5
2.1 1.3 8.9 1.8 1.3
0.7 4.5 30.4 10.7 3.6
7.6 12.3 5.5 4.2 2.5
0.2 17.1 22.7 9.6 3.8
8.6 14.8 0.3 4.8 2.2
0.4 16.9 13.8 1.0 5.3
6.4 24.5 2.5 15.2 1.3
9.0 7.6 8.8 4.4 20.8
13.8 8.9 3.7 4.2 28.5
0.4 0.8 18.8 11.7 2.1
13.9 4.1 14.6 1.3 3.3
2.0 10.1 16.9 18.3 18.1
14.8 6.0 3.8 0.5 14.6
3.1 5.2 18.1 12.0 18.1
4.6 1.6 4.5 18.6 5.0
0.4 8.0 4.4 11.0 4.4
2.5 5.5 13.5 3.0 3.6
4.2 0.6 1.0 21.5 5.0
7.8 11.6 1.0 9.1 11.5
2.9 10.4 1.6 4.4 20.3
2.1 7.0 2.8 3.8 4.5
18.8 13.8 2.1 8.8 11.4
17.5 6.4 19.4 13.5 8.4
7.4 6.7 7.9 10.4 11.8
2.6 9.2 7.2 0.5 6.5
10.3 6.3 1.2 13.9 12.5
2.1 4.9 3.9 6.8 5.9
5.5 2.2 15.9 13.0 2.7
10.5 5.7 1.1 1.4 9.1
12.2 0.1 6.9 6.4 6.6
9.0 7.4 8.3 1.0 19.3
2.4 10.0 16.9 8.0 10.2
10.1 10.6 1.5 6.3 3.1
18.8 12.0 22.0 8.5 1.7
6.7 5.5 1.8 7.0 12.2
2.4 9.7 0.5 9.8 3.8
23.9 2.5 5.3 8.0 24.7
0.4 1.2 2.1 9.1 15.7
2.3 11.6 1.8 2.1 4.5
7.6 0.9 12.5 35.4 7.9
1.8 7.7 6.7 2.9 12.1
10.6 20.0 8.0 18.6 2.9
1.0 7.6 10.8 10.5 4.0
9.7 1.2 5.2 11.0 14.9
23.0 5.7 0.8 3.6 16.8
8.4 11.0 9.1 4.0 2.4
10.3 12.1 2.4 4.3 7.8
2.4 7.5 0.1 11.9 1.4
17.2 4.5 5.6 0.2 12.2
14.8 11.9 4.8 11.8 0.0
6.2 5.5 14.2 4.6 5.7
4.1 10.2 1.2 5.3 6.8
13.0 3.7 2.9 12.7 0.3
3.0 12.8 0.6 4.0 8.2
6.7 0.0 10.6 11.7 2.8
17.2 1.0 5.3 3.7 4.9
5.6 3.7 11.8 14.5 0.9
7.8 1.8 5.0 3.5 5.7
2.2 18.2 6.7 7.2 7.9
4.1 10.7 1.3 6.0 17.0
6.0 13.7 7.8 17.0 4.5
4.4 14.6 1.0 19.5 1.4
0.6 2.7 3.9 8.8 5.2
6.1 4.0 11.2 28.0 19.6
6.5 2.3 7.3 3.1 17.2
16.6 7.8 14.4 11.9 20.6
5.2 1.5 14.9 3.9 1.2
0.8 8.6 0.7 4.3 3.7
8.4 4.7 5.8 2.0 3.6
17.0 5.2 7.3 9.8 1.7
25.7 12.5 7.1 16.8 11.3
6.9 9.9 8.5 3.9 17.4
1.0 7.3 12.5 4.5 7.5
3.6 1.6 14.9 2.4 6.0
8.1 3.8 10.2 7.5 2.8
8.0 2.4 0.4 3.9 3.7
5.5 23.2 1.0 10.9 8.5
8.2 15.9 3.3 0.5 13.8
11.5 21.6 3.7 2.7 7.4
1.0 19.0 6.8 5.2 5.5
4.0 1.7 10.1 11.0 6.9
5.7 3.7 2.6 5.7 16.0
8.1 9.1 0.5 0.6 6.5
17.7 36.0 6.2 0.2 6.0
16.9 1.5 6.5 3.1 13.9
3.5 1.9 12.7 0.7 8.2
9.3 9.3 13.2 8.2 9.4
12.4 4.9 2.9 14.7 0.1
5.1 10.9 20.5 1.6 8.9
2.8 18.4 5.0 0.5 14.1
12.9 0.4 11.4 1.6 9.2
4.4 14.9 16.3 7.9 8.2
2.9 28.9 6.8 5.6 6.9
19.5 1.8 1.8 3.5 10.3
8.3 14.9 17.2 0.8 7.2
0.5 11.5 1.2 1.2 13.6
1.6 3.6 5.8 0.7 4.0
4.0 3.6 1.2 0.1 6.1
12.0 7.9 0.3 12.5 5.1
7.2 8.3 4.1 2.0 18.9
11.6 18.1 15.7 14.0 15.4
1.6 13.2 9.8 15.2 8.2
10.9 12.3 2.9 1.8 25.4
10.4 14.7 0.1 4.9 10.4
11.2 6.2 1.8 10.5 2.8
1.8 1.9 9.5 13.1 1.6
14.4 8.4 9.9 7.7 12.1
6.3 11.7 4.6 16.3 14.9
12.5 26.1 2.6 12.4 15.0
2.4 14.3 0.5 2.4 19.1
4.0 5.9 1.4 10.4 15.3
4.5 9.6 17.4 8.4 16.6
0.7 1.6 6.7 11.0 7.6
1.7 2.5 1.3 11.8 7.2
9.7 1.6 11.9 6.6 12.5
4.1 4.4 7.8 8.8 13.1
1.4 0.3 18.1 1.5 13.5
5.1 12.6 12.8 19.3 2.7
5.5 9.9 1.5 3.0 11.5
12.9 12.6 4.7 4.5 0.3
0.9 2.1 10.9 22.1 6.6
2.2 18.9 22.2 13.4 4.2
9.5 3.7 14.7 6.2 2.6
18.9 7.2 5.6 8.2 1.9
2.7 3.5 1.5 6.0 5.8
1.0 6.1 1.9 2.5 10.5
13.6 8.0 3.3 5.7 6.6
7.2 28.9 12.8 1.3 18.3
20.5 9.1 13.8 5.5 2.4
9.1 8.3 10.9 4.3 2.3
11.0 4.2 7.6 3.1 12.6
8.3 7.6 4.7 13.9 4.8
1.8 0.2 8.7 0.6 16.4
5.4 0.1 0.3 12.6 8.3
3.0 1.9 5.3 10.3 23.7
3.0 2.8 7.0 19.5 11.7
3.5 1.5 0.6 3.3 4.6
22.5 7.4 6.4 14.4 12.8
3.2 1.4 11.5 18.2 24.6
5.1 12.9 13.1 15.0 3.6
4.9 13.2 3.5 7.5 15.7
12.2 19.9 11.9 5.0 8.1
10.5 1.8 0.8 3.2 6.5
0.2 7.6 1.9 13.5 11.3
5.1 2.0 20.7 2.5 4.0
14.3 29.1 1.4 3.1 16.5
26.4 6.0 5.6 0.7 1.0
7.5 1.4 10.9 14.2 9.0
12.8 0.5 9.7 22.0 12.6
10.5 5.4 12.6 4.5 4.5
19.9 3.4 2.4 10.0 0.4
20.4 24.3 6.8 7.3 1.5
16.2 19.0 10.6 3.0 8.9
15.2 15.7 10.4 16.8 1.0
4.9 5.4 3.0 2.1 7.2
20.0 3.5 4.4 12.5 3.5
7.6 1.3 13.3 9.2 6.6
1.5 11.6 5.5 3.5 2.6
8.5 17.6 4.5 22.0 11.3
8.9 9.9 5.5 14.7 7.3
10.2 12.9 8.5 16.9 2.1
5.0 2.7 2.2 5.2 4.6
12.1 7.6 8.2 3.0 0.2
2.5 6.9 1.1 9.7 2.5
15.5 15.3 4.4 4.3 2.9
3.0 0.4 2.2 1.6 9.4
8.3 10.8 6.6 5.5 5.8
4.1 2.7 1.4 2.2 4.5
5.1 19.5 6.3 6.5 0.8
3.6 7.3 1.0 4.1 5.5
6.8 17.2 2.7 13.6 9.4
7.3 2.5 16.1 7.1 6.4
2.9 10.7 10.2 0.3 11.6
18.1 5.8 1.8 10.5 11.0
20.5 11.1 2.1 0.4 3.4
5.3 24.5 3.0 12.5 12.2
13.5 2.2 7.0 1.0 2.4
0.7 7.3 0.1 19.9 11.1
14.6 10.6 0.6 0.4 15.3
15.3 12.7 3.3 0.8 9.0
1.7 10.4 5.5 8.6 6.3
23.3 10.4 11.7 10.4 17.8
7.0 8.0 6.9 1.9 1.4
0.9 5.1 17.8 6.9 15.6
4.6 1.1 12.7 6.7 12.0
2.2 9.6 10.8 3.9 16.3
9.8 0.4 8.9 19.7 21.3
2.5 4.4 7.0 2.8 1.6
10.1 13.8 9.2 1.7 5.4
2.9 10.7 3.6 0.6 25.2
1.7 9.3 3.6 5.7 9.2
15.0 5.3 14.6 16.9 3.2
10.9 3.2 15.3 19.8 4.6
3.8 3.8 5.9 1.2 13.2
6.3 5.6 5.9 9.9 6.2
12.1 9.0 12.5 2.4 7.0
16.1 3.3 7.0 1.4 11.0
14.9 10.4 0.6 5.0 4.3
0.8 6.4 2.3 3.9 4.6
9.4 4.7 10.9 12.2 8.1
3.2 2.9 2.6 8.6 2.8
14.6 7.7 4.4 8.3 3.1
1.7 3.9 7.9 13.8 4.1
19.5 3.2 4.4 12.2 9.8
0.2 1.5 9.5 18.9 4.1
13.3 0.4 11.4 1.2 21.5
10.6 3.9 15.2 7.1 17.7
4.2 5.9 3.8 22.0 14.5
7.6 4.9 5.9 9.2 30.1
4.8 4.6 7.5 3.6 0.6
0.5 15.9 3.1 4.2 2.7
1.4 0.4 2.0 12.7 4.5
6.5 3.5 7.3 1.6 13.4
1.3 2.2 3.8 9.1 22.1
14.7 12.3 5.1 14.4 7.4
7.1 18.9 1.6 6.1 17.8
0.1 6.2 8.3 1.1 6.8
11.8 15.1 14.0 8.8 12.9
4.1 3.7 2.7 2.8 2.5
2.3 5.3 0.8 1.7 3.1
0.8 10.3 4.0 16.7 12.7
28.6 5.3 2.9 10.5 2.0
8.8 3.7 0.5 2.7 22.8
4.3 1.2 11.8 0.7 1.2
27.1 6.0 12.7 15.3 0.0
8.7 12.2 11.2 4.9 18.5
0.5 7.3 8.8 5.0 13.8
14.5 3.4 4.6 3.7 7.2
3.2 4.9 1.3 4.7 2.6
20.5 25.7 3.7 2.4 25.1
2.1 10.7 1.1 12.9 9.0
4.1 10.0 8.8 0.3 2.6
21.1 9.1 18.3 15.2 28.4
8.1 25.0 2.9 4.8 0.0
16.3 14.6 0.8 15.3 8.6
2.9 0.4 6.3 5.5 10.7
5.1 6.5 18.3 16.4 4.2
9.5 13.0 7.3 8.9 16.6
1.0 1.0 8.4 6.1 8.1
0.9 0.8 21.2 5.9 1.5
16.5 8.7 2.3 5.3 7.4
31.7 4.5 21.6 13.8 2.5
25.0 14.0 1.0 9.6 9.3
4.8 6.7 18.2 5.9 4.9
10.8 15.1 4.2 4.1 7.1
6.3 2.1 10.2 5.4 0.1
14.5 11.1 12.8 14.0 9.8
14.0 0.8 6.1 1.2 5.5
13.0 16.2 4.2 10.7 1.9
2.9 10.2 7.6 4.0 2.3
7.5 12.9 11.5 5.0 7.5
3.6 17.9 2.5 2.4 2.8
3.1 7.6 19.4 15.6 2.2
12.2 10.1 15.7 0.5 12.7
1.7 2.8 9.5 13.9 23.1
1.0 3.3 5.8 8.5 12.4
5.2 17.8 4.7 4.3 7.7
5.6 19.5 3.0 2.2 21.9
11.5 0.7 11.5 1.4 10.3
10.6 9.7 0.3 21.8 5.8
11.2 2.8 2.6 9.9 6.9
12.8 5.8 0.9 1.0 13.3
9.5 10.2 11.7 5.8 7.2
0.2 5.3 14.9 2.8 16.0
14.7 23.6 8.6 8.4 5.1
4.6 10.4 3.5 20.4 6.1
1.7 10.5 2.0 6.9 9.4
12.7 5.3 7.7 3.8 7.7
12.7 0.8 7.6 6.8 1.9
15.7 17.6 4.9 9.2 10.2
7.4 6.2 0.4 4.4 12.8
11.0 9.0 4.1 1.4 4.5
11.0 7.1 16.9 8.4 0.2
22.6 6.6 12.7 9.7 4.8
13.7 23.3 4.7 16.7 15.2
14.5 13.1 2.8 11.5 14.1
8.5 2.6 2.3 14.7 5.8
7.3 20.2 7.7 8.3 5.2
10.7 5.8 2.9 5.6 17.8
5.8 13.8 7.0 8.7 16.0
14.8 9.4 1.0 2.8 3.7
0.9 20.3 19.0 4.2 2.6
2.2 11.3 4.0 1.0 13.0
1.1 3.1 5.2 8.1 8.3
0.2 5.7 1.3 13.1 12.1
25.7 9.2 2.5 3.5 5.2
8.5 1.4 1.4 19.5 17.4
5.3 21.6 3.3 6.3 19.6
4.2 6.8 16.8 7.6 0.3
9.5 22.4 11.2 2.7 14.8
16.6 1.2 2.7 2.2 6.9
14.0 9.2 13.4 3.1 0.6
6.2 12.3 0.0 10.9 20.1
1.1 1.2 15.2 11.8 9.6
2.3 6.3 15.8 5.5 13.9
12.5 11.8 2.4 23.6 2.3
13.5 21.5 6.9 1.9 11.9
8.1 10.5 8.3 9.1 2.2
3.1 18.5 13.3 15.7 13.4
6.1 0.0 8.8 2.9 9.8
15.0 0.4 1.4 3.6 22.0
8.5 17.8 7.8 11.0 17.7
17.0 13.0 10.5 2.0 1.1
3.7 5.2 4.1 5.0 5.0
2.6 0.1 22.6 0.7 23.9
7.2 8.7 3.2 6.3 19.3
5.0 7.4 10.2 6.1 5.1
0.7 0.7 0.0 6.7 0.3
12.7 14.8 7.8 7.0 5.1
16.8 13.2 2.1 1.0 4.5
12.2 4.8 9.4 10.2 12.6
28.9 0.8 5.7 2.0 7.4
7.4 18.0 6.6 15.9 6.5
3.0 16.7 1.9 11.6 2.0
14.1 0.0 16.6 4.6 3.4
0.4 0.7 9.0 6.5 0.5
2.9 8.3 9.1 11.2 1.3
17.9 7.3 9.2 1.3 17.2
13.9 3.4 19.4 11.3 15.7
6.8 3.9 4.6 1.8 9.3
11.7 7.6 11.0 5.7 0.6
7.7 5.6 17.1 4.4 7.8
7.9 9.1 4.0 0.7 8.0
4.6 6.5 9.5 2.0 3.4
9.3 1.0 9.2 4.1 15.8
8.7 10.1 6.6 1.2 1.3
16.1 20.8 4.9 2.1 13.0
0.4 11.7 1.7 4.4 22.7
7.3 8.5 5.3 16.6 11.0
12.6 0.6 7.3 0.8 7.7
11.3 14.1 21.9 9.8 20.0
16.5 0.1 1.3 3.1 5.9
10.2 2.7 1.9 23.3 10.9
0.6 11.1 10.8 10.7 12.6
14.9 16.1 3.3 5.0 2.2
4.2 22.8 15.5 4.1 0.0
4.3 0.6 8.0 6.6 2.9
20.4 2.0 2.8 2.7 8.3
11.5 17.4 6.6 21.4 5.2
10.6 7.8 2.9 3.2 4.9
15.6 10.1 6.6 0.6 1.1
15.8 1.8 8.8 4.8 4.0
1.0 1.2 0.1 8.5 7.3
3.3 6.2 0.7 7.5 1.3
1.9 0.9 9.0 12.5 21.1
19.8 1.3 6.7 27.4 17.2
7.8 1.8 12.4 2.7 2.4
12.4 1.9 14.4 8.7 0.3
0.9 3.9 4.5 3.4 2.2
0.3 19.2 4.1 23.6 7.9
0.2 10.6 2.1 17.2 4.9
14.5 2.5 3.0 10.0 15.2
17.6 2.3 4.3 9.6 0.8
9.3 2.3 6.2 14.4 6.6
27.7 8.2 11.4 0.8 8.0
14.8 6.2 16.2 9.2 20.5
4.2 25.7 12.0 3.0 0.1
4.4 24.6 10.0 4.0 4.0
1.5 11.5 8.2 10.3 15.0
3.4 2.9 11.8 1.9 19.0
10.3 7.6 3.1 9.5 1.7
7.0 13.5 8.0 15.3 3.0
6.8 9.5 8.7 6.1 9.8
8.0 4.4 5.3 11.6 5.4
0.8 9.7 2.6 15.3 11.6
3.8 5.2 10.3 7.8 12.8
5.4 2.1 1.6 3.5 4.5
22.1 9.9 8.4 13.7 3.6
10.2 6.9 9.8 9.9 8.5
16.0 17.4 10.4 7.4 1.9
0.9 15.1 9.3 14.6 8.5
9.1 7.0 8.8 0.2 1.6
6.7 7.3 1.4 2.0 2.4
13.6 2.8 12.0 1.9 7.9
6.3 0.3 6.4 0.0 2.9
2.6 6.5 20.0 0.0 2.0
9.1 7.1 12.2 1.4 16.6
24.3 2.2 13.0 18.3 11.3
5.8 5.1 6.7 2.3 16.1
3.2 5.9 22.0 16.1 3.8
15.2 14.6 2.0 4.1 8.0
1.3 3.5 1.2 2.0 4.6
8.2 0.0 4.6 1.0 19.8
0.3 1.9 3.7 3.5 4.2
12.6 6.6 5.7 1.4 0.4
0.2 9.9 16.0 3.6 8.0
1.2 6.1 8.1 29.0 9.0
0.8 20.8 6.4 4.1 13.7
6.2 7.5 4.2 6.8 6.8
2.0 23.4 0.0 17.2 22.9
6.8 12.9 16.5 4.0 4.3
5.9 19.0 25.6 6.7 3.9
1.6 4.3 9.2 0.9 9.5
9.9 2.9 1.1 4.3 1.8
11.0 2.8 2.7 11.1 12.5
15.3 10.4 7.1 3.4 25.1
0.6 18.8 18.0 14.6 11.4
9.2 22.5 9.7 6.7 12.2
12.8 6.3 8.5 4.5 16.3
13.3 3.1 7.8 12.9 0.6
6.6 19.9 6.9 16.3 4.7
2.9 2.3 1.0 10.9 19.1
2.4 6.8 9.3 5.1 4.3
6.2 7.6 1.2 12.6 22.7
1.2 11.9 11.4 4.2 2.1
19.7 4.4 5.3 6.6 2.0
1.0 2.9 12.0 9.6 6.9
4.7 10.5 2.9 5.3 10.5
5.4 0.6 5.9 10.4 15.7
20.6 22.4 3.1 17.9 10.1
8.9 0.6 1.9 12.4 12.2
0.5 6.5 1.8 19.0 14.1
12.7 4.3 11.2 2.0 5.5
2.5 4.4 5.7 12.6 4.0
9.2 3.4 11.1 6.4 1.2
1.8 17.6 12.2 10.2 11.1
5.6 5.5 0.5 0.1 12.2
2.3 13.9 8.5 11.8 2.7
17.6 3.3 5.1 18.1 9.7
5.9 0.8 5.2 2.3 5.2
1.9 12.4 10.8 0.1 5.4
14.3 6.0 0.7 5.1 4.9
10.5 3.0 9.4 2.4 6.9
7.1 0.4 9.9 1.6 7.6
12.6 20.0 12.9 7.6 7.4
3.8 4.6 2.6 2.5 8.3
1.0 4.4 10.4 2.1 13.3
3.7 15.7 9.5 5.8 10.4
0.8 7.3 6.0 17.2 9.1
1.1 12.2 7.0 12.8 8.4
4.0 27.9 0.3 14.4 5.1
1.2 0.6 7.9 4.6 24.8
8.7 13.1 8.0 6.8 7.3
6.9 12.0 8.8 4.3 1.0
11.8 3.3 7.0 3.1 25.9
9.7 13.3 14.7 9.4 3.1
2.0 3.6 7.6 9.2 19.1
4.0 2.0 10.0 16.8 17.5
7.0 9.6 5.2 1.6 12.0
18.2 7.8 5.8 3.4 11.5
1.3 3.7 0.7 0.8 20.6
8.7 5.9 6.0 15.4 14.3
14.8 4.5 13.3 0.9 5.3
8.0 5.7 0.9 2.1 12.2
6.1 8.1 0.4 1.3 0.3
9.8 5.3 8.8 12.8 8.0
1.4 13.8 14.9 3.7 6.0
26.0 8.1 7.2 7.1 6.3
2.7 15.6 3.5 8.2 0.1
6.2 2.8 6.8 3.2 7.4
1.6 1.4 4.5 11.0 11.0
9.8 4.0 9.9 0.3 1.5
8.5 1.2 1.8 3.1 13.7
6.4 7.5 5.9 10.6 1.6
13.2 3.0 2.2 7.6 8.2
4.4 0.3 12.3 7.9 10.2
0.1 9.3 1.5 9.2 6.3
0.4 2.6 6.3 3.3 8.2
7.5 2.8 12.7 7.7 0.5
15.1 1.9 2.9 2.6 14.9
2.5 0.2 22.9 16.9 24.7
4.7 0.1 6.8 5.2 0.6
1.1 2.7 4.1 8.5 12.9
5.8 4.0 6.8 22.9 15.5
3.8 8.4 12.5 9.6 1.6
9.7 4.0 6.2 14.7 12.1
10.5 1.1 7.3 3.6 1.0
9.6 4.6 9.8 6.2 19.3
8.6 7.9 7.8 4.2 5.7
13.3 2.7 4.1 13.1 12.8
2.2 3.2 17.7 5.8 11.4
6.4 0.5 19.5 0.5 2.4
1.7 5.4 5.2 9.2 11.6
2.7 7.7 9.0 1.3 10.1
1.3 0.1 6.2 6.9 11.7
10.3 29.3 6.9 10.6 5.1
2.4 3.0 10.6 3.1 17.8
2.8 1.3 0.8 2.3 12.2
5.4 19.5 5.3 15.9 12.0
24.5 1.4 19.3 3.8 1.1
3.8 5.4 16.0 16.0 13.1
3.1 10.9 5.3 6.1 17.7
10.5 8.1 2.6 1.2 0.2
7.5 8.3 3.2 6.5 0.0
11.4 7.2 5.3 11.0 13.4
12.3 13.9 2.8 16.0 2.9
6.7 14.6 12.0 3.1 8.8
10.3 2.5 7.2 13.2 1.6
0.6 2.6 9.9 4.4 5.5
15.5 7.3 7.6 3.6 2.6
2.8 8.6 2.3 15.3 5.7
7.5 18.8 0.6 10.3 26.5
2.3 19.6 0.9 17.4 1.7
3.8 5.1 3.5 18.0 18.0
14.1 11.3 6.9 4.4 10.1
10.4 3.8 18.5 6.5 0.9
9.2 0.2 7.8 4.2 5.2
17.8 3.2 13.2 15.8 15.4
16.9 4.9 7.9 4.9 10.8
17.9 21.6 3.5 5.1 5.8
1.5 8.4 6.8 0.9 5.5
6.3 9.1 4.4 5.2 2.2
4.2 15.9 4.5 11.7 3.8
4.0 6.4 7.6 5.4 1.4
4.1 0.9 3.4 7.6 8.4
10.1 13.9 8.0 4.4 8.4
10.2 5.9 11.0 4.7 0.2
3.5 7.3 3.1 17.3 6.2
12.4 16.4 19.6 6.8 10.4
1.8 0.5 7.3 15.8 0.9
18.7 2.9 6.7 6.5 16.8
2.0 1.1 0.2 3.6 3.4
7.5 0.8 13.8 14.5 0.3
8.7 6.8 9.3 1.2 1.7
7.3 9.4 17.0 6.8 13.3
1.1 16.3 2.4 4.1 7.6
2.6 16.1 7.1 17.3 0.6
9.4 12.9 5.6 6.2 2.2
0.9 1.8 4.5 17.4 7.2
3.4 0.2 7.8 3.7 17.8
17.1 0.8 1.9 6.6 8.2
0.1 11.5 13.3 9.7 6.7
5.7 16.4 3.9 8.4 7.5
11.1 3.9 10.6 10.6 12.0
3.4 2.1 1.3 14.5 5.3
25.5 12.6 10.7 2.3 11.0
5.1 16.7 18.2 1.9 12.0
13.5 2.6 1.0 25.2 10.8
2.4 0.0 2.1 11.6 22.2
0.3 1.7 10.2 10.3 13.2
17.5 8.5 17.8 1.8 5.5
3.9 12.8 3.3 10.1 3.4
8.4 12.4 10.7 6.8 8.3
2.1 3.0 6.0 11.0 14.7
0.2 2.0 2.3 3.0 3.8
1.7 5.3 12.0 0.4 16.6
7.5 3.3 7.2 0.8 16.3
2.6 8.0 0.3 2.6 2.3
5.9 4.2 4.9 16.3 3.2
9.5 12.5 17.8 1.3 1.4
15.7 7.7 15.6 16.4 16.7
7.1 17.7 10.1 3.6 2.5
0.6 20.1 3.2 5.6 5.4
2.0 17.9 16.9 2.8 5.5
2.4 20.3 9.9 7.9 0.2
2.9 5.0 16.6 5.4 0.1
17.2 1.1 11.0 2.5 7.6
1.8 4.7 8.5 0.2 2.2
6.1 10.2 5.8 18.0 16.7
6.9 19.1 0.4 4.0 15.2
3.2 6.8 7.4 3.2 5.8
12.8 8.8 6.3 3.6 4.3
7.5 4.9 21.5 8.1 0.9
12.0 7.3 12.7 8.2 6.3
6.0 11.0 4.8 16.6 21.2
3.6 15.8 29.2 0.1 9.4
10.6 3.8 1.1 5.0 5.6
11.3 0.6 0.1 3.8 15.1
13.4 8.1 4.7 7.0 15.3
10.4 6.6 3.2 9.7 22.6
21.3 22.7 1.3 20.4 6.7
7.5 10.5 13.5 0.5 7.5
13.2 1.1 14.8 11.0 4.9
11.3 2.1 22.5 0.1 3.6
9.3 2.0 6.9 1.9 2.6
17.5 1.7 6.7 8.4 5.1
6.0 4.4 15.6 9.7 2.2
2.5 9.4 1.5 2.5 17.4
11.9 4.7 8.6 3.3 6.1
23.1 5.3 1.7 5.2 0.5
3.0 9.8 4.5 1.5 10.1
2.6 10.4 1.4 10.4 11.8
11.4 14.7 6.0 3.4 3.5
2.6 1.2 1.1 13.1 24.1
18.1 3.2 3.8 4.2 4.2
15.0 19.6 10.6 17.7 1.5
21.6 11.4 16.7 4.7 18.3
11.5 13.3 1.5 1.5 0.0
14.1 8.7 9.3 4.4 0.3
0.3 14.1 10.8 4.8 4.1
14.4 1.1 10.2 6.7 1.2
14.6 11.3 18.5 10.7 11.1
4.3 14.9 0.6 22.2 0.3
0.9 23.6 7.0 5.2 1.4
0.2 3.8 8.1 10.4 5.4
8.5 3.5 6.4 14.0 8.8
7.4 2.7 3.6 0.4 0.8
5.9 8.4 1.6 0.7 5.3
1.2 9.6 11.6 2.5 7.4
0.1 17.5 13.2 0.5 22.4
4.2 4.6 7.2 4.6 2.9
14.3 4.3 10.8 0.7 2.7
8.9 20.8 4.3 7.2 7.0
1.2 8.4 2.1 4.5 2.7
0.1 1.0 1.2 14.3 3.6
9.7 13.3 10.5 9.3 4.0
7.6 7.2 10.8 10.6 11.4
16.8 8.6 1.8 6.7 1.7
0.1 4.5 18.3 16.6 17.0
13.3 5.2 17.0 0.8 8.0
1.7 6.8 2.5 12.9 13.7
3.3 13.9 17.9 0.6 24.1
8.7 12.3 17.5 3.7 8.1
5.8 8.6 1.9 4.0 4.7
14.8 2.3 14.5 13.9 4.9
8.1 8.5 16.0 9.6 5.3
1.4 2.2 9.6 2.5 2.4
11.4 4.5 1.5 6.6 15.3
5.5 8.9 5.0 10.7 0.8
0.5 11.6 4.7 2.7 2.2
13.3 0.7 11.2 3.2 5.7
1.3 9.1 0.2 1.7 0.6
6.7 9.3 2.2 3.0 4.7
13.4 27.0 3.9 5.0 8.0
5.7 3.8 8.5 6.6 5.1
0.4 0.5 4.8 16.7 19.4
23.7 8.8 18.1 2.4 26.2
0.3 6.8 3.8 0.2 8.1
9.0 9.2 3.9 18.2 16.6
12.2 14.0 2.2 0.6 3.5
4.8 6.7 5.3 7.4 5.0
1.5 11.0 3.4 4.2 5.2
7.6 4.1 4.3 1.0 6.6
15.5 0.0 9.6 0.8 10.1
3.5 2.3 16.8 5.7 4.6
8.8 1.2 9.2 2.8 22.8
24.1 15.9 8.6 3.6 3.0
10.3 0.7 11.9 8.8 1.1
11.5 1.9 13.6 6.6 38.6
5.4 13.0 1.5 3.4 5.6
4.1 11.9 2.6 9.5 4.8
1.5 3.4 0.3 5.0 4.5
18.6 1.0 6.3 17.8 6.0
0.2 13.7 0.4 16.4 17.5
5.7 4.7 10.2 20.3 13.5
5.2 1.3 15.2 14.2 0.4
14.5 9.2 1.7 0.4 17.0
0.3 4.0 0.8 10.5 7.7
7.1 2.4 2.7 1.4 16.2
4.5 1.7 6.8 3.3 3.8
8.1 2.1 11.0 13.5 4.6
8.5 0.9 9.7 4.6 26.7
2.4 1.6 1.3 23.7 15.4
0.2 2.2 5.8 6.1 5.0
9.2 0.1 16.5 5.0 10.6
0.3 5.3 0.3 11.6 11.0
2.8 10.3 18.7 7.3 8.6
9.0 13.1 13.8 13.9 11.8
1.5 12.0 21.0 4.0 0.9
6.3 6.3 3.1 0.2 6.7
16.7 19.9 3.5 10.3 1.1
3.6 9.5 6.1 14.6 12.2
0.7 5.8 8.2 1.0 2.5
14.5 7.3 0.5 25.7 7.8
8.0 11.3 7.8 5.3 7.1
0.9 8.6 4.8 15.0 1.4
8.8 7.1 10.1 6.0 4.3
4.3 1.8 12.0 5.8 2.5
0.7 20.0 17.8 17.3 3.4
2.2 7.1 4.1 5.7 12.5
9.8 16.3 2.8 19.9 1.2
6.9 7.5 3.5 3.3 8.1
7.8 8.0 6.0 4.0 6.4
7.1 6.0 12.6 10.1 12.3
0.9 3.2 15.4 12.0 8.0
4.2 2.9 4.4 7.0 2.4
12.7 0.3 4.8 2.3 2.2
12.6 6.6 7.6 5.2 4.3
11.8 8.4 2.4 9.8 5.1
7.6 4.5 7.4 25.2 5.4
5.9 4.0 1.5 10.9 25.1
7.7 7.0 14.3 5.5 13.8
12.3 6.0 2.6 11.1 2.6
13.5 1.0 1.8 6.1 20.1
3.9 2.6 1.6 2.9 9.9
12.4 4.5 20.7 12.9 0.8
10.4 9.0 0.6 0.3 16.0
5.0 24.4 9.3 3.9 24.8
22.2 4.1 11.3 0.4 10.4
6.1 8.5 8.4 4.3 18.8
9.5 3.0 0.8 10.4 4.7
3.1 1.4 5.5 13.0 23.0
4.5 7.6 4.2 6.0 15.7
2.1 11.9 2.9 10.3 4.7
7.6 11.7 6.0 0.4 6.1
13.6 18.6 1.7 0.2 6.9
10.2 8.9 14.1 14.5 16.9
4.0 1.6 2.8 4.8 3.3
4.9 0.9 10.2 11.1 0.6
7.2 3.8 4.5 0.3 19.3
20.8 9.3 10.4 0.5 11.9
6.3 9.4 5.7 11.6 15.5
5.0 11.2 8.0 20.5 19.0
0.7 6.3 13.2 5.2 5.2
7.0 0.6 18.9 9.3 15.1
3.2 25.0 9.1 2.0 10.9
10.2 3.2 6.4 17.9 5.2
5.7 0.8 5.9 12.9 17.0
7.1 7.6 5.9 11.0 4.7
8.1 14.0 10.7 5.1 7.3
8.8 7.7 21.4 3.9 3.3
15.2 8.9 4.0 1.5 16.3
2.2 8.0 6.6 5.1 0.5
2.7 6.5 14.5 2.3 10.8
10.0 3.1 16.8 8.7 14.7
15.8 12.0 17.2 5.7 0.2
0.9 3.3 0.6 17.2 1.0
15.5 4.0 13.4 9.1 0.6
7.6 2.8 3.5 22.7 15.6
17.1 20.9 16.9 11.2 14.2
7.0 12.2 4.0 4.1 3.7
10.5 3.2 9.0 14.6 7.9
8.2 8.8 0.5 12.9 6.6
13.8 6.7 8.0 17.6 8.2
4.0 14.9 18.3 2.8 17.7
7.2 4.0 6.9 0.6 7.3
0.6 2.7 13.4 0.2 8.8
8.8 9.6 0.5 14.7 13.4
24.5 15.0 4.2 18.3 11.6
5.4 6.7 8.0 1.7 6.3
3.1 14.7 17.5 7.2 5.1
2.2 11.8 1.8 12.1 6.9
4.0 2.3 1.4 0.4 13.0
7.5 2.8 20.0 15.8 3.8
6.4 2.3 14.3 5.9 0.1
9.6 4.2 18.4 0.5 16.2
4.6 18.9 16.7 12.5 6.3
3.9 9.0 20.0 3.8 4.8
5.4 1.9 7.7 21.1 3.3
7.8 6.3 15.7 9.0 10.6
2.5 11.6 0.5 4.0 3.9
11.8 0.4 7.0 4.7 2.7
18.8 1.3 17.1 0.5 5.7
2.8 7.7 9.9 15.6 13.7
14.6 1.8 16.0 16.6 1.9
10.2 9.3 26.1 8.3 19.0
2.2 3.0 9.2 3.9 7.1
6.6 8.0 7.0 5.5 13.9
7.4 17.9 2.2 6.0 1.0
19.3 1.8 7.2 12.6 0.7
1.8 7.4 4.9 7.0 18.8
9.0 7.6 0.1 8.4 3.6
4.1 6.9 4.1 3.8 4.8
12.8 0.4 18.0 6.8 5.8
14.5 8.5 2.5 1.3 2.8
7.2 7.8 17.4 2.7 8.6
6.4 15.7 10.1 0.2 9.2
1.5 5.9 18.1 6.4 24.4
7.6 6.1 1.6 4.9 5.8
1.3 7.6 8.9 2.9 4.3
12.5 6.7 7.2 2.7 0.8
0.0 8.4 4.6 3.0 6.5
5.1 6.8 13.6 5.5 0.1
0.2 10.6 7.5 18.4 6.5
1.7 6.5 13.3 2.1 8.4
3.4 1.2 5.3 9.0 0.9
3.1 3.7 3.1 12.2 1.3
11.2 13.6 6.9 16.1 1.3
6.5 9.2 9.9 11.3 20.8
6.2 4.1 6.2 0.6 3.1
10.3 5.4 10.7 10.7 4.1
8.4 1.8 3.3 20.2 4.8
12.1 11.2 2.2 10.4 3.3
16.2 30.9 7.2 1.8 4.7
12.7 16.0 1.6 7.0 13.4
9.7 10.7 12.2 4.8 1.4
3.4 5.1 2.7 9.5 8.3
20.3 6.8 18.1 4.3 5.4
1.4 1.5 1.5 4.0 7.4
7.9 10.5 4.2 9.8 2.7
2.5 5.3 2.3 9.6 8.3
19.8 7.9 5.2 3.7 6.7
1.4 5.3 15.1 12.7 9.3
9.5 2.7 2.3 10.5 8.3
4.2 8.9 6.9 10.6 7.2
3.8 11.3 1.4 3.7 4.2
0.9 3.0 6.0 8.1 14.9
10.2 2.4 12.9 9.5 2.7
14.0 10.8 7.9 5.1 14.6
24.9 10.4 11.5 20.1 6.3
14.7 7.3 8.8 6.6 0.5
4.7 2.7 5.3 5.9 5.7
5.7 5.3 14.4 1.4 12.8
2.9 2.8 7.5 7.2 16.4
14.7 1.0 23.8 13.6 6.2
3.6 11.8 2.6 5.9 1.0
6.7 5.5 0.8 8.9 4.2
2.6 4.1 11.3 6.4 2.5
2.0 8.2 2.2 0.1 1.6
2.0 2.3 5.3 6.9 2.2
2.4 4.4 11.5 18.0 6.8
1.1 3.6 5.8 0.3 0.9
2.8 4.8 3.0 1.5 5.9
9.3 3.9 0.5 0.2 4.3
12.7 1.6 9.4 1.2 2.9
5.9 17.2 6.1 9.9 4.0
12.7 5.4 2.4 18.0 1.4
8.4 1.5 0.5 11.9 7.1
3.4 3.4 9.0 8.2 8.5
14.1 9.9 6.6 16.8 8.3
4.0 0.9 2.4 6.1 10.8
12.0 0.6 11.4 2.9 12.2
8.8 2.3 3.8 2.3 10.5
4.5 13.6 8.2 7.2 5.9
9.4 12.3 7.9 6.2 5.7
4.5 3.0 5.4 22.0 12.1
16.9 0.2 11.0 26.9 12.2
4.4 2.1 10.5 21.6 14.1
12.6 8.2 7.4 10.8 25.9
11.1 3.3 5.5 0.5 18.4
11.8 6.5 15.7 0.1 14.8
8.2 4.6 1.5 3.6 10.3
4.4 4.2 5.5 5.9 11.5
10.9 2.9 12.8 19.9 1.9
1.5 1.2 5.1 19.8 4.2
6.0 11.9 29.5 9.0 3.5
6.8 9.8 3.9 0.2 16.8
3.8 5.4 3.5 23.1 11.6
0.8 6.9 7.8 11.4 1.2
13.4 16.6 5.4 4.1 2.5
2.8 18.4 3.5 2.4 14.4
1.4 9.8 8.5 6.1 11.6
4.0 11.3 10.5 2.1 5.5
6.1 1.0 9.9 3.2 4.8
5.8 5.0 0.5 2.8 7.3
8.7 4.8 4.2 1.8 8.8
0.2 11.5 2.6 9.4 17.0
12.9 16.9 1.3 2.4 11.6
7.9 0.7 15.9 6.0 21.1
3.3 1.3 5.7 1.4 5.8
14.0 16.1 1.1 14.3 8.7
10.1 16.2 0.9 1.4 0.7
1.3 6.0 7.5 13.9 19.0
8.3 16.6 8.1 19.3 10.1
5.2 9.4 26.7 3.2 8.5
2.7 4.8 15.2 3.0 17.9
1.9 4.4 4.1 2.5 0.6
14.3 6.5 0.8 20.8 11.8
2.1 8.0 1.0 1.3 9.5
1.8 7.4 9.0 9.5 3.5
15.5 3.3 2.1 13.1 17.6
1.0 16.3 8.9 16.2 7.3
4.9 3.8 7.0 3.4 4.3
1.4 3.7 4.1 0.4 5.4
3.3 2.7 5.1 20.1 6.5
11.9 23.1 10.6 6.5 5.4
6.3 1.5 7.1 2.4 2.2
6.9 2.8 3.6 7.7 6.0
7.8 3.8 8.8 9.4 4.7
2.1 3.0 8.4 6.7 9.5
22.9 7.0 2.9 22.1 1.7
18.6 3.3 7.5 10.4 12.6
23.8 9.7 10.4 0.4 2.1
16.7 16.1 5.5 11.5 10.0
2.6 0.3 7.4 4.3 6.3
7.6 1.7 14.2 6.1 10.8
1.2 1.7 3.9 4.8 9.3
1.1 1.5 14.2 9.0 3.2
26.2 5.2 5.9 22.4 5.2
7.3 8.1 9.3 20.7 4.1
5.0 2.8 3.4 1.2 6.7
3.5 7.3 7.8 0.6 2.1
3.9 13.1 5.7 0.9 1.1
10.0 2.1 2.4 2.0 1.1
0.6 9.6 2.8 2.1 12.9
4.2 8.9 13.4 20.8 5.1
4.1 9.0 7.5 16.5 12.5
5.4 19.2 12.4 1.3 7.0
3.1 17.1 3.8 0.8 10.0
1.8 3.0 1.2 2.3 4.1
6.7 4.7 0.8 11.7 14.2
13.6 11.1 6.5 12.3 17.9
8.1 9.6 6.9 1.2 5.1
7.3 7.7 4.8 7.3 8.5
3.0 7.8 7.9 1.5 14.0
7.6 14.0 25.5 8.2 0.3
9.8 15.0 4.5 9.6 0.3
4.3 3.2 8.3 6.4 5.0
6.5 9.3 0.5 11.4 0.8
3.8 20.9 22.2 19.5 7.1
7.0 1.7 5.1 2.0 3.1
2.1 8.9 9.1 13.3 1.2
11.9 2.6 14.5 8.6 3.2
14.5 10.0 3.8 2.5 18.5
4.3 1.7 23.3 12.5 5.9
4.3 3.4 15.1 0.7 12.9
2.1 9.7 3.7 19.0 13.2
6.9 6.2 1.5 9.6 3.3
4.0 2.7 9.0 1.9 6.3
7.7 1.6 11.7 0.4 0.3
14.9 26.2 0.1 5.7 7.6
11.9 5.4 3.9 14.9 0.3
13.2 20.4 6.8 5.7 1.4
1.7 4.1 6.2 3.6 24.8
7.4 9.7 0.7 3.5 7.4
1.3 20.3 5.7 12.0 13.7
8.6 12.8 2.2 9.4 0.9
2.5 1.3 18.3 0.4 3.2
12.1 3.1 7.8 16.5 6.8
17.3 8.7 5.3 21.5 1.6
14.0 16.2 9.1 9.2 15.1
7.1 11.1 14.6 11.1 6.5
2.1 5.3 0.6 3.3 2.7
7.8 6.3 1.0 8.1 7.2
0.6 6.0 6.5 10.9 10.3
12.1 13.4 11.0 25.2 17.6
4.0 8.8 12.7 5.4 10.6
4.0 14.8 1.3 0.4 6.0
9.1 19.7 0.0 15.4 6.0
2.0 10.2 3.7 0.6 5.5
21.5 14.9 10.9 6.6 8.5
22.2 21.5 17.0 11.1 5.0
3.2 12.7 5.5 4.0 0.8
3.5 11.6 5.5 9.9 9.4
4.5 4.6 12.7 2.2 8.8
0.6 4.1 24.6 6.7 15.7
13.8 3.0 5.3 2.5 11.2
9.9 3.5 16.1 5.5 19.8
11.7 5.8 24.1 7.4 1.5
9.9 7.3 21.3 20.8 3.8
0.7 14.3 20.7 21.0 1.2
1.2 7.2 4.4 0.4 13.2
6.7 14.6 4.3 1.6 8.6
2.7 11.9 6.2 8.1 7.6
6.4 14.9 4.5 9.3 18.5
12.3 10.4 17.3 4.2 8.1
2.7 21.3 2.1 3.5 15.1
15.7 11.8 3.7 6.9 16.4
6.7 18.7 8.0 1.6 7.0
10.7 8.8 23.9 0.9 0.3
11.0 5.5 3.3 3.3 6.5
5.5 11.2 20.8 3.8 13.4
0.9 14.1 6.6 9.4 0.1
0.2 7.2 2.2 4.4 4.9
1.5 2.7 2.4 7.4 18.2
3.0 6.1 12.2 3.3 12.1
6.1 5.8 14.3 4.5 8.3
1.3 3.0 10.1 7.3 5.6
1.8 17.6 8.4 5.5 16.1
0.1 14.9 16.6 13.3 2.5
4.2 9.8 31.4 10.0 2.2
7.8 9.2 11.3 13.2 4.8
2.9 3.7 6.5 11.3 0.1
25.2 12.8 19.5 6.7 2.5
0.6 7.0 0.8 5.0 0.3
13.9 7.6 4.5 6.9 5.7
7.6 9.8 11.3 24.9 8.4
9.8 1.6 0.0 6.1 11.7
17.5 3.4 6.0 6.6 1.3
8.0 9.8 1.5 12.6 10.5
1.9 23.0 5.2 15.3 11.3
9.7 4.4 6.9 12.3 3.8
8.1 6.3 4.0 12.5 5.6
5.0 0.7 2.8 2.3 2.0
25.6 3.4 15.6 3.8 3.3
15.2 2.0 7.7 3.9 7.5
12.7 16.4 11.9 0.9 5.8
1.4 12.1 13.7 7.0 10.6
7.6 7.3 16.3 2.6 3.0
0.2 5.8 5.6 10.1 6.5
3.0 15.9 5.8 6.9 4.5
4.7 7.3 5.7 5.0 2.3
23.1 10.3 8.3 12.9 8.0
16.9 7.3 2.9 4.5 14.2
19.9 13.5 6.8 0.2 0.9
4.9 14.6 7.4 7.9 3.0
14.0 0.9 3.6 16.8 1.1
2.1 8.7 7.3 5.7 6.2
2.0 8.7 20.7 0.1 14.7
7.8 5.3 6.2 11.9 1.0
8.0 1.2 1.6 6.4 8.6
4.8 10.3 6.3 7.2 14.7
0.7 14.3 14.6 8.5 9.2
19.4 7.3 11.1 8.6 12.7
15.6 10.9 3.0 13.9 0.3
4.0 9.5 8.4 4.7 6.6
0.6 4.6 0.0 5.1 11.6
12.9 5.2 1.9 5.7 3.0
6.5 5.6 10.9 14.5 3.2
8.6 10.9 14.4 4.3 1.4
3.3 17.7 11.5 6.9 4.7
9.9 15.3 0.5 0.9 0.7
9.6 0.1 2.8 13.3 18.2
12.3 2.6 1.8 10.6 4.0"""
    centers = lloyd_algorithm_k_means(6, format_matrix(data))
    for center in centers:
        for p in center:
            print(f"{p:.3f}", end=" ")
        print()