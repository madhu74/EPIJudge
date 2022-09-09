from test_framework import generic_test


def count_bits(x: int) -> int:
    # my dirty solution
    counter = 0
    str_binary_format = str(bin(x))[2:]
    for item in list(str_binary_format):
        if item == "1":
            counter = counter + 1
    
    return counter


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
