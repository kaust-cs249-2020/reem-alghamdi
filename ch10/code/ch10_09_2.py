"""
@BY: Reem Alghamdi
@DATE: 25-11-2020
"""
from ch10.code.ch10_09 import profile_hmm_pseudocount
import numpy as np


def sequence_alignment_with_profile_hmm(x, threshold, pseudocount, alphabet, alignments):
    states, paths, transition, transition_square_pair, emission, emission_square_pair = profile_hmm_pseudocount(threshold, pseudocount, alphabet, alignments)
    states.remove("S")
    states.remove("E")

    len_col = len(x)
    len_row = int((len(states) - 1) / 3)

    s_d = np.zeros((len_row, len_col), dtype=float)
    s_i = np.zeros((len_row, len_col), dtype=float)
    s_m = np.zeros((len_row, len_col), dtype=float)

    b_d = np.empty((len_row, len_col), dtype=tuple)
    b_i = np.empty((len_row, len_col), dtype=tuple)
    b_m = np.empty((len_row, len_col), dtype=tuple)

    
if __name__ == "__main__":
        al = """ACDEFACADF
AFDA---CCF
A--EFD-FDC
ACAEF--A-C
ADDEFAAADF"""
        sequence_alignment_with_profile_hmm("AEFDFDC", 0.4, 0.01, "A B C D E F".split(), al.split())
