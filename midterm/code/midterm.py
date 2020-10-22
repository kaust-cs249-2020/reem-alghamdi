from ch2.code.ch2_03 import score, motifs, profile_matrix
from ch2.code.ch2_05 import profile_most_probable_kmer
from ch4.code.ch4_02 import protein_translation
from ch5.code.ch5_10 import global_alignment
from ch5.code.ch5_extra import global_alignment_v2

if __name__ == "__main__":
#     matrix = """A C T G
# A G T C
# G C T G
# A C G T
# A G C A
# C C A G
# T G T C
# G A T G
# A T G T
# A G A A"""
#     m2 = ["AAGAACTGAA", "CGCCGCGATG", "TTTGCATTGA", "GCGTAGCGTA"]
#     m = []
#     for line in matrix.split("\n"):
#         m.append(''.join(line.split()))
#
#     print(m)
#     print(m2)
#
#     s = score(m)
#     p = profile_matrix(m)
#     print(s)
#     consensus, score2, count, profile, entropy, entropies = motifs(m2)
#     print(score2, entropies)
#     print(p, profile)
#     print(profile_most_probable_kmer("TAGA", 4, p))
#     print(profile_most_probable_kmer("TAGACGGC", 4, p))
#
#     # old entropy
#     # [1.5709505944546687, 1.721928094887362, 1.7609640474436812, 1.9219280948873623]
#     # after laplace
#     # [1.8100621371856374, 1.9287712379549449, 1.9487443319769198, 2.0632690347495855]
#     print(protein_translation("AGAUAAUACUCUUCU"))
#     print(global_alignment("ACACA", "CACAC", matches=1, mismatches=1, sigma=10))
#     print()
#     for i in range(1, 11):
#         print(i, global_alignment("ACACA", "CACAC", matches=1, mismatches=1, sigma=i))