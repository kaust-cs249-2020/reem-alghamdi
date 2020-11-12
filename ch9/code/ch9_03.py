"""
@BY: Reem Alghamdi
@DATE: 08-11-2020
"""
from ch9.code.ch9_extra import Trie


def trie_construction(patterns):
    trie = Trie()
    for pattern in patterns:
        current_node = trie.root
        for i in range(len(pattern)):
            current_symbol = pattern[i]
            b = trie.are_linked_by_value(current_node, current_symbol)
            if b:
                current_node = b
            else:
                b = trie.nodes[-1] + 1
                trie.link(current_node, b, current_symbol)
                current_node = b

    return trie

"""
PrefixTrieMatching(Text, Trie)
    symbol ← first letter of Text
    v ← root of Trie
    while forever
        if v is a leaf in Trie
            output the pattern spelled by the path from the root to v
        else if there is an edge (v, w) in Trie labeled by symbol
            symbol ← next letter of Text
            v ← w
        else
            return "no matches found"
"""


def prefix_trie_matching(text, trie):
    i = 0
    symbol = text[i]
    v = trie.root
    while i < len(text):
        if v not in trie.edges:
            return trie.path_from_root(v)
        else:
            w = trie.are_linked_by_value(v, symbol)
            if w:
                i += 1
                if i < len(text):
                    symbol = text[i]
                    v = w
                # else:
                #     return w
            else:
                return
    return v


def trie_matching(text, trie):
    matches = []
    i = 0
    temp = text
    while i < len(text):
        o = prefix_trie_matching(temp, trie)
        if o:
            print(temp, o, i)
            matches.append(i)
        i += 1
        temp = text[i:]
    return matches


def string_to_trie(string):
    t = Trie()
    for line in string.split("\n"):
        before, _ = line.split("->")
        after, symbol = _.split(":")
        t.link(before, after, symbol)
    return t


def solve_trie_matching(strings):
    trie = trie_construction(strings[1:])
    # trie.print()
    return trie_matching(strings[0], trie)


if __name__ == "__main__":
#     string_to_trie("""0->1:A
# 1->2:T
# 2->3:A
# 3->4:G
# 4->5:A
# 2->6:C
# 0->7:G
# 7->8:A
# 8->9:T""").print()


#     strings = """ATAGA
# ATC
# GAT""".split("\n")
#     t = trie_construction(strings)
    # print(t.path_from_root(""))

#     strings = """AATCGGGTTCAATCGGGGT
# ATCG
# GGGT""".split("\n")
#     strings = """TCGCGCGCCTGAAGCTGCAATACGCTCATAACGCCGTTACTTGGTAGATGTGCGTCTGATTCTTGTGGAGCGAAGGAATACCCGAGGGTCTCACATCCTGCATGGCTAAGGGCTGCTTACTACCTCTATGCCTCGACACCTCGACATTAATGTACGCAGCGTCCGGCATGCACGGGACGTACGGTCTGCCCATGCAGTGTCTCTTAGCTGGCCAAAGCCATGGCGACTGTGAGTGCACCTCCTTACTCCTTACTCTCCACAATTTTGCTAAAACTCTTAGACTGACTGGTGGCCTCGCTACAAGCAAGATGTGATTCATAGCGACCTGGCAGTGAGCACTCTTAGTTCCAATGCAGCAAGCACCCTACCTATTGCTGGGGAGTACTGCTGACTGCTGACTCAAGGCTTACAAGGGCCGTGATTCCTACTTCTAGCCCCGGGTCTGGTCAAAACGCCGATATTGACTTGAATCCGTAAGGATCTACGGTCCTGCCATGGACGGTGAGACTACAAGCTTTCCTCGCTGCGGGATACTCTTCCGAGTACCTGAGCATCGATCACTCGCGGCATATTTGGCCCGGAAGCACGGCGTAAACTCAGCTTACCCAGATCGACCATTCGTAGATCTCCGCCAAGACAAGTTTGTCTTGCCAAGGGAGTATGATGTGGACTGCTGACTGCTGACGCACACCGTCAGCTTCTCCTCCCCCGTAGGCATCTGCTGAATTGCTTCTATGTCATATTGTCGGGAAGTCGCACTAAACTGTAGCCCGATACGCGCCACTTATTAGGGGGAGATCGTCGCCGTAGGAGCGAAGTGAAGCCACGGTTCCCTACCGCCGTAGGTGCCCGCGCGGTTTTTATGCATCGAGATCCTGGGCTTCTATCCCGCAGATATTAGTCGGTCGTTCGACGAATAATCCGGCTAGGTAGAACCAGAGTCTAGTCTTATGGCGGCTTCGCGCTGCGCGCAAGTCTTGAAGGCCTCCAGTGTCGCCGGGTCATGAGTGGTCAGCGTAAACCCCGTAGACGTTCACCATCCCAGAGTTAGATCTAGCTACTACTCCTTGTTATTAGTGCCGCGGTGTGCATTTATTTATCCCTGTGACCCGTCTAGATTTCTAGAAGGTGAGACTAGAGGACGGAATGGCGCCCTGCTCAAGTGTGGGTACGTTTGATAGCAACGATTCGCTTTAGACAGCTAATCATCTTTTGTCGTGGAGCCAAGCTGTTCCACCGTTAACAACACTGACGACACATTAGCCGACTAGGTACGAGCACTGGTTAGAGCATTAAAATAAGCATATCCGGCACGTATCTCGTAGTCGCGAGACCGCAAAACAGCGTCTCAATCAATGCGGAGCCGTTCGCGATCAATGGCGCTCAGAATTACCCACCTTTAGTCTCTACCTGGGCCCCTCCTGCGAGCACCATGTGCCCCTCGATTGCTAGAGTTTGAAATATGATCGCGACAGGCCCGTGATGAAGCGAGTCTTCGTATACGGAGGAGGGCACGGTCTCGCGCACTCGCCTCAATCCGGCCTGAGGAATGGAATTACCTCGATCCGTAAACGCCTAGGGAGGAGCAGTACATTCCGCCTCGTTACGGATGTTCCAGAATTCTACCAGTGATGATAAGACTTCTCAAAGAGTCCGTGATATCGGCACCGCAACCGACCGACGACGGGTTTTTTGAATAGAAAAACCCCCGACCAGCGGAATACCGCATACGTTTTTGGAGGCTGCTAAGAGGGGATGCGCCACGCGACTCGATTATATCGAACTCTTCCAAAGAGTACCGTCACGACTCCTACTTCCTGTAGGGGTCAGACCGTAAATGCCGGCCCATTGTTGGGAATCGGGAGGAGCCTCCTTTCGGTCTCTAGGGATCGTCACCAGCACCGGTCGCAAGAGGGAGTTTGTTAAAGCTATGATACTGCTGACTGTGCTAAATAGCCATCCAAAGACTGACACATTAGCCTTGGAGGGCTGCGCTGCGCGCGCAACTCTTTGATACTATTTCTGACAATTACCCTCATAGAACACCCTTTCCTTAAGGGCTTGCGGTCGGGGGGGAAGGCTTTAGCGTTGTTTCTTAAGATGCCGTCACGACCGAAAAAACTAGTTGATGATACTGCTGTGATGGTCCAAATACAGAAGCATGACGTTAAAGTCAGTCCCTAGGGAATAATAGTTTTCTAATGCTGGCGTGCCGTCTTATTTCCAGGCGAAGATGGCTCTGTTCGGGCACAGTATTACACAATTCTTAGGTATGTAGAAACCTGTTTAACTGGAAGTCCTGGAAAAACGTGAAGGTACAATTAACGTGAAGGCACGTTAATCCAGGCGGATCATTGGATGTCTCCCTACGAGTCTATTCTTAACGGATAGCTATGCGCTAATAATTTCCTGCATGTTTCCATTCCGACCTTGTTGCATGCGCATCATTTGGTGGTAGATTTGGAGCTGCGCGCTTCCTGTCAACAGCCGAAGCCGGTTCGGGAAACCAATCTATACTCGGATCACTCTGTCGTCACTGTGGGTGTTCTAGCCCACGGGAGCTTGGAGTATCTTTTCGGAGGAAGCGGAAAGGCGTGGAGTAGTAAGTAGTAAGTGGCGTACACACTGTCAGTAGTGTGTGATGCATCCAGACGCCGATGCCCGTCCATGATATCTCTCTAGGTCGTTGGTACTAGCCAGCGGTGGGACAGCGTCGGGCTTAGAGACGCGTAGCGTCAGCGATCTTATAAAGGATTGGGGACGTCACCTTCAAGCTAGATGTAATTTAGAGTCGTCCCTAAAAATGCCCCTAACTCGTACCATGCGCCGGTCTATCGTCGTAACCTTTCTGTGAGGCCCGGTGTCGCGCATATTAAGAAGGCCGCCGGCCTAAGAATGGACGGTTTCTAAGTTGGTAGTAAGTGAGCGACAAGAACGTCTGGTGTGAACATCCCGGGGAACCTAAACCAATTTTAAACTATCCAATCTGCAGCTGGGATACTTACCCGCCCGCATGGCATGGATTCCAACTCCGCAGGCTAGATGAAGCCGACTGACGAAGAGTGTGCAATCAGCATGAAGGTTATCAAGTCATCAGTTGCTGAAGACCAGGTTTTGACGCGCTGACTGCTGACAGGATTTGAATTGTTACGTATAAGAACGCTAAAATCACGCGCGCGGCACCCCAGACGGGTGAAATGTTGACTCGAACCAGGAGGACCCTTGCGTGTGCAGCAACTACGCGGTCAACGCAGGGTTTGGAATCACGCTGTGTAATCTCGTACTACAGATGGAAGCTCGCCCTCGGGGGTGTCGCAAATTATAGGATATCCTCGACGATATAATTCTCTCTCGATGGAGCCCCAATTAGCCGGTACTGCAGTGGTCAACGAAGCTCCTTGTGGCCGTCCTTATTTTAAACTCTATATATGTATCGGCGTCTACCAATCAAATCGCGGGGGCCTATCGAAGCTGGCTCAGTATACCAGGTTTGTTTTACATCGTCGGGAGGCCGACGCCTGCACTACTCACCGTGTTGTGTTGAACATGTGGTTGGGCGTTTCTCCAGGGGACCCCGAGAAGCAAACAACGTTTACTTCGCTTATTTGTCTAACGGCTAGGTTCGGGCTGCGCGCTGCGCGCGTAAAATGGTAGGAAAAGAACGGCGGCGTTGGTGAGTTGGATTTCTTTAATCGTTCGTGCGTCTTGTCAAGTCGCTGTGCCGCCGGCTTTCCTACCACGCTAAGCGAGCTAGACACCATTCTAGATGGACTGCTCGTACAAATCCCACATGCGAGGCAGGCTCTTAACCCGGAAATTGGTGCGAAGGAGGTGACAATCGAGGAGCTCGCTAAGATCCCGAAAAAAAAGTTAGCGCCACGCCTGCCTGGCCGTCGTTGAATTAATACTCTCCCCTAAACCAGAGGGGTATCTAACGGGTCGGGGGTCGGGGGTCCGGCACTCCCGGGACGAAGACTATGATTTCGTTTCAAAGACTCCTTTTGACAGGGCTGAGCGTTCTCCGCTAGGCCGTTGAGGGGAGGAGGCTTGGTTTATAGGTAGCTACGTCGATATACCCGGACGGATGAGGTCGGGGGTCGGGGGCAAACTTGAGGGTTGATAAGGGTGAGGGGCCATCATTCAAATAGCCCTCAGTGGCCTGCAGCAAAAAAGTTTCCTCGGAGCTGGTTTTCCTCTAGCGGTAACGATGCCCGGTGGGAAACTGCTAAGGTTGCACAGGCCCTCGACGACAGGGCCTCTTGAAACGCGGTACCTCTGTTCCCGCCCTTACTAGTCTGACTCCTTCGTTATGGTTACCTTAGGCCATTCTAATGGCGATATTAAAGGAGACCTCAAAAGTCGCTCTATGCGAACGTGACAATTCTTTGGTTTGACCGAACAGCGCCTCAAGAAATCAGATTTACTCTCATGTGGGAGGCTGCCTTACGCTCCGGTAGAGGACCTCGTCTGGCGGGCGTAGGCCCTAGCCAGTTGCTCACGGGTTCCTTACTCGTGCTATGGCAATGCGGACCCCCTTAACATCACCGCGGGGTGGGCCATAAGGTCTGTGTGCAGATCCTTACTCCCAGGAGTAGTGCATCGAAATTCTGTTCGCTGACGCCAGGGCGCGACTTTGACTACGAATGGCGTTCTTTTGTATATAGTTCAGCTTTCATGTGTATACTACCAGCCCCAATTGCCATCTCCCACAGTCCGCAGAGCCGTAGGAAGCTTAAAGCCGAGTGCATCGGAACTTCGTTTTTCTCGGGATTCTAGTCTAGTACGGGTCCTCTCTAGATCCGCTTCGAGAGAGGGTAGAGGGACGTCATCGACGCTTCGATATTCTCTCAATAGTACGGGTCACAGCCAAAGCGGGGCCCGGGACCGTACCCGCCCTGGAATTCAATAACGTTACTGTACCCTAGAATTAGGGATACGACGACCTTTTCCGGTCCATTACTCGGGATGCTGGGTGACTGTAGTAAGTTCGCTAATAAGGAAAAAGCGTCAGCACCAAGAGATAGTATAACGCAGTTTATAGGTCCAGGACTGGCTCTTCGGATGAGGTTGTTTTGAGATCATCCGTAGCGGGTCGAAAGGTATGTCCTTACTCCTTACTCGGAGGCGATCCCCGCCTGAAATAACCGCGAATTCATTGCATAGAATATAAAGAATTGTTAGGGAGCGTTTCGCCCGTGGTGAGGTAGTCCAGAAATCGAGTAAAAATTGGTTCCGAGCCAAGTCTATGCACAGAAGGCCATTGGGGACCCATTTGCGCTGGAATAATTTAACATTTTTGAAAGGTAAAATGGACTGTACCCGCCTATGGTGGGCACTTGCCTTTGGGGTGCGTGTGTAAGGTCGCTACCCTCGCTCGCCCTAGCCGCTAGGCGCCATCTTTCGTGGCTCGAACTTGGATGCGCCACGCCGCGTCCGCGGGAGGCGGTGGGTACTCTATGGCTGATTACGTCTAGGCAGGAATGTAGTTTCACCGCTATGGTGCGCACGCTGGGCATTAGGGAGCGTTCTTGGAAGCCGTGCGTTAAGGATTCGATGCACGGTGACCAGACCAACCCGCATGTACAGATTATATGCTATTGGAGAACAGTTATGAAAAATTTAGTCCACTAAGTGACAGGGAACATAATTCATGACAAACCTGAATCTGGAGAACACAGCTCGTAGAGTAGCGTCAGGCAGCCAAACCAGGCCGTAGCCTCACAGTGGGGTGTGCCGATCGCCGAGTAAAAAAGTTTGCCAGCGGTTGTGGGAGCGCGCTTGCGTGATAATAAAGGCTGCTGCGGCCAGAGTGGGGCAAAGTAAGCGGTCCGCGGGAGTACATATTGAGGGCGTGTTAAGCTAGCCAACATTGAATGGTAGAGAGGATTTAGGGACACGATTTTCTTTGAAACAATGGCAGGAGTAGGAACTGGATGGCGCTATGATCGCTTTCCACACTAATCCGCTCTCTGCCAGTTTAATTTTACTGCTGACGGGGAATGAAAGTATGTCGTCATCGTTGGCTGCTCGCCCCCGTAGTAAGTCTTCTATCCGCGCCACGCGCCACGCCCTGAACATTGCTGCGCGCTGTAGATTTATGGCGAGCCTCGACTCCCTATCGGAACGGCGTACTACGCCTGACTGGTGACGAAATGTAGTCAAGCATGTACCTTGTGCGTTAACGGACCCCCTATTGCCACGCGGGGGCCTTGCAATAATTACCCTTGATGAAGTTCCCCACCTGACTCCATAGGTAAATTAACAAAAACAGACAATAAAAAGCTACACGTGGTGAAGCAGGACTTCGTTTTGGGTGAGCTGTAACTGACGACAGGTAGTAAGGGAAATATGCGTCTGGCGCGTAGATGGTTGCGGTCCACGGAGTCATAGTGAGAATGTGGCCGCCTATTTAGCAACCAAGGGGCCGCCTTTTCGCTAAAGGACTATTGCGGCTCTAATTTACACGACGGGAGTTCATGTCCCCTTTCTACGGTACCTACCACGGATTTCGCGGTCCTGGTGGGAGATCATGCCCCCATTTATAAGTACGATGACTAAGGGTCGGCGGCCAGTGGAGGCTGATCGATAGACCTTTTACATCATGAATCTTAGTGATTAAAGACCGTATCATCAGAACATCACGCAACCGTGCTCGGTGGGCGCCACGCTGGAGATCTCCAAGATCTAAGCCTTTGATGGGGGTTCTCCCGACGATGGGCTGAACCAGGGATACATGGACAGACCCTAAGCCAAGAGGGGGTACCGGAGCCTGATTGAGTAAGATGTCGAACGAGGAGGGTTCACCGGTTCAGGGGCGCCGCCCGTATGCACTCATATCAGCCCAAATCATCCGTAAAACCTAGATTTAACGGGGGGCTCTTGACATGACGCTAAACTCAGTCTCAACTGTAGCAGACCAGAACACGGATCAATAAGCAGCTTGGGTTCCGCTACTAGATTTCTGCTCACGCTATGTATCTATGCTCACCGAGAATGAAACAAGCGTGCCAACGATCAAGATCCATGACTCAACCTGACTGCCGACGGTCAATTTAGCACTCGCCATTACAACGCGTCAGATCATCTCTATCACTCTTCCCTAACAACGGACCTCTTCCCTCTTCCCTGCACCCACAGGTAGTTGCCTGGATATACGGCTGGTCACAGGTCTTTTAACCGGTGCTGTATTTTCGCGGGGCGGGGAAAAACTTAACTGCTCGAATAATAAATCGGAATATGTCCTGTTCCGAAAATTACACTGGGTGTCAGTCCGCCAAGATGCGTGCCTTAACCGGCCATTATGTGTGCGACCCTGATATCGTCGGCAAGGAACACGCACGTCACGCCCACTAAGGAGTGGATACGTGAGTATTCGTTTCTCGGGTGGTTTAGGTGTTAATCCTACGGAGAAGCCACTCCTCGCATAACGAAGGGTAATTGGTCCGCGTAATGAGCTGGGTCAGCTACTACTAGGATGAAAGTGTAATGGATCGCCACTAAGCTGCATGCCCATGCGTAAATAATCTATGCTGCGCGCTGCGCGCAATAACAGCACCGCGAGAATACAACTTTGCTTAAATCACCTCTGTCGTCCACCCCTTCTGAATCGAGATCTCTTCCCTCTTCCCTGCGAGACGAGCTGTACCGTTAGACCCTGGAGTCAGAGGTAACTACGGAGGCCAGAGAGCATCCGATGACACGAGCCGTGATATCGATTAATCCCAAGTTACGGTCCCGTTCGACTGGCAAAATCGCAGAACTGTCTCCCCATAGCGATCTGTAGGTAGTACCGAAAACATCTTATCATGTGTTTTGAATTCTCCTTGCAAGAACTCAGGTTTGGTTTAGCTATCCAGTTTTTATTTGTACTATTTTGGGGTCGTATTCTTCATCTCAAATAGCTGTCTGGGTTGGGAAACCCTGACCGCTTGTATTGTAATCTGTTTTAACTATCAGTGCTTATCAGCTAACTTCTCCGCCGTTAGTAACGCCAGCTCTCACTCTGCAGAGATCTCTCTGTTGCTGCCATGCTACGAACTTATTCCTTGGAACAGTGTGACGTCTGACTGGAGTTGACCCCTCTTCCCTAAAGTGTTGATACCGTTGACCTCGTAGTGGCTACACCAACGTCGCCAATAAGCTGAATTACTTCGCAGTGCGTCTACGAGCTGGCCGAATCGCCCCGGGTTGCTATGCGCGTCGCGATGGCGAGCAGCCAACGGTTAACGATTTA
# GTAGTAAGT
# GGTCGGGGG
# TCCTTACTC
# CTCTTCCCT
# ACTGCTGAC
# GCGCCACGC
# GCTGCGCGC""".split("\n")
    strings = """AGGTCCTTCCTGATTAGCGGCCTACGATGATGGTATATCGTCATTTCTGACACTCAATCCATCAACTCGGCTTTCATACAGATCGCTTATGGGGGTCTGCTTCACCGATGGATATGGTACGGCCGTTTCATTCTATTACAAGCGACTGTGACCCGATATCCGATTAATAAGCCAGACAGTCTAGGGAAAGGCTTAGATAACGAGACGACCGGGTGTTTTGCTCAAAGGGCAAAGAGTGCTAGATCTCTGTGGTGGGGTGTTGTGAAATTATGTCGACGTCCTGGTACTCCGACTACTGCAGTCAACAATATACTTCAATTCACAGACGGATAGTGAGTACATCAATCTATAGTGTAACATACCTTCGCATCCCCGGGCTAGCCACGCCCCACCAAGGATTGGCGTTCGTCTTCCTGATTACACGCGGAAAGGGTTTCAAGACCTGTGAACCGTGAACCGTGCCAGCGCCGAGCTCGCATACATCACTAAACCAAATTCTAAGAGGGCGAGCTTGCTTGGGGCCGTGTGGAATTTCAACTCAGGTATTTGTTGCTCGCGAATGTGACAGGTTAACTCAAGGGAATCCAACCGAGCCTATGAATGATCAATTATAAGCACCATTAATTTCTGACACTGGACTACGCGAGGCCAGCCGTACAAGTTATTCTCACTAGGCCCGGGGACTGTAGTCGTGTCCTGATAAGGTAAGGGCCCCGAGCTATTAGCCTGTCACCTGTCACCGATCCTACCGCTTAGCCCGGTCCCGGTAAAACAATGTGTAAACGTCTCAGTTCGAGTACCCTCCGAGCTCCTAGTCTAATTACGTGAGACGTCACTTAGAAGTACGTGTGTGCAGAAACAGCCTAGTTCAGGTACATTTCCCATCGTAGACTACTTGCGCGAAGCATAGCATAGGAACCGAGAAGAAGGACTGCTTAATTACCTTTAACGCGGGCCCATCTCTGATGTACTCTAAGTCATCACTTACTTCGGATGGCCTAAAGCCTTACACCTAGCGTTTCTCTATTCGTATGCTTCATTAGAGTCCGATTAATCAAAAAACACCCAGCAGGTGGCGAAGAATCACTGCGGACTCTTCAAGGGTAGCTCACCTTCATGTATTCCCCTTTCCCATTTGATTACAACAGCGCATTTATAACGTGCCTCTCAATGGCATGGCATCCGCCGGTAAGCGGCATCAGGTCGGTCTGACAATGGAATTGCACCGAGGCGTTGTCGCTCGTTAATAAGTCAGGCTACTCACATGCAATATGAACTATGCTGGAGCCTAGCAGCATCCAGCATCCACTGTCATCTACTGCAATATCAACAGTTGGAGCGGAATCCCATACCCGTCGTTCGGACCTTATTTCGCGCGACGCAGGTACCGCTTGTAAGGGATAGCCACTTTCTCATGTTCCTTTTCTGCCCATTGAGCAAATTCATCGGGTACGTGATGCCCACTATGCGAACTTCGTGAAGACTCGCGGGCAAGAATGCAGGATCGTGAGGGGCGGCTCATGTGGTCAAGATCAACGGGACCACCAACTACGCTTCGTATGCGCGGGGAGCCAGACCCTACATCTGGTGTGAACCGCGTAGGTTGGAGCTCCCCTTGGCGTGATAGGTTGTTAAGACTGCATTTATCATGTTGACTTTATGCATCCCCACGGTCATGATCTCTGTCTATCGTTACCTGTCACCACGCTGACTGAGCCCCGCGTGTGGCCACGCATGAACTGGCAGATAAACTTAGTCTAAACAATAGAAAGATGCGCGTTATCACCATCTGCCTTTCGGTATGCGGAAAGGAATAATTCGTGTCACGTGGCCCTATACCGTAAAACTCTTCCAAGATCGTGTAAAATTGACGCTATAGGGTTGTGCCCGAGATTCAGGGGGGTAACAACTAAAACCCCTTAGGGCCTCTATAAGTGCGCTAGTCCGGCACATCCTACTCTTGGACCGCATCTGCAATTTGGGACTACGCGGAGCGGCTCGAAGACATTTATAATCGCTAACCTTAGATCACGTCTAAATGACCTTTTTGGTAGATTTACCTAACTGGATGACCACCCATCTTTGACTCGATATTGCGTCCCTATTGTAATTTCATACCCACAGGGAGATGCGTCCTAGTAGGGAATCCGTCAAGATCGGGATGTCGCGCTAAATCCTGGGGAGTTTCATAGGGCGACCAGTTAGTATTAGCCCACGTGACGCCCATTGCTCACCGCGCATCCCAAGCAAACCTACTGCCGGTGTAAGATAGGATAAGAATATCTCCTGCAAGGGTGGCTTCCATGCCTGATGCCTGATGGTTGAATAGAGGCCGCCAGATTTGGAGTACTTATTGTAGAACTCTAGGGCGGTATAATGACGAGCCTGACGCGCTGGAATTACTAACAGAGTTGCCCTAACGCCATTTTTTACCTTCCCGGGCCAGAAAACTGGTGGGGTGTTCCGTGCGATACCGTGACGATACAAAGCCAGCACACTACAGTGCCGATCTTTTCCCCCGAGGCTCAAAGTTAGCGCCGGCCTTCAGATTCGAAGTTGTAAATATCTGACCCGTCTTTACCAACAACACAAGTGGCTGAAAAGGTTGAGCCTCCGAGCTTGTAGTCGACCGGAAGTAAACGAGCACCTTGTCATAAAAATATATTGAAGAGCCCCACGTGCACTCTGATTGCTATGAGTTACAGGTTACAGCTCAACCACTATGGCAAGTTTATTGAACCCCTGTCACCTGTCACCACTGGGGCATGATTAGCACGCGCAGGGCGATAGGGAGATAGTCTGATTAGTTATCAGTACTCGTAGGACAAAGAAACTGTCTAAGTCAGCATCCATAGCGCGACGACAATAGGGCGGTTCCTGCCCCGACTAACAAGTGTAATCTCTCCTATGTGGGTTCCTTATTTCGTGGACGTCTCTAGAATTCTAGGTGAGGCATTATAGCCCCCACAGGGCAGTCCCAGCGTCACTTTGATACAGCGACCAATACTGCGAACATGCGTGCGCGCTGTATCAAAGTGCCTTGGACCGAACTGCCGATTGTAAGGTCACGGGCCTTCTACGACGCAAATTCTTATGAATCGGTGCGCACACGTGTGCTTCATGGTGTATTAAGGATGGGGGCCACATGCAGTGCTAGGTGGCATTACTTCTATTTCTGGCCTTACGGGTCCGGGACATCGGAACCGTGTCTCGTTATTGCAATACATCCAGAGTCATACTACATGCCGGGCAATGCCTGATTCATCTTAATCGCGCCGCTAACAGCCGTTTCACCGTTTACGACTTCCGGTCAAGAGAAGCCAGTAGTAATCGAACGTCCTTCTGGAAAGCCATAAAGATTGGACACAGGTTAAGACCGTCATAAGGAACGGGGAGCACAGATGGTGCGAATTATCATGGATCGCCAGGTGACTTGCGTTCTCTTGATGGTAGCGGTCATGCAACTACCCTAAGAGCAGCAATGCCTAAGGTTTACGCGGGGGTAAATTACGAGGGTAAGGTTATATCGCGGGCAAAACGGCACTGGTTTAGCCCCAAATTTTTACGCTCTAGGGTCGTCATGCACACTACTGGCCTTTCGCATCAACACTGCCTTAGGGGTGTTTTCCAACGCATCCACAAACGTCATCATCTTAGAGCAGTGCGCTCTCTAGCGTTTCATGAAAACAGCAGGACTCCCCTTCTACGTCAGCAGCGAGACACTACAGCAGCCTTTGGTTAAGATCCAACTGAGAACTTAATTCATACAACCCAGACCAGGGTAGTGCAGCATCCAGCATCCAACAATTTAGCCCGCCTCCGTGTAAAGCAACGCGGGATGCGCACCCACACTTAACCGATTGCCAAATGCACATTGCACATATACTCCGAGCTGGTCAGTGGGAGCCAGAACATCGGACGATATACACGGCGAAGTCGCATCCTAGCGCGCGGCGACGCGGAATCGGTACGGCTTCCCAACCACTCACACGGATCTAACCTAGGTCTGTTTCGCGCCTACCTTAACCCTTAGTATCACAGATCGTAAGTCTTTTGCGGGACGACACATTTTACGTCGAAGAATTGGGGCACGGTGCCGAGCTAGACTTGTGGCTTACGTGCTTAGTTTCCTTCTGGCAATCAATTGTGGAAACGATGGAACTCGAGCTCCGGAAGCACAGCGGTATATCCCAGACCTACGTAATTTATTACTGTTGCTTGAAAATAAGACGGGAGAGGGTGCGCTGTAACGGTCTTGAGTAATAACATAAGGGGTACCGAATATTGGTAACTAACCATGTGCCACCCACTAGTGTAGCGGTCATCGGCCATCTTAAGACCTACCATACATTATGGTCAGCGGATTATGCCGGCTGCCTCCTTACGCAATCACGGTTCTTTGAGGGATTCTCATGTCACGACGGCCAAAAGACTCGTGACACTAACGGCCTGTCGTTGCCGGTTATAGTCTTCGTCGGAGTGTGGTGGGCATAGTACTAAGAGGTAATTTGCTGGCGTCGTTAGTGTCGGCACCTGTCACCTGTCACCGTCGTGTTCACATAACATTCGCGCCGTCCGCATGTCTATGAGTCCGCAGCCGGGGTACCAAAGACCCTCGCCTACCACTGGAGGGAGAGATGAGCATCGGCCATCCTGAATGACCGGGGCCCGGACACAATTTAAGCGACCCAATGATTGGACCGAATGTTGAGCATTGCATACGGTAGATTTGCTCACCTAAGGATTGAAAGAGACCATTACAAAAACACGGTGTAGATTGGAAACTGAAGATAGATGAGTCCAGAAACACAATCGGTCGTGGCACGTTTTTTGGAAATTATCGACCTCCGTTATTTGTCCTGGACGTAAAAAGTGGTCTGTACCATGACGCGCGGATATAGTTAACCCAGTCTAATCGTGTTGTAATGGCAGGATTGTGACCGGTAACATAGTCCGTTCATCCGCGAGGCCGGGCTCGGGGTTCGCACAGCCATAGAGACCTGGGACTCTGACTAGCGCCCTCTGCGACTTTCGGATGGCGTACGGAGGGCGAGATCTATGGCTGGCTAGCCATTCTCGAGCGTTCAGGACCCAGTGGAGCATTTCAGGATTAATTACAGTTGCGTCGCTCAGTGAAAGCGTGGCTGCAACCATACCCCCAGGTGAAGTATGCTGAGAAAGGTCGCGTATTCGGGAAATCAGGGGGAAAGTCAACTGATGTGTAGAACACGCACTGCGCCATTAAGTAAGTGTCCTCGCTCCACTGACTAGCAGGGCTCTAGTTAGCGTTGTAATTTTAGAATTGCCACGGCAGTGTACTACTAGACGGAAGACGGCATTCCTATTAAATGTGATTACTCAAGGACCTCAGTCCAGCGCTGTGGCAATATGTCAGCCGCGCCTAAGTACTATTTGCGAATAGTTCTCTGCATGCATTTCGCTGGACCTGGTCGTACTTAGTGCGTCCGTGTCTCACATCGGCCAGCGAACAGTACATTGTTTAGGCATCTGATCTTGTTTGAAAGCTTCGCTATGATCACATTTGATCTGAAAAAACCGCGGATAGGACCACAACGTTCATCAGGTCGAAGTATTCCGAAAATGTGCCGCGACCGCTCCATGATGCTATCATCGGCCAGCGCATCGATGCGTGAGTGAATTGGGTAGCCGCCGGTCACCTAGGTGTAAAAAGTACATGAGAATTTATAAGGTCCTTAGGGCTGGCAATGCCCGCCCGATTAAACCTATATCCAGAGTCGCCGTGGTATTTCGTGGCGTATTTTGCATTAATTTGGGAGTAAACTACATGTTTACTAGTGATGGCTCAACATTTTATTTACAGACTAACGACCGTTGTTGGAAAATACGTCAATGAAATTCTCCCAACTAGTAATGGTACAACGAGGTCGACGAGTGATAGCACGAGCATCCAAGTTAAAGACCGGTATTGTTCATAATCCCAGATAATGACGCTTTTGCGGGCGGTACTGTAACTGCTTGTGAGCGCGTCCAGGTCCAAAAGTACTGCGCCTATACGTCTTGCTAATTCGCTACGGCAAGGCGTCCTGTACTCGCCAAGGACGGTAAACGCCGCAATGCCAGGTTCACCATGTTCACAGGGCTGTCAGGGCAGGACTTACTCGCCAATCTCCTCCAATTGTGCCCTTAAATATTGGAAGAATCCTCCTGCCAAGGCGCGGGGACAATCGACAGAAATGAACATTTGTTTTTGGGGATGAACTTAGGATGAAAACTGTAATAATTGCTTAGGATCGACTTTGTCAGACGTCGTTCTGGCCCAATTGAACCGTGAACCGTGGTTAAGACTAGTATAGAGGGGGGGTTGAACCGTGAACCGTGCTAAGTTAAATTGAGCGTAATCAAAGTCTTACTATGCGTTCACGTGCTCGGTTTTTTTTAAGTGTGCTATGAGTCTGTCAGTTCATCCGTGCGAGCCACGACCCTAGCAAGTTGTGCGCTCGAAACAGCGGAGCGCACATTAAAACAAGCGCGGAGTAAGTGGTGTTTCAGTACGAGAATGGCGGTCCAGTACTACACGTGCTTCCCAAAGCCCCAGGTCACATATACGAAGATAATGCAACGTCCGACCAGGCGGCAGCCATGACTGGAATTCTTAGAACGGTATCTCGAAATGTGGTAAATGACTTCCCACATATCTTATTGAGTATTGCGTCCACTGGACTGGCGCAATTTTCTAACCTACGCCCTGGAGCGGGAAACTCCTCTCTCTCGCTCGCACCGTTGGCAGGAGAGGCTGGGGAGTAAACGAAATTGTGGGGACGGTCGCTGCCTAGATGCTACCGTCCACTACAGAGTGCTGTTATAGATGTTTCGACATGGCATGTCTGTTCGAACCAGTAAAGTCGAAGCTCACTTCATCCTGCACCATCCTGGCCCAGCTTATGAGTGATGGGCTTCAAGTATACGCCTAAATCCGCCACTACCACGTACACACGTGACGATGATTTTCTACGGGGTGACCAAAGCGCCTTACTTTCCTTGATACTCCAGACATACGAGCGAAGCCGGAATTCCGGGTCGAGAAATCCAACTATATCCCATTTTCTTGTCCACATGGGACGACACCAACATCGAGAGTCTTCGGCTCCCGTATGATCTCGCATGAACCGTGAACCGTGCGGTAGGAAAGGGGGGGAAATTTCGCACGCCCAGTACCACATTGTTCGTGATTACCTTGGTTAGTCACTTCCCCGTCTGTCGACTAAGGACTAACAGGACCTTCTTGCACTTGATTTTCCCGTATGAGCGTTACACCTTGCATTTTTCATTGGAGTGCGACGTTCGTCCGAACCGCTCATACCCGTTTGACCGTATAATCAGATCACCGGATGTTGAGGACCCACAGCATCCAATATCTGCATTGGGCACGAAACCTTAACTCACATCGGCTCGGCTACATACGTTCTCACATTGTCCAAATAGTGCAGCCAGACCGCTAACCGTCGGTATGCTCTAAGCCGAGTACGAATAAAATAGTCAAACCCGATCTGCGTTGTACTCGATTGCCCATAAATCGGAGTCATGGGACCTAGCCACACTTCAGGTGATTATTTTTATGAACCGTGGGTGTTCATCGGTTATCCCTTTGATAGGTGATCAACCTGCTGATCTAAAGGGACTCCTTGGTAGTTGATAGCACTCCCTCGATGCACGCGCCGAAGCAATAAGTGGTCTAGTATCGGCGGTATATAACGCATATCCCCAGCTATCCTTATAATCGGTTAGAACGGTGGGATAATAGGGTATTGAGGGACTCCACGGCTGGAGCCAGCGCCAGGGATATTAAGGAATTATGCCTGATGCCTGATTTCAACGTTTGGGACGATAGGGCCCGGCGTGACGCGAGTCCAGGCGCCCGATGTGGGCTTTACAGGTTTTTTGAACGTCCCCGGATCTTAGAAGCCATTGCCGGCGACAGTAAGTATAATCCATAAATGCGGATGGCAAGTGTCTCCGAGCTCCGAGCTCACTTACAGCAGCCACAACTTTTAGGTCAGGTTAACAATGGATCCATCGGCCATCGGCCAGAACGCTTGTGCGGTCTTCTCTTCACGAGATTTGTCAGTATCCTAAATAGTGCCACGTATTTTCCAACATAAAGAAGCAGTATACGCGTACTCCGAATGGTCTGGCCAACTCTTCATCATAACGCTAGTCCCAGCATGACACGCCGGATCACGCACCCTGGGCCTTGGCGGAAGGCCTTATGTGAGCCCTGTATAGCATGTACTCTAGCCAGGGAACTACCGGGGATGAATACGCCGTGTGGGGAACCGGGGGCTCAGTCTTATGGGCACCCAGAGTCTTAACATACTCAATGAGGCCTCAGTCGAGTAGTGGTAACGGAGTCTGAACCCTTTCAACATTAACTAACGGACAGACTGGTTGTATTTACAAGCGACAGGGTCCTGGAGATGATACTCGCAAGAGCTTCCAACCCAATCGACATCTCCTGCCAGTTGCTCGGGCTGTACAGGAACAAAGCGAGGGCCGTCTTCCTAAAACTCAGTAAAATTCCAAATACTTACAGGTTGCCATGGATCACGGATCTCGGTCCATTGAGTTTTGTAGTCTCCTACGGATCTGCTAAGTTTTCCTTGATTCGACTGTGACTTTTGAGTGCTTAGCTAGATTATGAACTAGCAGTGCTGTCAAAAAGGGCGATACGAAGCTGATGGAGCGGCCTTCGCGAGTTCTTCTGATGCTTACGGATAATACATAACCTATAACACACTGCCATATAACGAACGATCCCATCCTACCGGAGCCTCTATACATGCAATGCTCTCGGTGTCATCGGCAGCCTGAAAGGAATAGAAGGCGGACATGAGGAGCGCCGGC
TTACAGGTT
CATCGGCCA
ATGCCTGAT
TGAACCGTG
CAGCATCCA
CTCCGAGCT
CCTGTCACC""".split("\n")
    print(*solve_trie_matching(strings))


