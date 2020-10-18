"""
@BY: Reem Alghamdi
@DATE: 24-09-2020
"""
integer_mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                      'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                      'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                      'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def prefix_max_array(peptide, amino_list=None):
    if amino_list is None:
        amino_list = integer_mass_table
    prefix_max = [0]
    for i, letter in enumerate(peptide):
        prefix_max.append(prefix_max[i] + amino_list[letter])
    # print(prefix_max)
    return prefix_max


def linear_spectrum(peptide, amino_list=None):
    """
    :param peptide: amino acid string
    :return: the linear spectrum of peptide
    """
    prefix_max = prefix_max_array(peptide, amino_list=amino_list)
    linear_spectrums = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linear_spectrums.append(prefix_max[j] - prefix_max[i])
    return sorted(linear_spectrums)


if __name__ == "__main__":
    print(*linear_spectrum("AMILPRLDCKVWWETKWPFETRSKCYIRGWRWGTCMGAHLDLIIY"))
