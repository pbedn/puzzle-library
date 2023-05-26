OPERATION_NAMES = (
    "conjunction", "disjunction", "implication", "exclusive", "equivalence")


def boolean(x, y, operation):
    if operation == "conjunction":
        if x and y:
            return 1
    if operation == "disjunction":
        if x or y:
            return 1
    if operation == "equivalence":
        if x == y:
            return 1
    if operation == "exclusive":
        if (x or y) and not (x and y):
            return 1
    if operation == "implication":
        if x < y or x == y:
            return 1
    return 0

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"

#CLEAR
def boolean(x, y, operation):
    if operation == "conjunction": return x & y
    if operation == "disjunction": return x | y
    if operation == "implication": return (1 ^ x) | y
    if operation == "exclusive":   return x ^ y
    if operation == "equivalence": return x ^ y ^ 1
    return 0


#CLEAR
from operator import and_, or_, xor, eq

def implication(x, y):
    return not x or y

OPERATIONS = {"conjunction": and_,
              "disjunction": or_,
              "implication": implication,
              "exclusive": xor,
              "equivalence": eq}

def boolean(x, y, operation):
    return OPERATIONS[operation](x, y)


#CREATIVE
boolean=lambda x,y,o:1&~"dimpleqonx".index(o[1])>>y>>x>>y

boolean=lambda x,y,o:1&7+"gnu puns".find(o[2])>>2*x+y

boolean=lambda x,y,o:1&(8^902>>"spun".find(o[2])%7)>>2*x+y

boolean=lambda x,y,o:1&6-"cspn".find(o[2])%-9*3>>2*x+y



#CREATIVE
def boolean(x, y, operation):
    '''\
    x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
    --------------------------------------
    0 | 0 |  0  |  0  |  1  |  0  |  1  |
    1 | 0 |  0  |  1  |  0  |  1  |  0  |
    0 | 1 |  0  |  1  |  1  |  1  |  0  |
    1 | 1 |  1  |  1  |  1  |  0  |  1  |
    --------------------------------------'''

    symbol = dict(
        conjunction = "∧",
        disjunction = "∨",
        implication = "→",
        equivalence = "≡",
        exclusive = "⊕",
    )[operation]

    head, *body = boolean.__doc__.splitlines()

    for line in body:
        row = dict(zip(reversed(head), reversed(line)))
        if (row['x'], row['y']) == (str(x), str(y)): return int(row[symbol])



#SPEEDY
op = {"conjunction":"x and y", "disjunction":"x or y", "implication":"not x or y", "exclusive":"x != y", "equivalence":"x == y"}

def boolean(x, y, operation):
    return eval(op[operation])


#SPEEDY
OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

boolean=lambda x,y,o:{'co':x and y,'di':x or y,'im':y if x else 1,'ex':x!=y,'eq':x==y}[o[:2]]
​

