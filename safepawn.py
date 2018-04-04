def safe_pawns(pawns):
    ptups = [(ord(p[0]), int(p[1])) for p in pawns]
    safe_count = 0
    for p in ptups:
        dnleft = (p[0] - 1, p[1] - 1)
        dnright = (p[0] + 1, p[1] - 1)
        if any([True if dlr in ptups else False for dlr in [dnleft, dnright]]):
            safe_count += 1
    return safe_count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
