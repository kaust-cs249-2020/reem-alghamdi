"""
@BY: Reem Alghamdi
@DATE: 02-09-2020
"""


def skew(pattern):
    """
    This function takes a string, then compute the value of skew after each character read.
    If G is read then its incremented,
    if C is read then it is decremented, other wise it plateaus.
    :param pattern: the string to compute skew
    :return: the arrays of skew values
    """
    cumulative_skew = 0
    skew_arr = [cumulative_skew]
    for character in pattern:
        if character == 'G':
            cumulative_skew = cumulative_skew + 1
        elif character == 'C':
            cumulative_skew = cumulative_skew - 1
        skew_arr.append(cumulative_skew)
    # print(*skew_arr)
    return skew_arr


"""
We have just developed an insight for a new algorithm for locating ori: it should be found where the skew attains a minimum.

Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.

    Input: A DNA string Genome.
    Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|).
"""


def minimum_skew(genome):
    """
    this function return an array of positions where the lowest skew is
    :param genome: the dna string genome
    :return: the position of the minimum skew
    """
    skew_array = skew(genome)
    minimum_skew_array = []
    if len(skew_array) > 0:
        minimum = skew_array[0]
        for v in skew_array:
            if v < minimum:
                minimum = v
        for index, v in enumerate(skew_array):
            if v == minimum:
                minimum_skew_array.append(index)
    print(*minimum_skew_array)
    return minimum_skew_array


if __name__ == "__main__":
    skew("GAGCCACCGCGATA")
    with open("dataset_369238_6.txt") as file:
        genome = file.read()
        minimum_skew(genome)
