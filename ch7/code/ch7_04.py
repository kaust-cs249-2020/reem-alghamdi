"""
@BY: Reem Alghamdi
@DATE: 21-10-2020
"""


def greedy_sorting(p):
    """
    given a permutation, sort it and count how many operations were needed.
    eg: (-1, -2, -3) -> (1, 2, 3). Return 3 (number of reversals done)
    """
    sequence = []
    approx_reversal_distance = 0
    for k in range(len(p)):
        if p[k] != (k + 1):  # element is not in its right position
            try:
                i = p.index(k + 1) + 1
            except:
                i = p.index(-k - 1) + 1
            p[k: i] = [-x for x in p[k:i][::-1]]
            approx_reversal_distance += 1

            sequence.append(' '.join(['{0:+d}'.format(j) for j in p]))
        if p[k] == -(k+1):
            p[k] = -p[k]
            approx_reversal_distance += 1
            sequence.append(' '.join(['{0:+d}'.format(j) for j in p]))
    return approx_reversal_distance, sequence


if __name__ == "__main__":
    # print(greedy_sorting([-1, -2, -3]))
    # print(greedy_sorting([1, -3, -2]))
    # txt = "-3 +4 +1 +5 -2"
    txt = "-58 +79 -97 +70 -63 -37 +36 +43 +82 +76 -65 +128 +60 +12 -75 -85 -47 -104 -129 -93 +48 -14 +99 -17 -103 -31 -80 +113 -121 -81 -102 +69 +73 -50 -106 +86 -120 +105 +78 -4 -87 +1 +25 +125 -100 +32 -29 -26 +39 -92 +107 -59 +38 +6 +91 +88 -27 -101 +42 -66 -3 +123 +19 -56 -74 +95 +9 +10 -54 -24 +23 -64 +15 +116 +20 -115 +35 +83 +22 +108 +44 -8 -49 -57 +84 +114 -127 +77 -94 -5 -11 +55 +62 -96 +122 +110 +2 -51 +45 -98 +119 +41 -68 +71 +89 -61 -111 +30 +13 +124 -33 -117 -67 +34 -46 -118 -28 +126 -18 -72 +53 +130 +21 +131 -40 -112 +90 +109 -16 -7 +52"
    prem = [int(x) for x in txt.split()]
    distance, sequence = greedy_sorting(prem)
    print(distance)
    print('\n'.join(sequence))
