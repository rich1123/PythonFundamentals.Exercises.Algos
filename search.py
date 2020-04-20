import math


def binary_search(list_in: list, item: int):
    if item in list_in:

        l_ordered = sorted(list_in)
        middle = math.ceil(len(l_ordered) / 2)
        # print(middle)

        if item == middle:
            print(f'{item} is in list, {l_ordered.index(item)} is the index')
            return l_ordered.index(item)
        elif item < l_ordered[middle]:
            return binary_search(list_in[0:middle], item)
        elif item > l_ordered[middle]:
            return binary_search(list_in[middle:-1], item)
    else:
        return None

if __name__ == "__main__":
    binary_search([1, 2, 3, 4, 5], 3)
    binary_search([1, 2, 3, 4, 5], 2)
    binary_search([1, 2, 3, 4, 5], 3)
    binary_search([1, 2, 3, 4, 5], -1)
