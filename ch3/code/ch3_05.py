"""
@BY: Reem Alghamdi
@DATE: 17-09-2020
"""


def de_bruijn_graph_fromkmer(kmers):
    """
    :param kmers: array of kmers
    :return adjacency list of prefix/suffix
    """
    adj_list = {}
    for edge in kmers:
        from_prefix = edge[:-1]
        to_suffix = edge[1:]
        if adj_list.get(from_prefix):
            adj_list[from_prefix].append(to_suffix)
        else:
            adj_list[from_prefix] = [to_suffix]
    return adj_list


if __name__ == "__main__":
    with open("../data/de_bruijn_graph_fromkmer") as file:
        kmers = file.read().splitlines()
        adj_list = de_bruijn_graph_fromkmer(kmers)
        print(adj_list)
        for node, lists in adj_list.items():
            print(node, " -> ", ', '.join(lists))
    # with open("../data/dataset_369270_8.txt") as file:
    #     with open("../data/output/ch3_05.txt", "a") as output:
    #         kmers = file.read().splitlines()
    #         adj_list = de_bruijn_graph_fromkmer(kmers)
    #         for node, lists in adj_list.items():
    #             output.write(node + " -> " + ', '.join(lists) + "\n")

