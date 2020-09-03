"""
@BY: Reem Alghamdi
@DATE: 03-09-2020
"""


def to_binary(x):
    return "{:025b}".format(x)


if __name__ == "__main__":
    count = 0
    possibilities = range(0, 2**25)
    possibilities = map(to_binary, possibilities)
    for string in possibilities:
        print(string)
        if string.__contains__("01"):
            count = count+1

    print(count)
