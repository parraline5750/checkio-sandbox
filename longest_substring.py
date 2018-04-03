def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    import string
    longest = 0
    for c in list(string.ascii_lowercase):
        subs = (c*i for i in range(1, len(line) + 1))
        len_of_subs = [len(sub) for sub in subs if sub in line]
        longestc = max(len_of_subs) if len_of_subs else 0
        if longestc > longest:
            longest = longestc

    return longest

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')