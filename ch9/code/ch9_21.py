"""
@BY: Reem Alghamdi
@DATE: 13-11-2020
"""
from ch9.code.ch9_15 import modified_suffix_tree_construction


def preorder(edges, node, visited):
    if node not in visited:
        visited.append(node)
        if node in edges:
            for n, string in edges[node]:
                preorder(edges, n, visited)
    return visited


def suffix_tree_to_suffix_array(tree):
    edges = tree.lexicographical_sort()
    suffix_array = [x.label for x in preorder(edges, list(edges)[0], []) if x.label != None]
    print(suffix_array)


if __name__ == "__main__":
    tree = modified_suffix_tree_construction("panamabananas$")
    suffix_tree_to_suffix_array(tree)