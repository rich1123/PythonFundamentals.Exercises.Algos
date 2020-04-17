import math

def binary_search(list_in: list, item: int):
    l_ordered = sorted(list_in)
    l_length = math.ceil(len(l_ordered)/2)
    print(l_length)


if __name__ == "__main__":
    binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)