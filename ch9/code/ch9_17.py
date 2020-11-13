"""
@BY: Reem Alghamdi
@DATE: 13-11-2020
"""
from ch9.code.ch9_06 import suffix_array


def partial_suffix_array(text, k):
    partials = []
    array = suffix_array(text)
    for i, e in enumerate(array):
        if e % k == 0:
            partials.append((i, e))
    return partials


if __name__ == "__main__":
    # lst = partial_suffix_array("PANAMABANANAS$", 5)
    lst = partial_suffix_array("ATACGCTAATTCGGTACAGGCTGCGCTACCTCGGAACTCATTCACGTCCGACTGATTGTCCAGCGTGTACTTGTGTACAACCGATTGTCGTACGAGCACCCCCGTCAAGGCAATGACGAATTGCGTATCTCGCCGGCTGGCGAACCCGTTCATCAGTTCCCTCCTACCGAGGGTTTCGCAGATGTCGTGAGGCAACTTGCTCACTGGGTGCGACCATAGTCTGTCTTTTACTAACTGCGTAGTAGACGGCTACTATACATTGTGGTACACGCGGAGTTGGCAGGATTGGTAGAAGGCGCTTTGACAGCATGAGCTCTCCGGCTGGAGCATGGATTGCCTTGCGTCAATGAAGACGTTCCTTGTGGCGACGACCAGTCTCACGGCAATAACAAGAATGTCTGCGTCGCATAGGACCCCAAGACCTTGCCAACGTACCATAGACCATTGACGTAAACACGGGCTACGCATCCGATTTGTTGTAACACGTTTTGCGTAAGCGGACGGTCGGCTCTGGAAGTAGTTCCCATGTCGCGCTCCACGGAAAGGTGTTTGTATTTGGTGGTGCGAAATCATATGGATACGAAGCGCGCGTGGTGATTCGAAAGCAGTTGGGAAGGGCGCTAAGAGTATATTAATTCAATGGACTTATTGCAAGGGAGATATCCCATTGGAATTCTAGAACACGGGACTACACGTACTTCACCAGTAAGTTCACTGCGAAATCTAGGCCCCCCCCGGGTCAAAAGGTTAATATCCACCTACCGGCTTATGGGCACGGGAACGACTCACTTCTTACGTCGGGCTGATAGGGGACTAGTCGAGCGGACGATCCGCTTTTAGATTCTTACTACTCTGTGGATAGGGTAAACGGCAACGGTCATACCTAGTGATCGTGGGTGGAGCGGAAAAATGTTAGGCGCGAGAAGAACTTCAAGGGATAAAGCGCATGTTGGTTCATGTATGGGGAAACCATGTAGAGCGCGTATTAATGACCCATTGAGGGCACGAAGAACCTGTCTTACAAATGTGCTGGCCCTTAAGGGCGGATTCCGGTTTAGCCGTTAAAACAGGGCGGCAGTGTAACGGGTATGCTAGATTTTTTTTGTATTAAGCGACATAAAACAGCTTTGGCTCGGCTGTGGCGAGGCAGTACAATGGTGGCGACGACGGGAATGCGCAATTCGACTACGTCCGTTGGTAGGGGGTTGCCCCCACTACTAAAAGACACTAGTTCCCTTTAGGATTCACCCACATGTATCCCTTCTAGACAAGTTATGGCACTTTCCCCCCGTCATCTCAACACGGACTCTACAAACCTTAACATAGTTCACAACAATGATGTCATGCACCGCGGCTTAATCTTCGTTGAGGGCAGACACTGCTTGATCAGGAGAACCACTTGCACGCCTACATTATTCGACAGCGGACTGTCAGGCGTACGCACATCTGGTATAAGATAGTCGGAGCAAAGAACAACTAGCGCAAAATAGTCAACCTGCCTTACGAATCGCAAAAGGCCGTGTAGCCCCTTCCTGAATCGTAGTGGTGGCTTGCTGGCTTATGGCTGTTTGTCTAATCGAGGGCTGGGCCCCCGCCACCTTGCCCGTAGAGAAGTCGTGCGCTTCCGACCTTCCCCTCGATATGCGCAGATAGGCATGCAATTGAGACCCGACTTCTTCAATTTCACACTATAGCTACCGTAACCAAGAAGGGATAAGGTACTGCCGTGAAATATCCCGCTGCTGGTATCGGATCCATCTATGTGTACAATACGAACTCGGTCTACGAGAAGCACCAGAGAGCCCTGAAGTAACGATCATAGTCCCGATAGTGAGGGGAAAATGTACTGCCCAGTTCAGCCCCAGTCGTCGCGGAAAAATCATAGCGACTCCGGTTACCATTTGCTTCACACTCAAGCACTGCTGTCGTAGTTTTGGTTATGCCACACATCCCAGGGACTGTCATTCAGCTAATGATTTCTCCGGAGCCGACTACTTCGATCCACATGATCCTCCGCCAGCCTTATGACCATGCTCCTCTCCATGAGACCTTCGTTAGCCCGGACGAAGGTCGTGGCCGCAAAAGCTTGGTATAAGGAGGGGGGATCTATTTAATAAGTTCTTAGACGCGTATTTTGTTACGGCAAGACACGGTGCGCCAACGATTCTGGTAGGTGTGGGTCGCCTACATCCCGTTAAAACCCTCCCCGCGCGCATGATGCTCGGGTCGCACGCTGCTCAGTCCCTGTAACTGCAACTTAATTCCAGCATTGACTATAGTCTACACCCTTATCGCTCGAGGCCATAAGGTACACCGGCAATGGATCATCCAAACTCCTAAGTCGAAACCGATGTGGCGACGGCCCAAACTATTGCCTTGTCCTCCGTCCGGGCTTGGGCTTAAGAGCTGAAAAATTGCTGATTTGAGCGGGAGGGGTAGTTGTCGTGCCCGACGACATGTCGCGCGTGTTGCAGCGCCATGTTCCCGCTCTGCAACGCCATAGGAGTACACGAACCGATAGGGATTAGAACGTTGCACGGACAGCGATTACTAGGCAGTGGGGACATCAAAAAGCAGCCGAAAGTCTAACTTGCTGAGCCCAGTAAACGAACAAAGCAAAGACTAGTTCATACTGGTATTCGATCCTCAGCGGATGCCGTTAAATGTTGGTAAAAGGACACCACGCATTCTCTCTAAACATTAACGTTCGATCACTCTCTGGGAACCGTGGTAAAGCACTCATCGCTAAAATCACCCGTCGCGGCACACCTATCTTAAAATAGTTGGAAATCCCAAGAGTGTACTCCTAAGGATTCGCTATCCATCGAGCCGCTTGCACGTTGCTCAGCCTGGTACATGCTATTACGATAAAATCTTCAATGCCAGGCGCGGACACTTAAATTAAAACATACCCGCAAATCATAGGTATCTCTTCCTTAATCGCTTAACAAGCCGATATATGTATAGAGAGTGATCCTGCTGGGCCTCTGGCAGTGCTATCTCTCTGTCCACCAGGTGGGTTGCTGTCAAGCTGTGCGATGAGTAAGTCGAAACAATCGCGATTGATGGCCAACGGCGCCGCAAGCCACTGTATTTGTCACATCCAACCACAACATCTGCACAGGATGATGGTCCTAACAATACAGTCTGATGTCGACCCACGATTGTCCAGTTCCCAAGTCAAAAAAGGAGGGGCAGTTCACCCTGACTGTCCATCAGTGGTGTCAGGAGCGATTTGACAGGCGAGCCCGAACGTCCAGTCAATTAACTTTGGGGGGCAGAAAATGACGATGACTCTTCTGTAGAGAAGGAACGACAGCGATTGTAGAGGCGCTCCCACAGCTTAATACATCTACCACCTCTCAAATCGCCTGTACCAAGCTAGGAACATCCTATCACGGATTGATGCATGAAGACACTCTTTTTTGCGAACGAGGACACCACGACTTGGTAATACGGTAACAAGAGACCTAGTTATGTATAATGATACAGCTTTTGTGCATCGGTCTTATAGTCTGGTCCTAAGCATGGCACCCCACCAACTAGTTGTGATAATTTTCTGGCAATTCAAGCTAGAGTTTCGGACGGATCAAAGCTTCCATAACAGACCGCATGACAAGTCTGGCACATTTAGTTCAGGCAGGTGACTTGCCTTAATAATAGCCTCTCCCCTGATGGCGACGGGAATCCGATGACCCATTGAGGGAAGAGCCAGCTCAAGCTCGGCCTAAGGCAGGTCATACAACGACGGTAAAGGACCGAGAACCGAAAACAAATGGACATCATCGCTCATATCACCCTATCAATACTATACGGGGGCTAACCCATGATGGCGGAGTCAATTGTTTTTTACACGTATTATGTGATGACTAGATGTTGTTGAGCACTCACCCAGGATAGGCCTTCTCGAAGGCCGTCGAAGCAATGCTACACTTTCTGGCAAACCTACGGTGGTCACTTCAGAGTCAGACGGTGTGGAAGAGCGTGCATAAGGCAGCACCTGATCTGGGGGTGATAAAGTCAGTAGCAGCCTTTCTCACCGGGAAGCACCTCTGTATGGTCTCATGCAGTAGCGAGTCCGGGGTTGTATACGCTGACCATCTGCAAAAAACTTGCTCTTTCTACGTGGCGTAGGTAAGGCGCGCTACTACTTACAACAGTTGCGAGTAGCCACTGACTCTAGACCTAAATGGGAAAAATGGCCTGCGCAAATTCAATGCCCATTACACAGAGCTTTCACCCTATCTGGGACACTCCTGGGGACCAACACCCGAAGTTTGGTTGCGATACGCTGGGAAAACCTTAAGTATTAAACAACCAACACTTGTCTAATCTCATGCCAACGTGTGTGACCATAATTAGCAATTGCCAAAAATGACGTCACGCTGTCGGGTCGTACTACCGTAACAGTCGGGTCCACTTAAGCTTAGGAAAATGGCACATTACATAGCGCCCGCCACCGCGCTCCGCATACGGGTAATTGCGGAATCCGTTTTGGCAAACTAGCGGTCGACTGGCAAGGTCTTCACTCGTCCGCAGCACAGCGATGCTCAACCTAGTAATCTGCCCGGGAACATCTGCAGGTATATGTTGTCTCCCCAAAAGGAGGAGGCAACGTTAATTAGGACTTCCACCCTAGACCAGTATCGGTGCCGTATCTTGGATCCACCACAGTCTGAGAGAAGGAAAACAAAGTCCAATGTTCATCCCGGCTCCATATTGACCTGCCTTCCCGCGGCCGGGAAATCACTTGATGGTTGAGTTTGTACACGTGCTTTTAGGCCACACGCGACGATTACGGCGAGGCTACCCGCAGGTGGGCGACCGGTAGATCCACTTGTTCAACATACAGTGGAGCTATAGTTTGGTGAGGTTCCTCTTTAGGGGTTTCGGGCCCGCTACTTACTTAAGCGGTTCCTGCGCGAGCGAAATATCCCACGGACCTTCCCAGTCGATGGGACTCGGCGTCCAACCACAGAGCATACGAGTGTTTAGAGGAGTGTCGAAGGTGCGTTAACCCCTAGGGATAAGTGAGTTCGGTACAGATGGAACACCCGTAGAAGCCAGGTGTCGGGGTCCTTTCCATATGGGGTACTATGAGTTCCAGAACACTGGTGTGTTTGATTCGATAGTGGTCCTGAAATCGAAATAGAGCCAATTGTCCGCAATATCGGTATTCCCAACTCAGTTCGCAGCAGCTCTCAGCGGGATGTGCTGTACCCCCCATGCGCTCCTGCACCTGGATACTGATCCCTCCACAGCGGCAGGTGGTAAGTCGAAGTACCCAGTATTTACAGCGGCTCCGTGCTCGATCCGGTTTCCCAGATTGTACAACACAAAGCCAGCACAGTTTTTCGGAACTAAGCAACCGGATACGGACCCGCTTTCAAGCTATAAGTATCCTGAGATCGCGGTTGAGCGGCATGTCGATAACATTCACTGGGAATATAGATGATCTCGTCAGGCACACAAATCTGGTCACTGGCCAGGGCGCCGAAGCCCGTCGTGGGATCCTTGTACTTTGGTGGCGGCTCGTATGCGTTGTCACTCGTTTGCGAAAATACTCCATGCCAGCCCTTAGAGGTTGTCAGCTTTCATCTACCTCCTGGGTTTGTGGTCTGTCAGTACATTCATGCGGCTGTGCTTTTTTCCATGCAATCGTTACCGTTTTACGCTGCCGAATCCTAGGCATAGGATTTCTGAAGTGGCCAGAGCCCGTGAATTCTTGATCATTTAAGTTAAAACGTCCACTGCTCAACATAATCAGATAAATCAACAGGGGCGATTCCATGTTATAGGAGTGCCGAGTAAGTCGAACTCTGGCGAGTCGACTTGGGGCAGCATCCCCTTTCGGCCCATACCTAAGTGCTGGCCCGCCATTCACCGCTCCTCAAGCGGCATTTGCTGACAAAACAGCTAGCTAACATCCGTCGGAAGAGAAAGTGGTAGTGTAGTTACGAAGCCGCTACATTTTGTTTACTACGAGGCGTAGGGACTCTAGGTGCTCTGGTAGCCATATGTCTCCTTTGTCTAAATTTTATCTTGCAAACCCGCGTTCCTAGACTGGAGTGACTGTAGCTCAACATATGAAGGCACGTAAGAAAATTAACGGAGCGTACTGGAATCCGTACGTCGTCATGTGACCGGATCAGAACATAGTATATTGTTGCAGGCAGCCTCGAAGAATTATGGGTCCGTTGCTAGATCCCTCACGCGGTTTTATATCGCTAGCAGACCCGTAGGTTAGGAATTGTGAATCCATTCTCCAGAGTAGGTGCCGCGTTCGATGCTAGTGTGAATAGAGGGTCCTAGTACTAGGTTACACTCACAATATTACGCTCTGTAAAGGAAAGGTCCAGGTCTTTACTTAAGCCAGGTTCACAACGGTCAGGCTAGACCGTCAGTCTTCTCGCGCGGGAGTAGGCGTAACATTCTCGAAGAACAGCGGTAAAGGATCTAATACGCTTCTCGTGAATCACATCTTGAGGCTGTCATTAACTGAGGCTTGGACCTGTATGTATGCACCGCAGCTGGTAAATCATGGCGCGCTGTGAGATCTCAGCTGCCCTCTTGCCCACTGGCCTCTACGCACTAAAACAGATTGAGTTCCACATGTGCTCCGTGCATTCCTTGTCGCCTGCTCACAATTCCCCGTTAAAGCAAACATATACCGCTCTAATCCATTGGGATGGAGAGTCCCCACTCGAATACTCACTTACTAGGACGCAAACGAGCCATAAGAATTGGCAGAAGCCTCGCGAATTAAGCTCGTGAACGGGGATCATGTAGGGTAGTTTCGCGACAACGTGTACAGTTGGTTTAACTGCGCCCTGTTAGGGTCAAGTATATGTCCCTTGTGGCACAATATTCAAGACCAGAATCTGTACTCGCTAATCGCTTTTCGGGGCGTTTGAAAGCTAATAGAGGCTAAAGGAGTACTTAGCCACGCCTGGGCTATAGTCGCTACGTCGGTGTGCGTTTAGGCCTAATCAGCGTAAGACACTCCCGGCGTTCCTAGTCTGGGACTGACAAGTGGTCGCCATTACGAATTCACCGCTCCTAGCGCTCTACCAAGGAAGCGTCCGCAGAAGAAAGCAGCTCGTAGATATAATAACCATAGCCCGTGAGCCACTTGCGCAGAGGCTACGTGTCTTAGATTTGCCGCGGAGCACTACACAGTGCACTATAATATGGATAGGACTGTGAGGTTGTACTAACTTGGATCCAACGGTGGGCAATTGCCATACTCGCTCATGGGTCTCCCAGCACCACTCACGCTGACAATTAAACTTTGACCCAACAGAGCAGGATATCCGCATCAGTCATAAATCTTTTGTTATATCTTCTGGAAGTTTGCTATGGTATTCCCGCGTCTTATGGCGACAAAGAGATGCGACTTCATCAATTAGATTAACTTACATAAAGAATGTTTTTGGGGACCGCAAATCCGAAACCCCTCACATCTGATTGTTGCCACTAGCCAGGCGTTAGCTCTTGAGATCAAGTCGTCGACATAAAGGAAGCAAGCATAGCGGGCTCCCCCGACTCTCCTGCCCTGCCTGACGAGCGGCGTACTTACACGCCGGATCAACCGGGGTTTCGACCTTATAAATAAAATGCGAGTCAGAACAGTACTCCCCTCGGTGTTGTCTAGGGTAATTCGCTGGTAATACTACTCATAAGCGGGGCGGTAATTCTTTCGATCGACATCTTTATGCCGCATAGCTGTCCTCCAGATGATCCATCATGGACTTATTTTGCCTACAACTATCGTAATCGCTGGGCCTGGAATTCCCAACTCGACCGGTTTATTAGTAGAAGAACTCCGTCGGGTAGGTATGAGTTTAGTGATGATGCAGTTTTAGTAAACGGTTAGTTAACTGAGTCTCGGTATTTTTACAGGACCTGGGCAGGAAATTCTCCCTAGGGAGCGGTACCACGCGAATAGCGCAGGTCCAGATGAACACTTGTCCATCCATATCACCCGCCACCACGGTCGGGTCCGGGCAACTTAGGGTTATTTCCAAGTGAACAGTCGGAACCTTTATCGGCCAGTCACCCAATACCCTTTTGCCGAGTCAGATTCTTGCATAGTTAGTGCTATAGGACGCGCAGAACCAGTAGGAGACCGTAGGATGGACAGACGGTACGAAGACTGAGGGCATCGGAGGCTATAATACTAAACCTCACTTGCGCGTTCCTACACGGCCTGCGAACTCTCTCCGAGCGCATCGCAGAAACATCCGGATTGGAGGTTCAGTGGTTCCGTTAGCGTACCAATGGGCTAACAGTGTAGTGGCTGCATGATATGGATTAGCCCGGAGTCTTGAATGACACACTACTCGGCGGTTATATCCACAATTACAGTTCGCTGAATGACGAAGAATCGGACACACTTCCTCTAGAGAAGCACTCTTCCGTCCTTATTGCGACCTTCGTTCTGTCTTGTAGTAATAGGCACATTCATGATTGACGTATACACGTTTCATGGGTAGGTGCCGCTGCTCTTCTCGTTGAGCTGGATCAAGTAGCTCTTTGTATATCTTAGCCCGGATTGGTTTGACGCTGCTAATCGTCGAATCCCTTGTGCCCAACACGTAGTAGTGATCCTTCATGTGCGATAGTTGCCCTTCTGGTCCTAGCGAAATGTCCATGCCTGGGGGTGAATGTTCTTAGTCAAGACAATTTACATGGATTGTTGTGACGTAGAAACTGACTTACTGCCGGCCTAAATCGCGTAATACGCTCTACGTGACGTTGCGTACTTGTAGACAGTGCCTCGCGGACGTGAGGGGGTTAACTATATCATGTTATTTACATAGGAGAGCTGAACATCTAGGAGCTAAATTTTCCCTCATAGGTTGGCAGAAGCTGAGATTTAGGTAGAGAATGGGGCTCCACCAACGTCCCGGGCGTACTTTCTGGGCTCGGTTCTCCATATAGATTGATTCCCTAAGGTCCTAGGACACATTCTAGTCCCCAATATCGACAGTGTGTTTCGCTCATGATCTGGGAGTTCTCCAGGAGGATTGGATGAAGTAGGTAGCTGATTCTTTACACCACCGCACGGGGTTTATCTTTAGTGGCTACAATTTTGCCTGTTAGTTGGAATGGCTTCGAAAAGGGTCGAGATACCGCACTGTCTTTAAGCGATAATTGGCACAAGTTATATGAGTTATGGCGGTTGAGCGCAGCACCCACCAAATATAGCGGGACTGATTGTGGCCGGGGGGCGTCAGCCCGTCATTGCGAGGAACAGCGACAATGAGGTCTGCCCCTTGTAGCGATGCTCACCATATAGTATGCTAAGTCCCGGTCCCATACCCTAGAACAGTTCCGCTGTGTGGTATTCCAAAGTGGTAAGAGCTTAAAACGATTTACTAGTAGTGTTTTCTCCTGTTTCAGGTCACACTCGCTGTTCGGGCGATTGATCGGTTGTGCTTAAAGATCTGTAGCCTTGCCCACTTGGGGTAATTGAAGATGGAGCTTCAACTAGGCCCCTGGTTCTCCTGACGCATGGGCCGTTATGTGGGCTATCCTGTCCATAGTTATTGCAGGGTAATCCAGTTGTCGACCGTCCTCATTGCACCCCTAAAGTAGGCAGCCATTTAAGGTCACCTGGTCCGGCTATTAAGTCTAAATTCAGTCCCCCGCCGGAACTTCTGCCTGAGAGGCGGCAACCTCTGTGCAATCCCCATGAACTCACACTATGCTTCGATAATGGAAGAGTTAGATAAGAACGCGAAAAACTATGAAATACCTTAACTAATAGCTACACTACCCTGGATGTACGGCAGGAAACTAGGTGGTCAGGTAGTTCTCGCCGGGGAGCGCTTCATATGATCTGCATCTCTCTTTTCAACCCTTTGCAATTTGGAAAGAGGAGCACGAGACTACTTAAGCTAACCGTCGTAGAGAGCCCTCATCAGCTGGCGGTGGATATGTGGGACAGTAGTGCGATGCGCGCTTCGAATCGTTACGGGTGGCGCCGCCGTTGCAGGCACATTTTAAGACCGTTAACGCTGCGCTGTACGTATGTCATATCCCCTTTAAACGTGTACTTAGACCACTGACGGGTGCGTGGGCCGGCTCGAACGACTGGGTCCCTTAGCGATGCTATGAGTCTTATTTCTAAGTAACAGTCTCGTGGAAATATCACCTCTATATGAGCGAGTATCGAATAATTGTGCTCTTAACCTAGGGTGGTAACGGCAATTTGCGCCGAATGCGTGGGTCGGAGAAGTCTCTATGACGCCGGTGGTTCTCGTAAACTCTCCGCCCTCGCTGGAGAAGGATTGAGGTAAATTATAAGGGGTGGTCGGCGCACGGGTGCCACTGTCTACCCCCGGATTATAAAGAGGGCTGCCCTTTTCATTTTATCGGCATTATTGGTAGTTGACGAAGGTTCCTCAACGGCGAAGTCGTTTCTACCAGGTCGCATACCATTTTTACGAGTTCCGCCTTTCTTTTAGCGGGTTTTAGTCAAGTCCGATGGCATTTGACTACTGCTCGACGGTGATAAGGGGGAGATTACCGGAATTAGCCAGTAGACGTAGCTAGCCACCAATCTGCTACGGGCACAGGTAATGGATGCCGAATTAAGGAACTAGTGGTGCATGTTAGAAGTTTAATCTTAGCACCTAGGACGCCACTCCAAAGGAAGGACTGATGCAGTCGCCCACTCTGCTCGCAGAGATAACTCGGCACACCGTGTTAGTTCTATCCTGTCGGTACAATCAACAGGTTCATTAACTCAAAGCGTGCTCTATGCGGAGTATATGTGCGGACCGGGGCCGTTTTAAGACTACATGGTGGTGCAAGCGTGTCTGGCGCCGCCCGGAGGTAGCCAATGAAATGCGAGATTTGACCTCCGACACATGCGTTTTATCTCGTTTAAAGGAAAATTCTCGGCCTCATCTACGCGCTCTCTTGTCTATTGGCAGGCTGGTTCTGTAGCGGTGTATGCCCGGTGGTTACTTCTGGAGTTTCCGATCACATGGCCTGATTGCCATGAAAGAAGCGTGTGGATATTGCGTTATGTACTTTGCGTTTCCGTTACCATTTCTGAGCGTTTAATTCGCTGTAGGTACAGCAGAGTTAATTTGTCGGTAAGATTCTCCCTGAAGTCTGGAGCAGTAAAATGAAACCTGACCGTGCTTGGTGGTGATGTTTCTTACTCATATCGTAACACATTGCATTCCGCCTCACTCAGCGGCATCACCAACTGTGAAACTTATTTGTGTAAGGAAAGCTTGATTCGTCGTGCGCTGTAAAGACTTAGTTTCAAACTGTCAGGCGGCTTGCCTTGAATTTTCATCATTTTATACAACCACAGCTCCACCGTAGACGTGACCCCTCGGTAAGCTCTAAGCCTCGTTCGTTATACGCCCCTCGAGCAGGATCCTAGCTTTCTTACTTGAGGGGTGGCGCCCACATCCTCTTAGGAGTCGTCGTGAAATACGCTCAATACTCCGCGATTGTTGTAAGTGAGAAAATGAGCCTCAGCTCATGAGCGACAAGTGGCATGGTCTTCATCTTTGGATAGTTGGAGGTTTCATGCTGGACTTAAGTTGCACGGAACTCCTTAGTAGTGTTTCCGATCAGGCCACAGAGGGACTGTCGAGAGACCAGTAGTAGCAAGAAAGTGCACCGATTGGTTTGTATGAATAGCGCTGTACTCACATACGAGAAAGGCGTCAGGCGCCAAGGGCCAACAATTCCGAGGGTCTGAATTTACAGCCGGAAGTCTAATCACTCAATGGACTAAGACACTAGTCAAGTGCATATAGCACCGATTGATAACTGGCTTCTTTTGCACTTGCTTCACAGATAAAGTAGAAGATACGACAAGCAAAGCAGAACGTGGACACAGAGAACTCACATGAAGGGGGGTTGCCCTTTGTCAGATCCTAGGTATGGTCTGCAGCAGGAAGCATATCAGCTTATGGAATTGTGGTGATGGAGTAGTAATAATTCCTTATGATACTCCCATTTTACATCGTCGCTAAGGGATCTGACAGTTCCAAGAGTTATCGATCACTAACTGGCTCACACTGTTAAATCAACATTGGGAGTATACACTAGGTACCCCTCGGACAGCCAGACACGCGCCCAGTGACTATGGGCTAAGCATTTATCGCCTGCACGAACGGGTGTGACGGCGTGTATCCGCCCGCTACTGTGTTCATAGGCGCAATTCCTGGAGACTAGTCAGGTGCAGCAGGGGGAAACTATCGAACATATCCGATCCTGTCGTACTAAAGAAATAACCTCACTGGAAGAGGGTCCCCTGTCAACAACACGAGTGTTGGCCTGGCCAATGTACGAGACCACTGATGTAGTAGGCGGGTTTTGTCCTGCCCCTTGATCGTGGGAAAGCTACAGCGTCGACTCAGTACGACACGGGACAGCCGGTAACCAACGTATGCTCACACGTGAGGCCTCGCCGGCTCTTTCGCAGAGAATAACAGCTATTTCGTGCAGCAGTAGTCCGGCTAACGCCTTCCCGCTCCTCTGGCGTCTAGTACCGCCAATTTACCACCGGGTTTTTGATGCGCTATCTACGCGATATTCCTATTAGCTCTCCAGCCCGGACGCGTGAGTCCATCCAATACATGTAAGTCTATAAGTGAGTTATACTAGCGTCTCCCTAGCTAGAGGAGCCCCGTCGCTATCAGTACTGTGCACATCGGGCTGCACCTTCACGGCAGTACGGTAGCCACAGACAACTTAAAGCGTACTTTGCACCGCGACTACGGCGGAGTAAGCTCCTGTATGGGACCTGAACGTTGTATTTGCTCGCCCGAGAATCCATAGCACCATATCTACTATTCGCAATCGACCCCATTCATTTATCTGATGGTCAAGCTTTAGCCCGGACCATGCCACTGCCGATGGCGACCCACACTAAGGACTCGCCACCCTGTCTGTACCCCTATCAGTTGATTGTTGTGTAGTATCGCCCCCGAAAGATCCATTGGTTTCCTTCAGAGAACGCGCAAGCTCAAGAAGGCTGCCTCAGACTGGTAAAGAGACTCAGTCTAACCTCCAAACTACTCGGACTATACCGGTAAATCGACTTGTGCCAGCCTCCGGCACTCCACATTCCGAGTTTTTTTCATGGCCTTCATGACTGCTTCGTGTAATAGACTTTGAACCGTCCCTCTACCGCTAAGGCCGAATCCGGCAGTGCAACCCTTAACGCAAGACGCGCGTTCGTCTCGATCAGATGTCCATCACCCACCATAGCATGAGATATCTAGGTGATCGGATGAATTTCTTAAGGTAAGTATTGCTGTGAGTCAATGTTGCGGTAAAGCAGGGCCGTTTCTGCAGTTATGACGACCGACTAGGCGGTATTCACGGCTTAATCATGTTCACGTTCACAACTAAATCCCCTTATAACCCCCTCACTGGCCGCCTACCGGTTTGACGAATCCAAGCCACACCACCGACTGAAGGGCTCTACGATTAGTTGAATTTCGGAGAAATACCACGCCCACAGTGGGCCTAGCGGGCGCTCTCCTCCTGCATCTCTCGACAATACGATACGCGGCCCGCGCTCTGCGTGTCCCTATGAAGCGTTTGGGATGGTGGCCCTATGGGGAGAACGTGCAAGCCCAGCCAGGCTTGAACGACCATGCGGCAATACGGGCCTGACAACTTTACGATCGTACTGACGTAAGCGCCGGTTCGGCCGTCCGTAAAGAGGCCGCTATGTCGGGCACAAATGCAGTGCTTATCGGGAATCTTTATAGTCTGACTTACAGACTTCTTAGCAGGTCGTCTCCTAATAGAAGGGTACGCGTTCCTTCGCATAGGATGAGCAAAGGTGTTTATCTCAGTGACGTCAAGAGCCACACCCGGGGCGGCCGTCACGCGGCACAACTAGCGTCCAACACTTGACCCCAGAATTGGCCTGCAAGCGAGTCATAGGTTCACGCGTCCATACTTAGAGACAGATGGTTGCCTTGTAGTGTTTTCATGAATGATACAATCAATGGTTGAGATGTCTGTTTGTGGTGTTATAGCTTTCGCTTTCATGGTAGTTATTTAATTCACCGGAGAATCAAGCCTTGTCTCGGGCGTGCTTTCGCCTTCAGGGAGATGTGGATTCCTATTAGATTCGTTTATAGCGCCAGAAATACGTAATATTAACCTTTCTTCGATCAAACAGAATTAAATGCTCTGAATGTACAACTTTGTCACCGAGGCGGAACGGCTGTTAACTATGTCTTGCTGACAAGCGTTCCGCGCCGACCAGCACACTAGGGACGTTAGACACCTCAGATCGTGACAGCCAGCATGCTTTGGGATAGGACTCAGACTGTTGTCACAATCTACGGTCATAATTCGAGAACTTTATTTGGAGGAACATATGGGTTGGAAAAATCTACGGTAGCTCTTACAATGCTAGCGTCCTCGTAGACTTTGCCATATGTATGCCGTCCTACGAAGCCTTTGTACTGAGCAAGTGAGTATGAAGAAAAAGACGTTCCTAGCTTAAATTAAACTAAACCGGATGTGGTCAGCTTAGGACCTGTCTGAACATCCTCAATGCCGCGGTGAGATGCGACCTATAAGCAAGTAACGTGCGAACTGGCCATTGCCAACATTTTGGCCCTGACTGGAGCTGTGCCCATTGAGATTAGCAGTGGTTTCCGGATAGCTGAATTCGGTCCGGCAATGTACAAACGCTGTTATATACTTTCGGCCGGTTCCACCGTACCTGAATTCGATAACGTACGTGTTGCGTCTGAGCTGCGATTCGCGAATCAGCTCCCCGAAACTGCACGGTAATCGTGCTCTACCATAAACTAATAACATTCTCCGCAACGCGGCCCAGGTTAACGATCCGCTAGACCAATGACGTAACTAGTCTCAAGCGAAGATGGCCCTAACCTGCGCATCTCGCCATGCCGGCCTATGGAAGCAAACTCGCTCGCGCCCCTAAAATGGCTCGGCTTTTCTTACGGCCAAACACACTTAGAGTTAGGTTACAACTTTCTCTAAGCAGTCAAACCTTACAGGTCGTATCTGTAGAAGGGTTCTGCGAAATAACAGCCTTAACATTCGAGCACCTTACGCCAAAACTCACGGCGGAGCTTTCTCCATTCTATAAGCCCTATAAACCTTCGACCTCGTACCATAACGTGCCTCGACCTTACCATCTTACTCATCACATCCTGATTGGAGAGTAGGCCATCGCAGAGCGACAGGTGCGGTGGTGGATTTTGTTCTTCAGAGAACGCGATTATATTCCATGCCGTTTCGAGAACTCCACCATTCGACAATGCGCTCGCGGGAGGTACCGGTATAGCACGAGCACACGCTTAGCACAAAATCGTTGGGACGCATGGTCGGGCTACTCGCCACTATTGAGAGCAGTGTCGCGTATCCTCCGCCCGGTGTTCCTGTTAAGTGATCGCTTGGTATTGCCGACCACATTATTAGAGCACCGGCACTGAGGGGTGATCGAGGTAGGATCCAAAGGAAATCCACCACCGTTTTTTACGCCTCATGGATTTTTTCATGCGTCGCCACCTTTAAGCGCCTGGGGGCCGCTCGGGGCCAAGTCATCGAACGAGTAGGTCGGGTCCACCAACCTGCCGAAGGATTCATATAACATTGCCGTTGGTTCTCAGTAGCAAGATACGAACGAACAGTAACGTCCGCAAAGGACGACCCGGACATGAATTTCTAACCTCAAGACGAACTTAGTGCAACTACAGACTCTTGTCACTTCACGAGATTATTGCCCGCTCAACACTTAAACGGGATTCATGCAGGTGAAAAATCCAATTGGTGTATAAGAATAGTTCGTCCTTGTTTTGACCGAGTTATGCGAAATGTGATGTTGGCTGTATCTAAGGCCCGGAGATCTATAAGACTCTACCCTCTTGTTGGACGTTTAATGGCTATCTGAAATCCGCTGTTGGAATAAGGAGCCCTGATCCTTTCATTCAATGGTGCGTATAGACGCCGTTGCTCGTCTCCTCAAGCTCGCGAGTAATTGGTCTGAAAGCACGGCGTCAATTCGTTTCTATGTCCTCGATTGAGACCTTTGTGGATTCGGGTCCACGCCCCAGTAGTTAACTGACAGCCGCTTCCAGGGTCCCCCTATGTAAGACCGTATTCGGTAGCGTACCGGACTTCAGATCAGTTAGCGTGCTCCATTGGCGTAAGGAGACTTGGACAAACGATGTCGTTGGGGCTATTAATTTTCATCTCACCGACTGGAACCTTCTTGGGATTACATCAATTCCCAGACACATTGCACCTCCCGTTCGATTAGATCAGGTTACTCACTGTAGATAATCGCCATTCTCCTCGTACAGGTATAAAACAGCTAAAGTGACCAGGTTTCGGCTAAATTCCTAGCCAATGTAAGAAGAGCCTCCTACCACCTATTAGTTAAAAACAGGTCCGGGAACGATATAAGCCCCTGTTGGGCCGGCTTTGCTATTCATGCATAGTCGATCCGTCCCATTAGCTGCCCGCGAGTCTACGCCGGGAGGCGTAGTGAGTCGCAATACTTCCCTGATACATCCTCTCATAGAACAGCATTGAGGTCACTGGAGACCATTCACGCTTGGCATTCTGTTGTTTCAGAATAGCTAAATAGAAACCATCCGTAAAAAGACGGCGCTGGCACAAATGCCTTGCGAAAACCATCCACTTACCCGACTAGACCCTCCGAATTTTTCAATGCATATCCCAGTATCCAGCGCGCCTAACACCACTCTGGAGCCCGGACCCACATAAGTGTCGCCGGTTTAGACGAGGGTCGCGAGCCTGAGGTGAAGCTCAAGCATCTTGCTGGCCAGACCTTTGCACTGCCTCCCAAGCAAGCATCGCCCCCAATACAATCTGGTGATCATCCCGGGAATGCAGGCTGACCGATTCGCCACAGACACGGTATCGCAAGCTTAACTTGGACTCTGTCTCTTAATTCGAAACCTTCAGGTCTCAAAAGCTAAACAGTATGCGGTGCGCTTCTGTAGAACCACTGAGTCCGGTTTGGGCGTGAGGTCAAAGTACGGCATGAGCGCGATATATTGGATGCTCAAATTTAGGTATCAATCTTGAAAGCCTAGTTACACCAAGTGCCCTACAGAGTTTATGGCACGGTTTACTGATAGCCGTTGCCGAACTTTGGGTTACTCGTCTTCCCGTGATAGCAAAGCGACCTACGTTAATCGGAACATCTCGTTGCATGGGCGACGGCCGGGGGGCTAAATTTTACTCGAGAGCACCAGTATCCTGGCACTCGACTAATTTGTGAAAATCGGGTGAAGATCACCATTAAACGCCATCCATAGGGTTTCCTTACTCACCTGCGAGTACAAAGTCCGCTTCAACATTTAATATCCTAAACCCGACTCACCCTAGTGTGATAGTATTTACCGGTTAAAGTGTATCCCTGACACCGTGATTGTATCGCGTGCCCTTTTGGGTCCGGGCCGAAATGAAGATAACTACATATGTGGGCCTAACAAAGCGGTATTTTTACTAACGGATCTGAATTTTTGAGTCGCCAGACGAATCTCGGTGCCACACCGGGCTGTCCATTAAAGGCTCGCTCCAGGCAGAGTAGTTTGCGATGACATGCATACTGGTCTAGACATTCGTTCGTGCTCCGTTTGGAAAGGGCGGTCGGAAACATAGTCCTCGCGTCAAGGCTAACGCCTTGGTGTATTTGGGAGTATTGTTCCGCTCGGAAATAAGGACCGGTCCAGTCCGCATACATGAAACTTTCCCCTATACTGGAATTCCAACGCATGGGTCGACCGGACTAGGAGCTGAATACCCTACGTTTCACACAGCATGGATTGAATTAGTTGCTATATTGGGTAACCGTCAGTGTCTGGGCTAAGCACTTCCATATTAAACGAGTAACCGTTGACTTAGCTCAAATCGCACAGGGAGAGTGCCTAGCGAGAGATCTAATTGAGTTCCGGTTGGATGATACACTTTGATCGTAGGCCTGAACGGTCCACACGGCACTATGGCTTGGGCTTGAAGCGCTTACAACTTGTAACCCTTGGAACTAGAGTTCTAATGCGAATGACGTCGACACTAGTGGCCCTACAAAATGAGTTCGCTCGACAGCTAATAACTGCGTAGTGCAACGAACGTTCGTCCGATATTGTGACCATGAGAGCTCAACTCCTAACCAAACTCTTGACCCGGAAGAGTTGGAACTGCCAGTAGCTGGAGTGCATCAGTTTAGTACACCAGGCTTTATGCACCAATATTGAAGTGCTGTATATTTCAATGTCATCTATATCCCCGCGGGAAAATGAAAGCCACAAGTTTTCGCTGGCAACTATGTTTCCAGGGGGATCCGGGCGCACGGAAGGGGAACCAGCCATCCGGGAGTATGGGTACGGCGCCCCGTGGGCTGTTGCTTAATCTCCCCTTTCCGACAGGTCGTGCAAGCGGCAGGCTTACTGATTTAAAAACGGGCATACATATTTGGAGACGTGGTTGCGGTATCTTGTCTTTCCTGCCTGAGTTTGCTGTCCCGCATGTAATCAATGGGATCGATTACAAATGGGGAGACAACAGACCGGACATAACTTAGACATATACATCCGGCAATCGTCAAAATAGGCGCCCTTTGCAATGATTGGTCCTTACACTAGCCGGCCCATTAACCGGGAATGTATTTTGGACTTTCTGGCTGTGAGATGAACTCTCGAGTGCACTAAAGCCTTAAGGACCGACATCACTCCCGCAGTGCTTTTGCTGTCCGAATGCCTGACACTTCGGTCAATCTTCATGTGAAGAGAAAGCATCTCGGCGACATCAATAGTATGGCTTACGTCATAAGCAAACGGTTACAAGAATCTACAGTTGTCCTCGACATGATTACCCGGATCCCACCTGACGGTATGCGGATTTCTGTCTGGGGTCGCGTCTCTTCATAAAGCGTCTAGCGGAGCCGCGAGAAGAGTGTACGATTTAGTAACTGCCACGTATTGCTACCTGATTTCCGCCAAGGTAGCTCTCATTCGTCGGCAGCCCACCGATAGGCATCCCTATTAGTCTCGCGAAATTTGGGCTTGGCCGGTGCTTCGAGTTAGCGCCTCCGAAACATGCGAGTACGCTATGGCCGCCACTCTGACATTCTATACAGGGATCCGGTGGATCGAACCGTATACGAGAAAGTAGACTTATGTACGGCGGTCCAATAGCTACCTAGTGATAGAGGTCCCTGGTTGCTCCAGACCGAGAGCGCCACTTCAATCCCGTTGTCAACAACGTCTCTGGGGAGAATTCAAATCCCTTAGAAGCTGTCGCGCGCCTGTGCGCCTATATCACGAAATAGTTAAAATTATCTCCTAGCAGATACAGCGGACGCTGCAGTATGCAATGCCTTCGATCGGGTACGGACACCGCTGGGACGAGCACTTTGGGGCGACTATCAATCAGGCGCACGGGCTCGTATGAACATAGGAAATTACAAACGAAAACGATCACCAGTCGAGAAATACCCGTAGAAGAGCATGTCGGCCTGAGTTTTGCCCGAATACGCGGCGCAGAACTATGTGTCATCGCAGTGTGCGTGACGTATATCGGTTGGTTATCGCGACTACCATCTTTGGAGCGCGTGGAGAACGTACCAGGACGATGTGCACGATTAGGATGCCAGCCGTTATTACTTGCTTCCCAACGGGTGTACCATAGGAAGGTGGGAGGGCCAACACGCGTACTGTTCACTGCGTTGTAGCGATGTCGGAAGATCGTAGTACGGTATTCCGCCCTTCAGAAACCCCCTGAACCAAAACAAATTGATAGTTTTATAGTAAATAAACCTGTAGAGTATGGGTTGAGCGCTAGATGTAGACTTCTTTAGTTTACCTGACAAGATGGGGGAAGACTCGTCTTCGTTAACTTGCAAATAAAATGAGAAGCACTGCTGCTACCGTATGGCGTGCCTATCCTCCATAGCAGCATTCAATTTGCTCCCGGTGACGAGGCGATTCTTACAATCG$xercises", 9)
    for tpl in lst:
        print(','.join(map(str, tpl)))