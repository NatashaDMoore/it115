# Split and decode a binary string.

# from array import array

nine = '01001'

def decode(x):
    b = bytes(x, 'utf-8')
    tmp = 0
    for digit in b:
        tmp = tmp * 2
        if digit == 49:  # ASCII '1'
            tmp += 1
    print(x, tmp)

    # todo: return


decode(nine)