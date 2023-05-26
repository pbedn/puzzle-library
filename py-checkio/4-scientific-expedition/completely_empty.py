TESTS = {
    "Basics": [
        {
            "input": [[]],
            "answer": True
        },{
            "input": [[[]]],
            "answer": True
        },{
            "input": [[[],[]]],
            "answer": True
        },{
            "input": [[1]],
            "answer": False
        },{
            "input": [[[],[1]]],
            "answer": False
        },{
            "input": [[0]],
            "answer": False
        },{
            "input": [['']],
            "answer": True
        },{
            "input": [[[],[{'':'No WAY'}]]],
            "answer": True
        },{
            "input": "[iter(())]",
            "answer": True
        },{
            "input": "[(),(),()]",
            "answer": True
        }

    ],
    "Extra": [
        {
            "input": [[[[[]]]]],
            "answer": True
        },{
            "input": [[[1],[1]]],
            "answer": False
        },{
            "input": [[None]],
            "answer": False
        },{
            "input": "[iter((1,))]",
            "answer": False
        },{
            "input": "[type('', (), {'__iter__': None})()]",
            "answer": False
        },{
            "input": "type('', (), {'__getitem__': ().__getitem__})()",
            "answer": True
        }
    ]
}


def completely_empty(val):
    return all(getattr(v, '__iter__', None) and completely_empty(v) for v in val)

# print('====BASIC=====')
# for t in TESTS['Basics']:
#     if not completely_empty(t['input']) == t['answer']:
#         print(t['input'], 'should result:', t['answer'], 'and is:', completely_empty(t['input']))
#     assert completely_empty(t['input']) == t['answer']
# print('====EXTRA====')
# for t in TESTS['Extra']:
#     if not completely_empty(t['input']) == t['answer']:
#         print(t['input'], 'should result:', t['answer'], 'and is:', completely_empty(t['input']))
#     assert completely_empty(t['input']) == t['answer']

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert completely_empty([]) == True, "First"
    assert completely_empty([1]) == False, "Second"
    assert completely_empty([[]]) == True, "Third"
    assert completely_empty([[],[]]) == True, "Forth"
    assert completely_empty([[[]]]) == True, "Fifth"
    assert completely_empty([[],[1]]) == False, "Sixth"
    assert completely_empty([0]) == False, "[0]"
    assert completely_empty(['']) == True
    assert completely_empty([[],[{'':'No WAY'}]]) == True
    assert completely_empty([[[], [1]]]) == False
    assert completely_empty([['']]) == True
    assert completely_empty([iter(())]) == True
    print('Done')


"""
You need to figure if a wellfounded and wellsized iterable is completely empty.
An iterable x0 is wellfounded if there is no infinite sequence
x1,x2,x3... such that  ... in x3 in x2 in x1 in x0 (where in is meant iteratively,  x(n+1) will be encountered while iterating through xn).
A wellfounded iterable is wellsized if it has only finitely many iterable elements, and all of them are wellsized.
A wellfounded iterable is completely empty when all its elements are completely empty.
Some consequences of the above definitions:
any empty iterable is completely empty
a non-iterable is never completely empty
the only wellfounded string is '', and it is completely empty
bytes, and (possibly nested) tuples/frozensets of them are always wellfounded and wellsized
{'': 'Nonempty'} is a wellfounded and completely empty iterable
after c=[];c.append(c), c is a non-wellfounded iterable
itertools.repeat(()) is wellfounded but not wellsized
itertools.repeat(5) is wellfounded and wellsized
Input: A wellfounded and wellsized iterable.
Output: A bool.
"""

from collections.abc import Iterable

def completely_empty(val):
    f = lambda x: isinstance(x, Iterable) and all(map(f, x))
    return not list(val) or f(val)

# ------------------------------------------------------------

def completely_empty2(val):
    return isinstance(val, Iterable) and all(completely_empty(item) for item in val)
# --------------------------------------------------------------
def completely_empty3(val):
    return isIter(val) and all(completely_empty(i) for i in iter(val))

def isIter(i):
    return (hasattr(i, '__iter__') and i.__iter__
        or hasattr(i, '__getitem__') and i.__getitem__)