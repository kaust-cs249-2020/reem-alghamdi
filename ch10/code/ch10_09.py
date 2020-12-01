"""
@BY: Reem Alghamdi
@DATE: 25-11-2020
"""

import pandas as pd
import numpy as np

pd.set_option("display.max_rows", None, "display.max_columns", None)


def profile_hmm_pseudocount(threshold, pseudocount, alphabet, alignments):
    # make alignments* and profile(alignments*) using threshold
    alignment = pd.DataFrame(map(list, alignments))
    alignment_prime = pd.DataFrame(map(list, alignments))
    profile = pd.DataFrame(data=np.zeros((len(alphabet) + 1, len(alignments[0])), dtype=float), columns=list(range(len(alignments[0]))), index=alphabet + ["-"])
    dropped = []
    for column in range(len(alignments[0])):
        for row in range(len(alignments)):
            profile.loc[alignments[row][column], column] += 1
        profile[column]["-"] = profile[column]["-"] / sum(profile[column])
        if profile[column]["-"] > threshold:
            del profile[column]
            del alignment_prime[column]
            dropped.append(column)
        else:
            profile[column] = profile[column] / profile[column].drop('-', axis=0).sum(axis=0)
    profile = profile.drop("-")
    map_col = {}
    i = 1
    for k in alignment.columns:
        if k not in dropped:
            map_col[k] = i
            i += 1
    # print(map_col)
    # print(profile)
    # print(alignment)
    # print(alignment_prime)

    # make HMM
    k = len(profile.columns)
    states = ["S", "I0"]
    for i in range(1, k + 1):
        states.append("M" + str(i))
        states.append("D" + str(i))
        states.append("I" + str(i))

    states.append("E")
    # print(states)

    # alignment paths
    paths = []
    for i in alignment.index:
        k = 0
        path = []
        for j in alignment.columns:
            if j in dropped:
                if alignment[j][i] != "-":
                    path.append((f"I{k}", alignment[j][i]))
            else:
                if alignment[j][i] == "-":
                    path.append((f"D{map_col[j]}", "-"))
                else:
                    path.append((f"M{map_col[j]}", alignment[j][i]))
                k += 1
        paths.append(path)

    # print(paths)

    # transition matrix
    transition = pd.DataFrame(data=np.zeros((len(states), len(states)), dtype=float), columns=states, index=states)
    edges = {"S": 0}
    for i in range(len(paths)):
        for j in range(1, len(paths[i])):
            if j == 1:
                edges["S"] += 1
                transition.loc["S", paths[i][j - 1][0]] += 1
            if j == len(paths[i]) - 1:
                if paths[i][j][0] in edges:
                    edges[paths[i][j][0]] += 1
                else:
                    edges[paths[i][j][0]] = 1
                transition.loc[paths[i][j][0], "E"] += 1

            if paths[i][j - 1][0] in edges:
                edges[paths[i][j - 1][0]] += 1
            else:
                edges[paths[i][j - 1][0]] = 1
            # print(paths[i][j - 1], paths[i][j], end=", ")
            transition.loc[(paths[i][j - 1][0], paths[i][j][0])] += 1
            # print(transition.loc[paths[i][j], paths[i - 1][j]])
        # print()

    # print(edges)
    for edge, l in edges.items():
        transition.loc[edge] = transition.loc[edge] / l

    transition_square_pair = {}
    # PSEUDO-COUNT PART!!!!!!!!!!
    for i in range(0, k + 1):
        if i == 0:
            rows = [f"S", f"I{i}"]
            cols = [f"I{i}", f"M{i + 1}", f"D{i + 1}"]
        elif i == k:
            rows = [f"M{i}", f"D{i}", f"I{i}"]
            cols = [f"I{i}", f"E"]
        else:
            rows = [f"M{i}", f"D{i}", f"I{i}"]
            cols = [f"I{i}", f"M{i + 1}", f"D{i + 1}"]
        for row in rows:
            c = []
            for col in cols:
                transition_square_pair[col] = transition_square_pair.get(col, [])
                transition_square_pair[col].append(row)
                if transition.loc[row, col] == 0:
                    transition.loc[row, col] = pseudocount
                else:
                    c.append(col)
            transition.loc[row, c] /= transition.loc[row].sum()
            if not c:
                transition.loc[row] /= transition.loc[row].sum()

    # print(transition.applymap('{:,g}'.format))
    # transition.to_csv("../data/10_09_t.csv", sep="\t", float_format='%.3f')

    # print("--------")

    # emission matrix
    emission = pd.DataFrame(data=np.zeros((len(states), len(alphabet)), dtype=float), columns=alphabet, index=states)
    pairs = {}
    for i in range(len(paths)):
        for j in range(0, len(paths[i])):
            if paths[i][j][1] != "-":
                if paths[i][j][0] in pairs:
                    pairs[paths[i][j][0]] += 1
                else:
                    pairs[paths[i][j][0]] = 1
                emission.loc[paths[i][j]] += 1

    for pair, l in pairs.items():
        emission.loc[pair] = emission.loc[pair] / l

    # PSEUDO-COUNT PART!!!!!!!!!!
    emission_square_pair = {}
    for i in range(0, k + 1):
        if i == 0:
            rows = [f"I0"]
        else:
            rows = [f"M{i}", f"I{i}"]
        for row in rows:
            c = []
            for col in alphabet:
                emission_square_pair[col] = emission_square_pair.get(col, [])
                emission_square_pair[col].append(row)
                if emission.loc[row, col] == 0:
                    emission.loc[row, col] = pseudocount
                else:
                    c.append(col)
            emission.loc[row, c] /= emission.loc[row].sum()
            if not c:
                emission.loc[row] /= emission.loc[row].sum()

    # print(emission.applymap('{:,g}'.format))

    # emission.to_csv("../data/10_09_e.csv", sep="\t", float_format='%.3f')

    profile.columns = list(range(1, len(profile.columns) + 1))
    alignment_prime.columns = profile.columns
    return states, paths, transition, transition_square_pair, emission, emission_square_pair


if __name__ == "__main__":

    al = """DA-
-AA
DAC
DAC
DA-
DA-"""
    profile_hmm_pseudocount(0.314, 0.01, "A B C D E".split(), al.split())
#     al = """ACDEFACADF
#     AFDA---CCF
#     A--EFD-FDC
#     ACAEF--A-C
#     ADDEFAAADF"""
#     profile_hmm_pseudocount(0.35, 0.01, "A C D E F".split(), al.split())