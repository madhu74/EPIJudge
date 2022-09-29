from test_framework import generic_test

# Note need to redo this (TODO)
# Time complexity is O(1)
def swap_bits(x, i, j):
    if (x>>i)&1 != (x>>j)&1:
        # bitmask can be calculated using right sift or left shif depending on bit position
        # bit mask is calculated using 1's where the bit mask XOR input will give
        # the swapped bit result. 0^1 = 1 and 1^1= 1
        bit_mask = 1 << i | 1 << j
        x = x ^ bit_mask
    
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
