def create_new_pawn(new_letter, new_index):
    if new_letter and new_index:
        return "{}{}".format(new_letter, new_index)


def safe_pawns(pawns):
    letters = "abcdefgh"
    count = 0
    for p in pawns:
        letter_loc = letters.index(p[0])
        new_letter = letters[letter_loc - 1] if letter_loc > 0 else False
        new_index = str(int(p[1]) - 1) if int(p[1]) > 1 else False
        lower_left_pawn = create_new_pawn(new_letter, new_index) in pawns
        new_letter = letters[letter_loc + 1] if letter_loc < 7 else False
        lower_right_pawn = create_new_pawn(new_letter, new_index) in pawns
        if lower_left_pawn or lower_right_pawn:
            count += 1
    return count


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]) == 7
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""
Almost everyone in the world knows about the ancient game Chess and has at least a basic understanding of its rules.
 It has various units with a wide range of movement patterns allowing for a huge number of possible different game positions
 (for example Number of possible chess games at the end of the n-th plies.) For this mission, we will examine the movements
 and behavior of chess pawns.

Chess is a two-player strategy game played on a checkered game board laid out in eight rows (called ranks and denoted
 with numbers 1 to 8) and eight columns (called files and denoted with letters a to h) of squares. Each square of the
 chessboard is identified by a unique coordinate pair — a letter and a number (ex, "a1", "h8", "d6"). For this mission
  we only need to concern ourselves with pawns. A pawn may capture an opponent's piece on a square diagonally in front
  of it on an adjacent file, by moving to that square. For white pawns the front squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall. With this strategy,
one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square. We have several white pawns
on the chess board and only white pawns. You should design your code to find how many pawns are safe.

pawns

You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Example:

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

How it is used: For a game AI one of the important tasks is the ability to estimate game state.
 This concept will show how you can do this on the simple chess figures positions.

Precondition:
0 < pawns ≤ 8
"""


def safe_pawns(pawns):
    def is_safe(p):
        file, rank = ord(p[0]), int(p[-1])
        return (
            chr(file - 1) + str(rank - 1) in pawns
            or chr(file + 1) + str(rank - 1) in pawns
        )

    return sum(is_safe(p) for p in pawns)


# ------------------------------------------


def getdiags(pawn):
    c, r = map(ord, pawn)
    return chr(c - 1) + chr(r - 1), chr(c + 1) + chr(r - 1)


def safe_pawns(pawns):
    return len([p for p in pawns if any(d in pawns for d in getdiags(p))])


# ------------------------------------------


def safe_pawns(pawns):
    safePawns = 0

    for col, row in pawns:
        defenseRow = str(int(row) - 1)
        defenseLeft = chr(ord(col) - 1) + defenseRow
        defenseRight = chr(ord(col) + 1) + defenseRow

        if defenseLeft in pawns or defenseRight in pawns:
            safePawns += 1

    return safePawns


# ------------------------------------------


def safe_pawns(pawns):
    positions = [(ord(i) - 96, int(j)) for i, j in pawns]
    safePawns = 0
    for col, row in positions:
        defenseLeft = (col - 1, row - 1)
        defenseRight = (col + 1, row - 1)

        if defenseLeft in positions or defenseRight in positions:
            safePawns += 1
    return safePawns


# ------------------------------------------


def safe_pawns(pawns):
    safeones = 0
    pawns_indexes = set()
    for pawn in pawns:
        row = int(pawn[1]) - 1
        col = ord(pawn[0]) - 97
        pawns_indexes.add((row, col))
    for row, col in pawns_indexes:
        is_safe = ((row - 1, col - 1) in pawns_indexes) or (
            (row - 1, col + 1) in pawns_indexes
        )
        if is_safe:
            safeones += 1
    return safeones
