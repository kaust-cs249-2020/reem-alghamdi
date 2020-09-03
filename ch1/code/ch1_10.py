"""
@BY: Reem Alghamdi
@DATE: 03-09-2020
"""
from ch1.code.ch1_03 import pattern_matching_positions
from ch1.code.ch1_07 import minimum_skew
from ch1.code.ch1_08 import frequent_words_with_mismatches_and_reverse_compliment

if __name__ == "__main__":
    with open("../data/Salmonella_enterica.txt") as file:
        text = file.read()
        k = 9
        d = 1
        words = frequent_words_with_mismatches_and_reverse_compliment(text, k, d)
        print("frequent words with k = {} and d = {} are:", k, d)
        print(*words)
