"""
@BY: Reem Alghamdi
@DATE: 01-12-2020
"""
from ch4.code.ch4_04 import cyclic_spectrum
from ch4.code.ch4_06 import mass
from ch4.code.ch4_09 import spectral_convolution
from ch4.code.ch4_11 import linear_spectrum, prefix_max_array

mass_table_reverse = {57: 'G', 71: 'A', 87: 'S', 97: 'P', 99: 'V', 101: 'T', 103: 'C', 113: 'L', 114: 'N', 115: 'D', 128: 'Q', 129: 'E', 131: 'M', 137: 'H', 147: 'F', 156: 'R', 163: 'Y', 186: 'W', 4: "X", 5: "Z"}
amino_acids = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'L': 113, 'N': 114, 'D': 115, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186, 'X': 4, 'Z': 5}
integer_mass_table = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99,
                      'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114,
                      'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131,
                      'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186,
                        'X': 4, 'Z': 5}


def spectrum_graph(spectrum):
    spectrum.insert(0, 0)
    adj_list = {}
    for i in range(len(spectrum)):
        adj_list[spectrum[i]] = {}
        for j in range(i + 1, len(spectrum)):
            try:
                adj_list[spectrum[i]][spectrum[j]] = mass_table_reverse[spectrum[j] - spectrum[i]]
            except:
                continue
    return adj_list


def print_adj_list(adj_list):
    for k1, v in adj_list.items():
        for k2, w in v.items():
            print(f"{k1}->{k2}:{w}")


def all_paths(adj_list, sink, next_node, visited, paths):
    if next_node not in visited:
        visited.append(next_node)
        if next_node == sink:
            paths.append(visited.copy())
        for n in adj_list[next_node]:
            all_paths(adj_list, sink, n, visited, paths)
        visited.remove(next_node)
    return sorted(paths)


def decoding_ideal_spectrum(spectrum):
    w_adj_list = spectrum_graph(spectrum)
    adj_list = {}
    weights = {}
    for k1, v in w_adj_list.items():
        adj_list[k1] = []
        for k2, w in v.items():
            adj_list[k1].append(k2)
            weights[(k1, k2)] = w

    paths = all_paths(adj_list, spectrum[-1], 0, [], [])
    for path in paths:
        peptide = ''.join([w_adj_list[path[i]][path[i+1]] for i in range(len(path) - 1)])
        ideal = ideal_spectrum(peptide)
        if ideal == spectrum:
            return peptide


def ideal_spectrum(peptide):
    parts = []
    masses = []
    # prefix
    for j in range(len(peptide) + 1):
        parts.append(peptide[0:j])
        masses.append(sum([amino_acids[x] for x in parts[-1]]))

    # suffix
    for j in range(1, len(peptide)):
        parts.append(peptide[j:])
        masses.append(sum([amino_acids[x] for x in parts[-1]]))
    return sorted(masses)


if __name__ == "__main__":
    # string = "57 71 154 185 301 332 415 429 486"
    # string = "87 128 185 224 281 314 437 445 566 601 695 729 858 876 961 1039 1060 1168 1223 1331 1379 1487 1507 1618 1638 1746 1794 1902 1957 2065 2086 2164 2249 2267 2396 2430 2524 2559 2680 2688 2811 2844 2901 2940 2997 3038 3125"
    # print_adj_list(spectrum_graph(list(map(int, string.split()))))

    # string = "57 71 154 185 301 332 415 429 486"
    string = "113 163 184 250 298 381 426 509 525 622 638 693 766 856 869 997 1003 1084 1090 1205 1247 1276 1350 1462 1536 1565 1607 1722 1728 1809 1815 1943 1956 2046 2119 2174 2190 2287 2303 2386 2431 2514 2562 2628 2649 2699 2812"
    # string = "103 131 259 287 387 390 489 490 577 636 690 693 761 840 892 941 1020 1070 1176 1198 1247 1295 1334 1462 1481 1580 1599 1743 1762 1842 1861 2005 2024 2123 2142 2270 2309 2357 2406 2428 2534 2584 2663 2712 2764 2843 2911 2914 2968 3027 3114 3115 3214 3217 3317 3345 3473 3501 3604"
    print(decoding_ideal_spectrum(list(map(int, string.split()))))
    # print(ideal_spectrum("REDCA"))