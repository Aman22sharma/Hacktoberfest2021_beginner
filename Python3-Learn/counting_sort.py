def counting_sort(lst):
    """Sorting list using counting sort"""
    count_list = [0] * (max(lst) + 1)

    for elt in lst:
        count_list[elt] += 1

    for i in range(1, max(lst) + 1):
        count_list[i] += count_list[i - 1]

    sorted_list = [0] * len(lst)
    for i in range(len(lst) - 1, -1, -1):
        current = lst[i]
        count_list[current] -= 1
        new_position = count_list[current]
        sorted_list[new_position] = current

    return sorted_list


def test_sorting():
    """Testing the sorting function"""
    random_list = [7, 9, 9, 3, 1, 4, 7, 5, 2]
    sorted_list = [1, 2, 3, 4, 5, 7, 7, 9, 9]
    assert counting_sort(random_list) == sorted_list
