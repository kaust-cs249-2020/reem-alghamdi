"""
@BY: Reem Alghamdi
@DATE: 09-09-2020
"""
import operator

from ch2.code.ch2_03 import score, profile as profile_matrix

map_nucleotides = {'A': 0, 'C': 1, 'G': 2, 'T': 3}


def profile_most_probable_kmer(text, k, matrix_4xk):
    """
    Th
    :param text: the text
    :param k: k-mer length
    :param matrix_4xk: the profile matrix (A, C, G, T) x (profile)
    :return: A Profile-most probable k-mer in Text
    """
    probability_table = {}
    for index in range(len(text)-k + 1):
        kmer = text[index:index+k]
        probability_table[kmer] = 1
        for i, nucleotide in enumerate(kmer):
            probability_table[kmer] *= matrix_4xk[map_nucleotides[nucleotide]][i]
    return max(probability_table.items(), key=operator.itemgetter(1))[0]


def greedy_motif_search(dna, k, t):
    best_motifs = [x[0:k] for x in dna]
    print("best motifs: ", *best_motifs)
    for index in range(len(dna[0]) - k + 1):
        kmer = dna[0][index:index+k]
        motifs = [kmer]
        for i in range(1, t):
            profile = profile_matrix(motifs)
            print(profile)
            motifs.append(profile_most_probable_kmer(dna[i], k, profile))
            print(motifs[i])
        if score(motifs) < score(best_motifs):
            print(score(motifs), score(best_motifs))
            best_motifs = motifs
    return best_motifs


if __name__ == '__main__':
    # print(profile_most_probable_kmer("ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT", 5, [[0.2, 0.2, 0.3, 0.2, 0.3], [0.4, 0.3, 0.1, 0.5, 0.1], [0.3, 0.3, 0.5, 0.2, 0.4], [0.1, 0.2, 0.1, 0.1, 0.2]]))
    # print(profile_most_probable_kmer("TGCCCGAGCTATCTTATGCGCATCGCATGCGGACCCTTCCCTAGGCTTGTCGCAAGCCATTATCCTGGGCGCTAGTTGCGCGAGTATTGTCAGACCTGATGACGCTGTAAGCTAGCGTGTTCAGCGGCGCGCAATGAGCGGTTTAGATCACAGAATCCTTTGGCGTATTCCTATCCGTTACATCACCTTCCTCACCCCTA", 6, [[0.364, 0.333, 0.303, 0.212, 0.121, 0.242], [0.182, 0.182, 0.212, 0.303, 0.182, 0.303], [0.121, 0.303, 0.182, 0.273, 0.333, 0.303], [0.333, 0.182, 0.303, 0.212, 0.364, 0.152]]))
    print(*greedy_motif_search(["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"], 3, 5))
