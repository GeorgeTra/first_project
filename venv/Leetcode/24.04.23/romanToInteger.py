
def romanToInteger(s: str) -> int:
    rti = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    s = s.replace('CM', 'DCCCC').replace('CD', 'CCCC').replace('XC', 'LXXXX').replace('XL', 'XXXX').replace('IX',
                'VIIII').replace('IV', 'IIII')

    return sum(map(lambda x: rti[x], s))


print(romanToInteger('MCMLXXXVI'))
