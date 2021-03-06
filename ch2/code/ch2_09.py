"""
@BY: Reem Alghamdi
@DATE: 11-09-2020
"""
import random

from ch2.code.ch2_05 import map_nucleotides
from ch2.code.ch2_06 import profile_matrix_pseudocounts, score_pseudocounts

"""
 GibbsSampler(Dna, k, t, N)
    randomly select k-mers Motifs = (Motif1, …, Motift) in each string from Dna
    BestMotifs ← Motifs
    for j ← 1 to N
        i ← Random(t)
        Profile ← profile matrix constructed from all strings in Motifs except for Motifi
        Motifi ← Profile-randomly generated k-mer in the i-th sequence
        if Score(Motifs) < Score(BestMotifs)
            BestMotifs ← Motifs
    return BestMotifs
        
"""
def profile_randomly_generated_kmer(text, k, matrix_4xk):
    """
    :param text: the text
    :param k: k-mer length
    :param matrix_4xk: the profile matrix (A, C, G, T) x (profile)
    :return: A Profile randomly generated k-mer in Text
    """
    probability_table = {}
    for index in range(len(text)-k + 1):
        kmer = text[index:index+k]
        probability_table[kmer] = 1
        for i, nucleotide in enumerate(kmer):
            probability_table[kmer] *= matrix_4xk[map_nucleotides[nucleotide]][i]
    i = random.uniform(0, sum(list(probability_table.values())))
    c = 0
    for kmer, value in probability_table.items():
        c += value
        if i <= c:
            return kmer


def gibbs_sampler(dna, k, t, n):
    _motifs = []
    for string in dna:
        r = random.randrange(len(dna[0]) - k)
        _motifs.append(string[r:r + k])
    best_motifs = _motifs
    for j in range(n):
        i = random.randrange(t)
        profile = profile_matrix_pseudocounts([x for index, x in enumerate(_motifs) if index != i])
        _motifs[i] = profile_randomly_generated_kmer(dna[i], k, profile)
        if score_pseudocounts(_motifs) < score_pseudocounts(best_motifs):
            best_motifs = _motifs
    return best_motifs


def iteration_gs(dna, k, t, n, times):
    best_motifs = gibbs_sampler(dna, k, t, n)
    i = 0
    while i < times:
        _motifs = gibbs_sampler(dna, k, t, n)
        if score_pseudocounts(_motifs) < score_pseudocounts(best_motifs):
            best_motifs = _motifs
        i += 1
    print(score_pseudocounts(best_motifs))
    return best_motifs


if __name__ == "__main__":
#     print('\n'.join(iteration_gs(['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT', 'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
# ,8, 5, 100, 20)))['CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
#          'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

    print('\n'.join(iteration_gs(
        ['TTAATGTTTTGACCCTGTTAAGACGGTGCCCACAACGAGGACTACCGATAGCGCGGACCAAAAATTTGGTGCTACTGTTCTCATTAATAAGCCGTTTCCATCATGCTCTCAATGGCGTATCTTCTTTACCAAAGGCGACGAGCAATCCTCGATGATGTTATCTAGGGAAAAAAAACTAGCCCGTTCACACTACCCTTCGGTAGAGTTCTAAAGCCTAGTGGGGAGTATTTCGAACCACCTATAGGATAAAATGGTGGTGGGCCTATCCAATGTGGAAAACGCTTATTTGTCCTACGGTCTGTACGCACGGATTTAATGTTTTGACCC', 'TGTTAAGACGGTGCCCACAACGAGGACTACCGATAGCGCGGACCAAAAATTTGGTGCTACTGTTCTCATTAATAAGCCGTTTCCATCATGCTCTCAATGGCGTATCTTCTTTACCAAAGGCGACGAGCAATCCTCGATGATGTTATCTAGGGAAAAAAAACTAGCCCGTTCACACTACCCTTCGGTAGAGTTCTAAAGCTTAGACTTGCTAGAACTAGTGGGGAGTATTTCGAACCACCTATAGGATAAAATGGTGGTGGGCCTATCCAATGTGGAAAACGCTTATTTGTCCTACGGTCTGTACGCACGGATTTAATGTTTTGACCC', 'CGATGACGTCTATGCGGGACTCTCCTTTCCGGTTGGGTATTACTATTGGCCGAATGCTCTGGCGAGCGTATAGCAGCCTCGATGGCGCCTGTGAACTTGTAGCGTACAGCATGTCCGGCTCCTCAGTGCGGTTTAAGGTTGCGACATTCCGGCGCACGCGGCCACGATCCGCCTGTCCCCGCGGCAATCAAGAATCGGATTTGAACTGACCTTGTGCATTGCGGCGGCGAGGACTAACTCTTAAGGTGCAGTTGCTCGGGATTGCAGGAACCGATCATGAGAGTGTGAAGTAGTCTTGAATCGCGGTGTCTCGAGCACTATCCGAAG', 'TATAAATACATGATGCTATATGGAAACGGACAAACGACCTATGACTCATTAGGTCGCTATGTTACCTTCCGACTACTTCACTGGTGAGCCGCACCCTTTACCCCTGCTAGAAAATTTTACCGCGGCAGATGGAAGGCAGCATGTTTCTAGGGGAAAATCACCATATGTAGGGTGAGACTGCTTCAGACACCTGCCCAGCGATTGCGGGTGCAGTAACCGTGTAATCCCTTCCGTGCATCCTGGTTTCAGATTGGGTGCAAGAGACCCTTCCAAAGTTTCCTGTATCCGTGTTCCTCATTCTCCGGCGTGCGTGCCGCCAAATGTTTT', 'CTCACTAAGATCCCACTTGAAGTAAGCGTTATAGCACCCACTTGCGCATCGTTCGAACCGGGATCAGCCGCTTTAATAGTTCAATTATTCGCTCCGGGAGTAGTCGTCTGACACCAGCTCCACAATAACCGTTAATTCCCTTAATCCGCTATTTACGTAGTCTGTAGATCCGAGAGTCCTCTTTTACTATTGCAGAAAATCCCAAGAGTGGTCTATGTGACCCCGACGGACCTTTGATTACATAGAAAAATCGACGTCTTAAGCTTCCGTCATAACACTATCCGTCAGTCAGTCACGGTCCTGGTTTCCGGTTTTGGCCGACAATAC', 'ATAAGAGGACAAAGGATGTCTCTCACTATGCAGAGAACTTACGATGAGGTTCACCGGAGGCCTTTACGGCTGGTCCGGTCCCTACCGCTGACTACTGACCGCCTTGGTCACTCGAATAGTTTACTATTGCTACTGCCGGAGACGGAACCTAAATCCGATGGAGGACCATTACAAGGACATATCCGTATGATAGGAGCGACGACGAAGGCGCATGTTATGTGATCTTTCCGGGACAAGCTAGCCACGCTCGAACGACGCCTAGAATTCCACTGACATTCGTCCTAGTCATAATGTGCTTTCGTAACTTAACCACTATGGGCCATTCTA', 'ACCACCGTTAAATTTACTAAAAAGTTCCGCATTACTTACGCTAGAAGCCAAGGTGATTAACCCACGATCTGGAGCGGTACAAGTCCAGAAGCGTAAGTCTGAAGGTCAGACCGGCCACCCGGTGGAAGCTGAAATCATGGTATATAACAGTCCTAAGTGTGGCATAATGCACTTTTCCCCACGGCGGCTCGGCGTGAGTAGTAATCCTCACGTCGCGCGTTTACTACATCGGAGTCACAACCAGAATTACAAGGGGGGAACCTTCAGTGAGGCCACTTCTTGGGGCTGCCTTGATTGGCACATGCTTGCTGATGTCGTCGGCTATTG', 'CCAAGAGCTTAGGGAGGCTGGGAAGGACCTGTCGTCTTAGTAGAGAGCACGCCTGGGTCGTTCCTTACTAAGCCTAGAATCACACTATCGCGGTCATTACTCTGTGGACGGCGTCTTCTTACTACGAACTCTCCCCGACCTTGCCTTATGGTCCCCACATGCGGCCTGTCATCGTTGGGTCCCTCATGCAGCTATGCTTACATTATAGCGCTGCTTCTTTTGCATGATTTGTGTCCTCACAAACTAAGAGTATTCTAATCATAACCACCGCCCACTACGGTCCAGTAAGGTGCCTCAAATTAGTTAATAAATAAGTTCACCGCCTAA', 'ATAGCTATTACTTCGCGTTAACCTGTCGTTTACTATACTTAGAACGAATACAAGTTTGCGTGAGCCGACATTGTTAGGAGCCGCTCCTGCGTACGATGCAATACGAATTAAAACCAAAAAAACCCCAGGCATACCATTCTCAAAAACTTGATGGTGTGTAGAACTAAGTACGGACCTCACCGGTCCGGTCTGGATTGTTGTGCCTATGTCGTCTTCCGGCTTTCCGGCCCTTGCAATTGTAGTTCTGAGGTCACCGCCGCTCAATAAATGTCACGAGGTGAGGCGCTACATTCGTTGAAGCATTACGAGTTTGCCACTTACCAGGAA', 'TAAGTGAACCACTTTTCCCTAGATTGCCCGAGCGCGATGGTGCCAATGCGGAGTGCTAAGCTGAAGAATCGTTTGTCATACCTGGTTATTGCTAGAACGAGCGCCGCAACCGGCCAGGCATCATTTCCTCGCTAGCTAAAGGCGGCAGTTCGACGCGGAATTCCCGTGGATTAATATGCTGTACCATCTATTCATAAATGCTTGGGTGCGTTCGGGGACGGTACCACTATACTTATTACAGAGTCTACTTGATGTCAGTTTTGGTCAGGATCTTAACCCTGCAGGACCTGAGACCACAGATAAAATTGATCTTTGTCAAGCCCGTCT', 'CTGGAAACAGGAGTCTATCAGATTAGAAGAATGGTGTTGTCAAGTCGCACCATTAGGTTGACTCTCCCTCCGTGTTTCTTAGCTTCACTACCTGCTCCAATGACTGTGGCTAGGCTAGGGGCAATGAGACTTCAATACAACTGACACCTCCTTGATACACTTAACCTGTCAGCAATTATCCATTAAAACGTATTACCGGTGCTAGAACGGACCCGTTGCGCAGGCCTCTGCCAGAACTGTTTATGGAAAAGGTAGTGAATTTTGGCCAGCCCAGACCGCCAGGAAAGTTTTCAAGAAATACATCGTGGTAGTATGAGAACCACAATA', 'TTTCTGCTAGGATTTACGCGTTCAAATACGTCCCCGTATTAAATGTCGTGATCCCTTTCAGGACTTACTCCAGCTAGAAGCAGGTCACTTTCAGGTGGTATCACCACTCAGATTGTGGAAGATCGAGCCACGTGGCGCGTACCCTGCTATCTCGTACTTACCACATAGCGATCGTCCGCCGCAGCCCTGAACACAAGCTACATTGTCACCCGGGCTAGGGTATCCACGCGATCCTGTGTCACTCAGGTAGACTCACCCGTACTTCTGGAAAAAGGATAAAGGATCACTTTCCCCGGGTGACACAGCTCTGGTCCGTTAAGTTCACAG', 'CGTACTATTGCTAGCTCGGCGCACACACTACACTTACTTGCGCCTACGCCAAGTGTACGGCGAGAGTCCTGAGCACCTTAACAGTCTGGCGCCGAGAGACACCGGGAGTCCAAGCTGGAGTAACGGGCATGTTCGGGGATCAAGGCGGAGAGCGTACACCTGTGCTAACGCACCATTTCCTGCAACCTACCAGTGGTAGTGGGCGCATGTCTCGGCCGTTCATGGCGTACGCAAACGTACTATTAGTTGCCTACCACATCAATTCAGGATGACTTCCCGCATGTCAGCGCTGATGCGAATACTGGGTGTCACTGTCTCGCCCTTCGT', 'AGGACCTCTGTATACTGGACCCTAGACCACAACCCGTCCATTCTTCCGGCGGCTTAGCAACATGTCGGTAACGCAAATAGCGACGAGGTTACTACATCTAGAACTGCTAGCCGCTTGGTATGAAAATCGGTCCGTTTCCAATTTAAGAAATTTGCGCGGTTACACCATACTCGCCACCTGTAACAGCTTCAATCCACATACGAATTGAATTACACATTAAGCCAGCAGGTAAGTGATGATTACTGGGTTGTCAACAGCTGGGGATCGAAGACGGTACGGTGGTATTGACGGGGGGTAGCTTCATTACGCCTTGTTTACAAATGTCGT', 'TGCTTACTCGAGGCAGTTCCCCGCTTTCTGAACGAGGAGACGCATGTAAGGTAGGCTTAACGGTTTGCGCTCGGTAACCGAACATGTTATTGATCTAGCGTAGTGCTCTAGAAGCGTCCGCTTAAGGTTGCTAGAATCCTTGCACGCTAAGCTGTAAAATCTCGGAAAGCTAGGCACTGACTCCCCGGGAGCGTCCGTAGTCGTATTTACGCCTTAATAGGGTCGCGTTATGCGGCACTGCTGTTTCCTCGGTCGCCGAATCGCGTACCGACGACCGTCTTTCACCGATTCACATGAGGCAAACAGGTAGGGATATGTTTCTTAACT', 'AGCCTTTAATTAGTTATGAAAGGCGAGGTTATCGTTTCTATCCGGCTCCGCTATGTGTGCCCCGGATGTAACCCTTACTATTATCAGAACCTGACGTGATGTCTTTAATCCTACGTGTGTCAATGAGATACTTATGTTGACAAAGAGTAAGGATCATGTTCTAACTGTTCTAAGTGGTGAGCAGGTATAACTACATTCCATGTCATAAGTTTCCAAGTTGGCTTTAATGTGCCAATTATAGTTGTAGAATGACGACTCTCAGCCTGGACATAGCCACCACAACCATCTGATAAAATACAGTCCGACCAATAGAAGTGGAGCGCACCG', 'CGATGCTTCCATACACATTTTAAATAGTTTTGGTTCCTGCCACCTAATTTCTTACTCACTCTATTCGCCCTACGAATTTTAATTGCTAGAAGCGCCGATGTACCAGGCAGCCAGCATACTACCAGTATGCCGACCCGGGTCACAGGTGCAAGCTTTGGCGTTTGTCGCATCGATCCCCGCCTGACCGGGTCGCTAACAATCGGCGCGATTAGTTGGCCGCCGTGAAGTTAGGCAGGCGTTACAGGTGCCACAACCGGAGGGTGAAATAATGCACCTCAGCGCCTGGTCGGGTGGTCCTGCCTTACCATTATTTACTGACTTTCTTTG', 'TGTGCACCTGACTCCTTCAACATCGACTAAGATAGCCCGTGCATTAACATATGCACTCCGACCATTACTATTGCTGACAGTCCTGAAGCGCATAAGTTAGACCGCTTCTCGATGGAGCACAAGGTTATCGTACGTAGACAATATCCAAGCACAAGGCCAAAAAGCAACAAAAGGGCGTCTGTAGACGGGGCGCTAAGAGCATTAGCGCCTCTGTTTCTACGACCAGATCCTGAGGGGGGACGGGTCACTCCTGCTGCAGGACCGTTACGCTTGGTAGGAGGCTGCTTGGTATCAGCCCTTCATAGTGGCAGCTATAGAGAGACCCAA', 'GACTATGCCAAGGTGTGAACTTACTGTCGGCGAGCTATCCCCGAACCACGCAATGATCATAGGCCTGTTGAACTCTTTCCCACGACGTCATCTTGGACTATTGCTAGAGTGGTGACGGATGATCACCGGGCAGTGACCGCACATTTATATAGCGGTGAGCCTTTACGTATCTACCGACGGACTCTATGAACACGACCAAAGAAAGAAATTTCTTACGTGCTGTCAGAACCTCCCGGTTTATTAACTATGTGTGAACCTGCTACTATCGGATGACGCCGACAGGCTGGCTTTGTTTAGCTCTGCATGAAACTCAAAATCAACAGTAGC', 'CCACCATCATTCATACCAGACGCTGCCTGAGTTGCGCTGTTGTGGAATTGCGTAGATCTGCGAGAGCACGGTATACTAGTATTTGAGTTCCAGTTACGCTCAGGTTGCGAAACGTGCGAGTTCCTCCTTAATGCGATTCTACCCGGAACGTGCCTTATGGCTGGGTAGTCTTCTCGAGTGCAATCGCCACGTGTAGGCGTGAGCCACTAGTCTATTGCTAGAATCCGAGGATTCGACCCTGATGACATGGCTCTGGGCGATACTTGTTTTCCCACCCTAATTTTCTTATAGATCAACGTACTGACGGATGTCCGGTAACCCGGTACC']
        , 15, 20, 2000, 20)))