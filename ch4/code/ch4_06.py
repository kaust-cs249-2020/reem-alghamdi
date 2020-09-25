"""
@BY: Reem Alghamdi
@DATE: 25-09-2020
"""
from ch4.code.ch4_04 import cyclic_spectrum
from ch4.code.ch4_11 import integer_mass_table, linear_spectrum

integer_mass_table_18 = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                      'T': 101, 'C': 103, 'I': 113, 'N': 114,
                      'D': 115, 'K': 128, 'E': 129, 'M': 131,
                      'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def num_subpeptides_linear(n):
    """
    :param n: length of a linear peptide
    :return: number of subpeptides of the peptide
    """
    # sum of series from 1 to k + the empty string
    return int(n * (n+1) / 2 + 1)


def mass(peptide):
    m = 0
    for amino_acid in peptide:
        m += integer_mass_table[amino_acid]
    return m


def cyclopeptide_sequencing(spectrum):
    """
    :param spectrum: spectrum (list of int)
    :return: list of integers (amino acids)
    """
    parent_mass = max(spectrum)
    candidate_peptides = [""]
    final_peptides = []
    final_peptides_masses = []
    while len(candidate_peptides) > 0:
        candidate_peptides = expand(candidate_peptides)
        if len(cyclic_spectrum(candidate_peptides[0])) > len(spectrum):
            break
        for peptide in candidate_peptides:
            if mass(peptide) == parent_mass and peptide not in final_peptides:
                print(peptide, mass(peptide))
                if cyclic_spectrum(peptide) == spectrum:
                    final_peptides.append(peptide)
                    num = []
                    for amino in peptide:
                        num.append(str(integer_mass_table[amino]))
                    final_peptides_masses.append('-'.join(num))
                candidate_peptides.remove(peptide)
            elif not all(a in spectrum for a in linear_spectrum(peptide)):
                candidate_peptides.remove(peptide)
    return final_peptides_masses


def expand(peptides):
    new_peptides = []
    for peptide in peptides:
        for amino_acid in integer_mass_table_18:
            new_peptides.append(peptide + amino_acid)
    return new_peptides


if __name__ == "__main__":
    print(num_subpeptides_linear(16238))
    print(*cyclopeptide_sequencing([int(x) for x in "0 113 128 186 241 299 314 427".split()]))
    # print(*cyclopeptide_sequencing([int(x) for x in "0 97 113 113 114 128 137 156 156 186 211 227 250 253 265 269 269 314 324 342 366 367 378 383 406 451 455 470 480 480 480 503 534 564 569 583 593 607 617 631 636 666 697 720 720 720 730 745 749 794 817 822 833 834 858 876 886 931 931 935 947 950 973 989 1014 1044 1044 1063 1072 1086 1087 1087 1103 1200".split()]))

