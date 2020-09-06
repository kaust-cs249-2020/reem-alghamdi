"""
@BY: Reem Alghamdi
@DATE: 01-09-2020
"""


def reverse_compliment(pattern):
    """
    This function takes a genome of letters A, T, C, G and find its reverse compliment:
    basically exchange A and T, C and G then reverse the result
    :param pattern: the string
    :return: the reverse compliment
    """
    pattern = pattern.replace("A", "t")\
        .replace("G", "c")\
        .replace("C", "G")\
        .replace("T", "A")\
        .upper()[::-1]
    return pattern


def pattern_matching_positions(text, pattern):
    """
    This function takes a string and a pattern, then return an integer array of the indexes where the pattern starts
    :param text: the string
    :param pattern: the pattern to match
    :return: an array of the start positions in which this pattern appeared
    """
    positions = []
    for index in range(len(text) - len(pattern) + 1):
        substring = text[index: index + len(pattern)]
        if substring == pattern:
            positions.append(index)
    return positions


if __name__ == "__main__":
    print(reverse_compliment("TCCCTGCTGAACTCTGGGCCCGCGCTGGAGCATGTGCTAGGGGTCCGATAAGGACGCACAAGCTTGGAAGAAACTTTGAAAAAATCAATGGCAAATGACATCGTCGTGGAGCTGCCGGACCTATTTCCACTGCCTGTTGAGCACCTACCGAAAAGAACGGCCTCGAATCGCGACCTCCTCGCGCATAAACTGCCCGCGGGGGTAGTTAGGAAGATGGGACGCTACCGTGCAGACCTTTTTCTAGGTTACCAGTGGTAATAGCAGGTTGCACGATTTACAACATGGTCTGAACAGATTGAACACACGCCGGCACATATGGAGACTTAAATTTGGGACACCCCCCAGAGCCCGAATATCCCTCTAAAAAGGTTCTACCGGGGCGACAAGTGAGATTTTTCCTTGGCATGACGAACACGTCCGTGGAGACACCACTTCATTGTTTCAGACTCGGCTAGTGCTACCAAAAGAGAAGTGCATCAGCAAACGCTGGTATCCCGTTCATTACCCGTTGACCCCATGTTAGATCGACGTCAATCTGAGCGCATTGCGTAGAATCCGTCCTAAAAATCGGAATACGCGATCTGCTCTCCGAAATAGTGGGCTATCTAGTTATGACTTTGGAACCTTTGAGTCTTTTCCCCTTGGCGCGACTGCAAGGGTTGTCCTATTAGGGTATAAGAACAAGATTAAACAGCGATCCTGACTCAGTTCGGTTTGAACCCGCGATAGGTCTAAGAGCTATCAGGGACGCTGTATCAGAGGCATAGTCTCCGCGTGGTCTTGTCTTACGCGCTGAGTCCCAGGAGAGTCAAGCCGCCACCGCCCTACAAGAAGCTGAACTAGAACGGTGGCGTCAATATAAGTGGTTGTATGACCGAAATCGAATCGGATCTAGACGATAGTCTATTGACGATGAGGATCGCTCGAGCATACCATACGCTAGACCAGAGTGAGCTGGGGGTGAATGAACATACTCGCGGAGTGATAGCATTTCTAGAGGAACTGCGCAGGATTAAGGATTTTGAGGGTTCGCGTTACCCTTCTGTGGAGTAACACCCAATTGGGGTCTCGAGAGACCCTCTTCTGAGCCGTCGAGCAGGACAGACAGGGTATGCGATATCAATAGACATCTGATCCGCGACATGGGAGGGCTGTATACGTAGCCGAGCACTCATCGTCTCGACTCTCTTCGATATGAGTCTCGTAGGCGTATGCCGTTCGGTGTCATGAAATGTTTACGGCAACGGTACTGAACTCCTTAGTGTGCACCGCCGTCCTTAAAGCCGAACACAACATACCTTTTACACGCAATGTTACCATGTTCCGCGGCGACGACTGTAAGGGAATTCTCGCGGATATACAGGCAGTGATTCCGCCGGTGAAGGGTTGGATGTTTCTACTAGTCGTCCAATGTTTCCAACGGGAAACCTCGAGTTCTGGTAGGAAGCCTCCGGGACAATCATGTAAGAATAAGAGTCTTATGCGTTACTGTTAGAGCCCCCGGTATTCCGAATACATACAGACAGGATGTGAAACAGTCGCCAAATCCGAATCCTTAAACTGCCATTGGCCTAAATGGACGAGTCGCTCAATGCATCACGTGGAACGGGGAAGCAGTTCCCCGCTTCTGTGCCGATACAGGCTGACGTCAACGCCAGTGTCAGAGGATACCTCTTTAGAGAACAAGAAGTGCAAGGATGTGCAGCCTAGCCTACTGCACAAGGTCAGTGGGACCGGTGCTTTAAATCCAGAGCCTAGTAACCGAAGATAACTCCTGTGCTGGTAAACGAGCGAATGGTGAAGCATACTATAACCATGAACTAACAAATTTACGCATGCTCTGGACGCAAGAACGTTGTGCGAGAAGTACCTGCGCTAGCATGCGTCGGTGCAGACGCGCCTAAATAATCGGGTCTATGCCAAAGAAACTTTAACGTACAGCTTGAAGGATGCTGGTTGGTTATCGACTTTGACACTACTGTATGATCCTGCGGGGCATATACTCTGCGACCGGATGACGCTAATGAGTCTGGGAGCGGTTGTCAGCGACTTATTTGTGATAGGGCATCTATACGATTGATCCGAGACAGAATAGCGCCTGTTTAAGAGGTTCCCCCGCCGGTAGATTAATTGCAAACGCACTACTATCTGTAGCAAGCGGCGACATTAGTAACGTTATGGTCGTCAGAGTAACCATCTTCTGTAGGCTGTCTTGATATTCGTGCAGAAGCGTCTAGGTCAACCACTATCAAGTTGCACGAGGAGTCGGTTGTTGTCTACTTGATAGAGGTTTGGCGGACTTTCTAGTGGCTTGCAATGCGCCCGTGAAAAAACCGTGCATTTCGCTCGCGAGAATCATTGAGACTGAGATCAGATACCGAGCCGCGGTCTATCGAAATGCACGCTGGAAGATTGCTGGTCGTCATGCACAGGGTCGGTAACTCCACGCGTGCGGTGGACTTGAAATGCAATCCGGTACTCAACCGAAAATGGTATGTGTGCAACGGTGGACAACAGGTCGTTCCCCACTATAGAACCTTCCCAGTATAAACTCGCGAATCATTGAACCGACTCTTGGCGTATAGGCTTTGTAAAGCCGATGTTGAGCGTATGACTCCTTAAGTTTGAAGCCAGAGGTCAACCTTGATTATCATGACCCTCCGATAAGTCCCTAACATGAATCCCGGTAGCAAGACGTCAGCGCCGGGACAGGCACCTAACCTCATTTCAGAAGACACTCGCGCTACGTCATCACAGTCGTTACCCATAGAGAGAGCTTAGTTATGATTAAAAAACGAAACTATGACGAAGTGAAGCTATCGGGTTCGTCCTTGAGTATAGGGATGGTGGCTTTTGGAGATCCTGTACGTTCCATCGCTCTCTGCTATCAGCGGCGTCGTAAAAACCGTGCTGTCAGTAAGAAGCGGCCAGGTCGAGACGAAGCGAAAGCACCCAGGGAATAGTAAATGACACCGACAATAATCAATGGATCTACTCACCCACGGTCGAAGAGCGCTGCCTGCTAAACAGGTTCAGTCGTCACTGAAAGAGCCAGTTTTACGTCCATTGGCTCTTTTTGACAAGTGCGTGTTACCGCTGATACTTCTTAGAAACTCGATAAAAAGCGAGGGGCTGGTCTACTTTGGAGCGAGCCTTTTCCTTATGATCGGACGCCTGTAATCAACATGTCGGCTAGGGCCAATACCCGCGCATGCGTGCGGGTACGAGAAATGGCTGGATCACTACTCCACGGTGCTGCGGATCCAGTGCTGCGCCTCATCATCACAACATATTCCATCGAGGTTTGACAGATAAGTCTCTGTACGCCCCAAGAACCAGGGCGGGTGTGCGGCTATCTGACTCGAGCAGGCTCAGCTAAGGTCCAGCCAGCAAAGAACCGTTTAGCATATTCCCTCGCATCGATGCCAAATCTATATTGGAATCTTGGACTCGAAATGTTATGCGAAGTGGAACGACTTACCAAGAAATCTTGAGACCTATATACGACATATACCGGTATCGAAAAACCCATGGACGAGGCCCACTACGGACAGTCTGAGCGACGATGCCGTAACACGGTAGGTCTCTCTGTTCACGAGGGATTGCGGGGTTAGGTATTTATCTGAGGGCTAGGACCTTACCGAAGGAAGTGTGAAATGTCACTACGGGGGTCAGGAGAAAATTGCAGGGTAAGAATCGGCTACAGTTGGGTGACTGCACAATAGGATAGCCTAAAGCATAAACACCTGAGATATCGGGCAGCGGAAGGTGCGCCTTAAGTGCTGCCTAACGCGTCCATGAGATCACTCCTCGTGACATCTTCATATGCCAACCCATATATGCTCAGGGGCGGCCGGGCTATCCCTAGAACCATAGGCAGCTAGCCGTAGGGAAGTACAGGGCCATGGTTACTGGGACGGCGACCTAGAATCTTTTTCGTCCATGTGTGTATATCCCTGGGTACCCGTGTCATCGATTCACGAAACCCGTCGCGGCGCCCGGCCTTTCCGCTGCCAGCTGTAAACATGGTGGGGGGTCTTATTCCCCAGAAAATTTACCGCCACGCGCGCAGGAGGTGTGTGAGGGCCGGGTTATAGGTCCTCTAGGACTTCCTTTAAACTATATCAGAAATGTATAGAGTATACAGATAAGATGGACGAATCAACTCAAGCCCCAACAGGCAACCGGGATTACAGGGACTGGTTTTTAACCTCTCTCCGTAAGCACTAAGAGCTCCACTTGTTTGAGAATGTCAAACCTACGTCTAGGTGAGATCTAGTCCCTTGAGTTAAGAGTGTGGCCATCTTTCATCCTTCCGTCTAGGCGAGGTAGGACGCGGGTTCTGTGCGGCCCCATAGCGGAGTTTCCCTTGTAGTCCGGATTTCTCCTAGTCACAAGTGAGCCCGGAAGGTCGTGTTAACTTCTAATTTTGTAAATGACTGTTCAAAGTAAGGTGCAAACGTCCACTCCCGGAGCTTCCATTGCATTATCGAGATTCAATTTTATAGCCTGTCGTTTACCGCTAACGACCCCCGGAGGATGACTACCAGATAGCGAAGGTGCATAAGTCCATGGAGCGTGTTCACGTAGTCAGAAGACCATGATACTTCCCATAGGTGGTTGCCTTAGCACTTGCCGACTTTAGGGTCAACCGCTAAACCCGAACAGCTCTTCATCCACCAGACGCCACAGTCGTCGGTATACGCTCAGTGGAAGATGGTGGTAACTTTATGACAGTGATCTTGTGTAATGGGTTGTCGTGACCCAACCGATTGCCTCGGTTGGTTATACAGGTTACGGCGAAAGGTCCTAGCGGATCTATATGCTCAAGGGTCTTGCAAGCGGAACCGGGGCCGACGCCGATGAATTGTCTTCGTTCGATGCCAGATTCCCCAATGTTTCCACATCGACACATTGTCAAGTCCGGCCTGGTCCTGTCTTGGAAGCGAATCTCCAAGGTTCATTTCTTTCATTTGTCCCTTTGCCGTTGCGGGGAGCATCTCTTGTGTCACGACCTATTGCCAAGTGAACGTGGAAGGCCGATGGTTGAACCCTGCTCTATATGAAGAAAAAGCAGACATGCGGGGGAATGTAGCGCTCGAATGGCCACAAGCACGAGCCACAGGCTAAACCAGTGCAGCGAAGCAAGAGTATGGAAAGTGATGGACTATTGTGTGGCTTATTAGACGTCTAATATGGGGAATGAGTCCGGGGCACCAATTTGACCGAGATCACGACACTATTCCCAAAAGTGAGGGTCTCTTTTCTGGGCACCGGTGAGCTTAAGTGCGACTGGTATGCCGGTCGTTGCCCCCTGTTAAATTATAGGCTAGAGTTTAAGTAGGAACGTAAACACAAATACATAAAAGGTCACCAGTGTAGAATCAACAGAGGGTTTATTGTGGCGCGCACCAACGTTCTTCTACACTCACGACTTATCGTTTCGCCAGATTTAGCAGATCCTCTATCACGCGGAGCGACTAGTTCGAACGAGTATCTATCTGTCCAACAGCGGTAATTAAAGATTATACTACGACGATCCTGTAGACATCCGACGAGTAGCTCAACGCGCGTTATTAATCTACGCTTTCGAGTCAATCACTTTGGTGAATGGTATATGCCCAACGGGACCTACAGCGAAAATCAATTGGCAGCGTAGGGGCTCAACAACTGAGTTATCGGTCGTAGTGAAGATTATCGTACTGGGGCGGTCTAGTCCATACGACCTATACTGGCTAGAGTAACTGCAGTCTGACTGGACATGTCGACCTCGCCATGCCGAAATCGCCTACAAGCTATCCAAAAACTTCAGGACGAACCTCGCGGCCGCAGATGACTCATCGGGTAGCGTATTGAGGATTGTTCATGAAGAGTCCCATAGATCAATTAGACACATATTGCACCTGGCGGTCCCTCATCCTTTACGCCTCAGATACAGGGCGCTTCTCCCACCGGTTGAGAGCGGTGAACGATCTACCGTATTAGCCTCTTTACAAAATGCAGTAATGCGCATGCCCGCCTAGCAGACGAACGTGCCACATACTAGAACTTTTTCTCCTTCCTCCTCAGTAATTATGATTGAGTTTCACATGGTCGTCGTTCCACTGGGCTCCACCTATTGACTCACTAGGAATGCCGGAGGGACCAATGATTAGAGTGTGCGCACCGTGTTCCTAGGGGTATAAATTCGGGTCTCTGTGCAACTTCTCCGTATTAAATCCTGGAATTACCGTTCGAGCTGCGCATTAGGCGTACATGTCTGTTTCATATGCCCTAACGGCGATGGATTTCGACACCGGGCTAACTAAAGCCACTTGGGATATCACCCTCGGTCTTTTGTATGCGCCCCCTGTCTCCGAGAGCATCTTCTTGCTTTGCAATCACTTCAGTTGGAGAAAGGGTTTAACCGGATAATGTTATTTTAGCTGGATTGAATCAATGAGCTGCGGTACGGAAGTTCAATCAGGCAACGATACTCACTTGAACGCCGCTAAGGCAGGAAGCGGCACTGGGCCGCGATAAAAACCATGGACAGAGTCACTAAACCACTGGCAATCCGTTAAAATGAAGGAACGTACCTGGTACATATCAGTCAAGGTGGATATAACCAAGACTAAGGTTCGGAACGCGAAAAACAGCGGGATCCGTATGTTTCTATTTGGTGCTAGAAGGTTGTTACCTTGAGGTTAATAGGATGATGCCAGACGGTCAGCTGTCCTCGGTTTGATGTCTTCTTCCTGTAGCAGGACTAACAATAGGATCCAGGTCCAGGCCATTCTGAGGCGATAACAAAGCGCTGTTGCCATAGCGTGCTGAAGCTTTCTCTACTTGACTCGTACGATGCTTAGTCATCCCTTTGTTGACAGCCAACCTTTGCTAGTCCTTTCGAGTGCGGTTATACAAAGGTGAGCGAGCGCCTGCCCAGCCAGTAACTTCAGGTTCGCCTATAGCAACTATCGATTAAATAGTTCATCCCGACTGCACGATCTGCACTTGATCACGGGCTTTTCAATCCACATAGCCGATAGACGCTGGGGATTGGAGTCATGAAGGTACGACCTGATCTCGCTTACCGCGGCAGCCCACCAGGAAAGATGAATAATTTTTTCATACGATCTTATCCTTCGGTTCAATCGGGAGTGTAGAGTGGGAGGTAGGATCATTTCTGTTCCCTGTCTGATCTGGTATGATTTTGCCTTGAGGTTGTTTGGTTGACCTAAATTTGCACGCGTCATCGCGAGATACGCTGAACCACATTACAGAAAGTGGGCTCCGGCGAGTATGTCTCACTCGTGGGCCTGTAATTGCATCATTAATTGGGCTAAACGGCTGATGACCTGATCGAGCACTAGCCCAATGGTTCGATGGGAATGGTCCCACTGGGATTTGACGCCCCTGAGAATTCATCCCGTACACAAGGGTTTATCTGAGTGCTCACGTCCCTCTACCTATCCCGCGGCCCCATCTGATAATCACACGTTTATTGTTGGTCGATACGCAATGTAGACCCACACGTATCCGTTAGACCCTCCCAACCCTGATTCACTCCGAAAGGCAACACTCGAGGGCGCCGACACGACCGTGAGAGAACGATGAAGGATCGATGTCATTTTTTCTTAAAGTTATGATGTTCGGATAGACTTGACGGTATAAGCTTACAGAGGTGGAACGGATATGCGAATATTTGCTCGCGTAGTACGTCCGATGTGAAATAATGGATATGTAGATTTGTTCGAATTCACATCGTAGAAATATTAGTCACATGATCCATTTATTTTACGGGCTCAAGTTTTACGGGTTTAGTCATCGCGAAGGCATCCGCAAATGTGCATGTGGGACCCCAATAATGGTATAATTGCACGCAGCACATTTGACATACCGGAAGTAGTGGAGTGGTGAGCTAGGACTCACTAGCCCGCGGTTGGAAACCTTCGTCAAAGTGCCTCTTGTCAGATCTGCGGTAGAACATCACATGTACATGCGATTCTGTGCTCTCAGTTGTGTTTTCTAGAGAGACTTCTAATTGAAGGCCAGAAATCGGTGATGATGCTGATCATCTTCCGTCAGCTACCTCGCCAAGTCGAGGTACTAGTAAAGCTTCCCTATGTTGGAAACGCTGTTAGCATTGGGTACCATAACCCATTATAGAAGGTAGGCATGGTGTTGCCATGCCTAAATTGTCCAATATGTCATTTGGCGGATGTAATGTGCTACCGTGACTGATGTTCATACCTCTAAGTTTAGGCTATCATACCAAACAACCTCTTGTACAGACTTCTCGTCACTTGTATGCGCTTCGCGATAAAACAGAACGGTTCGCCACATTGGCATGGAAACGGACTTGGTCAATGTTTGTTCTTACTGCGTAACAACTACCTGAATACAAGCTGCTTCGTGATCTCCCATTCTCCGCAAGGATGCCATCTGAAACCACCAGCCTCGTACGGTTTCCTGGGGGCACGGATCGAAAGAGCACTGGCCTACACCAGCCATCGAGCTTATAGTACACAGCGTAGCCTCACGCTAACGTGAACCTGTTGAAGATTGCTTTTTAATGAACTAGAGATACTTCTGAAACAGCCTCCTGCACCCTCGTGAAGTGAAAACCCAGCTGGAGTTGTCCGCGTGTCCGCTTCTGAAACGCAGTGGTACGAGACGTCGATTGACTCGTGGGAGGTGGTGCAAATAGGTTTCGTTGCCGAGCTCCGTCCAGCGCGACAGCCATTCTGCAACAGAAAATCTACTACGTTACAACAGTCTGCAGCATGACCCACGCACCTGGCGTGTAAAATTAAACTTGGTATCAGCTATCATCGTATCGTAGTGTGCTCAAACCGTGAACCGCATCTGCATCACGGCATAGGAGGAGACAGTCTATTGACGGACGCTGTCCGTTCGCGGGTTGCCTAGACATGCTAACCCAGTAACAAGTCCTGTTCGGACGGACGGGAACATCCGTCTCTTTATTGTGCCGTTCGGATTTTAGCTCGCCGGGAGTCATGAGGCTTATGATCAGGGATTTCTAGAAGAAATCGTCCCTTAAGGCATTCTCTGTTTATTTCCCTTGCCGCTGATCGTGTTTATTTGCCTGGTTACGCAATGGAACTGACAGACCCCTACCCGCATATGGAGATGCGGACTCGTGTGAGTCAAGGTCCTCTTTGTCATCTCGCCAGTTTAGACGCCTACTCAGTTGTCGATGATACATGCCGGAAATGTTGCGTTGAGCAGATGGGAAGCACGACATCGGGCATGGTGGGTCTGCCGGATTTTAGGGACTTCCAGCTGACACCCTGAACAACCGGGCTACCATGGGGACACCCGATGCTTCGATCTCACAACCACTAGGCCACGTTACTGCTATACGTAAGGTGACATGAAGGACTCTACCGCTTCAAATAGCCTTAATTGTACCAGGCAGTACCCTGTAAGCAGTTTAGTTAAGGTAGTCAGACCGAGACTCAGTCTAAAAGTCCCCGACAAACCGAAGGGTGTCCGCTGGACTGCTATGATTGTGCCGGACTTGATAACTGCTACCACCTGACTCATACATCGCCAGGTTATGCAGTCGGGAGGTCCTTAAAGGTTGCTCGTGGGGAAACCCAGCCCACACGGTGGGCTCCCCGACGACGCCAGCCGGTATTGTGTACTATTAGAGACTAGAGTCCCGATCTGTAACTAACTAGCGATTCTGATGAATTAGATTTGAGGAAATGACTGGAGGCCGGACTGCGCGTAGTGTGGACTGAGCTGATCACGCATGCCCCACGGGACCAGTAGGTGTGATGGCCTAGTCGAAGTGGCTCGGAGAGAGACTCGATGATTCTGAGACAGGACGGCAAAGGGTATAGCTGTGGTGATATACCCCTATCGAACTGCTGTGCGTGC"))
    print(*pattern_matching_positions("ATGCAGGAAAGCAGGAACAGTGTGCTGGCGGACTTGCAGGAAGCAGGAAGGCAGGAACGCAGGAAGCAGGAATAATGCAGGAAGCAGGAACGCAGGAAGCAGGAAAGCAGGAACCGCATCCATTGGGCGCTGCAGGAAGCAGGAAGGCAGGAAAGCAGGAACTGGCAGGAAGTCTGCAGGAAGAGCTGCAGGAAGGCAGGAAGCAGGAATGCAGGAAGCAGGAATCGCAGGAAGCAGGAACGCATGCAGGAACGCAGGAAAAGTTCCGGCAGGAAGGCAGGAAATCCAGCAGGAAGCAGGAAGGCAGGAACTAGGTAAGCAGGAATGCAGGAAGCGCAGGAAGGCTCGTGCAGGAACAGCAGGAATAGCAGGAAGGCAGGAAAGCAGGAACCGTAGAACCGCAGGAAGCAGGAACGCAGGAATGGAGAATCGCAGGAATTCGCAGGAAGGCAGGAATTTCAGGACGACCCGGCAGGAAAGCAGGAAGGGGAGCAGGAAGCAGGAACGCAGGAATCGAGCAGGAAGGCAGGAACGCAGGAATTTCGAACGCGGGCAGGAAGCAGGAAAAAGTGCAGGAACGCAGGAAAAAGCAGGAAGCAGGAATAAAATAGGCAGGAACACGTGCAGGAAGTGCAGGAAGCAGGAAATTTCTGACTTGCCGTATGCAGGAATGTCGCAGGAAGCAGGAAGTAGCAGGAAGTAGCAGGAATACGCACCTAATGCAGGAATCGTGGCGCAGGAAGCAGGAAGCAGGAAGCTCGCAGGAAGGGCAGGAAGGCAGGAAAGTACGCAGGAAATAGGCAGGAATTCTGCAGGAAGCAGGAAGCAGGAAGCAGGAATCCGCAGGAAGCAGGAATGCAGGAAATGCAGGAATGGCAGGAACCAGCAGGAACGCAGGAAAGCAGGAACTTGCAGGAACCCCCCAGGCAGGAAGCCTGTGTAGCAGGAAGAGCAGGAAGCAGGAACCCCGTGGAGACCGCAGGAAGCAGGAATACCCGGCAGGAAGCAGGAACGCAGGAATGTGACGTGGCAGGAAGCAGGAATGGCAGGAACCGCAGGAATCGCAGGAAACGCAGGAAGGTCGGCGCAGGAAGAGCAGGAACCGCAGGAACATGCAGGAATGCAGGAATTAGCAGGAATAATGCAGGAATAAGCAGGAACGGCAGGAAAGCAGGAAGAGCAGGAAGCAGGAATTGATGCAGGAAGGCAGGAAGCAGGAAAGCTGCTCGCAGGAAGCAGGAAATTGGCAGGAAGCAGGAAGCAGGAAAATAGGGCAGGAAGTGAGCAGGAAGCAGGAAGGCAGGAACGCAGGAACTTCCCCGCAGGAAGCAGGAAGCAGGAACCGCAGGAACCGCAGGAAAGGCAGGAAGAGCAGGAACGCAGGAAGCAGGAAGCAGGAAGCAGGAACCGGCAGGAATTTTGCAGGAATAGGCGCAGGAAGCAGGAAGCAGGAAGACGCAGGAAGAAGCAGGAAGGCAGGAACTGCAGGAACGCAGGAAGAGAGGCAGGAAGCGGCAGGAACGCAGGAAAGCAGGAAAGGTCTGTTCGCAGGAAAAATGCAGGAAATGCAGGAAGCGCAGGAAGGCAGGAAAAGCCTAGCAGGAACATAGCAGGAAAAATGCAGGAAGCAGGAAGGCGTGCGGTGAGCAGGAAAGCAGGAAAACGGCCGCAGGAATATCGCAGCAGGAACGAGTGGCAGGAACGCAGGAAGCAGGAAGCAGGAATGGTGCAGGAACGCAGGAATGCAGGAATAGCAGGAAGGCAATCAAGGCAGGAAGCGCAGCAGGAAACGGACTGTTTGGGGCAGGAAGGATTAGTCTGGGCAGGAAGTGTGCAGGAAGCAGGAAAGACTGCAGGAAGCAGGAAAGCAGGAACAGCAGGAATCGAGCAGGAAGAGGCAGGAAATGTCCGCAGGAACCGCAGGAATAGCAGGAAAGCAGGAACTGGCAGGAAATTCTTAGCTACGCAGGAATGCTGCAGGAACGCAGGAAGGCAGGAAGATGCAGGAAAACGCAGGAATGCAGGAAGCGTAGAAGCAGGAATAGAGGCAGGAACGTGCAGGAATGTGCAGGAATAGGCAGGAACCGGGCAGGAACAGAGTGGCAGGAAGCAGGAAGCAGGAATTGCAGGAAGAAGGGCAGGAACAGATCGAGCAGGAAGCAGGAACGCAGGAAGCAGGAATCGGGCAGGAAGCAGGAAGCAGGAACAAGTGCAGGAAGGCAGGAAGTGTAGTCCTAGCAGGAAGCAGGAAGCAGGAAAAGCAGGAATGGCAGGAAGCAGGAAGCCGCGCAGGAACTGTGCAGGAAACTCGAGCAGGAAATAGCAGGAACGTGCAGGAACGTGCAGGAACTCATGCAGGAATACGGCAGGAACGCAGGAACTGCAGTAGCAGGAATGCAGGAAGTAACCAGCAGGAATGCAGGAATAGGGCAGGAAAGTGCAGGAAGCAGGAACGAGCAGGAACGCAGGAAGCAGGAATAGCAGGAAGGTCGCTGGTCCTAGCAGGAAAGCAGGAAGTCAGGCAGGAAAAGGCAGGAATGCAGGAAGCAGGAACCAGTCTTAAGCACCGCATGCAGGAAGCAGGAATCCGCAGGAAAAATTTTCGCAGGAAGCAGGAACGCAGGAAGCAGGAAGCAGGAAGCAGGAAGGCAGGAAACGCCAGCAGGAAGCAGGAAAGGGCAGGAAGCAGGAATAGGCAGGAATCCAGCAGGAAGCAGGAACGCAGGAAGCAGGAACTATGCAGGAACAGAGCAGGAAGTTAGAGCAGGAAATACGCAGGAAGGTGAACTGCAGGAAGCAACCCTTACGCAGGAAGCAGGAAAGGGCAGGAAGGGGCAGGAACGCAGGAAACTAGCAGGAAGCAGGAAAGCAGGAATTTGCAGGAAGCAGGAAAAGGTTGGCAGGAAGCAGGAAGGAGCAGGAAGCAGGAACCATAAGCAGGAACGACACTTTGAAGCAGGAACATCGCAGGAATGCAGGAAGCAGGAAGCAGGAAGCAGGAAGCAGGAAGCAGGAACGGCAGGAACGCAGGAAGAAACGTGCAGGAAGGCAGGAACCGCACCGGCAGGAATGCAGGAAAAGGGCAGGAAACGGCAGGAAAGCAGGAAGCAGGAATTGCAGGAACCCTGGCAGGAAATGCAGGAACCTAGCAGGAACGCAGGAATAGCAGGAAGCAGGAAAGGCAGGAAAGTGTGTGCAGGAACGCAGGAACTATTAAATCAAAAGCAGGAACTGTCGCAGGAAGCAGGAAGAGAGAGGTCAGCAGGAAGCAGGAACCGTGCAGGAAGCAGGAAGTAACCCTTTACAGCAGGAACCTCGGCAGGAATATGCAGGAAGCAGGAATTCGAGTGCAGGAAATGCAGGAAGCAGGAAGCAGGAACATCCTTTTGAGCAGGAACGAAGCAGGAAAAGCAGGAATGCAGGAATAACGGCAGGAATTAGCAGGAATGCAGGAAACCGCAGGAAGTGCAGGAACAGCAGGAATGCAGGAAAGCAGGAATGGCAGGAAGCGCAGGAAGGTTTTGCAGGAATTCCAAGCAGCAGGAATGTGCAGGAAGCAGGAAGGTGCAGGAAGCAGGAATGCCTCTAAGGCAGGAACCGCAGGAATACCGAGCAGGAATCAGCAGGAAAGACGAGCAGGAAGCAGGAACGAATGCAGGAAACGCAGGAAGGCGCAGGAATAAGCAGGAACCCTGTATCAAATGTCAGCAGGAACGGCAGGAAGCAGGAAGCAGGAAGGCAGGAACAAGACGGGCGAGCAGGAACTGGAGCAGGAAGCAGGAAACTTAAAGTTGCAGGAACTGCAGGAAATCGCAGGAACACGCAGGAAGCAGGAAAGAGGCTGTAATGCGCAGGAAGCAGGAATCGCAGGAAGGCAGGAATCTTGCAGGAACAGCAGGAAGCAGGAATGCAGGAAGGCAGGAATGCAGGAAGGCAGGAAGCAGGAACAATTCGCAGGAATGGCAGGAAGGGCAGGAATGGCAGGAATGCCAAGGGAGCAGGAACCGCGCAGGAATTGGCAGGAACTCGAGAGTGCAGGAATAGGCAGGAAAACAGGCAGGAAGCGCAGGAACTAAACTCATGCAGGAACTGCAGGAAGGCAGGAAGCAGGAAAGGCAGGAATGCGCAGCAGGAAGCAGGAACCCTAGACAATGACAAGCAGGAAATACGTGGAAAGTCCCACGCAGGAATGCAGGAATGCAGGAACTGCAGGAATCGCAGGAAGCAGGAATGCAGGAACTAGCAGGAATATTGCAGGAAATCGCAGGAATAGCAGGAACGTATGCAGGAAAGTCGCAGGAAGCAGGAAGCAGGAAGTAATCTGGCACGCAGGAACAAGCAGGAAGGCAGGAAGCAGGAACAGCAGGAATGCAGGAAATCCGCAGGAATGCAGGAAGGCAGGAATTCAGCAGGAAGCAGGAAGCAGGAAAAATGCAGGAAGCAGGAATCGCAGGAAGCAGGAAGAAAGGCAGGAAAGCAGGAAACCAGCAGGAAAGTTGCAGGAAGCAGGAATGCAGGAAGCAGGAAGCAGGAACTAATATCGCAGGAAAAAGGCAGGAACTTCGCAGGAAAATACGCTGGGAGAAGCAGGAACATGCAGGAACAGTCTGTGTAGCAGGAACGCAGGAATTGCAGGAAGCAGGAAGCAGGAATGTGCAGGAACGCAGGAAGAGCAGGAAAGCAGGAACAGCAGGAAGCAGGAATACGAGTGCAGGAAGCAGGAATCGCAGGAATGGCAGGAAAACGTGCAGGAAGCAGGAACCTAGTGCAGGAAACTGCAGGAAGAGCAGGAAGGCAGGAAGCAGGAAAGCAGGAAGGCAGGAAGCAGGAACGCAGGAAGCAGGAAAGCAGGAAGCAGGAAGCAGGAAGCAGGAACGTGTAGTAGAAGCAGGAAGTGCAGGAAGCAGGAATGCAGGAAAGCAGGAAAGGGCAGGAATGCAGGAATGCAGGAAAGCAGGAAGCGGCAGGAAAGCAGGAAACTATAACTCGTAGCAGGAAAAATGCAGGAAGGGCTCACAGCAGCAGGAATGAGCAGGAAGCAGGAATAGCAGGAAGCAGGAAAACTGCAGGAAGCTAGCAGGAAAGCAGGAAACGGCGCAGGAAGGCAGGAAGGCAGGAATTACCAGGATGGATCTGCAGGAAGCAGGAAGATTGCAGGAACGCAGGAAGAGCAGGAAGGCCTGATGCAGGAACTGCAGGAAGCAGGAAAGGCAGGAAGCAGGAATCGCAGGAACGCAGGAATTCTTACTGCAGGAAAGGGCGCAGGAAATGCAGGAACCACGCAGGAAGTTGGCAGGAACTGCAGGAAGCAGGAACGCAGGAACGTTTCCGTCCTGCAGGAAGGATGCGCAGGAAGCAGGAAGCGCAGGAAACTGCAGGAAGCAGGAAAGCAGGAACGGCAGGAAATGTGCAGGAATGCAGGAAATGCAGGAAGCAGGAAGCGCAGGAAGCAGGAAGGCAGGAAAGCAGGAAGGCAGGAAGCAGGAAGCAGGAACATGCAGGAAGGCAGGAAATGTGCAGGAATGCAGGAAACTAGCAGGAACAAGGCAGGAACAGTGGCAGGAAGCAGGAAGCAGGAATTGCAGGAATTGCAGGAAGGCAGGAATAAGGCAGGAAGTGCGCCGCAGGAATGGTCCGCAGGAAAAGCAGGAAGCAATGGAGGCAGGAAATGCGCAGGAAACGTCGGCCCAGCAGGAATGGCAGGAACGCAGGAAGGGCAGGAAAGCAGGAATGGCAGGAACTGCAGGAAGCAGGAACAGCAGGAAATAGCGTCCGGCAGGAAGAGCAGGAAAGCAGGAAGCAGGAAGCAGGAAGGCAGGAATGCAGGAATGGCTGCAGGAAGACGCAGGAAAGAGGCAGGAAGCAGGAACCGGCAGGAAGCGTCCTTTACGCAGGAATTGCAGGAACCACAGACAGCAGGAAGCAGGAACGCGCAGGAACAGCAGGAATTGCAAGCAGGAATGCAGGAAATGCAGGAAGGACCAAGGGGGGCAGGAAAGCAGGAAGCCCATTTGTTGCAGGAACTAGTGGCAGGAAAGCAGGAAGCAGGAACTGCAGGAAGCAGGGCAGGAAGCAGGAAGGCAGGAAGCCAGGTAATGGCGCAGGAATGAAATCGGCAGGAATGGCAGGAAGTTTGCAGGAAAGCAGGAAACGCAGGAAGGGGCAGGAATAACGCAGGAAGGCAGGAATCGGCAGGAATGTAGCGGATCCTAGGCAGGAAGCAGGAAATAGCAGGAACAGCAGGAACGGCAGGAAGCAGGAAGCAGGAACGGCAGGAAGCAGGAAGGCGCAGGAAGGCAGGAAATAAGAGCGAGCAGGAAAGTGGCAGGAATGCAGCAGGAAAGCAGGAAAGGCAGGAACGCAGGAAAAGCAGGAAGCAGGAATGGGCAGGAAGGCAGGAAGAAGCAGGAACCCGGGCAGGAAACGCAGGAAGGCAGGAACGCAGGAACGCAGGAACTATGCAGGAAGCAGGAAACGAGAAAAGCAGGAATTAGCAGGAACGCAGGAAGAACGGTCATGCTAGCAGGAAAGCAGGAACTGCAGGAAGGGCAGGAAGCAGGAATGTCAGTCGCAGGAATTCGGGCGCAGGAACGAGCAGGAACCCGGCAGGAACGCAGGAAGGCAGGAAGCAGGAAGATTCGACGCAGGAAACGCAGGAAGTGGCAGGAATTTAGCAGGAATCATTTGGTTACCAGGCAGGAAGCAGGAACGCAGGAAGGCAGGAAAGTGGAACCCAGGAGGCAGGAATACGGCAGGAAGACGCAGGAAGGGCAGGAACGCATGGGTGGCAGGAAGCAGGAAGTGCAGGAAATAGCAGGAAGCAGGAATGAGCAGGAAAGGCAGGAAGCAGGAAGAGCAGGAACATCTGAGCCGCAGGAATCTTTACGTCAGCAGGAATTGAGCAGGAAAGGACGCAGGAACCCGCAGGAACCGCAGGAAGCAGGAAGGATCCAGCAGGAAGGCAGGAAGGCGCAGGAAGGCAGGAATCGCAGGAAGCAGGAATACCCACCGCAGGAACACATAGCAGGAAGCAGGAAGCAGGAAGTGAGCAGGAAAGCAGGAATAGCAGGAAAGCAGGAACGCAGGAAAGCGTGTTTGAGCAGGAACTGGCAGGAACGCAGGAAGACACTCTGCAGGAAGCTGTTTTGCAGGAAGGAAGCAGGAAGCAGGAAGCAGGAAGCAGGAAAGTCGGCAGGAAACTGCAGGAAGTGCAGGAAGAGCAGGAAGCAGGAATGGCAGGAAGCAGGAACGCAGGAAGTCTGTTGAGCGTAGCAGGAAGCACGCAGGAACAGCAGGAAGCAGGAAGCAGGAATCTAGCAGGAAGAGGCAGGAAGCAGGAAAGCAGGAACCGCAGGAATAGCAGGAAATTGCAGGAAATAGCAGGAATTTCGCAGGAAGCACGCAGGAATGCGCAGGAAGGGGCAGGAAAGCAGGAAGCAGGAAAGATGCAGGAACGCAGGAAAAGCAGGAACCATGCAGGAAGTGGCAGGAACGCAGGAAAAGCAGGAAGCCGTGGTGCAGGAATCGCAGGAAGGCAGGAATGCAGGAACACGCAGGAATTCCGCAGGAATAAGCAGGAAAGTGTATATTTGCAGGAAGCGCAGGAAGAAGCAGGAAAGGTGTAGCAGGAATGAGCAGGAAAGGGTGCAGGAATGCAGGAATAGGCAGGAACGCAGGAATATACTGCCATGCAGGAAGCAGGAACCCAGCAGGAATTAGCAGGAAGGTTCGCAGGAATTTCGCAGGAAGCAGGAACGATGGAGCAGGAATGCAGGAAACCCACTTTTTGAGCAGGAAAGGGGCAGGAAGAAGCAGGAAATGCAGGAAGCAGGAAGCCGCAGGAACAGCAGGAATTTGCAGGAAACGGCAGGAAGCAGGAATGCAGGAAGCAGGAAGCAGGAATTTAAAGCAGGAATTTGCAGGAACTCGGCAGGAACGCAGGAATCTCTAGTGGGGCAGGAAAGTGGGCAGGAAGCAGGAAAACCGCAGGAAAATTGCAGGAACCGCAGGAATGCAGGAAGTCCCGCAGGAAGCAGGAACGCAGGAAGAAGATTCGCAGGAAACCCGCAGGAATGTGGAGACATCTTCGCGCAGGAAAGAAAGCAGCAGGAATGCAGGAAATTGGCAGGAATGCAGGAAGCAGGAAGCAGGAATTAAGCAGGAATAGGCAGGAATAATACTACCGTATTCTTTAGCAGGAAGCAGGAACGTGCGCAGGAACGCAGGAAGCAGCAGGAATGCAGGAAGCAGGAAGCAGGAAGCAGGAAGCAGGAAGGCAGGAAGGCAGGAAGCAGGAAGA", "GCAGGAAGC"))
    with open("../data/Vibrio_cholerae.txt") as file:
        text = file.read()
        print(*pattern_matching_positions(text, "CTTGATCAT"))