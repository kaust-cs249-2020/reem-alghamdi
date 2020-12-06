"""
@BY: Reem Alghamdi
@DATE: 06-12-2020
"""
from ch9.code.ch9_05 import colored_shared_depth_first
from ch9.code.ch9_15 import modified_suffix_tree_construction
from ch9.code.ch9_16 import tree_coloring

"""
3. Give an example of a string P = P 1 ...P n over alphabet Σ = {A, B} whose
uncompressed suffix tree has size Θ(n^2 ).


suffix tree guarantee O(|text|) space complexity. so only strings with length = 1 will have size O(n^2).
So either "A" or "B"
"""

"""
4. A palindrome is a string that is identical when reversed. Given a string
S, design an algorithm that can find the longest palindromic substring of
S.

I would use the same approach as longest shared substring, I would use text1 = string and text2 = inverse of string
"""


def longest_palindromic_substring(text):
    combo = text + "#" + text[::-1] + "$"
    colored_tree = modified_suffix_tree_construction(combo, len(text) + 1)
    tree_coloring(colored_tree)
    return colored_shared_depth_first(colored_tree, combo, colored_tree.root, 0, 0, [], "", [])[0]


if __name__ == "__main__":
    print(longest_palindromic_substring("reem"))  # should be ee
    print(longest_palindromic_substring("sjdfhfaeaefeaeaoiuijl")) # should be aeaefeaea
