
def check_sort_status(nums):
    if len(nums) <= 1: return "Sorted"
    is_ascending = is_descending = True
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            is_descending = False
        elif nums[i] > nums[i + 1]:
            is_ascending = False

    if is_ascending: return "ascending"
    if is_descending: return "descending"
    return "unsorted"


def two_pointers(nums, target, order):
    """Handles the two-pointer search based on known sort order."""
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]

        if order == "ascending":
            if current_sum < target:
                left += 1
            else:
                right -= 1
        else:  # descending
            if current_sum < target:
                right -= 1
            else:
                left += 1
    return []


def binary_search(nums, target, order):
    """
    Performs binary search adapted for ascending or descending order.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if order == "ascending":
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        elif order == "descending":
            # For descending, logic is flipped
            if nums[mid] > target:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def linear_search(nums, target, order):
    """Finds target in any list in O(n) time."""
    if order == "unsorted":
        for i, num in enumerate(nums):
            if num == target:
                return i
    return -1

