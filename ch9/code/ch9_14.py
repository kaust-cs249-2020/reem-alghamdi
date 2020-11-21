"""
@BY: Reem Alghamdi
@DATE: 20-11-2020
"""
from ch1.code.ch1_08 import hamming_distance
from ch9.code.ch9_06 import suffix_array
from ch9.code.ch9_07 import burrows_wheeler_transform_construction
from ch9.code.ch9_13 import data_checkpoints, burrows_wheeler_matching_positions


def solve_burrows_wheeler_approx_matching_checkpoints(string, patterns, d, C=5):

    bw_text = burrows_wheeler_transform_construction(string)
    partial = suffix_array(string)
    first_occurrence, last_column, checkpoints = data_checkpoints(bw_text, C)
    pos_final = []
    patterns = patterns.split()
    """
    Theorem: If two strings of length n match with at most d mismatches, then they must share a k-mer of length k=⌊n/(d+1)⌋.
    We first divide Pattern into d+1 segments of length k=⌊n/(d+1)⌋, called seeds.
    After finding which seeds match Text exactly (seed detection),
    we attempt to extend seeds in both directions in order to verify whether Pattern occurs in Text
    with at most d mismatches (seed extension).
    """
    for pattern in patterns:
        # SEED MAKING
        n = len(pattern)
        k = n // (d + 1)
        seeds = [(pattern[i:i+k], i) for i in range(0, n - k + 1, k)]
        # print(seeds)
        pos = set()
        for seed, i in seeds:
            # SEED DETECTION
            positions = burrows_wheeler_matching_positions(last_column, first_occurrence, checkpoints, C, partial, seed)
            # print(positions)
            for position in positions:
                pattern_position = position - i
                if pattern_position < 0:
                    continue
                if pattern_position + len(pattern) > len(string) - 1:
                    continue
                # SEED EXTENSION
                string_part = string[pattern_position:pattern_position + len(pattern)]
                # print(position, position - i, pattern)
                if hamming_distance(pattern, string_part) <= d:
                    pos.add(pattern_position)

            # print(pos)
        pos_final.extend(pos)
    return sorted(pos_final)


if __name__ == "__main__":
    print(*solve_burrows_wheeler_approx_matching_checkpoints('panamabananas$', "asa", 1))
    print(*solve_burrows_wheeler_approx_matching_checkpoints('ACATGCTACTTT$', "ATT GCC GCTA TATT", 1))
    # with open("../data/dataset_369400_10.txt") as file:
    #     data = file.readlines()
    #     print(*solve_burrows_wheeler_approx_matching_checkpoints(data[0] + "$", data[1], int(data[2])))

