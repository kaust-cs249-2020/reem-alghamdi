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
        for peptide in candidate_peptides[:]:
            if mass(peptide) == parent_mass and peptide not in final_peptides:
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
        for amino_acid in integer_mass_table_18.keys():
            new_peptides.append(peptide + amino_acid)
    return new_peptides


if __name__ == "__main__":
    print(num_subpeptides_linear(16238))
    print(*cyclopeptide_sequencing([int(x) for x in "0 113 128 186 241 299 314 427".split()]))
    print(*cyclopeptide_sequencing([int(x) for x in "0 71 99 103 113 113 115 137 137 147 147 170 186 202 216 250 252 260 260 273 284 284 285 315 323 363 386 388 397 397 397 397 399 422 462 470 500 501 510 512 525 533 534 544 569 583 599 613 638 648 649 657 670 672 681 682 712 720 760 783 785 785 785 785 794 796 819 859 867 897 898 898 909 922 922 930 932 966 980 996 1012 1035 1035 1045 1045 1067 1069 1069 1079 1083 1111 1182".split()]))

