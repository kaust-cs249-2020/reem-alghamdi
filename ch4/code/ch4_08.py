"""
@BY: Reem Alghamdi
@DATE: 17-10-2020
"""
from ch4.code.ch4_06 import expand, mass, peptide_to_masses
from ch4.code.ch4_07 import score
from ch4.code.ch4_13 import trim

"""
EDIT ALL OF THEM TO ALLOW FOR THE EXTENDED ALPHABET
"""

extended_amino_list = {'伐': 57, '伏': 58, '刑': 59, '旬': 60, '旨': 61, '匠': 62, '叫': 63, '吐': 64, '吉': 65, '如': 66, '妃': 67, '尽': 68, '帆': 69, '忙': 70, '扱': 71, '朽': 72, '朴': 73, '汚': 74, '汗': 75, '江': 76, '壮': 77, '缶': 78, '肌': 79, '舟': 80, '芋': 81, '芝': 82, '巡': 83, '迅': 84, '亜': 85, '更': 86, '寿': 87, '励': 88, '含': 89, '佐': 90, '伺': 91, '伸': 92, '但': 93, '伯': 94, '伴': 95, '呉': 96, '克': 97, '却': 98, '吟': 99, '吹': 100, '呈': 101, '壱': 102, '坑': 103, '坊': 104, '妊': 105, '妨': 106, '妙': 107, '肖': 108, '尿': 109, '尾': 110, '岐': 111, '攻': 112, '忌': 113, '床': 114, '廷': 115, '忍': 116, '戒': 117, '戻': 118, '抗': 119, '抄': 120, '択': 121, '把': 122, '抜': 123, '扶': 124, '抑': 125, '杉': 126, '沖': 127, '沢': 128, '沈': 129, '没': 130, '妥': 131, '狂': 132, '秀': 133, '肝': 134, '即': 135, '芳': 136, '辛': 137, '迎': 138, '邦': 139, '岳': 140, '奉': 141, '享': 142, '盲': 143, '依': 144, '佳': 145, '侍': 146, '侮': 147, '併': 148, '免': 149, '刺': 150, '劾': 151, '卓': 152, '叔': 153, '坪': 154, '奇': 155, '奔': 156, '姓': 157, '宜': 158, '尚': 159, '屈': 160, '岬': 161, '弦': 162, '征': 163, '彼': 164, '怪': 165, '怖': 166, '肩': 167, '房': 168, '押': 169, '拐': 170, '拒': 171, '拠': 172, '拘': 173, '拙': 174, '拓': 175, '抽': 176, '抵': 177, '拍': 178, '披': 179, '抱': 180, '抹': 181, '昆': 182, '昇': 183, '枢': 184, '析': 185, '杯': 186, '枠': 187, '欧': 188, '肯': 189, '殴': 190, '況': 191, '沼': 192, '泥': 193, '泊': 194, '泌': 195, '沸': 196, '泡': 197, '炎': 198, '炊': 199, '炉': 200}


def leaderboard_cyclopeptide_sequencing_list(spectrum, n, amino_list=None):
    """
    :param spectrum: spectrum (list of int)
    :return: highest score amino acids
    """
    leaderboard = [""]
    leader_peptides = []
    parent_mass = max(spectrum)
    leader_score = 0
    # print(parent_mass)
    while len(leaderboard) > 0:
        print(leaderboard[0], leader_score)
        leaderboard = expand(leaderboard, amino_list=amino_list)
        for peptide in leaderboard[:]:
            mass_peptide = mass(peptide, amino_list=amino_list)
            # print(mass_peptide)
            score_peptide = score(peptide, spectrum, amino_list=amino_list)
            # print(score_peptide, mass_peptide)
            if mass_peptide == parent_mass:
                if score_peptide > leader_score:
                    leader_peptides = [peptide_to_masses(peptide, amino_list=amino_list)]
                    leader_score = score_peptide
                    # print("LEADAA", leader_peptide)
                elif score_peptide == leader_score:
                    leader_peptides.append(peptide_to_masses(peptide, amino_list=amino_list))
            elif mass_peptide > parent_mass:
                leaderboard.remove(peptide)

        leaderboard = trim(leaderboard, spectrum, n, amino_list=amino_list)

    print(len(leader_peptides), leader_score)
    return leader_peptides


if __name__ == "__main__":
    # sp25 = "0 97 99 113 114 115 128 128 147 147 163 186 227 241 242 244 244 256 260 261 262 283 291 309 330 333 340 347 385 388 389 390 390 405 435 447 485 487 503 504 518 544 552 575 577 584 599 608 631 632 650 651 653 672 690 691 717 738 745 770 779 804 818 819 827 835 837 875 892 892 917 932 932 933 934 965 982 989 1039 1060 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1322"
    sp10 = "0 97 99 114 128 147 147 163 186 227 241 242 244 260 261 262 283 291 333 340 357 385 389 390 390 405 430 430 447 485 487 503 504 518 543 544 552 575 577 584 632 650 651 671 672 690 691 738 745 747 770 778 779 804 818 819 820 835 837 875 892 917 932 932 933 934 965 982 989 1030 1039 1060 1061 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1225 1322"
    # # sp = "0 97 99 114 128 147 147 163 186 227 241 242 244 260 261 262 283 291 333 340 357 385 389 390 390 405 430 430 447 485 487 503 504 518 543 544 552 575 577 584 632 650 651 671 672 690 691 738 745 747 770 778 779 804 818 819 820 835 837 875 892 917 932 932 933 934 965 982 989 1030 1039 1060  1061 1062 1078 1080 1081 1095 1136 1159 1175 1175 1194 1194 1208 1209 1223 1225 1322"
    leaders = leaderboard_cyclopeptide_sequencing_list([int(x) for x in sp10.split()], 1000, extended_amino_list)
    print(' '.join(leaders))

