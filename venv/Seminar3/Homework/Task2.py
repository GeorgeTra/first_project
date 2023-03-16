# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = '''If there is only one argument, it must be a dictionary mapping Unicode
       ordinals (integers) or characters to Unicode ordinals, strings or None.
       Character keys will be then converted to ordinals.
      If there are two arguments, they must be strings of equal length, and
       in the resulting dictionary, each character in x will be mapped to the
      character at the same position in y. If there is a third argument, it
      must be a string, whose characters will be mapped to None in the result.'''

punct = ',.()'
text_lower = [word.rstrip(punct).lower() for word in text.split()]
print(*sorted(set(text_lower), key=text_lower.count, reverse=True)[:10], sep='\n')