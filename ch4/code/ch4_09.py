"""
@BY: Reem Alghamdi
@DATE: 26-09-2020
"""
from ch4.code.ch4_06 import integer_mass_table_18
from ch4.code.ch4_07 import leaderboard_cyclopeptide_sequencing
from ch4.code.ch4_08 import leaderboard_cyclopeptide_sequencing_list, extended_amino_list


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


def convolution_cyclopeptide_sequencing(m, n, spectrum, amino_list=integer_mass_table_18):
    """
    :param m: top m elements (with ties) of the convolution
    :param n: top n peptides for the leaderboard with ties
    :param spectrum: the spectrum
    :return: A cyclic peptide LeaderPeptide
    """
    counted = counted_convolution(spectrum)
    # print(counted)
    convolution = [t[0] for i, t in enumerate(counted) if i < m]
    for t in counted[m:]:
        if t[1] == counted[m - 1][1]:
            convolution.append(t[0])
    # print(convolution)
    reduced_amino = {k: v for k, v in amino_list.items() if v in convolution}
    return leaderboard_cyclopeptide_sequencing(spectrum, n, amino_list=reduced_amino)


def convolution_cyclopeptide_sequencing_list(m, n, spectrum, amino_list=integer_mass_table_18):
    """
    :param m: top m elements (with ties) of the convolution
    :param n: top n peptides for the leaderboard with ties
    :param spectrum: the spectrum
    :return: A cyclic peptide LeaderPeptide
    """
    counted = counted_convolution(spectrum)
    # print(counted)
    convolution = [t[0] for i, t in enumerate(counted) if i < m]
    for t in counted[m:]:
        if t[1] == counted[m - 1][1]:
            convolution.append(t[0])
    # print(convolution)
    reduced_amino = {k: v for k, v in amino_list.items() if v in convolution}

    return leaderboard_cyclopeptide_sequencing_list(spectrum, n, amino_list=reduced_amino)


if __name__ == "__main__":
    # sp = "0 137 186 323"
    # sp = "0 57 71 87 99 113 113 114 128 128 147 185 185 199 200 213 218 226 227 227 234 256 284 305 313 313 326 340 341 346 347 384 398 403 412 418 427 433 439 454 460 483 490 511 526 526 531 531 546 567 574 597 603 618 624 630 639 645 654 659 673 710 711 716 717 731 744 744 752 773 801 823 830 830 831 839 844 857 858 872 872 910 929 929 943 944 944 958 970 986 1000 1057"
    # print(*spectral_convolution([int(x) for x in sp.split()]))
    # sp = "0 71 97 99 101 101 103 103 114 128 128 129 137 147 147 163 200 202 204 215 218 229 234 236 238 243 244 250 256 275 292 301 315 337 339 341 343 344 347 349 357 363 378 381 403 406 418 438 440 440 448 471 472 477 477 478 486 504 506 507 510 519 537 543 578 581 585 587 600 605 607 607 614 618 624 635 640 656 682 684 690 706 706 710 715 721 721 725 742 747 755 763 787 787 811 818 819 820 822 824 834 843 843 850 853 858 910 915 918 925 925 934 944 946 948 949 950 957 981 981 1005 1013 1021 1026 1043 1047 1047 1053 1058 1062 1062 1078 1084 1086 1112 1128 1133 1144 1150 1154 1161 1161 1163 1168 1181 1183 1187 1190 1225 1231 1249 1258 1261 1262 1264 1282 1290 1291 1291 1296 1297 1320 1328 1328 1330 1350 1362 1365 1387 1390 1405 1411 1419 1421 1424 1425 1427 1429 1431 1453 1467 1476 1493 1512 1518 1524 1525 1530 1532 1534 1539 1550 1553 1564 1566 1568 1605 1621 1621 1631 1639 1640 1640 1654 1665 1665 1667 1667 1669 1671 1697 1768"
    # print(convolution_cyclopeptide_sequencing(17, 336, [int(x) for x in sp.split()]))

    # sp = "0 87 87 101 103 113 115 115 115 128 156 174 186 186 190 216 228 228 243 243 257 277 289 301 301 314 330 343 344 356 372 376 402 414 416 417 429 431 433 459 463 471 504 517 529 529 532 534 542 546 558 591 619 619 630 644 645 645 649 657 657 673 706 720 732 732 745 747 760 760 772 786 819 835 835 843 847 847 848 862 873 873 901 934 946 950 958 960 963 963 975 988 1021 1029 1033 1059 1061 1063 1075 1076 1078 1090 1116 1120 1136 1148 1149 1162 1178 1191 1191 1203 1215 1235 1249 1249 1264 1264 1276 1302 1306 1306 1318 1336 1364 1377 1377 1377 1379 1389 1391 1405 1405 1492"
    # print(convolution_cyclopeptide_sequencing(18, 388, [int(x) for x in sp.split()]))

    sp25 = "0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322"
    leaders = convolution_cyclopeptide_sequencing_list(20, 1000, [int(x) for x in sp25.split()], amino_list=extended_amino_list)
    print(' '.join(leaders))
