"""
@BY: Reem Alghamdi
@DATE: 26-09-2020
"""
from ch4.code.ch4_06 import expand, mass, peptide_to_masses
from ch4.code.ch4_07 import leaderboard_cyclopeptide_sequencing, leaderboard_cyclopeptide_sequencing_list
from ch4.code.ch4_13 import linear_score, trim


def spectral_convolution(spectrum):
    """
    :param spectrum: the spectrum
    :return: the list of elements in the convolution with correct multiplicity
    """
    """
    col - row
        000 137 186 323
    000 -   -   -   -
    137 137 -   -   -
    186 186 49  -   -
    323 323 186 137 -
    return: 137, 186, 323, 186, 137, 49
    """
    convolution = []
    for m in spectrum:
        for n in spectrum:
            diff = m - n
            if diff > 0:
                convolution.append(diff)

    return convolution


def counted_convolution(spectrum):
    convolution = spectral_convolution(spectrum)
    counted = {}
    for d in convolution:
        if 57 <= d <= 200:
            if counted.get(d):
                counted[d] += 1
            else:
                counted[d] = 1

    counted = [(k, v) for k, v in sorted(counted.items(), key=lambda item: item[1], reverse=True)]
    return counted


def convolution_cyclopeptide_sequencing(m, n, spectrum):
    """
    :param m: top m elements (with ties) of the convolution
    :param n: top n peptides for the leaderboard with ties
    :param spectrum: the spectrum
    :return: A cyclic peptide LeaderPeptide
    """
    counted = counted_convolution(spectrum)
    print(counted)
    convolution = [t[0] for i, t in enumerate(counted) if i < m]
    for t in counted[m:]:
        if t[1] == counted[m - 1][1]:
            convolution.append(t[0])
    print(convolution)
    return leaderboard_cyclopeptide_sequencing(spectrum, n, convolution)


def convolution_cyclopeptide_sequencing_list(m, n, spectrum):
    """
    :param m: top m elements (with ties) of the convolution
    :param n: top n peptides for the leaderboard with ties
    :param spectrum: the spectrum
    :return: A cyclic peptide LeaderPeptide
    """
    counted = counted_convolution(spectrum)
    print(counted)
    convolution = [t[0] for i, t in enumerate(counted) if i < m]
    for t in counted[m:]:
        if t[1] == counted[m - 1][1]:
            convolution.append(t[0])
    print(convolution)
    return leaderboard_cyclopeptide_sequencing_list(spectrum, n, convolution)


if __name__ == "__main__":
    # sp = "0 137 186 323"
    # sp = "0 57 71 87 99 113 113 114 128 128 147 185 185 199 200 213 218 226 227 227 234 256 284 305 313 313 326 340 341 346 347 384 398 403 412 418 427 433 439 454 460 483 490 511 526 526 531 531 546 567 574 597 603 618 624 630 639 645 654 659 673 710 711 716 717 731 744 744 752 773 801 823 830 830 831 839 844 857 858 872 872 910 929 929 943 944 944 958 970 986 1000 1057"
    # print(*spectral_convolution([int(x) for x in sp.split()]))
    # sp = "57 57 71 99 129 137 170 186 194 208 228 265 285 299 307 323 356 364 394 422 493"
    # print(convolution_cyclopeptide_sequencing(20, 60, [int(x) for x in sp.split()]))

    # sp = "0 87 87 87 113 115 115 115 128 129 129 137 147 147 156 186 202 215 216 224 228 234 244 244 262 269 271 273 275 276 323 331 349 353 358 362 362 373 375 384 384 391 391 401 410 410 449 460 468 471 477 497 499 504 505 506 520 531 538 539 548 564 586 597 607 618 619 625 626 633 635 635 646 654 660 685 720 722 733 733 741 744 746 748 750 754 772 772 775 775 783 833 835 859 859 861 862 869 870 880 887 890 901 904 906 930 948 972 974 977 988 991 998 1008 1009 1016 1017 1019 1019 1043 1045 1095 1103 1103 1106 1106 1124 1128 1130 1132 1134 1137 1145 1145 1156 1158 1193 1218 1224 1232 1243 1243 1245 1252 1253 1259 1260 1271 1281 1292 1314 1330 1339 1340 1347 1358 1372 1373 1374 1379 1381 1401 1407 1410 1418 1429 1468 1468 1477 1487 1487 1494 1494 1503 1505 1516 1516 1520 1525 1529 1547 1555 1602 1603 1605 1607 1609 1616 1634 1634 1644 1650 1654 1662 1663 1676 1692 1722 1731 1731 1741 1749 1749 1750 1763 1763 1763 1765 1791 1791 1791 1878"
    sp = "0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322"
    print(convolution_cyclopeptide_sequencing(20, 1000, [int(x) for x in sp.split()]))

    # sp = "0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322"
    print(convolution_cyclopeptide_sequencing_list(20, 1000, [int(x) for x in sp.split()]))
