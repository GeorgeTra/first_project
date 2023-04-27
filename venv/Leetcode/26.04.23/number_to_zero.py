"""
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2,
otherwise, you have to subtract 1 from it.
"""

def steps_to_zero(num: int) -> int:
    steps_count = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        steps_count += 1
    return f'Steps to zero: {steps_count}'


print(steps_to_zero(20))