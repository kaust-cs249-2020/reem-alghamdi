"""
@BY: Reem Alghamdi
@DATE: 20-11-2020
"""
from ch1.code.ch1_11 import neighbors
from ch9.code.ch9_06 import suffix_array
from ch9.code.ch9_07 import burrows_wheeler_transform_construction
from ch9.code.ch9_13 import data_checkpoints, burrows_wheeler_matching_positions
from ch9.code.ch9_17 import partial_suffix_array


def still_good(str1, str2, d):
    distance = 0
    for ch1, ch2 in zip(str1, str2):
        if ch1 != ch2:
            distance = distance + 1
            if distance > d:
                return False
    return True


def seed_extension(i, j, k, pattern):
    a = i
    b = i + k + 1
    from_right = 1
    from_left = 0
    if i - j >= 0:
        a -= j
        from_left = -j
    if b + j <= len(pattern):
        b += j
    # print(pattern[a:b], from_left)
    return pattern[a:b], from_left


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
    with at most d mismatches (seed extension)."""
    for pattern in patterns:
        # SEED MAKING
        # print(pattern)
        n = len(pattern)
        k = n // (d + 1)
        seeds = [(pattern[i:i+k], i) for i in range(d + 1)]
        # print(seeds)
        pos = set()
        for seed, i in seeds:
            # SEED DETECTION
            positions = burrows_wheeler_matching_positions(last_column, first_occurrence, checkpoints, C, partial, seed)
            # print(positions)
            for position in positions:
                if position + len(pattern) > len(string):
                    continue
                # SEED EXTENSION
                j = 1
                extensions = [seed_extension(i, j, k, pattern)]

                while extensions:
                    triple = extensions.pop()
                    seed_pattern, start_offset = triple
                    string_part = string[position + start_offset:position + start_offset + len(seed_pattern)]
                    # print(position, seed_pattern, pattern, string_part, still_good(seed_pattern, string_part, d))

                    if string_part.endswith("$"):
                        continue
                    elif len(seed_pattern) == len(pattern):
                        if still_good(seed_pattern, string_part, d) and len(string_part) == len(seed_pattern):
                            pos.add(position + start_offset)
                        else:
                            continue
                    else:
                        j += 1
                        extensions.append(seed_extension(i, j, k, pattern))
            # print(pos)
        pos_final.extend(pos)
    return sorted(pos_final)


if __name__ == "__main__":
    print(*solve_burrows_wheeler_approx_matching_checkpoints('panamabananas$', "asa", 1))
    print(*solve_burrows_wheeler_approx_matching_checkpoints('ACATGCTACTTT$', "ATT GCC GCTA TATT", 1))
    # with open("../data/dataset_369400_10.txt") as file:
    #     data = file.readlines()
    #     print(*solve_burrows_wheeler_approx_matching_checkpoints(data[0] + "$", data[1], int(data[2])))

