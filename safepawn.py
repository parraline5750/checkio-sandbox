def safe_pawns(pawns):
    import string
    cols = list(string.ascii_lowercase[:8])
    rows = range(1, len(cols) + 1)
    board = [(c, r) for r in rows for c in cols]
    
    print(board)
    print(len(board))
    return 0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
