"""
@BY: Reem Alghamdi
@DATE: 23-10-2020
"""
from ch1.code.ch1_03 import reverse_compliment


def shared_k_mers(k, v, w):
    kmers_positions = {}

    for i in range(len(v) - k + 1):
        v_mer = v[i: i + k]
        v_reverse = reverse_compliment(v_mer)
        if v_mer in kmers_positions:
            kmers_positions[v_mer].append(i)
        else:
            kmers_positions[v_mer] = [i]

        if v_reverse in kmers_positions:
            kmers_positions[v_reverse].append(i)
        else:
            kmers_positions[v_reverse] = [i]

    pairs = []
    for j in range(len(w) - k + 1):
        w_mer = w[j: j + k]
        w_reverse = reverse_compliment(w_mer)
        if w_mer in kmers_positions:
            pairs.extend([(x, j) for x in kmers_positions[w_mer]])
        elif w_reverse in kmers_positions:
            pairs.extend([(x, j) for x in kmers_positions[w_reverse]])

    return pairs


if __name__ == "__main__":
    # print(len(shared_k_mers(2, "AAACTCATC", "TTTCAAATC")))
    # shared = shared_k_mers(3, "AAACTCATC", "TTTCAAATC")
    # print('\n'.join((map(str, shared))))
    # with open("../data/dataset_369339_5.txt") as file:
    #     data = file.readlines()
    #     shared = shared_k_mers(int(data[0]), data[1], data[2])
    #     print('\n'.join((map(str, shared))))

    with open("../data/E_coli.txt") as e_coli:
        with open("../data/Salmonella_enterica.txt") as salmonella:
            shared = shared_k_mers(30, e_coli.read(), salmonella.read())
            print(len(shared))