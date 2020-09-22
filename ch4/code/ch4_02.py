"""
@BY: Reem Alghamdi
@DATE: 22-09-2020
"""
from ch1.code.ch1_03 import reverse_compliment

genetic_code = {
    "AAA": "K",
    "AAC": "N",
    "AAG": "K",
    "AAU": "N",
    "ACA": "T",
    "ACC": "T",
    "ACG": "T",
    "ACU": "T",
    "AGA": "R",
    "AGC": "S",
    "AGG": "R",
    "AGU": "S",
    "AUA": "I",
    "AUC": "I",
    "AUG": "M",
    "AUU": "I",

    "CAA": "Q",
    "CAC": "H",
    "CAG": "Q",
    "CAU": "H",
    "CCA": "P",
    "CCC": "P",
    "CCG": "P",
    "CCU": "P",
    "CGA": "R",
    "CGC": "R",
    "CGG": "R",
    "CGU": "R",
    "CUA": "L",
    "CUC": "L",
    "CUG": "L",
    "CUU": "L",

    "GAA": "E",
    "GAC": "D",
    "GAG": "E",
    "GAU": "D",
    "GCA": "A",
    "GCC": "A",
    "GCG": "A",
    "GCU": "A",
    "GGA": "G",
    "GGC": "G",
    "GGG": "G",
    "GGU": "G",
    "GUA": "V",
    "GUC": "V",
    "GUG": "V",
    "GUU": "V",

    "UAA": "*",
    "UAC": "Y",
    "UAG": "*",
    "UAU": "Y",
    "UCA": "S",
    "UCC": "S",
    "UCG": "S",
    "UCU": "S",
    "UGA": "*",
    "UGC": "C",
    "UGG": "W",
    "UGU": "C",
    "UUA": "L",
    "UUC": "F",
    "UUG": "L",
    "UUU": "F"
}


def dna_to_rna(string):
    return string.replace("T", "U")


def protein_translation(rna_string):
    """
    transform an RNA string into an equivalent amino acid string
    :param rna_string: the RNA string
    :return: amino acid string
    """
    amino_acid = ""
    for i in range(0, len(rna_string), 3):
        _3mer = rna_string[i: i + 3]
        if genetic_code[_3mer] != '*':
            amino_acid += genetic_code[_3mer]
        else:
            return amino_acid
    return amino_acid


def peptide_encoding(text, peptide):
    """
    the DNA string GAAACT is transcribed into GAAACU and translated into ET.
    The reverse complement AGTTTC, is transcribed into AGUUUC and translated into SF.
    Thus, GAAACT encodes both ET and SF.
    :param text: A DNA string
    :param peptide: an amino acid string
    :return: all substrings of text encoding peptide
    """
    substrings = []
    k = len(peptide) * 3
    for i in range(len(text) - k):
        kmer = text[i: i + k]
        kmer_transcribed = dna_to_rna(kmer)
        kmer_translated = protein_translation(kmer_transcribed)
        compliment = reverse_compliment(kmer)
        compliment_transcribed = dna_to_rna(compliment)
        compliment_translated = protein_translation(compliment_transcribed)
        if kmer_translated == peptide or compliment_translated == peptide:
            substrings.append(kmer)
    return substrings


if __name__ == "__main__":
    # with open("../data/dataset_369290_4.txt") as file:
    #     print(protein_translation(file.read()))

    with open("../data/dataset_369290_7.txt") as file:
        print(*peptide_encoding(file.read(), "RGLNENQHC"))

    # with open("../data/Bacillus_brevis.txt") as file:
    #     t = peptide_encoding(file.read().replace("\n", ""), "VKLFPWFNQY")
    #     print(t)
