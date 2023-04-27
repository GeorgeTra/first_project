# def isPalindrome(x: int) -> bool:
#     x = str(x)
#     return x == x[::-1]
#
#
# print(isPalindrome(1234321))


def isPalindrome(x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    half = 0
    while half < x:
        half = (half * 10) + (x % 10)
        x = x // 10
    return x == half or x == half // 10


print(isPalindrome(1234321))