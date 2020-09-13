"""
@BY: Reem Alghamdi
@DATE: 11-09-2020
"""
import random

from ch2.code.ch2_05 import profile_most_probable_kmer
from ch2.code.ch2_06 import profile_matrix_pseudocounts, score_pseudocounts


def motifs(profile, dna):
    """
    :param profile: 4 x k profile matrix
    :param dna: dna matrix of s x t motifs.
    :return: t x k string array of best motifs found
    """
    best = []
    for i in range(len(dna)):
        best.append(profile_most_probable_kmer(dna[i], len(profile[0]), profile))

    return best


def randomized_motif_search(dna, k, t):
    """
    :param dna: dna matrix of k motifs.
    :param k: kmer length
    :param t: length of dna
    :return: t x k string array of best motifs found in greedy search
    """
    _motifs = []
    for string in dna:
        r = random.randrange(len(dna[0]) - k)
        _motifs.append(string[r:r+k])
    best_motifs = _motifs
    while(True):
        profile = profile_matrix_pseudocounts(_motifs)
        _motifs = motifs(profile, dna)
        if score_pseudocounts(_motifs) < score_pseudocounts(best_motifs):
            best_motifs = _motifs
        else:
            return best_motifs


def iteration_rms(dna, k, t, times):
    best_motifs = randomized_motif_search(dna, k, t)
    i = 0
    while i < times:
        _motifs = randomized_motif_search(dna, k, t)
        if score_pseudocounts(_motifs) < score_pseudocounts(best_motifs):
            best_motifs = _motifs
        i += 1
    print(score_pseudocounts(best_motifs))
    return best_motifs


if __name__ == '__main__':
    # print(*motifs([
    #     [4/5, 0, 0, 1/5],
    #     [0, 3/5, 1/5, 0],
    #     [1/5, 1/5, 4/5,0],
    #     [0, 1/5, 0, 4/5]
    # ],
    #     ['TTACCTTAAC',
    #      'GATGTCTGTC',
    #      'ACGGCGTTAG',
    #      'CCCTAACGAG',
    #      'CGTCAGAGGT']))
    print(*iteration_rms(['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA'], 8, 5, 10000))
    print('\n'.join(iteration_rms(
        [
            'CCCTCCGAGGGAGCAAATACATTGATATACCTAGCAGACCACCATGCAATCGGAACTTAAAGGCTGTGAGGCTTTCCTATGCGGGGAAGTTGACGGTTTGAAGGGTCGCAAGTAACTACATTGTCCTTATCTGAGTACAACTCCAAGGTCCAGGTTTCTGAGGCCCGGAAGCCCCTCCGAGGGAGCA',
            'AATACATTGAGGCATCGACCATAACTATACCTAGCAGACCACCATGCAATCGGAACTTAAAGGCTGTGAGGCTTTCCTATGCGGGGAAGTTGACGGTTTGAAGGGTCGCAAGTAACTACATTGTCCTTATCTGAGTACAACTCCAAGGTCCAGGTTTCTGAGGCCCGGAAGCCCCTCCGAGGGAGCA',
            'TAGGACGTCTACACTCGTTCGACGCCCTTGACTCGGACCGTGCTATAATTTCTCTTCCGGTGGCAAGCCTTCTCAGATACAGATGAACTAATAAGCTACTTTGTTGGCCGAGTTTATAACCGTTCGTGAGGGCAAGCCATCAATGGTAAAGTCACGGCAGCTATCCAGTACTATGTCCGAAATAAAG',
            'GTCTCAACGGAGGCTTCTATGATTAGTCATGGGACATATGTCGTCGGGGGACGGCCGGTATTCCTTGCTGCCTCAAACCCCATCAGCTGCTCTCTTTGCTGCAGACACCAGAGATAAGACGTCCAACGTCTCCGCTCTGAAATAAACGTGTTTCCTGGTCTTGCCGAGACCATACTAGAGCTGTACA',
            'CATTAAAAGGTGGGTGTACAAGGGCTAAATACTGGGAAATTTCACCCGTCAGGCTCCGACTCTTCGCAATTTAGATGGTCGACCTCCAGTCCGGGGTTATGATCTGCATTTTGTTATGACTGCTCTACCGGGCCGAGACCAGCGCCAGCGTGCGCAGATCGGTTTACTGAATAGATGCTATAGTTTA',
            'TCAAATACAGGGACCTATAGCCCGCTTGAAAGCAGGGTATAGCGCGGCTGTTGGAGACCATAACGATTCGAACGCATGAGGCTCTTAAATTGCAAACAGAGGCGACTGATTAGAGGGTCCAAAGGCGGGTGGGAGGAGCCAACCGGCGCGAAGCCGTTTATAGTTATCATGGATCGGGGATACAGGT',
            'CCGCTCCCTTAGGCGCGTCTCGGAACTATCTGTGATTTATTTCAACGCCGCCCTTCGGGGAGAGGTAGCCGAACTTGCGGGTAAGAATTATTAGTGCCCTAACGGCCGTCGCCATAACTGGACTACCAAGCCGCGTCTCGCCACTCGGGCAGTACGGAGGATACGTGAGTTCGGCAAGATTACATGC',
            'ACCAAATGCTTAAAGACGCTAAACCCAATAGCTTAGAGGAAAAAGTGAATCCTATCGTGCGTGCAGTGCCCTGCGGACAACCGCTCTATCTGATCATTAGTATCTCCGGAGGCGGCGTCGGGCCGAGAAATTAACGCATAACTTCAGCGCTATATGAAATAAGGGAGTACTAAAATGGCCGGGTCCT',
            'GTGTGAAATTTTGAATTAGCTAGTCAGTAAAATGGTAGCTATGCCTCACTGAGTTACCAGGCTTTCAACTCCGCCGTCCAACCACCGTTTTGCGGCGTCGGCGTTTCCCCATAGCCTTATGCTCTTGCTCGGCCTCAACCATAACGTTTACCCCCGCGACATGGTGGTATCGAAGAGCAAGCTTGTA',
            'TGTCCTACTTGCTTGGCCACTACCATAACGATGCGAGAGCTGCAATTCACTTGTCCCAAAGTGAAGCCTACTTAACTTCCTCTTAATCCGTTTGTTCGGCGGCAGCTACTTACGACATAGGCATATCGGGAGAAACAGAGCAGGTCGGAGGGGGCGATTCACATACGATAGAAAAGCCTCCAGTATA',
            'CCCACCTGCCATCCAAGCTTTCGCCACAGACCGTCTGGGGCTAGGACCATAACTACAGGACAGACGTAATTCCTCACCGCGTGGGAAGTTGTATATATACTGGAGGCAATGTTCAAGTCTCATTGCGTTAGCATCACTCACGGACGAAGCAGGTGGCAGACGAGGTGCGCAGTTCCTAGACGCTAGT',
            'GGGTCCGCCCTTCAGCCTCATGTGTCTTATCATTCAAAAGGGGTCTCTTGATCTTTTGAGAGGCTGCCAGCGCGGGTCGCTGACCGGGCCCTAGTGATAGGCCGGTTCCATAACCTTATAACCCGAGGCCGCCTCCCGGCCCGACCCCCGGACCTGCTGAGCGCTCGATCATTTATTACGACTAAGA',
            'GTTAAGCGTGCTTAGCGGCGCACCCCAAACATACACCCTGACCCTGGAAACTACAGTATTGAAGCGGAAAAGACCATAACGCTGCGTTCAAACTCATTACGCTCGCGTAACATCAGATCTACGGTCTTATCTTTCTGATGACACCATCTGCCGGCCCCGATGTATGCGGAAGGGCCTTGTATCCCCA',
            'GCCGAAAATTATGAAATTCTACGCCTCAGCCGGAGACCGGCAACATAGCTCGCTTCTCGTTTCAGATTATTTGGGCCAAACCGAGACCATAAGTAAGCAGAATGACTATATCCTATTCTCGTGAATCATCGGGTGTTCCTTGAGCTTTCGCGGCAGCACCCGGTTCCTTTTCTCCGATATTCGGGGC',
            'TTGCGAGGAGCTCAGGGCATAGTGTTCTCACATAGCCTAAGGTGGACCTTTATGAACTAATCCTTTTGATAGTCCGGAGACTTTTAGACCGCAGGGTGATTAAATCTCCGTGCCCCTTTCTCTCACGCGAGACCATAACGCAGGACCAACTGGTATCATAATTCTACTCGCGGCGCGATACACAGCT',
            'CTCCAGACTCTGACCAAGGCCGAGACACAAACGGGCAGCAGATCAGGAGCTTCGATGCGTCACAATTACTTCCGACACGCGGCTACGAGTCCGGTGAGACAGCATAGTTAAGAACAATCCGTGCAGCTCTCTGGTTTGCACGTCCGTCCGTTGTGTTAGGAAGGCGGCGCGAGTACGAGATAGTCGT',
            'CGATTACTACGTTCCGTGACCTCAGGATGAGCTAGTGTAATAGACTAAACTTATGTAGTCCTAAGGCGGACTGCTTATTCGACCTAAGAAATAATCGTCACAACAGCCTCCCGGCATCACTCTAAACAGAGTCGGCCCTCGAACTGTCATACTATGTATTATGGGCGGATGGCCGACTGCATAACCT',
            'TCCGAGGCGTGATCATTTAACACAATGGTGCTTTCACCGAGTATTCAAGTAGGCGGTCCTGAATGGGGGCCGATTACATAACCTCCGAGTGCACCACTTTCGGCTTGCAGACATTCTAACCCGGGATGGTCATCCACAGTTAAGGATACATAATGGGCTATGCTTAATCGCTGCTATCGTCAGGGGT',
            'ATATCACGACAGTTTGTAGGCCAGCCGCCCTTGGCCGAGACCATCCTCGACCCCCATGAAAGGCAATATGCGTCGCTACTATTAGAGCAGAAATATGAGATTACTATCATTAGACTGAGATAGCTTCACGGTAACTTTATGCGGCGACCCGAAGTGTGCAATAGCTGTTATCTAAGAGTGCATGGCA',
            'TGCCGTGGCTTAGTGAGTTTTTGCGTTGTCGAGTGCCTTGAAAAATATATCTTTTCTAAATGTCGATCCTGGGCCGAGACCGGTACGTGCCTGTCGCTTCAGTACGTGCGGTGCCTCTTGCAGCCGGCAATAACTTCCAGGCCTTCCACATATCGGTAAAAACATCTACTAGGTAATGTTAGATATA']
        , 15, 20, 1000)))