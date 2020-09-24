"""
@BY: Reem Alghamdi
@DATE: 24-09-2020
"""
integer_mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


def prefix_max_array(peptide):
    prefix_max = [0]
    for i, letter in enumerate(peptide):
        prefix_max.append(prefix_max[i] + integer_mass_table[letter])
    return prefix_max


def linear_spectrum(peptide):
    """
    :param peptide: amino acid string
    :return: the linear spectrum of peptide
    """
    prefix_max = prefix_max_array(peptide)
    linear_spectrums = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            linear_spectrums.append(prefix_max[j] - prefix_max[i])
    return sorted(linear_spectrums)


def cyclic_spectrum(peptide):
    """
    :param peptide: amino acid string
    :return: the cyclic spectrum of peptide
    """
    prefix_max = prefix_max_array(peptide)
    peptide_mass = prefix_max[len(peptide)]
    cyclic_spectrums = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            cyclic_spectrums.append(prefix_max[j] - prefix_max[i])
            if i > 0 and j < len(peptide):
                cyclic_spectrums.append(peptide_mass - (prefix_max[j] - prefix_max[i]))
    return sorted(cyclic_spectrums)


if __name__ == "__main__":
    print(*linear_spectrum("AMILPRLDCKVWWETKWPFETRSKCYIRGWRWGTCMGAHLDLIIY"))