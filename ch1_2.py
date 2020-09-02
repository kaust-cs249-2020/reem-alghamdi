"""
@BY: Reem Alghamdi
@DATE: 01-09-2020
"""


def pattern_count(text, pattern):
    """
    This function takes a pattern and count how many times it appeared inside a bigger string
    :param text: the full string
    :param pattern: the pattern to count in string
    :return: number of occurrence of pattern in string
    """
    count = 0
    for index in range(len(text) - len(pattern) + 1):
        kmer = text[index: index + len(pattern)]
        if kmer == pattern:
            count = count + 1
    print("{} is the number of times {} showed in {}".format(count, pattern, text))
    return count


def frequency_table(text, k):
    """
    This function takes a text and the length of the k-mers. Then construct a dictionary of ALL k-mers along their occurrences

    :param text: the full string
    :param k: the length of each substring needed to build k-mers
    :return: a dictionary where the keys are the k-mers and the value how many times they appeared
    """

    table = {}
    for index in range(len(text) - k + 1):
        kmer = text[index: index + k]
        if table.get(kmer):
            table[kmer] = table[kmer] + 1
        else:
            table[kmer] = 1
    return table


def max_map(dictionary):
    """
    This function takes a dictionary of keys and positive values, then return the max value
    :param dictionary: the dictionary. ex: frequency table
    :return: the max value
    """
    _max = 0
    for key, value in dictionary.items():
        if value > _max:
            _max = value
    return _max


def better_frequent_words(text, k):
    """
    This function takes a string and a pattern length, and return the patterns with highest occurrence
    :param text: the text
    :param k: the k-mer length
    :return: list of k-mers of most occurrence
    """
    frequent_pattern = []
    freq_map = frequency_table(text, k)
    _max = max_map(freq_map)
    for pattern, freq in freq_map.items():
        if freq == _max:
            frequent_pattern.append(pattern)
            print(pattern, end=' ')
    return frequent_pattern


if __name__ == "__main__":
    pattern_count("TTATGTGCTACGTGTGCTATGTGCTATGTGCTAGGCCCGGCTGTGCTACATGTGCTATGTGCTATTTTAGAGTGTGCTAATGTGCTACTGTGCTACCGTGTGCTACTGTGCTATGTGCTAACGACAGTGTGCTAATGATGTGCTATGTGCTATTTCCAGTGTGCTAGTGTGCTACGTCTGTGCTATGTGCTATGTGCTATGTGCTATGTCGTGTGCTATGTGCTAATGTGCTACGCTAGGTTGTGCTAGTCTGTGCTAAGTCTTTGTGCTACGTAGATGTGCTACTGAACCGTATGTGCTACTGTGCTACGTATGTGCTAAGCGTGTGCTACATGTGCTAATGTGCTATGTGCTAGTCGTTGTGCTATTCTGTGCTATGTGCTATGTGCTAGTGTGCTAGTGTGCTATGTGCTACTTGTGCTATTGTGCTAGGGTTTGTGCTAATTGTCGATGTGCTAGTGTGCTAATGTGCTAATGTGCTATGTGCTATGTGCTACTGTGCTAATGTGCTATGTGGCAATTGTGCTATGTGCTAGCATGTGCTATCGAGCTCATGTGCTAACCGGATTGTGCTATGTGCTAATATGTGCTAAGATGCTGTGCTATGTGTGCTATGTGCTAGCCAGGGGTGTGCTATTGTGCTAGTGATCTGCTGTCATGTGCTAGGTTGTGCTACGATGTGCTAAACTCGTGTGCTAACTTGTGCTATTGTGCTATGTGCTACGTGTGCTAGATGTGCTAAAGCAAGTGTGCTATGTGCTATTGTGCTATTTCTGCCGTGTGCTATGCTGCATGTGCTATGTGCTAATGTGCTACAGTGTGCTATTGTGCTAGTGTGCTATGTGCTATGTGCTATGTGCTAAATGTGCTATGTGCTAGAATGTGCTATGTGCTATGTGCTAAACACCTGTGCTATGTGCTATTGTGCTAAATCTAGCCTGTGCTATTATTATGTGCTAACTGTGCTAAGGTGG", "TGTGCTATG")
    better_frequent_words("ACGAGGAGAAAAAAGCCCTCACAAGTAAACGAGGAGAATATGTTTAACCTGACCTTTCTGACCTTTTATGTTTAACCTGACCTTTCTGACCTTTCTGACCTTTACAAGTAATATGTTTAACACAAGTAAACGAGGAGAAAAAAGCCCTCCTGACCTTTAAAAGCCCTCTATGTTTAACAAAAGCCCTCTATGTTTAACAAAAGCCCTCTATGTTTAACTATGTTTAACACAAGTAAAAAAGCCCTCACAAGTAACTGACCTTTCTGACCTTTTATGTTTAACACAAGTAAAAAAGCCCTCACGAGGAGAACTGACCTTTACGAGGAGAACTGACCTTTACGAGGAGAATATGTTTAACAAAAGCCCTCCTGACCTTTACAAGTAAACGAGGAGAAAAAAGCCCTCAAAAGCCCTCACGAGGAGAAACGAGGAGAAACGAGGAGAAACAAGTAAACGAGGAGAAAAAAGCCCTCTATGTTTAACCTGACCTTTACGAGGAGAACTGACCTTTTATGTTTAACTATGTTTAACCTGACCTTTCTGACCTTTCTGACCTTTAAAAGCCCTCACGAGGAGAAAAAAGCCCTCCTGACCTTTACAAGTAACTGACCTTTCTGACCTTTACGAGGAGAACTGACCTTTACGAGGAGAAACAAGTAAACAAGTAATATGTTTAACAAAAGCCCTCCTGACCTTTCTGACCTTTACAAGTAAACAAGTAACTGACCTTTTATGTTTAACTATGTTTAACACGAGGAGAAAAAAGCCCTCAAAAGCCCTCCTGACCTTTACAAGTAACTGACCTTTACAAGTAACTGACCTTTTATGTTTAACCTGACCTTTACGAGGAGAACTGACCTTTCTGACCTTTCTGACCTTTACAAGTAAACGAGGAGAA", 12)
