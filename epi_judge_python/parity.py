from test_framework import generic_test


def parity(x: int) -> int: # my solution
    # TODO - you fill in here.
    counter = 0
    while x:
        counter = counter + (x&1)
        x = x >> 1
    return counter % 2

def parity_(x:int) ->int:# book's brute solution
    result = 0
    while x:
        result = result ^ (x & 1)
        # print("Each level--->", result)
        x = x>> 1
    # print(result)
    return result

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
    # r = parity(15)
    # print(r)
