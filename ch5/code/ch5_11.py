"""
@BY: Reem Alghamdi
@DATE: 12-10-2020
"""
import numpy as np


def edit_distance(v, w):
    """
    Edit Distance Problem: Find the edit distance between two strings.

    Input: Two strings.
    Output: The edit distance between these strings.
    """
    len_v = len(v)
    len_w = len(w)
    s = np.zeros((len_v + 1, len_w + 1), dtype=int)
    for i in range(1, len_v + 1):
        s[i][0] = i
    for i in range(1, len_w + 1):
        s[0][i] = i

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            if v[i - 1] == w[j - 1]:
                s[i][j] = s[i - 1][j - 1]
            else:
                options = [s[i-1][j] + 1, s[i][j-1] + 1, s[i-1][j-1] + 1]
                s[i][j] = min(options)

    return s[-1][-1]


def fitting_alignment(v, w, sigma=1, matches=1, mismatches=1, scoring_matrix=None):  # passed all test cases
    """
    Fitting Alignment Problem: Construct a highest-scoring fitting alignment between two strings.

    Input: Strings v and w as well as a matrix Score.
    Output: A highest-scoring fitting alignment of v and w as defined by the scoring matrix Score.
    """
    ind = (-1, -1)
    max_score = -float("inf")
    len_v = len(v)
    len_w = len(w)
    s = np.zeros((len_v + 1, len_w + 1), dtype=int)
    backtrack = [[""] * (len_w + 1) for i in range(len_v + 1)]

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            match = int(scoring_matrix[v[i - 1]][w[j - 1]]) if scoring_matrix else matches if v[i - 1] == w[j - 1] else -mismatches

            options = [s[i - 1][j] - sigma, s[i][j - 1] - sigma, s[i - 1][j - 1] + match]
            s[i][j] = max(options)

            if j == len_w:
                if s[i][j] >= max_score:
                    max_score = s[i][j]
                    ind = (i, j)
            if s[i][j] == options[0]:
                backtrack[i][j] = "↓"
            elif s[i][j] == options[1]:
                backtrack[i][j] = "→"
            elif s[i][j] == options[2]:
                backtrack[i][j] = "↘"
    # print(s, backtrack)

    i, j = ind

    v = v[:i]
    w = w[:j]

    while i != 0 and j != 0:
        # print(backtrack[i][j], end=", ")
        if backtrack[i][j] == "↓":  # first option si-1,j - sigma
            i -= 1
            w = w[:j] + "-" + w[j:]
        elif backtrack[i][j] == "→":  # second option si,j-1 - sigma
            j -= 1
            v = v[:i] + "-" + v[i:]
        else:  # third option si-1, j-1
            i -= 1
            j -= 1
    v = v[i:]

    return max_score, v, w


def overlap_alignment(v, w, sigma=1, matches=1, mismatches=1, scoring_matrix=None):
    """
    Input: Two strings v and w, each of length at most 1000.
    Output: The score of an optimal overlap alignment of v and w,
    followed by an alignment of a suffix v' of v and a prefix w' of w achieving this maximum score.
    Use an alignment score in which matches count +1 and both the mismatch and indel penalties are 2.
    """
    ind = (-1, -1)
    max_score = -float("inf")
    len_v = len(v)
    len_w = len(w)
    s = np.zeros((len_v + 1, len_w + 1), dtype=int)
    backtrack = [[""] * (len_w + 1) for i in range(len_v + 1)]
    # for i in range(1, len_v + 1):
    #     s[i][0] = 0
    for j in range(0, len_w + 1):
        s[0][j] = -j * sigma

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            match = int(scoring_matrix[v[i - 1]][w[j - 1]]) if scoring_matrix else matches if v[i - 1] == w[j - 1] else -mismatches

            options = [s[i-1][j]-sigma, s[i][j-1]-sigma, s[i-1][j-1] + match]
            s[i][j] = max(options)
            if i == len_v:
                if s[i][j] >= max_score:
                    max_score = s[i][j]
                    ind = (i, j)
            if s[i][j] == options[0]:
                backtrack[i][j] = "↓"
            elif s[i][j] == options[1]:
                backtrack[i][j] = "→"
            elif s[i][j] == options[2]:
                backtrack[i][j] = "↘"
    # print(s)

    i, j = ind
    v, w = v[:i], w[:j]

    while i != 0 and j != 0:
        if backtrack[i][j] == "↓":  # first option si-1,j - sigma
            i -= 1
            w = w[:j] + "-" + w[j:]
        elif backtrack[i][j] == "→":  # second option si,j-1 - sigma
            j -= 1
            v = v[:i] + "-" + v[i:]
        elif backtrack[i][j] == "↘":  # third option si-1, j-1
            i -= 1
            j -= 1

    v = v[i:]
    w = w[j:]

    return max_score, v, w


if __name__ == "__main__":
    print(edit_distance("PLEASANTLY", "MEANLY"))
    # print(edit_distance("GAGA", "GAT"))
    # print(edit_distance("GACT", "ATG"))
    # print(edit_distance("AC", "AC"))
    # print(edit_distance("AT", "G"))
    # print(edit_distance("CAGACCGAGTTAG", "CGG"))
    # print(edit_distance("CGT", "CAGACGGTGACG"))
    # v = "MSSKVHTCCCKMGQMENKTNQECNYQNNEHTFYCPSCDFRNSYTSGHMSQKVWMHFLVLIHFYQICARTVCVDFMNEKGTSMERWMYLHTDCHNAQHRVGSSIVVCFGCTIGAQSIGEEWCFPCLEKDWIFGHFAHYYFWISKGFCNLFLMCCNCVDYTRQFLRIHLYPRLWSQMQYRCAPHFMWYLMANVPVPEGHDYLAHGDNNKNYENQIVASSSEFTVWIIHKHRHSMLTKEWSMYAHDEYLYGCWRPCLDEEATLTNGSSELWMFEDANGWRVWLPMIQTMLIWYDPCFIIEFNGEWTLGECPKLFDQWYSWQQDFFACHHEPIHKIFSNPGVCRCKVSPCMLASLYQEAEWGFIHMTLPFKQKLSPMPAISYRYSSNWNDIIWVTDSFEEHAVFFAVYESRKNMPFPHKRFPSYRYFGHLSHDVQFVCIATFNIHFSVWGMYVFEIKPLGITIKWGQRWHKLHLHAECGPEGWRFMGDAPGLCPVNWKIMCAQQPCSDPMTGMMVKKNLFLKTFDITWVAGGGCKRMMWRWYVGCKNFEPQRVKFIKYHLNKTWEWQDDSHYSMSQSDQYNHYEDCPMNISWKWYDMSDTQAVCFMRRCCSDIKGPILHQTAAWWDLMESSIVTQWGWRQAFDWGVYREPFGVGCWVDGYMIVNPPVTGCTHWKLCNDNAGHLRGKCQNNNWYMMMSWTGPKPHPARMKHQTVTWLCYKPRQHEQTFSKDWCSWWWWDYSIDFYLNSRCRFWKTNMDGCPFGTAKAVAPTWQQHTETSKLRPQLDGNENHSVFKPTDTWWIIFNPKEEDVKVIISHCMCDHDKSAKYFDALASALWSVYIDHHRTRSE"
    # w = "DWFESQPMGIQWIRGSKVHTCCCKMGVFFFFAYCFEPAAKTNQEHTFYCPSCNFGNSNMSGHMSQFVWQHFLVLIHFYQIDISFNFARTWCVDFMNNKGTSMERWMYLHTDCANREVQHRDGSSIVVCFGCTIGAQSIFEQGMNDHNMWCFPTLEKDWIFEHFAHYYFWISKKWNIKHIGKCNDWDQHWLYYFPITRQFLRIMQYRCAPHFMWYLMIDLPNVPWLPVFYHGDNNKNYETHANHVVASSSEFTVWIIHKYRHSMLTKEWSHDELAGQCWFRWPMGVHEAWMPEDSKDENGWRVWLPMIQRMDIWYDIIEFNGEWTPKLFKQWYSWQTRVCHHELYTYPKRRIEIFIKIFSNCGVCRCHEIIMSDMDVWPCMLATRLYQEAEWGGRVGAIAVDEDLPAMTLPFKQKISPMPAISYRYSENWNDIIWVHFDSFEEHAVIFPNKRPTRRRYWNGHQFVCIPIAHFNAAGQEDPWYHASVWGMYVIKPLGITIKWGSRWHCLHLMAECFMADAPGLCPVNWKIMTGMMVKYNTTIEHDVHKPHPGFKTFDITVVCGGGTKKRVGCKNFEPQRVKFIKYHLNFTWEWQDDSHYSMSQSDQYNYYWWYDFKEEGYIDTQWVCFMRRCCSDIKGPILHVTAAWWMLMESSIVTQWGWRQVYLEPFGVGASRAGEMNPPKYNCEKVKFTHWKECINDNAGHLRGKCQNYMMHSWHPARMKHQVVTWLCEQTFSKYYAIGHFIEHWCSWHWWDYSIDWKTNMDAVAVTWQQHTETAPSGNENHPVFKPNGNTWQIVFHSCNIIFNPNEEDVKVITAEISTSLDFLPTNCGCDADDSAVCSQHLHIEINFWHKLFDAVASALWSAYIDHHYTRSC"
    # print(edit_distance(v, w))

    print(fitting_alignment("GTAGGCTTAAGGTTA", "TAGATA"))
    print(fitting_alignment("GAGA", "GAT", sigma=2, matches=1, mismatches=1))
    # print(fitting_alignment("CCAT", "AT", sigma=1, matches=1, mismatches=1))
    # print(fitting_alignment("CACGTC", "AT", sigma=1, matches=1, mismatches=5))
    # print(fitting_alignment("ATCC", "AT", sigma=1, matches=1, mismatches=1))
    # print(fitting_alignment("ACGACAGAG", "CGAGAGGTT", sigma=1, matches=2, mismatches=3))
    # print(fitting_alignment("CAAGACTACTATTAG", "GG", sigma=1, matches=10, mismatches=1))

    # print()
    # v = "CTCCGGCCACATGACGTTGCATCCTGGTGCCCGAGGCATAAACCTAGCCTCACTCGCCTCAACATCCCTTTTGGGCGCCGTGTTTATTAGAGAATGTCATCCATGGCCATTTGCGTAGCTCCCCAATGGATCGTTACATAAGCTCCTTTTACACTCAGCCAGGCGAACCACCGTAAAATTTTAGGGCGGAAGGGGGTCATCCAGGCATTCGCAGTGAGGGTATCAACCTTTTATTAACTTTGATGAATAGTACCGGACCTTGCCCTGACTTAATGAACTGTTGAATGAGGTGGGTGAGGGGACAGGTCCAAAAGTCCGGTACCAACGCCTGCGCCACCGACCGTGCAGTTGCAATAGCTTCTGGTGGATGATATTCGTACCTTGGTATATTCTTAAGCTTCGTTAGATCCGACCGACTCGCTGCTGGCAATCGAGACAGTAGAAAACGGCCGAATCCATGATGTTGCTGGGTTGCTGGTAGCTCGCGGCTGCCAGCTTCTGTCAGAGAGCGCGACAGACCGACGTGCAACAGACGTTGCTTCTCAAACGAAACCACCACTCTTGATTCCAATAATAAGCAACATGGTACATTGTGAACTGAGGCAGAAAAGGCGTATCCAGATCTTCATTACGTGATCGCCAACATTTGCAGCGGCCCTGGCGATTATAGGAGGCCATGCAAACGAACCGACGACCCCCTGAGCACTAACAGACCTGATTACATCAAACAGACAAAGTTCTGTTTGCAAGGGCCCGCTCCCGCTAGTCTTTTCCCTGAGTTCAGGTTTGTACCGGTTCTGCTAAGCAGACTGCTTATACGGAGTCCGTATACAATACCCTACTTGACAAGTTTAGGGGTCTAGTTCTCATCCCA"
    # w = "ACAACGCGTTAATGAGAGATATTGTGTTGATACGAGAGTCAAGCTCGTCCGAGCCGGTCGTTCCATCGGCTGCAGAGGGCTACATAAAG"
    # s_max, v, w = fitting_alignment(v, w)
    # print(s_max)
    # print(v)
    # print(w)

    print(overlap_alignment("PAWHEAE", "HEAGAWGHEE", sigma=2, matches=1, mismatches=2))
    # print(overlap_alignment("GAGA", "GAT", sigma=2, matches=1, mismatches=1))
    # print(overlap_alignment("CCAT", "AT", sigma=1, matches=1, mismatches=1))
    # print(overlap_alignment("GAT", "CAT", sigma=1, matches=1, mismatches=5))
    # print(overlap_alignment("ATCACT", "AT", sigma=1, matches=1, mismatches=5))
    # print(overlap_alignment("ATCACT", "ATG", sigma=5, matches=1, mismatches=1))
    # print(overlap_alignment("CAGAGATGGCCG", "ACG", sigma=1, matches=3, mismatches=2))
    # print(overlap_alignment("CTT", "AGCATAAAGCATT", sigma=1, matches=2, mismatches=3))

    # # v = "GCTATAAGAATAAACCACTAGATCACCTCCGGCTCGCTCACTCCTGATCATGGTTCGTGCTAACATCGCGCCGCGCTGACGCCGAATCGTTCGTAGGAGACAAGTCGACGACCTCATCTACAGGCAAAAGTTAAATTAGCTCTCGGCTAGATGTGACAATCGGAACCCTGCACCCTGCGTAATAGGGTAAATAGTCGGGAGTTGATGCACACACCTAGATATTGGCTGAATGACAGACTGCCATTCCTGCACTGGAAAGTAGAGTGCATATGTTTCGTGAGATTATGCAGGCTCTACGGTTATACTGGGCTCCACGGATTCGACCGGTACTGTTGATTGAAGACTCTTCTATAGAGGCTCTAACCGCGGAGGCCGCAACCAATCGACAATGAAGCACCCGTCGTCGGTATCGTTGGGAAGGACGACACCGTAAGGGCAGACTTTATCGTGACCCGTCTGCTTGCTAGAAAAGCCCTGGCGTTTGTACAACGTCCGTGCAGAATTAGCGTTTTTCTCAGGAAAGATGAGGGGGTTGATCATCATCTCGTTTCGCACGGGTCAAGCGCATTTTCCTACTGTTTTGGACACAGTACGTCTTCCACTGATCTCATACGGACATTACCAGCACCCTTTTGTACCTGTCGTAACTTGTGCCATTCTAGGCCCGTTTTCACTTGCGCTTATGATCATGGTTCCGCTGATCTATATGGGCCGGGTAGGGCACTCCCAGATGAAGGGGAGTAATGGTAGCCGGATCCAAGTGACGCGCCCTAGCGGCTCCGGAGTTTGATAGACGTCGTGCTATGGAGCGTTGGAGCGACAACGCGCTCGTGCTCTGGAAGGTCGCTGCTGATCCGTAA"
    # # w = "TACTGGTCCTGACCCACCTCACTTTGATGTCCCCTTTTCTCGTTTGCGCATCAAGATCTGGCCCGCAACTATTGGCCGTGAAAGGCACTCATCAATAAAGACAGTACTCACGCGGTCGGATCCAAATGCGCGCACCGAGCGGCCCAGGAGTTGATAGCGTCGAGTAACCTATTAGGACTCGAGGCAACTCGCGCTCTCTCAGGAGGCTCGCCTGCTAGTCCGTGAACGACGGATCTTTGGTGCTGCCTTCCTATCATGACATTGCCTAATAACGAGCGGCACCTACTCCCAGGTCTTTGAAGGGATGGCTTGTTTACCCCGATTCCGAGAAATAGAGATGACTCCTAAGGAAGTAATGAAGGAAGTTCAGTGGTATGGGTATCGTTTAGTTTGCCAGGGAGATTGCCCATAACCTAAGTCCCTAATACAGCAGTAGATCTCACCATAGATGTAGGAAAGCACAGTGATTTAGACGCTTAGCCAAATACAAAGGAATGTACCCCCTCCTAACACTGAGCACCGCTTATTTACTAGTATACTCAGAGTGTGGAGCGCTGAACGTTGTGTCAACAAGAACATAAGCCGCCGTGAATGAATTTGTGAAGGGGAGTGATCATGGTTTTACTCGTGGTAGATTTGGGCAGAACCTGATTCCTCACGTGTGAATGTAATTGAAGCTGACTCCCACACATACAGGCACGATTCTTTTAGATGATGTTTTAGGAAGCGCATTTCGTATTAACACTGCCTTGCATTTGATAACCATCACTTGTTCATTACATGATCCCATAGGGCCGTGTTGTTACTTTCGTGTTAGTCGAGCAGTATGACCACCTTTTCGGCGCTTGATATGCCTCAAGACGTGCGATTCAAGGAATCAAACAAATGAACGCCGCACTGGATGACTGGG"
    # v = "AACAGCGACCTATATAGGAGTACCGTACACGACGAACACTTAACGCGGTCTTAACTTTTAGGCATCTGTGACGCTGGGGGCTTTTGACGCTTTCGGACGGTCGTGGACGCACTTACGCTTACGACATAGCAACCGCGCTCCCGGCAACGGAAGTGCCATAATCTATCAGTGGATAGAATGTTCAGCCTCGCGAGAGGGGGCGAGATTGCTATAGACCCAGTCCTTGGAAGTCCCTCGCAAGATTCAGAGGAATGGAGTAGGACCACCACTCTGTGATAACCGTCTCGGAACGGTAAGGGAGCACAGTGTTCTCCCCACATAACATGTCGCACGTAACAGGGACGCCCATTACATCGCATGGAATGGGTATCGACTTTCGACCATTAGAGAGATGGCCGTCATTAGTGCGTGTGAGCCTCGGAGTAACATGTTCGACTATCATCTTAAGTGCGACGAGGGGTTGTTTACCTACTAGGTGTAAGCCACCCACTCTCCCTTTAGTAAGGAATTGCTCAGAACAAAAGTACCTTCCAATGAGGCAGTTACCACGCCCCGCGTTCTGAAGCCTATTGCCGTCGGTCTGTCCATCTTGCAATTGAATGTTCTCCAGAGGGACGAATCTACAATCGGCCCCGCATCATCGCTCGTTTAAGTTTCATTGGCGCCAGGCCTTAGTGAACCATAACCGCGATCCGGAAACACTTATCGTAACGTCAGCCGTCTGTACGAAGGGTTTGGTTTCGTGCGGTGTCGCGGACCTATTCGAAACCCTAACTTCTCCATGAGGAATGAGATAGTAAAAGCGCGAGCACGAGCACTTAGAAGGTTTTAGCCGACGGAAATTATTCATCTTGGGGATAACGCATGTATCTAATTTACTAACTACTTTACGACTCTATAACTTCGGCTCAGTTGGCATAGGTTCTCTTGGTGTCAGCGGCGGA"
    # w = "ATCGCCCGTCCGGAACACTATCGCCGTAGCTGGGTAAGATCACAAAGGGCTTATTTGGTGCGGTGCTCGGGACCATTCGAATAACCTAACCTCCCCAGAGGGAACTGAGATAGTAAAACCGCAATACGAGCACCTAGAAGTTGTTCAGCAAGGAATTATTTGCACCTGGGGGATAACAGCATGTGTAATTTACAACTGCTCTATGATTTCTTAATTGCGGCTCCTGTTGTATGGTTTTTGCCAGTGTGCGCATTGCGTGGACCCGAATAAACGTAAGTTGGCAGAGCTTGCGTGTACTTTCGAGTCAAATCAACATAACGCTGAGTTTTATTACGAGCATCGATCGAGCTACCTTATCAGGGATAACGTCATGCAATAATCGGGTTGCATTTTGTAATACGTATCGGTAGCGTAGGCAGGTGGTTGATCTGAAGGAGAGGGACTGAGTGGATCTGACCGTTCCGCGCCTTTCCACTGAACTGCTAGTCCCGAAGTAACGCAAGGCTGTAGGACATAAGTAACGACGATGACCTATGATGGTCTCCTTGGCCTTGAAGAAAAATCTACGCAGGAATGAGTGATAGGGGCAGTAATCAACTTGACAAACATGGGGATAAGCATATTTGGGATATAAGGGCGAGGTGTTCCCGTTAAGGATTTCTTGGCCCCCCGGAAAATCCCGTGCTCCTGAGTCTCAGAGACGAGCGCGCTCTCAGTGTCCACGGCCCAGGCAAGGTGCATATGCTAGAATGGTAGGGTAGTCCAGGTGACTTAGCTAGCGTATCTGCCCGTTTCCTGTAGTGAAAGAGCTATTAAAGCATGTGGGGGTGGTGCACAATCAATAGGTCTTAAAATCTATAAGGGTAGGTC"
    # #
    # s_max, v, w = overlap_alignment(v, w, sigma=2, matches=1, mismatches=2)
    # print(s_max)
    # print(v)
    # print(w)