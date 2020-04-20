import math


def binary_search(list_in: list, item: int):
    l_ordered = sorted(list_in)
    middle = math.ceil(len(l_ordered) / 2)
    if item > l_ordered[-1]:
        print(f'{item} is not in the list')
    elif item < l_ordered[0]:
        print(f'{item} is not in the list')
    elif item == middle:
        print(f'{item} is in list, {l_ordered.index(item)} is the index')
    # elif item != l_length
    elif item > list_in[middle]:
        binary_search(list_in[middle:-1], item)
    elif item < list_in[middle]:
        binary_search(list_in[0:middle], item)



if __name__ == "__main__":
    binary_search([1, 2, 3, 4, 5], 1)
    binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 12)
    binary_search([1, 2, 3, 4, 5, 6, 7, ], -1)
