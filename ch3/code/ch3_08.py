"""
@BY: Reem Alghamdi
@DATE: 18-09-2020
"""
import operator

from ch3.code.ch3_03 import genome_path
from ch3.code.ch3_05 import de_bruijn_graph_fromkmer


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


def euler_cycle(graph):
    """
    this function walks depth first in the graph to find the cycle
    :param graph: the graph
    :return: euler circle -if it exists-
    """
    cycle = []
    stack = []
    new_start = list(graph.keys())[0]
    stack.append(new_start)
    while len(stack) != 0:  # while the graph is not empty
        start = stack[-1]  # the start node is the top of the stack
        if graph.get(start):  # if it exists in the graph
            end = graph[start][0]  # the end node is found with adjacency list
            stack.append(end)  # add it to the top of the stack
            graph[start].remove(end)  # remove it from the graph
        else:  # if the start node is not in the graph
            cycle.append(stack.pop())  # add the start node to the cycle AND remove it from the stack

    num_edges = sum((len(v) for v in graph.values()))
    if num_edges == 0:  # check to see if all edges were visited
        return list(reversed(cycle))  # the cycle is in the reverse order
    return []


def get_balance(adj_list):
    """
    this function calculates the balance of each node.
    if the node is connected to a node that is connected to another node, then the balance is gonna be zero
    but if the node is connected to a node that is not connected to anyone, then the balance is -1
    """
    balance = {}
    for start in adj_list.keys():
        if not balance.get(start):
            balance[start] = 0
        for end in adj_list[start]:
            balance[start] -= 1
            if balance.get(end):
                balance[end] += 1
            else:
                balance[end] = 1
    return balance


def euler_path(graph):
    """
    this function walks depth first in the graph to find the cycle
    this runs the same way as cycle, but we have to start with node with highest degrees
    :param graph: the graph
    :return: euler circle -if it exists-
    """

    path = []
    stack = []
    balance = get_balance(graph)
    stack.append(min(balance.items(), key=operator.itemgetter(1))[0])
    while len(stack) != 0:
        start = stack[-1]
        if graph.get(start):
            end = graph[start][0]
            stack.append(end)
            graph[start].remove(end)
        else:
            path.append(stack.pop())

    num_edges = sum((len(v) for v in graph.values()))
    if num_edges == 0:
        return list(reversed(path))
    return []


def string_reconstruction(patterns):
    """
    take a list of k-patterns
    then find de bruijn, then euler path and finally path to genome
    """
    adj_list = de_bruijn_graph_fromkmer(patterns)
    path = euler_path(adj_list)
    text = genome_path(path)
    return text


def k_universal_string(k):
    values = 2 ** k
    patterns = [f'{x:0{k}b}' for x in range(values)]
    adj_list = de_bruijn_graph_fromkmer(patterns)
    # cycle = euler_cycle(adj_list)[:-(k-1)]  # for exercise question: make it circular
    cycle = euler_cycle(adj_list)  # for extra question: linear
    text = genome_path(cycle)
    return text


if __name__ == "__main__":
    # with open("../data/ch3_08_euler_cycle") as file:
    #     print("->".join(euler_cycle(format_adjacency_list(file.read()))))
    # with open("../data/ch3_08_euler_path") as file:
    #     print("->".join(euler_path(format_adjacency_list(file.read()))))
    # with open("../data/dataset_369273_7.txt") as file:
    #     print(string_reconstruction(file.read().splitlines()))
    print(k_universal_string(3))
