import json
from functools import wraps


def to_json(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        res = func(*args, **kwargs)
        if type(res) == dict:
            res = json.dumps(res)
        return res

    return new_func


CONST = "ABC"


def func_1():
    return {'a': CONST, 'b': [1, 2, 3], 'c': ['1', ['2', 3]]}


@to_json
def func_1j():
    return {'a': CONST, 'b': [1, 2, 3], 'c': ['1', ['2', 3]]}


@to_json
def func_2():
    return 'I LOVE PYTHON'


print(func_1())
print(func_1j())
print(func_2())
