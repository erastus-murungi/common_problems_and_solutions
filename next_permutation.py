def next_permutation(digits: list[int]):
    # Firstly, identify the longest suffix that is non-increasing
    # (0, 1, 2, 5, 3, 3, 0)
    pivot_index = len(digits) - 2
    while pivot_index >= 0 and digits[pivot_index] >= digits[pivot_index + 1]:
        pivot_index -= 1
    # nums[pivot_index + 1:] is weakly increasing
    # suffix = [5, 3, 3, 0]
    # pivot = 2

    # find the smallest element in the suffix that is larger than the pivot and swap the two elements
    if pivot_index >= 0:
        pivot_successor_index = len(digits) - 1
        while digits[pivot_successor_index] <= digits[pivot_index]:
            pivot_successor_index -= 1

        # successor = 3 (the first one from the right)
        digits[pivot_index], digits[pivot_successor_index] = (
            digits[pivot_successor_index],
            digits[pivot_index],
        )

        # (0, 1, 2, 5, 3, 3, 0) -> (0, 1, 3, 5, 3, 2, 0)

    # Finally, we sort the suffix in non-decreasing (i.e. weakly increasing) order because we increased the prefix,
    # so we want to make the new suffix as low as possible
    digits[pivot_index + 1 :] = digits[pivot_index + 1 :][::-1]
    # (0, 1, 3, 0, 2, 3, 5)
    return digits
