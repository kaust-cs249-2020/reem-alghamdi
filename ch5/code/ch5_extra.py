"""
REDO USING 5.8_2
format graph using the score format
"""
import numpy as np

# def manhattan_tourist_with_longest_path_in_dag(graph):
# def global_alignment_with_longest_path_in_dag(graph):
# def local_alignment_with_longest_path_in_dag(graph):


def two_strings_to_weighted_graph(v, w, scoring_matrix=None, sigma=None):
    # 0->10:6
    len_v = len(v)
    len_w = len(w)
    total_nodes = (len_v + 1) * (len_w + 1)
    total_edges = len_v * (len_w+1) + len_w * (len_v + 1) + len_w * len_v
    adj_string = ""
    # for i, a in enumerate(v):
    #     adj_string += "0-" + str(i) + a + "->" + "0-" + str(i + 1) + (v[i+1] if i+1 < len_v else "$") + ":" + "-1" + "\n"
    #
    # for j, b in enumerate(w):
    #     adj_string += "1-" + str(j) + b + "->" + "1-" + str(j + 1) + (w[j+1] if j+1 < len_w else "$") + ":" + "-1" + "\n"
    # for i, a in enumerate(v + "-"):  # vertical
    #     for j, b in enumerate(w):
    #         adj_string += (str(i)+a) + (str(j)+b) + "\n"
    #
    # for j, b in enumerate(w + "-"):  # horizontal
    #     for i, a in enumerate(v):
    #         adj_string += (str(j)+b) + (str(i)+a) + "\n"


    return adj_string


if __name__ == "__main__":
    print(two_strings_to_weighted_graph("GACT", "ATG"))