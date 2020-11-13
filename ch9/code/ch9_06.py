"""
@BY: Reem Alghamdi
@DATE: 13-11-2020
"""


def suffix_array(text):
    d = {}
    for i in range(len(text)):
        d[text[i:]] = i
    arr = [v for k, v in sorted(d.items(), key=lambda x: x[0])]
    return arr


if __name__ == "__main__":
    string = "panamabananas$"
    # string = "AACGATAGCGGTAGA$"
    # string = "ATTTATCGGATAACCTCTTATCGTAAAATAGCGAAAGAATGAGGAGATCGTGCCACGTGTCCAGCACATATAGAATCGATTTCCTATTTCCTTTCCTGACAAACCCCGGCGAAAGTGTTAGCACGTAATAAACGGAATAGCCTTCGGCGATCTCGCAAGGGTGGTACACCGCTCTAACCCCATGACCAAGGTTTTCAGTTAATTCCCCTGTTCGGGTGTCGAGTTAATCATCTTTACCCGATATATAGCATGGTCTTCGCGTTCCACGGGAAACGTTTTAGAAGTCTCGTGAATATGTTAAAGGTGCCGCCTTAAAGCGGAATTTCGTCCAGAAGTTGCAAACTTTGTCACGCGCAGCTTTATACCAGACTGAGTCAGGCTTGCTTTGATTAATCGAGCCAGCCTAGATCCCGATCAAAATGCAAGCTTAAGACCAGTCAGAGGGCGGAATGTTGGTACTGTATTCATCTGTGTTAAGTCTCTCGGTAGCACGGCCAAGGGACAGGCTCCCTGGGGGGCGCTTCGATCGGGGCTAGCCAAAAGCTCATGTCCTGTGCTCAGGTAGCGAATGGAGGTTCCTTGCTTCAAGGAGACGGAGAAGCTATTGTGTGATGGTCTCATTACGTCACCGAAGGACGTGAGGGTAGATCTTGTACATCTGTGACGAGAGCATGTTCCATCATGCTTCCCCTAGGGGTACAGCCCACTTTTGACGCTAACCTCCCATGACAGCGCTACGCAGCTTAATCATTTAACGGTCATCTGAGTTGGACTCCAGCAGGGAGTTCGCAGCGCCGTCATTGGTGATAGGTGCCATTTTTGTGTATCGACTCGTGTGTTTCATACTTATAAACATCAAACATCTTCTAGACATTGAATACGCGAGCCTGGTGTTAAAAATCGGAGCTACGTTTAATT$"
    print(', '.join(map(str, suffix_array(string))))
