from test_framework import generic_test


def reverse_bits(x: int) -> int:
    # Note - This solution is wrong and need to understand lookups a bit more
    # approach
    x = bin(x) # binary conversion
    x = str(x)[2:]
    x = x[::-1] # reverse
    idx = 0
    while idx < len(x): # remove leading 0's since it is binary
        if x[idx] == '1':
            break
        idx = idx+1
    # print(x[idx:].ljust(64, '0'))
    return int(x[idx:].ljust(64, '0'), base=2) # do int conversion ljust 64 since it is a 64 it is number


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
    # 1351510410656   
