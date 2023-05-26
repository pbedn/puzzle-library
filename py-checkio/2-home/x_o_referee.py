def check_result(pattern, game_result):
    winners = ["X", "O"]
    for i, j, k in pattern:
        w = game_result[i]
        if game_result[j] == w and game_result[k] == w and w in winners:
            return w
    return False


def checkio(game_result):
    game_result = [y for x in game_result for y in x]
    horizontal = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
    vertical = ((0, 3, 6), (1, 4, 7), (2, 5, 8))
    diagonal = ((0, 4, 8), (2, 4, 6))

    for pattern in (horizontal, vertical, diagonal):
        res = check_result(pattern, game_result)
        if res:
            return res
    return "D"


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(["X.O", "XX.", "XOO"]) == "X", "Xs wins"
    assert checkio(["OO.", "XOX", "XOX"]) == "O", "Os wins"
    assert checkio(["OOX", "XXO", "OXX"]) == "D", "Draw"
    assert checkio(["O.X", "XX.", "XOO"]) == "X", "Xs wins again"
    assert checkio(["...", "XXX", "OO."]) == "X", "X wins .."
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players (X and O) who take turns marking the
spaces in a 3×3 grid. The player who succeeds in placing three respective marks in a horizontal, vertical, or
diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for this games results. You are given a result
 of a game and you must determine if the game ends in a win or a draw as well as who will be the winner.
  Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".

x-o-referee

A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).

Output: "X", "O" or "D" as a string.

Example:

checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"

How it is used: The concepts in this task will help you when iterating data types.
They can also be used in game algorithms, allowing you to know how to check results.


"""


# CLEAR
def checkio(board):
    # First we put everything together into a single string
    x = "".join(board)

    # Next we outline the 8 possible winning combinations.
    combos = ["012", "345", "678", "036", "147", "258", "048", "246"]

    # We go through all the winning combos 1 by 1 to see if there are any
    # all Xs or all Os in the combos
    for i in combos:
        if x[int(i[0])] == x[int(i[1])] == x[int(i[2])] and x[int(i[0])] in "XO":
            return x[int(i[0])]
    return "D"


def checkio(game_result):
    sample = "".join(game_result)
    data = (
        game_result + [sample[i:9:3] for i in range(3)] + [sample[0:9:4], sample[2:8:2]]
    )

    if "OOO" in data:
        return "O"
    elif "XXX" in data:
        return "X"
    else:
        return "D"


def checkio(result):
    rows = result
    cols = map("".join, zip(*rows))
    diags = map("".join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)

    return "X" if ("XXX" in lines) else "O" if ("OOO" in lines) else "D"


import re


def checkio(game_result):
    # join the array to one long string
    # row - search for 3 equal game characters next to each other: r"([OX])\1{2}"
    # column - search for 3 equal game characters separated by any 3 characters: r"([OX]).{3}\1.{3}\1"
    # diagonals - like a column, different offsets: r"([OX]).{4}\1.{4}\1" and r"([OX]).{2}\1.{2}\1"
    res = re.search(
        r"([OX])(\1{2}|.{3}\1.{3}\1|.{4}\1.{4}\1|.{2}\1.{2}\1)", "-".join(game_result)
    )
    if res != None:
        return res.group(0)[0]
    return "D"


# CREATIVE
def checkio(r):
    p = map(int, "093193293094272")
    r.extend("".join(r)[next(p) : next(p) : next(p)] for _ in range(5))
    return {t * 3 in r: t for t in "OX"}.get(True, "D")


def checkio(data):
    try:
        check = (
            lambda i: len({data[i[j]][i[j + 1]] for j in range(0, 6, 2)}) == 1
            and data[i[0]][i[1]] != "."
        )
        inp = [
            [0, 0, 0, 1, 0, 2],
            [1, 0, 1, 1, 1, 2],
            [2, 0, 2, 1, 2, 2],
            [0, 0, 1, 0, 2, 0],
            [0, 1, 1, 1, 2, 1],
            [0, 2, 1, 2, 2, 2],
            [0, 0, 1, 1, 2, 2],
            [2, 0, 1, 1, 0, 2],
        ]
        res = next(filter(check, inp))[:2]
        return data[res[0]][res[1]]
    except StopIteration:
        return "D"


import re


def checkio(game_result):
    s = "".join(game_result)
    ms = "-".join(
        [
            el
            for i in range(0, 9, 3)
            for el in [s[i : i + 3], s[i // 3 : 9 : 3], s[0:9:4], s[2:7:2]]
        ]
    )
    return (re.findall("(XXX|OOO)", ms) + ["D"])[0][0]
