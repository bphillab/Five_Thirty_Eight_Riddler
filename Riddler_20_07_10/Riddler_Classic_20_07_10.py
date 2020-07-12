"""

"""

from itertools import permutations


def check_if_stack_is_stackable(arr):
    fail_flag = True
    for i in range(len(arr)):
        if arr[i] < i:
            fail_flag = False
    return fail_flag


def check_if_stack_is_too_high(arr, n):
    summer = 0
    lowest = len(arr)
    for i in range(len(arr)):
        if arr[len(arr) - i - 1] < lowest:
            lowest = arr[len(arr) - i - 1]
        if arr[len(arr) - i - 1] > lowest:
            summer = summer + 1
    return summer <= n - len(arr)


def check_if_valid(arr, n):
    return check_if_stack_is_stackable(arr) and check_if_stack_is_too_high(arr, n)


def create_list_of_perms(n):
    return sum([[i for i in permutations(range(n), j + 1)] for j in range(n)], [])
