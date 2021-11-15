#learning Decorators

from functools import wraps
from time import time
from statements import lazy_return_random_attacks #import function from statements.py file

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"fun: {f.__name__}, args: [{args}, {kw}] took: {te-ts} sec")
        return result
    return wrap

@timing
def some_attachs():
    attack = lazy_return_random_attacks()
    for _ in range(5): 
        print(next(attack)) #notice this function is passed into decorator and calculates time taken by function passed