"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    """
    >>> twoSum([1, 2, 3, 4, 6], 6)
    [1, 3]
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == target - nums[j]:
                return [i, j]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

