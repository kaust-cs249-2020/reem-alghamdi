"""
@BY: Reem Alghamdi
@DATE: 22-11-2020
"""

import pandas as pd


def format_to_df(transition):
    df = pd.read_table(transition, sep="\t")
    return df


def probability_of_hidden_path(path, states, transition):
    path_probability = .5
    for i in range(1, len(path)):
        path_probability *= transition[path[i]][path[i - 1]]
    return path_probability


def probability_of_emission_given_path(x, alphabet, path, states, emission):
    conditional_probability_of_emission_given_x = 1
    for s, e in zip(path, x):
        conditional_probability_of_emission_given_x *= emission[e][s]
    return conditional_probability_of_emission_given_x


if __name__ == "__main__":
    # with open("../data/hmm1") as file:
    #     transition = format_to_df(file)
    #     print(probability_of_hidden_path("BBABBBAABBAAABBABBBAABAABBABBBAABBBBAAABABAABAABBB", "A B".split(), transition))

    with open("../data/hmm2") as file:
        emission = format_to_df(file)
        print(probability_of_emission_given_path("yzxxxzxyxzyyzyyyxyzzxxxyyyyyzzzxzxyzzxxyxzzyyyzyzy", "x y z".split(), "BAABBAAABAAABABBBAAAABABBABBAABABABABAABBAABBBBABA", "A B".split(), emission))

