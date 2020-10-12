"""
@BY: Reem Alghamdi
@DATE: 07-10-2020
"""
import numpy as np


def global_alignment(v, w, score, sigma):
    """
    given two strings and a score matrix,
    return the alignment of the strings with max score
    """
    len_v = len(v)
    len_w = len(w)
    s = np.zeros((len_v + 1, len_w + 1), dtype=int)
    backtrack = [[""] * (len_w + 1) for i in range(len_v + 1)]
    for i in range(1, len_v + 1):
        s[i][0] = - i * sigma
    for i in range(1, len_w + 1):
        s[0][i] = - i * sigma

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            match = int(score[v[i - 1]][w[j - 1]])
            # if v[i - 1] == w[j - 1]:
            #     match += 1
            options = [s[i-1][j]-sigma, s[i][j-1]-sigma, s[i-1][j-1] + match]
            s[i][j] = max(options)
            if s[i][j] == s[i-1][j]-sigma:
                backtrack[i][j] = "↓"
            elif s[i][j] == s[i][j-1]-sigma:
                backtrack[i][j] = "→"
            elif s[i][j] == s[i-1][j-1] + match:
                backtrack[i][j] = "↘"

    score_max = s[-1][-1]
    i = len_v
    j = len_w
    # print(s, backtrack)
    while i != 0 and j != 0:
        if backtrack[i][j] == "↓":  # first option si-1,j - sigma
            i -= 1
            w = w[:j] + "-" + w[j:]
        elif backtrack[i][j] == "→":  # second option si,j-1 - sigma
            j -= 1
            v = v[:i] + "-" + v[i:]
        else:  # third option si-1, j-1
            i -= 1
            j -= 1

    for i in range(i):
        w = w[:0] + "-" + w[0:]

    for i in range(j):
        v = v[:0] + "-" + v[0:]

    return score_max, v, w


def local_alignment(v, w, score, sigma):
    """
    given two strings and a score matrix,
    return the alignment of substring with max score
    """
    len_v = len(v)
    len_w = len(w)
    s = np.zeros((len_v + 1, len_w + 1), dtype=int)
    backtrack = [[""] * (len_w + 1) for i in range(len_v + 1)]

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            match = score[v[i - 1]][w[j - 1]]
            options = [s[i-1][j]-sigma, s[i][j-1]-sigma, s[i-1][j-1] + match, 0]
            s[i][j] = max(options)
            if s[i][j] == s[i - 1][j] - sigma:
                backtrack[i][j] = "↓"
            elif s[i][j] == s[i][j - 1] - sigma:
                backtrack[i][j] = "→"
            elif s[i][j] == s[i - 1][j - 1] + match:
                backtrack[i][j] = "↘"
            else:
                backtrack[i][j] = "TAXIIII"

    i, j = np.unravel_index(s.argmax(), s.shape)
    max_score = str(s[i][j])

    # Initialize the aligned strings as the input strings up to the position of the high score.
    v, w = v[:i], w[:j]

    # Backtrack to start of the local alignment starting at the highest scoring cell.
    while backtrack[i][j] != "TAXIIII" and i != 0 and j != 0:
        if backtrack[i][j] == "↓":  # first option si-1,j - sigma
            i -= 1
            w = w[:j] + "-" + w[j:]
        elif backtrack[i][j] == "→":  # second option si,j-1 - sigma
            j -= 1
            v = v[:i] + "-" + v[i:]
        elif backtrack[i][j] == "↘":  # third option si-1, j-1
            i -= 1
            j -= 1

    # Cut the strings at the ending point of the backtrack.
    v = v[i:]
    w = w[j:]

    return max_score, v, w


if __name__ == "__main__":
    blosum62_matrix = {'A': {'A': '4', 'C': '0', 'D': '-2', 'E': '-1', 'F': '-2', 'G': '0', 'H': '-2', 'I': '-1', 'K': '-1', 'L': '-1', 'M': '-1', 'N': '-2', 'P': '-1', 'Q': '-1', 'R': '-1', 'S': '1', 'T': '0', 'V': '0', 'W': '-3', 'Y': '-2'}, 'C': {'A': '0', 'C': '9', 'D': '-3', 'E': '-4', 'F': '-2', 'G': '-3', 'H': '-3', 'I': '-1', 'K': '-3', 'L': '-1', 'M': '-1', 'N': '-3', 'P': '-3', 'Q': '-3', 'R': '-3', 'S': '-1', 'T': '-1', 'V': '-1', 'W': '-2', 'Y': '-2'}, 'D': {'A': '-2', 'C': '-3', 'D': '6', 'E': '2', 'F': '-3', 'G': '-1', 'H': '-1', 'I': '-3', 'K': '-1', 'L': '-4', 'M': '-3', 'N': '1', 'P': '-1', 'Q': '0', 'R': '-2', 'S': '0', 'T': '-1', 'V': '-3', 'W': '-4', 'Y': '-3'}, 'E': {'A': '-1', 'C': '-4', 'D': '2', 'E': '5', 'F': '-3', 'G': '-2', 'H': '0', 'I': '-3', 'K': '1', 'L': '-3', 'M': '-2', 'N': '0', 'P': '-1', 'Q': '2', 'R': '0', 'S': '0', 'T': '-1', 'V': '-2', 'W': '-3', 'Y': '-2'}, 'F': {'A': '-2', 'C': '-2', 'D': '-3', 'E': '-3', 'F': '6', 'G': '-3', 'H': '-1', 'I': '0', 'K': '-3', 'L': '0', 'M': '0', 'N': '-3', 'P': '-4', 'Q': '-3', 'R': '-3', 'S': '-2', 'T': '-2', 'V': '-1', 'W': '1', 'Y': '3'}, 'G': {'A': '0', 'C': '-3', 'D': '-1', 'E': '-2', 'F': '-3', 'G': '6', 'H': '-2', 'I': '-4', 'K': '-2', 'L': '-4', 'M': '-3', 'N': '0', 'P': '-2', 'Q': '-2', 'R': '-2', 'S': '0', 'T': '-2', 'V': '-3', 'W': '-2', 'Y': '-3'}, 'H': {'A': '-2', 'C': '-3', 'D': '-1', 'E': '0', 'F': '-1', 'G': '-2', 'H': '8', 'I': '-3', 'K': '-1', 'L': '-3', 'M': '-2', 'N': '1', 'P': '-2', 'Q': '0', 'R': '0', 'S': '-1', 'T': '-2', 'V': '-3', 'W': '-2', 'Y': '2'}, 'I': {'A': '-1', 'C': '-1', 'D': '-3', 'E': '-3', 'F': '0', 'G': '-4', 'H': '-3', 'I': '4', 'K': '-3', 'L': '2', 'M': '1', 'N': '-3', 'P': '-3', 'Q': '-3', 'R': '-3', 'S': '-2', 'T': '-1', 'V': '3', 'W': '-3', 'Y': '-1'}, 'K': {'A': '-1', 'C': '-3', 'D': '-1', 'E': '1', 'F': '-3', 'G': '-2', 'H': '-1', 'I': '-3', 'K': '5', 'L': '-2', 'M': '-1', 'N': '0', 'P': '-1', 'Q': '1', 'R': '2', 'S': '0', 'T': '-1', 'V': '-2', 'W': '-3', 'Y': '-2'}, 'L': {'A': '-1', 'C': '-1', 'D': '-4', 'E': '-3', 'F': '0', 'G': '-4', 'H': '-3', 'I': '2', 'K': '-2', 'L': '4', 'M': '2', 'N': '-3', 'P': '-3', 'Q': '-2', 'R': '-2', 'S': '-2', 'T': '-1', 'V': '1', 'W': '-2', 'Y': '-1'}, 'M': {'A': '-1', 'C': '-1', 'D': '-3', 'E': '-2', 'F': '0', 'G': '-3', 'H': '-2', 'I': '1', 'K': '-1', 'L': '2', 'M': '5', 'N': '-2', 'P': '-2', 'Q': '0', 'R': '-1', 'S': '-1', 'T': '-1', 'V': '1', 'W': '-1', 'Y': '-1'}, 'N': {'A': '-2', 'C': '-3', 'D': '1', 'E': '0', 'F': '-3', 'G': '0', 'H': '1', 'I': '-3', 'K': '0', 'L': '-3', 'M': '-2', 'N': '6', 'P': '-2', 'Q': '0', 'R': '0', 'S': '1', 'T': '0', 'V': '-3', 'W': '-4', 'Y': '-2'}, 'P': {'A': '-1', 'C': '-3', 'D': '-1', 'E': '-1', 'F': '-4', 'G': '-2', 'H': '-2', 'I': '-3', 'K': '-1', 'L': '-3', 'M': '-2', 'N': '-2', 'P': '7', 'Q': '-1', 'R': '-2', 'S': '-1', 'T': '-1', 'V': '-2', 'W': '-4', 'Y': '-3'}, 'Q': {'A': '-1', 'C': '-3', 'D': '0', 'E': '2', 'F': '-3', 'G': '-2', 'H': '0', 'I': '-3', 'K': '1', 'L': '-2', 'M': '0', 'N': '0', 'P': '-1', 'Q': '5', 'R': '1', 'S': '0', 'T': '-1', 'V': '-2', 'W': '-2', 'Y': '-1'}, 'R': {'A': '-1', 'C': '-3', 'D': '-2', 'E': '0', 'F': '-3', 'G': '-2', 'H': '0', 'I': '-3', 'K': '2', 'L': '-2', 'M': '-1', 'N': '0', 'P': '-2', 'Q': '1', 'R': '5', 'S': '-1', 'T': '-1', 'V': '-3', 'W': '-3', 'Y': '-2'}, 'S': {'A': '1', 'C': '-1', 'D': '0', 'E': '0', 'F': '-2', 'G': '0', 'H': '-1', 'I': '-2', 'K': '0', 'L': '-2', 'M': '-1', 'N': '1', 'P': '-1', 'Q': '0', 'R': '-1', 'S': '4', 'T': '1', 'V': '-2', 'W': '-3', 'Y': '-2'}, 'T': {'A': '0', 'C': '-1', 'D': '-1', 'E': '-1', 'F': '-2', 'G': '-2', 'H': '-2', 'I': '-1', 'K': '-1', 'L': '-1', 'M': '-1', 'N': '0', 'P': '-1', 'Q': '-1', 'R': '-1', 'S': '1', 'T': '5', 'V': '0', 'W': '-2', 'Y': '-2'}, 'V': {'A': '0', 'C': '-1', 'D': '-3', 'E': '-2', 'F': '-1', 'G': '-3', 'H': '-3', 'I': '3', 'K': '-2', 'L': '1', 'M': '1', 'N': '-3', 'P': '-2', 'Q': '-2', 'R': '-3', 'S': '-2', 'T': '0', 'V': '4', 'W': '-3', 'Y': '-1'}, 'W': {'A': '-3', 'C': '-2', 'D': '-4', 'E': '-3', 'F': '1', 'G': '-2', 'H': '-2', 'I': '-3', 'K': '-3', 'L': '-2', 'M': '-1', 'N': '-4', 'P': '-4', 'Q': '-2', 'R': '-3', 'S': '-3', 'T': '-2', 'V': '-3', 'W': '11', 'Y': '2'}, 'Y': {'A': '-2', 'C': '-2', 'D': '-3', 'E': '-2', 'F': '3', 'G': '-3', 'H': '2', 'I': '-1', 'K': '-2', 'L': '-1', 'M': '-1', 'N': '-2', 'P': '-3', 'Q': '-1', 'R': '-2', 'S': '-2', 'T': '-2', 'V': '-1', 'W': '2', 'Y': '7'}}
    pam250_matrix = {'A': {'A': 2, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': -1, 'L': -2, 'M': -1, 'N': 0, 'P': 1, 'Q': 0, 'R': -2, 'S': 1, 'T': 1, 'V': 0, 'W': -6, 'Y': -3}, 'C': {'A': -2, 'C': 12, 'D': -5, 'E': -5, 'F': -4, 'G': -3, 'H': -3, 'I': -2, 'K': -5, 'L': -6, 'M': -5, 'N': -4, 'P': -3, 'Q': -5, 'R': -4, 'S': 0, 'T': -2, 'V': -2, 'W': -8, 'Y': 0}, 'D': {'A': 0, 'C': -5, 'D': 4, 'E': 3, 'F': -6, 'G': 1, 'H': 1, 'I': -2, 'K': 0, 'L': -4, 'M': -3, 'N': 2, 'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4}, 'E': {'A': 0, 'C': -5, 'D': 3, 'E': 4, 'F': -5, 'G': 0, 'H': 1, 'I': -2, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': -1, 'Q': 2, 'R': -1, 'S': 0, 'T': 0, 'V': -2, 'W': -7, 'Y': -4}, 'F': {'A': -3, 'C': -4, 'D': -6, 'E': -5, 'F': 9, 'G': -5, 'H': -2, 'I': 1, 'K': -5, 'L': 2, 'M': 0, 'N': -3, 'P': -5, 'Q': -5, 'R': -4, 'S': -3, 'T': -3, 'V': -1, 'W': 0, 'Y': 7}, 'G': {'A': 1, 'C': -3, 'D': 1, 'E': 0, 'F': -5, 'G': 5, 'H': -2, 'I': -3, 'K': -2, 'L': -4, 'M': -3, 'N': 0, 'P': 0, 'Q': -1, 'R': -3, 'S': 1, 'T': 0, 'V': -1, 'W': -7, 'Y': -5}, 'H': {'A': -1, 'C': -3, 'D': 1, 'E': 1, 'F': -2, 'G': -2, 'H': 6, 'I': -2, 'K': 0, 'L': -2, 'M': -2, 'N': 2, 'P': 0, 'Q': 3, 'R': 2, 'S': -1, 'T': -1, 'V': -2, 'W': -3, 'Y': 0}, 'I': {'A': -1, 'C': -2, 'D': -2, 'E': -2, 'F': 1, 'G': -3, 'H': -2, 'I': 5, 'K': -2, 'L': 2, 'M': 2, 'N': -2, 'P': -2, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -5, 'Y': -1}, 'K': {'A': -1, 'C': -5, 'D': 0, 'E': 0, 'F': -5, 'G': -2, 'H': 0, 'I': -2, 'K': 5, 'L': -3, 'M': 0, 'N': 1, 'P': -1, 'Q': 1, 'R': 3, 'S': 0, 'T': 0, 'V': -2, 'W': -3, 'Y': -4}, 'L': {'A': -2, 'C': -6, 'D': -4, 'E': -3, 'F': 2, 'G': -4, 'H': -2, 'I': 2, 'K': -3, 'L': 6, 'M': 4, 'N': -3, 'P': -3, 'Q': -2, 'R': -3, 'S': -3, 'T': -2, 'V': 2, 'W': -2, 'Y': -1}, 'M': {'A': -1, 'C': -5, 'D': -3, 'E': -2, 'F': 0, 'G': -3, 'H': -2, 'I': 2, 'K': 0, 'L': 4, 'M': 6, 'N': -2, 'P': -2, 'Q': -1, 'R': 0, 'S': -2, 'T': -1, 'V': 2, 'W': -4, 'Y': -2}, 'N': {'A': 0, 'C': -4, 'D': 2, 'E': 1, 'F': -3, 'G': 0, 'H': 2, 'I': -2, 'K': 1, 'L': -3, 'M': -2, 'N': 2, 'P': 0, 'Q': 1, 'R': 0, 'S': 1, 'T': 0, 'V': -2, 'W': -4, 'Y': -2}, 'P': {'A': 1, 'C': -3, 'D': -1, 'E': -1, 'F': -5, 'G': 0, 'H': 0, 'I': -2, 'K': -1, 'L': -3, 'M': -2, 'N': 0, 'P': 6, 'Q': 0, 'R': 0, 'S': 1, 'T': 0, 'V': -1, 'W': -6, 'Y': -5}, 'Q': {'A': 0, 'C': -5, 'D': 2, 'E': 2, 'F': -5, 'G': -1, 'H': 3, 'I': -2, 'K': 1, 'L': -2, 'M': -1, 'N': 1, 'P': 0, 'Q': 4, 'R': 1, 'S': -1, 'T': -1, 'V': -2, 'W': -5, 'Y': -4}, 'R': {'A': -2, 'C': -4, 'D': -1, 'E': -1, 'F': -4, 'G': -3, 'H': 2, 'I': -2, 'K': 3, 'L': -3, 'M': 0, 'N': 0, 'P': 0, 'Q': 1, 'R': 6, 'S': 0, 'T': -1, 'V': -2, 'W': 2, 'Y': -4}, 'S': {'A': 1, 'C': 0, 'D': 0, 'E': 0, 'F': -3, 'G': 1, 'H': -1, 'I': -1, 'K': 0, 'L': -3, 'M': -2, 'N': 1, 'P': 1, 'Q': -1, 'R': 0, 'S': 2, 'T': 1, 'V': -1, 'W': -2, 'Y': -3}, 'T': {'A': 1, 'C': -2, 'D': 0, 'E': 0, 'F': -3, 'G': 0, 'H': -1, 'I': 0, 'K': 0, 'L': -2, 'M': -1, 'N': 0, 'P': 0, 'Q': -1, 'R': -1, 'S': 1, 'T': 3, 'V': 0, 'W': -5, 'Y': -3}, 'V': {'A': 0, 'C': -2, 'D': -2, 'E': -2, 'F': -1, 'G': -1, 'H': -2, 'I': 4, 'K': -2, 'L': 2, 'M': 2, 'N': -2, 'P': -1, 'Q': -2, 'R': -2, 'S': -1, 'T': 0, 'V': 4, 'W': -6, 'Y': -2}, 'W': {'A': -6, 'C': -8, 'D': -7, 'E': -7, 'F': 0, 'G': -7, 'H': -3, 'I': -5, 'K': -3, 'L': -2, 'M': -4, 'N': -4, 'P': -6, 'Q': -5, 'R': 2, 'S': -2, 'T': -5, 'V': -6, 'W': 17, 'Y': 0}, 'Y': {'A': -3, 'C': 0, 'D': -4, 'E': -4, 'F': 7, 'G': -5, 'H': 0, 'I': -1, 'K': -4, 'L': -1, 'M': -2, 'N': -2, 'P': -5, 'Q': -4, 'R': -4, 'S': -3, 'T': -3, 'V': -2, 'W': 0, 'Y': 10}}
    # print(global_alignment("PLEASANTLY", "MEANLY", blosum62_matrix, 5))
    # v = "INAYHDYDRAVRQDMSKTPCTCMPWANEPIRRAWIIDANKSEQAYVAHMAQVMIFVVKCCRIKQRLYCQGSGKLDYLYFCFYGCHGKLKWEAKLHWPNPYILHYGYHITQEGKGFKAWEFPPVIWRKLYLHTVSVTGDSNMHFMVHARAFHDSSSMVVMELRNWSCNLDCDNMAGLAVQEPNNRPCPDITKLCCLRHEAWLNRKMEEMGMHKRTGLNFIWIFYANSSTKSCVQNRPKIGKCPAIFVYWHGLAQSWREIFAYPVGCWATFAQWRFSAIPVMPSGTFQTFKNPRDMVASLPALYGIAGAHRNSVSYYYREMYRRWFHQCAMSMPINFWYDGQKDSHMPKAELGGERPHWQQTETQIVRWDFQKWLFHMLGRIWSKNIRVCHYKPVEMYTAPEGLFMWKRVYTYMPYDNMGPVTCFPQHFRTTGNPDEEGGRALACLAEVGCWVTGYFCTLDEHEDPLELLQTDSDYHYWENKIRVDDPVTIMRFMQGISMDAVDILWSIPCLHNWWMNSYQAYFDDKNNRTAAYKGCSGIGSREMNTVPWAMIFRGYFTREQKYGSTTAFNVDCNKNPHCPDGDFQSASIKWFGQCKLIVSLTLANSMNFPDTPYRDFVTHMIADCDGVYITRSPICHRCKYFFKCKSATNHMPMEKSADHPDSWIRGLREEHYSAFRLWFGIYRMFDLWAKEKKLTKWHRWMYWLRSIPHRKMPHTDVYTGMFTKMHIPCPFALIYDQIARARYAGAVIQTDNKHQIYSNMDCINVPIP"
    # w = "INAYHDYDRAVRQDMSQWHNEPIRRAMIPDKYVFEYVACAQVMSHEFVVKHHCIKMRLYTQGSGKLDYLYFCFYGCHGKLKHANPYILHYGYHPDQYWEFPPVIWKLYLHTVSVTGDSNMHFSSSMVVMELRNWSCNLDCDNMAGLARPITLHEYWLNRKMEEYGMHKRTGLNFSWIFYAVSSTCVQIGKCPAIFVYWHAQSWREIFSHTWLWALVNVWDFAQWSPVHMIVIGFHNAIVMPSGGPPKNCVTSDQTAIAGAHRNSVSYYYREMYRRWSVEICTDGVTQCAMKMPINFWYDGQKDSHQENGIPEAHWQQTETQIVRWDFQIRVCHYRPVEMYTAPEGLFTWTWFRVYTYMPYDNMGVTCFPQHFRTTGNNDEEGGRYTLDEHEDPLELRPHYMENMLYSAIWDEMRGISMDVVDILWSINVLQCPMSYQAYFDDKNNRTAAYKGCSGIGSREMSTVYGHMCDFYPVRLGTSYRELKHIGYFTRHRNQYDQKYGSTTAFNVDCNKNPHCPDFDFQSASIKWFGLANIMNFPDFVLMMIADCDGVDITFTCKYSFARKWGSDVSKCKDATNHMPMEKSADHPEHGFGPINSLMSAFPLWFQIYRMFDLWAKEKKLTKKRWMYWSGSVDRKVRSIQSDISMFQKSYPFYARKHSMTKMHIPCPDQIARARVHTTDNKYSQGTSGHIFDCNNVPIP"
    # s_max, v, w = global_alignment(v, w, blosum62_matrix, 5)
    # print(s_max)
    # print(v)
    # print(w)

    print(local_alignment("MEANLY", "PENALTY",  pam250_matrix, 5))
    v="RWKGCTQFRHWWCHSYAWMDNKMQNDPNKATWVHHKWCDEPEKARTFRQYMWASQGIIQANDEKPDEMSTHKRDNWFMARQKYMLNLRGYRKEVFRESARVFYHKWEWFQDVGNNILTRCILILEWYLMPYSHHQRDHWCGMILFDWMLSITWDKKQHKTPIPQDCPKGCNDLSQCSIHQDLKFCASYKQGKESCISVSQVNHKHNWVNSDQAVLYRHCGNTESRGPMTRTARWGGNNRLACANLFPVNCLWIYCFSLCMEGDKMILGFTPARWHYEMPLYSFLNEQWKCVGCPQDIALHPWPYPQQGHTIYWVSTPCAQFRNWMIPFDMKKSDWCHKHNLWEGPEMDWCYTNERDIFAYNNWCRAFGITQQNWHRPNCMKEMWIFEVATCWTVGMDPEDQVQVKVARPLRAYIFWHNQQLMAWVFWRIPVVMLRMNLQVHKMKGTVPGPNLELVSYNVAWYCIWECMCNAWYAQDLIFHTVLTTPLLLYCRMCMNKMGKFFIILEYWLDLFNHIWLNDCDAVFGCRSCEIAPSNEYVCDGEATIMPHNKCWRCLKRKLATKFWYLEVGWEGMAIFWQIVDVKCIKWDSPEGEFTEGIKRRHHNMAPYSVMNGKKTDWLNVQNTMYEGWPMGWVCIHSPQWYKQEEAQRWPNNTFQIVQDYEWMAHHVVLTVGDCYIEVTYALARCMEKMDVNEEWNKRSSSPPGKFMSENAEKKTSQKALTSVWGKQPQWSQPIAQIYTHGTMRPSITDFVTQQANHNYMGLAGCWVEKQYQERHNIWYGGDAHPAIGRCCFWMCDDNQSHWLDPEVDYCWNCAVTVPAWRYYCCVDGRFWFSYGINMWHLHMFLMQPSPENYNDFHNWHYELAKPVWIPEDFMANESHNWLLSEQAIMMSSRCFQSDM"
    w="FNMAPRAHYLHLHIQVDTGTYLMIQWYNKAKCSKRQKKYSWCFDLPCTLEVNCECCAQIVVLPVRQLAKHCQVVCNPLKFVSWLPEQNKLSTCPEMAMWKMYYWHCESYTYINYIAGDALRWMRGQDQGLIIGGSGSDVFCHNIKKAKRYEWCMPCNEYMHKCAYQTLTHMEPAQGSGVQNECMIEKTAVCFMKCQNVFRETCRYLSWNWMSYTNMDREDKYDFMPSAANIFAIGNNGSPQENLYICFNRCWDPYEGTNMWGGVVQCLCFSCCPSNSLFRNWMAPFDMKKNLWEGPEMDWCYTNIHNAYNNWCRAFGITQQNWHRPNMQIFEVATCWTVGMQVKVARGLRAYIFWHNQQLANRQDHFWVFYMIWFVLATRIPVVYFQYTALFQLMNQNLQVHKMKGTVPGLVSYNSGSGPRTNMRWECIWECMCNNWYAFYQTTPLLLYCRMYMNKMGKFFIILEYWLDLFNHVFWDSGTCNSCYNMPMPFWIPMLIAPICVYVIFWERHCDTATADPEGEATIMPHTLCWRCLMYMCHRKLATKFWYLEVGWENRGPEYDMAIFWQIVDVKCIKWDSPEGEHMLSVPYVINKILNVNNAKKTDWHNVQNTMYSANITWGGCNERVMPMGVVCMHSPQPCYCDWCGDHQDMTVFNKDAAVRCKPVDCGCNAWQFLMKNYTGGMLYQIPLLTCFFSVIFAPQTKAAVAAYTMSTMWISCFKNRLSKHRACFMHAAEFNEVVCAGTGSSEYPENGKPHIYWPIIQIQMPTATFNSIGEAWSMFRTSYTCSKKGSQRVLCYKTYFLEYIMGIYLKVDIGINHSNQWRCLWVKSQEMTMAKARFAKRMARRNTSHEDHYIGMMSTGDCNANNQSTNPLVFVLPRCTDCCHPKYGIWYCGMTGHERIHQK"
    s_max, v, w = local_alignment(v, w, pam250_matrix, 5)
    print(s_max)
    print(v)
    print(w)