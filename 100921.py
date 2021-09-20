import random
import string

names=[]

def decorator(func):
    def inner(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        result = func(*args, **kwargs)
        print('Result: ', result)
        return result
    return inner