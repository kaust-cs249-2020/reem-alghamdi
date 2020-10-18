"""
@BY: Reem Alghamdi
@DATE: 18-10-2020
"""
from ch1.code.ch1_03 import reverse_compliment
from ch2.code.ch2_03 import motifs
from ch3.code.ch3_08 import k_universal_string_linear
from ch4.code.ch4_02 import dna_to_rna, protein_translation
from ch5.code.ch5_10 import global_alignment, local_alignment
from ch5.code.ch5_11 import fitting_alignment
from ch5.code.ch5_extra import global_alignment_v2, local_alignment_v2, fitting_alignment_v2

if __name__ == "__main__":

    """
    Given the following sequences, compute the profile and its score:
    • ACAA
    • TTTT
    • AAAA
    • GGGG
    """
    matrix = ["ATAG", "CTAG", "ATAG", "ATAG"]
    consensus, score, count, profile, entropy, entropies = motifs(matrix)
    print(score)
    print(profile)

    """
    How many amino acid sequences are encoded by the DNA string
    “CACCACCCC”? List all of them.
    1. CAC CAC CCC = HHP
    2. GGG GUG GUG = GVV
    """
    kmer = "CACCACCCC"
    kmer_translated = protein_translation(dna_to_rna(kmer))
    compliment_translated = protein_translation(dna_to_rna(reverse_compliment(kmer)))
    print(kmer_translated, compliment_translated)
    """
    Find a 5-universal string.
    """
    print(k_universal_string_linear(5))
    """
    Given two sequences ACATTTTTTT and GGTTT, find an optimal global
    alignment, a local alignment, and a fitting alignment. Assume that a
    match scores +2, indels -5, mismatches -2. Provide the alignment and the
    dynamic programming matrix created for each problem.
    """
    v = "ACATTTTTTT"
    w = "GGTTT"
    m = 2
    sigma = 5
    mu = 2
    print(global_alignment(v, w, matches=m, mismatches=mu, sigma=sigma))
    print(global_alignment_v2(v, w, matches=m, mismatches=mu, sigma=sigma))
    print(local_alignment(v, w, matches=m, mismatches=mu, sigma=sigma))
    print(local_alignment_v2(v, w, matches=m, mismatches=mu, sigma=sigma))
    print(fitting_alignment(v, w, matches=m, mismatches=mu, sigma=sigma))
    print(fitting_alignment_v2(v, w, matches=m, mismatches=mu, sigma=sigma))

    """
    Show that the number of ways of intercalating two sequences of lengths
    n and m to give a single sequence of length n + m while preserving the
    order of symbols in both sequences is n+mCm .
    
    A process of intercalating a sequence x 1 , . . . , x n by another sequence
    y 1 , . . . , y m can be described as the filling of a row of n + m empty cells with n + m
    symbols x 1 , . . . , x n , y 1 , . . . , y m (one symbol per cell) while keeping the order of
    symbols in each sequence. Every selection of n cells for symbols x 1 , . . . , x n defines
    only one way to accommodate these symbols which cannot be permutated. As soon
    as x’s are placed, the positions for y 1 , . . . , y m are also determined unambiguously,
    as they fill remaining empty cells without permutations. Hence, the total number
    of distinct intercalated sequences is the same as the number of ways to choose n
    cells out of n + m cells,
    """

    """
    Amino acids D, E, and K are all charged; V, I, and L are hydrophobic.
    What is the average BLOWSUM50 within the charged group of three?
    Within the hydrophobic group? Between the two groups? Suggest a
    reason for the pattern observed.
    
    avg = sum / 9
     hydrophobic             charged              mix
       V   I   L             D   E   K           V   I   L
    V  4   3   1          D  6   2  -1        D -3  -3  -4
    I  3   4   2          E  2   5   1        E -2  -3  -3
    L  1   2   4          K -1   1   5        K -2  -3  -2
     avg = 2.66            avg = 2.22          avg = -2.77
    
    As expected, the scores of substitution between amino acids with similar
    physico-chemical properties (within the charged or the hydrophobic group) are
    higher than the scores of substitution between the amino acids with different prop-
    erties (between the groups). The sequence alignment algorithms maximizing the
    total score will maximize the number of aligned pairs of amino acids with similar
    physico-chemical properties.
    """

    """
    You plan to sequence a single-stranded RNA virus; you expect your virus
    genome to be of a length between 25,000 and 30,000. Your sequencing
    technology will introduce on average one error every 20 bases. Addition-
    ally, you expect your viral genome to contain several repeats not exceeding
    a total length of 500 bases. Suggest an approach of sequencing your virus
    to maximize your chances of correctly assembling the viral genome. Con-
    sider the sequencing approach, length of the k-mers, coverage, and choice
    of assembly algorithm. Justify your answer.
    
    You plan to sequence a single-stranded RNA virus; 
    you expect your virus genome to be of a length between 25,000 and 30,000. 
        ANS: length is large. Brute forcing won't work
    
    Your sequencing technology will introduce on average one error every 20 bases. 
        ANS: Cyclopeptide Sequencing won't work, because it assumes no errors
        
    you expect your viral genome to contain several repeats not exceeding
    a total length of 500 bases. 
        
    
    Suggest an approach of sequencing your virus to maximize your chances of correctly 
    assembling the viral genome. 
    
    Consider the sequencing approach, length of the k-mers, coverage, and choice
    of assembly algorithm. Justify your answer.
    """
