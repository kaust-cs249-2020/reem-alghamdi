"""
@BY: Reem Alghamdi
@DATE: 24-09-2020
"""
from ch4.code.ch4_04 import cyclic_spectrum


def counting_peptides(m):
    """
    given the mass m and the mass_table masses, find the number possible combinations
    solved with counting coins problem
    """
    masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163,  186]

    array = [1] + [0] * m  # count sub-problems from 0 to m
    for i in range(1, m + 1):
        for mass in masses:
            if i - mass >= 0:  # if the difference between i - mass >= o (mass fits into the bag)
                # the box i is incremented by the value of the box with the difference between i and mass
                array[i] += array[i - mass]
    return array[-1]


if __name__ == "__main__":
    print(counting_peptides(1024))
