def binary_search(numbers: list[int], search_target) -> int:
    """
    Finds the index of a target value within a sorted array.
    Args:
        numbers (list[int]): list of integers sorted in ascending order.
        target (int) : The integer value to search for
    Returns:
           int: The 0-based index of the target if found;  otherwise returns -1
    Note:
        Time complexity: O(log n)
        Space complexity: O(1)
    """

    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid_index = (start + end) // 2
        middle_number = numbers[mid_index]
        if middle_number == search_target:
            return mid_index
        elif middle_number < search_target:
            start = mid_index + 1
        else:
            end = mid_index - 1

    return -1


if __name__ == "__main__":
    test_numbers = [4, 5, 6, 7, 8]
    search_target = 8
    target_index = binary_search(test_numbers, search_target)
    if target_index != -1:
        print(f"Target {search_target} found at index: {target_index}")
    else:
        print(f"Target {search_target} was not found in the list")
