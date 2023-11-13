# Split and decode a binary string.

# from array import array
import functools

nine = '01001'

def decode(x):
    b = bytes(x, 'utf-8')
    converted = functools.reduce(
        lambda x, y: x * 2 + (1 if y == 49 else 0), b, 0)
    print(x, converted)

    # todo: return


decode(nine)