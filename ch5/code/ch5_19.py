"""
@BY: Reem Alghamdi
@DATE: 13-10-2020
"""


def merge(l1, l2):
    l_sorted = []
    while len(l1) > 0 and len(l2) > 0:
        min_1 = min(l1)
        min_2 = min(l2)
        if min_1 < min_2:
            l_sorted.append(min_1)
            l1.remove(min_1)
        else:
            l_sorted.append(min_2)
            l2.remove(min_2)
    l_sorted += l1 + l2
    return l_sorted


def mergesort(l):
    if len(l) == 1:
        return l

    first = l[:int(len(l)/2)]
    second = l[int(len(l)/2):]
    first_sorted = mergesort(first)
    second_sorted = mergesort(second)
    l_sorted = merge(first_sorted, second_sorted)
    return l_sorted


if __name__ == "__main__":
    list1 = [2, 5, 8, 7]
    list2 = [3, 4, 6]
    print(mergesort(list1 + list2))
