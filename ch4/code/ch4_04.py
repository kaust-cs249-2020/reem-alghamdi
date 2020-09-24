"""
@BY: Reem Alghamdi
@DATE: 24-09-2020
"""


def num_subpeptides(n):
    """
    :param n: length of a cyclic peptide
    :return: number of subpeptides of the peptide
    """
    return n * (n-1)

"""
Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.

    Input: An amino acid string Peptide.
    Output: Cyclospectrum(Peptide).

Code Challenge: Solve the Generating Theoretical Spectrum Problem.
"""
if __name__ == "__main__":
    print(num_subpeptides(26369))