"""
@BY: Reem Alghamdi
@DATE: 17-09-2020
"""


def euler_cycle(graph):
    """
    this function walks depth first in the graph to find the cycle
    :param graph: the graph
    :return: euler circle -if it exists-
    """
    # graph = {
    #     '0': ['3'],
    #     '1': ['0'],
    #     '2': ['1', '6'],
    #     '3': ['2'],
    #     '4': ['2'],
    #     '5': ['4'],
    #     '6': ['5', '8'],
    #     '7': ['9'],
    #     '8': ['7'],
    #     '9': ['6']}
    cycle = []
    stack = []
    new_start = sorted(graph.keys())[0]
    stack.append(new_start)
    while len(stack) != 0:  # while the graph is not empty
        start = stack[-1]  # the start node is the top of the stack
        if graph.get(start):  # if it exists in the graph
            end = graph[start][0]  # the end node is found with adjacency list
            stack.append(end)  # add it to the top of the stack
            graph[start].remove(end)  # remove it from the graph
        else:  # if the start node is not in the graph
            cycle.append(stack.pop())  # add the start node to the cycle AND remove it from the stack
    return reversed(cycle)  # the cycle is in the reverse order


def format_adjacency_list(text):
    adj_list = {}
    text = text.split("\n")
    for line in text:
        from_ = line.split("->")[0].strip()
        to_ = line.split("->")[1].strip().split(",")
        if adj_list.get(from_):
            adj_list[from_].extend(to_)
        else:
            adj_list[from_] = to_

    return adj_list


if __name__ == "__main__":
    with open("../data/dataset_369273_2.txt") as file:
        print("->".join(euler_cycle(format_adjacency_list(file.read()))))
