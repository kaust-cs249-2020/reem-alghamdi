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
    # sum of series from 1 to k+1 + the empty string
    return int(n * (n+1) / 2 + 1)


def peptide_to_masses(peptide, amino_list=None):
    if not amino_list:
        amino_list = integer_mass_table
    """
    given a peptide string, return equivalent masses separated by -
    """
    num = []
    for amino in peptide:

        num.append(str(amino_list[amino]))
    return '-'.join(num)


def mass(peptide, amino_list=None):
    m = 0
    for amino_acid in peptide:
        m += integer_mass_table[amino_acid] if not amino_list else amino_list[amino_acid]
    return m


def cyclopeptide_sequencing(spectrum, amino_list=None):
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
                    final_peptides_masses.append(peptide_to_masses(peptide, amino_list))
                candidate_peptides.remove(peptide)
            elif not all(a in spectrum for a in linear_spectrum(peptide)):
                candidate_peptides.remove(peptide)
    return final_peptides_masses


def expand(peptides, amino_list=None):
    new_peptides = []
    for peptide in peptides:
        for amino_acid, mass in integer_mass_table_18.items() if not amino_list else amino_list.items():
            new_peptides.append(peptide + amino_acid)
    return new_peptides


if __name__ == "__main__":
    # print(num_subpeptides_linear(16238))
    # print(*cyclopeptide_sequencing([int(x) for x in "0 113 128 186 241 299 314 427".split()]))
    print(*cyclopeptide_sequencing([int(x) for x in "0 97 103 114 114 128 137 156 156 156 163 186 234 242 242 253 259 259 277 300 312 319 323 356 390 405 409 415 415 420 422 428 433 437 512 519 534 536 542 546 561 565 571 576 578 649 662 664 668 675 679 690 692 705 732 734 776 778 805 818 820 831 835 842 846 848 861 932 934 939 945 949 964 968 974 976 991 998 1073 1077 1082 1088 1090 1095 1095 1101 1105 1120 1154 1187 1191 1198 1210 1233 1251 1251 1257 1268 1268 1276 1324 1347 1354 1354 1354 1373 1382 1396 1396 1407 1413 1510".split()]))
    # print(*cyclopeptide_sequencing([int(x) for x in "0 71 99 103 113 113 115 137 137 147 147 170 186 202 216 250 252 260 260 273 284 284 285 315 323 363 386 388 397 397 397 397 399 422 462 470 500 501 510 512 525 533 534 544 569 583 599 613 638 648 649 657 670 672 681 682 712 720 760 783 785 785 785 785 794 796 819 859 867 897 898 898 909 922 922 930 932 966 980 996 1012 1035 1035 1045 1045 1067 1069 1069 1079 1083 1111 1182".split()]))

