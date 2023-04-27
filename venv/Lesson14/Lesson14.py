
# def is_prime(p: int) -> bool:
"""
    Checks the number p for simplicity using finding the remainder of division in the range(2, p).
    >>> is_prime(42)
    False
    >>> is_prime(73)
    True
    >>> is_prime(3.14)
    Traceback (most recent call last):
    ...
    TypeError: The number P must be an integer type
    >>> is_prime(-100)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(1)
    Traceback (most recent call last):
    ...
    ValueError: The number P must be greater than 1
    >>> is_prime(100_000_001)
    If the number P is prime, the check may take a long time.
    Working...
    False
    >>> is_prime(100_000_007)
    If the number P is prime, the check may take a long time.
    Working...
    True
    """
#     if not isinstance(p, int):
#         raise TypeError('The number p must be an integer type')
#     elif p < 2:
#         raise ValueError('The number p must be greater than 1')
#     elif p > 100_000_000:
#         print('If the number p is prime the check can take a long time. Working...')
#     for i in range(2, p):
#         if p % i == 0:
#             return False
#         return True
#
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()


# import unittest
#
#
# class TestCaseName(unittest.TestCase):
#     def test_method(self):
#         self.assertEqual(2 * 2, 5, msg='Видимо и в этой вселенной не работает :-(')
#
#
# if __name__ == '__main__':
#     unittest.main()


import pytest


@pytest.fixture()
def data():
    return [2, 3, 5, 7]

def test_append(data):
    data.append(11)
    assert data == [2, 3, 5, 7, 11]

def test_remove(data):
    data.remove(5)
    assert data == [2, 3, 7]

def test_pop(data):
    data.pop()
    assert data == [2, 3, 5]


if __name__ == '__main__':
    pytest.main(['-v'])


# import pytest
#
#
# def sum_two_num(a, b):
#     return a + b
#
# def test_sum():
#     assert sum_two_num(2, 2) == 5, 'Математика покинула чат'
#
#
# if __name__ == '__main__':
#     pytest.main()