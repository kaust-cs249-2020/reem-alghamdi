"""
@BY: Reem Alghamdi
@DATE: 08-09-2020
"""
import operator


def profile_most_probable_kmer(text, k, matrix_4xk):
    """
    Th
    :param text: the text
    :param k: k-mer length
    :param matrix_4xk: the profile matrix (A, C, G, T) x (profile)
    :return: A Profile-most probable k-mer in Text
    """
    map_nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    probability_table = {}
    for index in range(len(text)-k + 1):
        kmer = text[index:index+k]
        probability_table[kmer] = 1
        for i, nucleotide in enumerate(kmer):
            probability_table[kmer] *= matrix_4xk[map_nucleotides[nucleotide]][i]
    return max(probability_table.items(), key=operator.itemgetter(1))[0]


if __name__ == '__main__':
    print(profile_most_probable_kmer("GGCGTTTGCAATGAACTCTATGAGCCGGGGACGGGAAGGATGCCTGGAAGACCAGAAACTGATAATCGGTATCTACATGCGCCCAACAAACCCGTCGTCGGCCTGCATACCCCGCTATATATGTTTCCTTTAACATGGCCACCATCTCATTGAGCAACAGGAATTAACCCTAAGTTGAGGATTAAATCACTCACAGTTGTACCGAGGGGGGCCGCGTATCGTTCCGTAATCTTTCGTTAATGTGGGCTTTAGGCATAACCTTGAGCAGCCCGACACGATACGGACATTGGCACGCGTCGGCGAAAAGCCAATGAGTCAAGTCGCAGCCCCCCTCCTAGTAATCGGGGCTTTAGTAAAACCACGAGTAATAACGTGAAGAGAGCACCGCCGGGCTATCCCGACCCACACATTCCTGTCAAAACAGTCGGTGGCTACGACGTGACTCTACATTTAGCGTCGAGCCTCGGGATAACTACTCTCTTGAGCCTGGATAGGCCCTAATGAGTAAAGAAAGTAAGTACCTGGAGAATCACCCACGCGCAAGTGGAGGAACATGGCCAGTGGCGGGGGACAGTGCGTCTACTCTAAGTCCTTAGTGAGAACCGGTCGAAATTGAAACTGCAATCGGAGTTTTTATTGCAATAGTCTCGACCTTGTCCTGAAACACATGTAATGGCAAAATGTTCGGCGAGGCCTACATAAATTCCACCCTATTCGGGTCCTTTGATTTCACGCGGGGCTCCAACCTTGTCATAGGTTTTGGTCCAGGCGGGGACACAGATGGTGAGTAGGAGCCTTGACTCCTAAATCAACGGCGGAGCGGGGCATCCTCTCGCCGATGCTACGACAATGGAGCGTCAAAACCTGTGTGGCACACCGCGCCACAGCTCCGACGTACTTCTAATTAAAGTTATAGTTACCCATGGAGTAGCTTCTCTAACATGCAAAATCCCACGACCCTGCTATGGCTTCGAGTTATAAGACCAAGATCCACCATCTT", 14,
                                     [
                                         [0.254, 0.254, 0.296, 0.282, 0.239, 0.282, 0.282, 0.211, 0.169, 0.31, 0.183, 0.324, 0.296, 0.169],
                                         [0.211, 0.239, 0.211, 0.282, 0.254, 0.211, 0.282, 0.225, 0.254 ,0.141, 0.31, 0.239, 0.239, 0.338],
                                         [0.324, 0.31, 0.254, 0.239, 0.239, 0.282, 0.296, 0.254, 0.225, 0.254, 0.31, 0.183, 0.254, 0.268],
                                         [0.211, 0.197, 0.239, 0.197, 0.268, 0.225, 0.141, 0.31, 0.352, 0.296, 0.197, 0.254, 0.211, 0.225],
                                     ]))