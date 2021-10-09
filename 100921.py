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


def gen_names(count_names):
    for i in range(count_names):
        name = ''
        name = chr(random.randint(65, 90))
        rnd_num = random.randint(3, 10)
        for u in range(rnd_num):
            name += chr(random.randint(97, 122))
        names.append(name)
    return names

print('Введите количество имен:')
n = int(input())
b = decorator(gen_names)
print(b(n))