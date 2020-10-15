"""
REDO USING 5.8_2
format graph using the score format
"""
from ch5.code.ch5_08_2 import longest_path_in_dag
from ch5.code.ch5_10 import blosum62_matrix, pam250_matrix, local_alignment


def two_strings_to_weighted_graph(v, w,
                                  scoring_matrix=None, sigma=None, matches=None, mismatches=None,
                                  is_local=False, is_fitted=False, is_overlap=False):
    # len_v = len(v)
    # len_w = len(w)
    # total_nodes = (len_v + 1) * (len_w + 1)
    # total_edges = len_v * (len_w+1) + len_w * (len_v + 1) + len_w * len_v
    nodes = {}
    weights = {}
    sink = (0, 0)
    start = (0, 0)
    # initialize the nodes
    for j, b in enumerate(w + "-"):
        for i, a in enumerate(v + "-"):
            nodes[(j, i)] = []
            if i == len(v) and j == len(w):
                sink = (j, i)

    # make edges
    for node, edges in nodes.items():
        if (node[0], node[1] + 1) in nodes.keys():
            weight = -1
            if sigma:
                weight *= sigma

            nodes[node].append((node[0], node[1] + 1))
            if is_fitted and node[0] == 0:
                weight = 0
            if is_overlap and node[0] == 0:
                weight = 0
            weights[(node, (node[0], node[1] + 1))] = weight

        if (node[0] + 1, node[1]) in nodes.keys():
            weight = -1
            if sigma:
                weight *= sigma
            nodes[node].append((node[0] + 1, node[1]))
            if is_fitted and node[1] == 0:
                weight = 0
            weights[(node, (node[0] + 1, node[1]))] = weight

        if (node[0] + 1, node[1] + 1) in nodes.keys():
            if scoring_matrix:
                weight = int(scoring_matrix[v[node[1]]][w[node[0]]])
            elif matches is not None and mismatches is not None:
                weight = matches if w[node[0]] == v[node[1]] else -mismatches
            else:
                weight = 1 if w[node[0]] == v[node[1]] else -1
            nodes[node].append((node[0] + 1, node[1] + 1))
            weights[(node, (node[0] + 1, node[1] + 1))] = weight

        if is_local:
            if node != (0, 0):
                if weights.get((start, node)):
                    if weights.get((start, node)) < 0:
                        weights[(start, node)] = 0
                else:
                    nodes[start].append(node)
                    weights[(start, node)] = 0

            if node != sink:
                if weights.get((node, sink)):
                    if weights.get((node, sink)) < 0:
                        weights[(node, sink)] = 0
                else:
                    edges.append(sink)
                    weights[(node, sink)] = 0
    return nodes, weights, sink


def longest_common_sequence_v2(v, w):
    # first, build the graph string
    # print("start")
    adj_list, weights, sink = two_strings_to_weighted_graph(v, w)
    # print("got adj string")
    path = longest_path_in_dag((0, 0), sink, adj_list, weights)[1]
    # print("got path")
    sequence = ""
    for index, n in enumerate(path):
        i = n[0]
        j = n[1]
        if index < len(path) - 1:  # if the next node is diagonal
            next = path[index + 1]
            k = next[0]
            l = next[1]
            if k == (i + 1) and l == (j + 1) and weights[(i, j), (k, l)] == 1:
                sequence += v[j]
    return sequence


def global_alignment_v2(v, w, scoring_matrix=None, sigma=None, matches=None, mismatches=None):
    # first, build the graph string
    # print("start")
    adj_list, weights, sink = two_strings_to_weighted_graph(v, w, scoring_matrix, sigma, matches, mismatches)
    # print("adj_list")
    cost, path = longest_path_in_dag((0, 0), sink, adj_list, weights)
    print(path)
    for index, n in enumerate(path):
        i = n[0]
        j = n[1]
        if index < len(path) - 1:
            next = path[index + 1]
            k = next[0]
            l = next[1]
            if k == (i + 1) and l == j:  # if the next is horizontal
                v = v[:i] + "-" + v[i:]
            elif k == i and l == (j + 1):  # if the next is vertical
                w = w[:j] + "-" + w[j:]
            # elif k == (i + 1) and l == (j + 1): # if the next is diagonal

    return cost, v, w


def local_alignment_v2(v, w, scoring_matrix=None, sigma=None, matches=None, mismatches=None):
    # print("start")
    adj_list, weights, sink = two_strings_to_weighted_graph(v, w, scoring_matrix, sigma, matches, mismatches, is_local=True)
    # print(adj_list)
    # print(weights)
    cost, path = longest_path_in_dag((0, 0), sink, adj_list, weights, is_local=True)
    # print(path)
    sink = path[-1]

    v = v[:sink[1]]
    w = w[:sink[0]]
    start = None
    for index, n in enumerate(path):
        i = n[0]
        j = n[1]
        if index < len(path) - 1:
            next = path[index + 1]
            k = next[0]
            l = next[1]
            if weights[((i, j), (k, l))] != 0:
                if k == (i + 1) and l == j:  # if the next is horizontal
                    v = v[:i] + "-" + v[i:]
                elif k == i and l == (j + 1):  # if the next is vertical
                    w = w[:j] + "-" + w[j:]
                if not start:
                    start = (i, j)
    v = v[start[1]:]
    w = w[start[0]:]
    return cost, v, w


def edit_distance_v2(v, w):
    # first, build the graph string
    # print("start")
    adj_list, weights, sink = two_strings_to_weighted_graph(v, w)
    # print("got adj string")
    path = longest_path_in_dag((0, 0), sink, adj_list, weights)[1]
    # print("got path")
    count = 0
    for index, n in enumerate(path):
        i = n[0]
        j = n[1]
        if index < len(path) - 1:  # if the next node is diagonal
            next = path[index + 1]
            k = next[0]
            l = next[1]
            if k == (i + 1) and l == j:  # if the next is horizontal
                count += 1
            elif k == i and l == (j + 1):  # if the next is vertical
                count += 1
            elif k == (i + 1) and l == (j + 1) and weights[(i, j), (k, l)] != 1:
                count += 1
    return count


def fitting_alignment_v2(v, w, scoring_matrix=None, sigma=None, matches=None, mismatches=None):
    """
    correct score and correct right trim .. I need to trim the left side and fix the - added
    """
    # print("start")
    adj_list, weights, sink = two_strings_to_weighted_graph(v, w, scoring_matrix, sigma, matches, mismatches, is_fitted=True)
    # print(adj_list)
    # print(weights)
    cost, path = longest_path_in_dag((0, 0), sink, adj_list, weights, is_fitting=True)
    start = False
    cut = 0
    for index, n in enumerate(path):
        i = n[0]
        j = n[1]
        if index < len(path) - 1:
            next = path[index + 1]
            k = next[0]
            l = next[1]
            if k == (i + 1) and l == j:  # if the next is horizontal
                v = v[:j] + "-" + v[j:]
                start = True
            elif k == i and l == (j + 1):  # if the next is vertical
                if not start:
                    # print("cut", v, v[1:])
                    cut += 1
                else:
                    w = w[:i] + "-" + w[i:]
                    start = True
            else:
                start = True

    v = v[cut:]
    v = v[:len(w)]

    return cost, v, w


def overlap_alignment_v2(v, w, scoring_matrix=None, sigma=None, matches=None, mismatches=None):
    # print("start")
    adj_list, weights, sink = two_strings_to_weighted_graph(v, w, scoring_matrix, sigma, matches, mismatches, is_overlap=True)
    # print(adj_list)
    # print(weights)
    cost, path = longest_path_in_dag((0, 0), sink, adj_list, weights, is_overlap=True)
    print(path)
    print(v, w)
    sink = path[-1]

    start = False
    cut = 0

    for index, n in enumerate(path):
        i = n[0]
        j = n[1]
        if index < len(path) - 1:
            next = path[index + 1]
            k = next[0]
            l = next[1]
            if k == (i + 1) and l == j:  # if the next is horizontal
                v = v[:j] + "-" + v[j:]
                start = True
            elif k == i and l == (j + 1):  # if the next is vertical
                if not start:
                    cut += 1
                else:
                    w = w[:i] + "-" + w[i:]
                    start = True
            else:
                start = True
    # print(start)
    v = v[cut:]
    # w = w[:sink[0]]
    w = w[:len(v)]
    return cost, v, w


if __name__ == "__main__":
    # print(longest_common_sequence_v2("GACT", "ATG"))
    # print(longest_common_sequence_v2("ACTGAG", "GACTGG"))
    # print(longest_common_sequence_v2("AC", "AC"))
    # print(longest_common_sequence_v2("GGGGT", "CCCCT"))
    # print(longest_common_sequence_v2("TCCCC", "TGGGG"))
    # print(longest_common_sequence_v2("AA", "CGTGGAT"))
    # print(longest_common_sequence_v2("GGTGACGT", "CT"))
    # v = "ACCGTCTTAGCGATCAACACATTTAACAACGCGCCGCACCCCCCGTCAAACGAGCTTTTGGGCTCTTGTCCTTTTACAAGCTTCACGACGCATACAGCCTTGATCAACGGTTTGATCTGTCTCCCTTCAGCTGGCTTTAAAGGACATACATATGAAGGCCTTAATAAGGTCCGGGAACTCCACATATTCGGTACTGGGCAAACCCCATGAACCACCTCAACATGAAGAGTCCGAGGACTCTCACGATCCACCAATGCAGATCGGAACTGTGCGATCGCGTAATGAGCCGAGTACTTGGTTTGTGTTTAGGTTATGGGGGCCGGGAGCCGGTTCAATATAAGGAAGTAGTTGCAGATTAGTTGTTGCGAACGGTCATAAATTTGATGGGTAAACGTGAACTTAACAAACCGTGATAGCTAATCCTATGCATCCCTTACGTGGATCGACTCGAGTACCCAGGTGAACCGACTACTTGATAACCGGAAATCGCGGTATAAAAGCGCTCACGGTCAGGAGATATACCTCCAAGCAGTAGTCTTTCTGAGCCTAGAGTAGTAAATTACAGGGACGATGTCTTTTACCGAGGCAACATTTTATTGAGAATCACATGAGGCACAGGTAAAGGCGACATCACGATCGAGATCAACCCCTACTTGTTCAAAACATTGAGAACCAGCTCTGTTTTGGAACCTAGAAAGATAACGCATCCGCTTGATATTCCACGGCTTGTCCCTCTTGTGCGGTCCATCTATCGGAGTTTCCTCCGATACGACCCGCAATGTTTCCAGGCGTACGGTACTTTATGAATACACTCGCGCTGTAACCTGTTATGTGAAACACACACGACAGAGCTTCGCGTGGGCCCAGCGACCCGGTAATACTACATCACCGCACACGACCTCGAGCAGTCTTTGCCGGCGTCCGTAAGTAGTCTAAAGTTGTGTTGATGCTTGGGGTTAAAGCTAAATCGTCCGCAGAATACGACTCTCATCCCAAT"
    # w = "ACCCGCACGCGCTTTGGTCTAGATTCTAGCTCCAACTTGCCTGCTAGATACTCTGTTAAAAGATGGTTTTACAACCCCCTCCTCTGTCCCTGGGGTATTATATAATACGTCGGATAGTCAGGTACAAATACAAGTGGGTGGGAATACTTTTCCTCGGATCCTAGACCACGGATTACTGCGTGGTTGACAAGAGTCGGCCCGGAGGGAAACGTGAAGGTTAGTGCAATTAAAGTCTCTAATGTGAAGCCTCCGCGAAGCGAGGAGTTTCTGAGATCGAGTACTATTTAGAGTTCGAAATCACGGCTTAACCTCACTGCCACGCATAACTTGCCGGCAATCCAGTTTTGCAACGATACTTAATTTGTGCAGCTCATCTTTGCTGTCCAGAAATAGAGCTAGTCGATCTCATCTTGCGGGTAGCCAGAAGTCCTACCGTCTCCTCCATGTAGCTTAAAAATTTCGGTGAGGATCAAAAATGATAAACGTGACAGGTAAGCTCCTACGTCTATCCTATGACCCCCGCGGCAGAATAGGTTGGTAGTGTTAGTGCGTGAGCTGGTAGAATAGAGCACACTTAGGGAAACGGGAACCGTTATGTAGGGCTGCGACACACAAAAAAGTGTTCGTTGGTAAGCTGCCTCTCCACTAAACAGGATTTCTCTGGATGATCCCATCGAAGCAAGTTACGCACCACGCCGAGGCGGACCCTGGTACTAGCTGCCCCCCCCTTTATGGGGCGCTCGTACATCAAGATGATCGCGGACTCAACCTGATTACGAGTTGTCCAAGTAGTCCAGGGTAAGAGAAACTGGAGAGA"
    # print(longest_common_sequence_v2(v, w))

    # print(global_alignment_v2("PLEASANTLY", "MEANLY", scoring_matrix=blosum62_matrix, sigma=5))
    # print(global_alignment_v2("GAGA", "GAT", sigma=2, matches=1, mismatches=1))
    # print(global_alignment_v2("ACG", "ACT", sigma=1, matches=1, mismatches=3))
    # print(global_alignment_v2("AT", "AG", sigma=1, matches=1, mismatches=1))
    # print(global_alignment_v2("TCA", "CA", sigma=1, matches=2, mismatches=5))
    # print(global_alignment_v2("TTTTCCTT", "CC", sigma=1, matches=1, mismatches=10))
    # print(global_alignment_v2("ACAGATTAG", "T", sigma=2, matches=2, mismatches=3))
    # print(global_alignment_v2("G", "ACATACGATG", sigma=2, matches=3, mismatches=1))
    # v="ILYPRQSMICMSFCFWDMWKKDVPVVLMMFLERRQMQSVFSWLVTVKTDCGKGIYNHRKYLGLPTMTAGDWHWIKKQNDPHEWFQGRLETAWLHSTFLYWKYFECDAVKVCMDTFGLFGHCDWDQQIHTCTHENEPAIAFLDLYCRHSPMCDKLYPVWDMACQTCHFHHSWFCRNQEMWMKGDVDDWQWGYHYHTINSAQCNQWFKEICKDMGWDSVFPPRHNCQRHKKCMPALYAGIWMATDHACTFMVRLIYTENIAEWHQVYCYRSMNMFTCGNVCLRCKSWIFVKNYMMAPVVNDPMIEAFYKRCCILGKAWYDMWGICPVERKSHWEIYAKDLLSFESCCSQKKQNCYTDNWGLEYRLFFQSIQMNTDPHYCQTHVCWISAMFPIYSPFYTSGPKEFYMWLQARIDQNMHGHANHYVTSGNWDSVYTPEKRAGVFPVVVPVWYPPQMCNDYIKLTYECERFHVEGTFGCNRWDLGCRRYIIFQCPYCDTMKICYVDQWRSIKEGQFRMSGYPNHGYWFVHDDHTNEWCNQPVLAKFVRSKIVAICKKSQTVFHYAYTPGYNATWPQTNVCERMYGPHDNLLNNQQNVTFWWKMVPNCGMQILISCHNKMKWPTSHYVFMRLKCMHVLMQMEYLDHFTGPGEGDFCRNMQPYMHQDLHWEGSMRAILEYQAEHHRRAFRAELCAQYDQEIILWSGGWGVQDCGFHANYDGSLQVVSGEPCSMWCTTVMQYYADCWEKCMFA"
    # w="ILIPRQQMGCFPFPWHFDFCFWSAHHSLVVPLNPQMQTVFQNRGLDRVTVKTDCHDHRWKWIYNLGLPTMTAGDWHFIKKHVVRANNPHQWFQGRLTTAWLHSTFLYKKTEYCLVRHSNCCHCDWDQIIHTCAFIAFLDLYQRHWPMCDKLYCHFHHSWFCRNQEMSMDWNQWFPWDSVPRANCLEEGALIALYAGIWANSMKRDMKTDHACTVRLIYVCELHAWLKYCYTSINMLCGNVCLRCKSWIFVKLFYMYAPVVNTIEANSPHYYKRCCILGQGICPVERKSHCEIYAKDLLSFESCCSQKQNCYTDNWGLEYRLFFQHIQMECTDPHANRGWTSCQTAKYWHFNLDDRPPKEFYMWLQATPTDLCMYQHCLMFKIVKQNFRKQHGHANPAASTSGNWDSVYTPEKMAYKDWYVSHPPVDMRRNGSKMVPVWYPPGIWHWKQSYKLTYECFFTVPGRFHVEGTFGCNRWDHQPGTRRDRQANHQFQCPYSDTMAIWEHAYTYVDQWRSIKEGQMPMSGYPNHGQWNVHDDHTNEQERSPICNQPVLAKFVRSKNVSNHEICKKSQTVFHWACEAQTNVCERMLNNQHVAVKRNVTFWWQMVPNCLWSCHNKMTWPTRPEQHRLFFVKMRLKCMHEYLDVAPSDFCRNMQAYMHSMRAILEYQADFDLKRRLRAIAPMDLCAQYDQEIILWSGGYIYDQSLQVVSCEGCSYYADCYVKCINVKEKCMFA"
    # cost, v, w = global_alignment_v2(v, w, scoring_matrix=blosum62_matrix, sigma=5)
    # print(cost)
    # print(v)
    # print(w)

    # print(local_alignment_v2("MEANLY", "PENALTY", scoring_matrix=pam250_matrix, sigma=5))
    # print(local_alignment_v2("GAGA", "GAT", sigma=2, matches=1, mismatches=1))
    # print(local_alignment_v2("AGC", "ATC", sigma=1, matches=3, mismatches=3))
    # print(local_alignment_v2("AT", "AG", sigma=1, matches=1, mismatches=1))
    # print(local_alignment_v2("TAACG", "ACGTG", sigma=1, matches=1, mismatches=1))
    # print(local_alignment_v2("CAGAGATGGCCG", "ACG", sigma=1, matches=3, mismatches=2))
    # print(local_alignment_v2("CTT", "AGCATAAAGCATT", sigma=1, matches=2, mismatches=3))
    # v = "AMTAFRYRQGNPRYVKHFAYEIRLSHIWLLTQMPWEFVMGIKMPEDVFQHWRVYSVCTAEPMRSDETYEQKPKPMAKWSGMTIMYQAGIIRQPPRGDRGVSDRNYSQCGKQNQAQLDNNPTWTKYEIEWRVQILPPGAGVFEGDNGQNQCLCPNWAWEQPCQWGALHSNEQYPNRIHLWAPMSKLHIKIEKSSYNRNAQFPNRCMYECEFPSYREQVDSCHYENVQIAFTIFSGAEQKRKFCSCHFWSNFIDQAVFSTGLIPWCYRRDDHSAFFMPNWNKQYKHPQLQFRVAGEGTQCRPFYTREMFTKVSAWRIAGRFAGPYERHHDAHLELWYQHHKVRTGQQLGIIWNNRDKTRNPCPFSAYYNKLPWWKINQNAFYNCLQNIAHSTHDETHEFNPVKCIDWLQGTMVPTECKKGFVHEKCECYRNPGPPLHDMYHQMEDIFGVRFDCLTGWKHLSDYNPCQERRNINDFYIFAYEIAPAVKNLVLSPQPLADATKKCAFNYTPLDQSPVVIACKWYIHQPICMLLIVLICAMDKYNAHMIVIRTTEGQQPMHACRMTEGPGMCMKEPLVTFTLPAQWQWPNHEFKYVYMYVLNYHLSQYTYTDEGHAGGQHYSFNVAVDVGMAWGHNRCYCQPACYSQQETQTRTIDYEKWQYMKHQAFKWGLWFCEQERHAWFKGQNRCEMFTAKMTRMGADSNLDQYKLMLAQNYEEQWEQPIMECGMSEIIEIDPPYRSELIFTFWPFCTYSPWQNLIKCRCNNVIEEMDQCVPLTFIGFGVKQAGGIQAWAFYKEEWTSTYYLMCQCMKSDKAQYPYEIILFWMQPMDTGEQEPPQQNMWIFLPHSWFFDWCCNAPWSEICSSRHDHGQCQDAFYPCELFTVFDDIFTAEPVVCSCFYDDPM"
    # w = "WQEKAVDGTVPSRHQYREKEDRQGNEIGKEFRRGPQVCEYSCNSHSCGWMPIFCIVCMSYVAFYCGLEYPMSRKTAKSQFIEWCDWFCFNHWTNWAPLSIVRTSVAFAVWGHCWYPCGGVCKTNRCKDDFCGRWRKALFAEGPRDWKCCKNDLQNWNPQYSQGTRNTKRMVATTNQTMIEWKQSHIFETWLFCHVIIEYNWSAFWMWMNRNEAFNSIIKSGYPKLLLTQYPLSQGSTPIVKPLIRRDQGKFWAWAQMWWFREPTNIPTADYCHSWWQSRADLQNDRDMGPEADASFYVEFWYWVRCAARTYGQQLGIIWNNRLKTRNPCPYSADGIQNKENYVFWWKNMCTKSHIAFYYCLQNVAHYTHDVTAEFNPVKCIDWLQGHMVLSSWFKYNTECKKLFVHEKCECYRMFCGVVEDIFGVRFHTGWKHLSTAKPVPHVCVYNPSVQERRNINDFYIFYEIAPAVKNLVLSAQPLHDYTKKCAFNYTPITITRIISTRNQIIWAHVVIACQFYSPHQMLLIELAMDKYCADMNVRRSTEGHQPMHACRSTFGPGMAAKEPLVTFTLVAFWQWPNHEFQYVYMYTEDKIIQIGPHLSNGCEMVEYCVDCYAKRPCYRAYSAEAQYWRMITEAEDYSYKTRNAIAATATVRGQYCHPFRWLGIVWMAHHDCFFANECGTICIPQMAEMRPPETTPYEIDIIFMMFWKEHMSTTILDVVGMYRPATFSHWHDAHHQCEPYLTPLMCQSKLVFDAAFTQVGVKGVWYHTEKLELMAGFNHMKFKKEEAQQSCFYWFQDCPDYDPPDAVRKTDEKHIRAHGEIWWLMRYYCMYHILHIASRHEWMHLRWDQACTNPGYELFEFIPWVLRRYVVYDKIRYNYSYRNSASMEFV"
    # cost, v, w = local_alignment_v2(v, w, sigma=1, matches=2, mismatches=3)
    # print(cost)
    # print(v)
    # print(w)

    # print(edit_distance_v2("PLEASANTLY", "MEANLY"))
    # print(edit_distance_v2("GAGA", "GAT"))
    # print(edit_distance_v2("GACT", "ATG"))
    # print(edit_distance_v2("AC", "AC"))
    # print(edit_distance_v2("AT", "G"))
    # print(edit_distance_v2("CAGACCGAGTTAG", "CGG"))
    # print(edit_distance_v2("CGT", "CAGACGGTGACG"))
    # print(edit_distance_v2("GGACRNQMSEVNMWGCWWASVWVSWCEYIMPSGWRRMKDRHMWHWSVHQQSSPCAKSICFHETKNQWNQDACGPKVTQHECMRRRLVIAVKEEKSRETKMLDLRHRMSGRMNEHNVTLRKSPCVKRIMERTTYHRFMCLFEVVPAKRQAYNSCDTYTMMACVAFAFVNEADWWKCNCAFATVPYYFDDSCRMVCGARQCYRLWQWEVNTENYVSIEHAEENPFSKLKQQWCYIPMYANFAWSANHMFWAYIANELQLDWQHPNAHPIKWLQNFLMRPYHPNCGLQHKERITPLHKSFYGMFTQHHLFCKELDWRIMAHANRYYCIQHGWHTNNPMDPIDTRHCCMIQGIPKRDHHCAWSTCDVAPLQGNWMLMHHCHHWNRVESMIQNQHEVAAGIKYWRLNRNGKLPVHTADNYGVLFQRWWFLGWYNFMMWHYSLHFFAVNFYFPELNAGQMPRFQDDQNRDDVYDTCIWYFAWSNTEFMEVFGNMMMYSRPMTKMGFHGMMLPYIAINGLRSISHVNKGIGPISGENCNLSTGLHHYGQLRMVMCGYCTPYRTEVKNQREMISAVHCHQHIDWRWIWCSGHWFGSNKCDLRIEDLQNYEPAKNKSNWPYMKECRKTEPYQDNIETMFFHQHDLARDSGYIANGWHENCRQHQDFSNTFAGGHKGTPKGEHMRRSLYVWDTDCVEKCQWVPELFALCWWTPLPDGVPVMLGTYRQYMFGLVVLYWFEVKYSCHNSWDYYNFHEGTMKDSDPENWCFWGMQIIQFHDHGKPEFFQDPMKQIIKTECTAYNSFMMGHIGKTTIVYLVSYIGRLWMKSCCLTWPPYATAPIKWAEETLLDFGQGPHPKYACHFTHQNMIRLAKLPMYWLWKLMFHE", "GMWGFVQVSTQSRFRHMWHWSVHQQSSECAKSICHHEWKNQWNQDACGPKVTQHECMANMPMHKCNNWFWRLVIAVKEEKVRETKMLDLIHRHWLVLNQGRMNEHNVTLRKSPCVKRIMHKWKSRTTFHRFMCLMASEVVPAKRGAQCWRQLGTYATYTVYTMMACVAFAFEYQQDNDNEADWWKCNCAFVPVYFDDSCRPVVGAFQCYRLGLPFGTGWNYAEENPFSKLKQQMHRKTMGECKNMMIWAYCANELQLPIKWGSMYHEHDFQLPPYHPNRFHKIRITILHKSFYGMFTQHHLFCKELDWRIMAWANRYYCIQHGWHTNNPDDPITRHKCMIQGGQNSRNADIRHMPVQCGNWGHAIGLEMPMPMHHCHHANRVESMIQTQHYWGPKLNRNADWWFLGWQNFEIFRMPILRWMGAYEWHYSLHFFAVNFYFPELNAGQMPRFQDDQNNNACYDVWAWSNTEFMEVNGIKKLRFGNMMMYSRPMTKMGFHGMMKSRSISHVNKGIGPISGENCSTGLHHYGQLTEVKNQREMISAVHCHQHIWCKCDLRIEPAKNKGYWPYQKEFCWRKQINSRKTEPYQVAPVINIETMFFDFWYIANGMHENCRRTGHKPNPDCVEKCQWVPELFALCWWRAMPDGVPVMLGTMFGLVVYWFEVKYSCHNSLYRRVTDYYNFHEGTMKDHEVPWNWDNEHCHDHGKAEFFFQMLKIPICDPMKAIIPSTEMVNTPWHPFSFMMGHDGKTTIVYSGSYIGRLWVPSRWKPYAPANWKMPIKWAEETLLMVPHPHFTHQQLWGTTLRLAKLPMYWLWKLMFHHLFGVK"))

    # print(fitting_alignment_v2("GTAGGCTTAAGGTTA", "TAGATA"))
    # print(fitting_alignment_v2("GAGA", "GAT", sigma=2, matches=1, mismatches=1))
    # print(fitting_alignment_v2("CCAT", "AT", sigma=1, matches=1, mismatches=1))
    # print(fitting_alignment_v2("CACGTC", "AT", sigma=1, matches=1, mismatches=5))
    # print(fitting_alignment_v2("ATCC", "AT", sigma=1, matches=1, mismatches=1))
    # print(fitting_alignment_v2("ACGACAGAG", "CGAGAGGTT", sigma=1, matches=2, mismatches=3))
    # print(fitting_alignment_v2("CAAGACTACTATTAG", "GG", sigma=1, matches=10, mismatches=1))

    print(overlap_alignment_v2("PAWHEAE", "HEAGAWGHEE", sigma=2, matches=1, mismatches=2))
    print(overlap_alignment_v2("GAGA", "GAT", sigma=2, matches=1, mismatches=1))
    print(overlap_alignment_v2("CCAT", "AT", sigma=1, matches=1, mismatches=1))
    print(overlap_alignment_v2("GAT", "CAT", sigma=1, matches=1, mismatches=5))
    print(overlap_alignment_v2("ATCACT", "AT", sigma=1, matches=1, mismatches=5))
    print(overlap_alignment_v2("ATCACT", "ATG", sigma=5, matches=1, mismatches=5))
    print(overlap_alignment_v2("CAGAGATGGCCG", "ACG", sigma=1, matches=3, mismatches=2))
    print(overlap_alignment_v2("CTT", "AGCATAAAGCATT", sigma=1, matches=2, mismatches=3))
