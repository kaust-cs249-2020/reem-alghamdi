"""
@BY: Reem Alghamdi
@DATE: 06-09-2020
"""
import math

from ch1.code.ch1_08 import hamming_distance


def d(pattern, dna):
    distance_sum = 0
    for string in dna:
        distances = []
        for index in range(len(string) - len(pattern) + 1):
            kmer = string[index:index + len(pattern)]
            distances.append(hamming_distance(kmer, pattern))
        distance_sum += min(distances)
    return distance_sum


def kmers(dna, k):
    kmers = []
    for string in dna:
        for index in range(len(string) - k + 1):
            kmer = string[index: index + k]
            kmers.append(kmer)
    return kmers


def median_string(dna, k):
    min_distance = math.inf
    median = None
    patterns = kmers(dna, k)
    for pattern in patterns:
        distance = d(pattern, dna)
        if min_distance > distance:
            min_distance = distance
            median = pattern
    return median


if __name__ == "__main__":
    print(median_string(["GTCACGCCAAGATTCCTGAGCGCGGACAACTCCATACCGAGC", "ACAGTTGGTTCACGGTTACGTTATCTCTATTACCTGAAGCGA", "TCCCTGAAACGGTGGCGTGTAAATGCAAGAATACACTGGCGT", "CTTGAGTGAGACTACCTGGCCGTGACTACTTTCTTCGGCGTG", "GTAAATGAAGTAAGGCAATACCTGACCCCAAATAATGGCCTC", "CTTCATACTAGGGATCACTTAACGGATTAGTCCCTGGTACGG", "ATAAGATTCCTGTTGCCCGCTGGAACGCCCAGGGGTCGCTTC", "TACCTGCTAATACTCAGATTGGTATCTTCGAGCGAATAGATC", "CCCAGTTCCCTGCTAACTGGCGGCTAAACCAAGAGGTGGTCC", "AGATACTTTCTCACGGATTTTAGAACTTGTTGCCTGAACCAG"], 6))