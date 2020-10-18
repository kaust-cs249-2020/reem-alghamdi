"""
@BY: Reem Alghamdi
@DATE: 24-09-2020
"""
from ch4.code.ch4_11 import prefix_max_array


def num_subpeptides(n):
    """
    :param n: length of a cyclic peptide
    :return: number of subpeptides of the peptide
    """
    return n * (n-1)


def cyclic_spectrum(peptide, amino_list=None):
    """
    :param peptide: amino acid string
    :return: the cyclic spectrum of peptide
    """
    prefix_max = prefix_max_array(peptide, amino_list)
    # print(prefix_max)
    peptide_mass = prefix_max[len(peptide)]
    cyclic_spectrums = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclic_spectrums.append(prefix_max[j] - prefix_max[i])
            if i > 0 and j < len(peptide):
                cyclic_spectrums.append(peptide_mass - (prefix_max[j] - prefix_max[i]))
    return sorted(cyclic_spectrums)


if __name__ == "__main__":
    print(num_subpeptides(26369))
    print(*cyclic_spectrum("WPIEMPQCVQWMLH"))