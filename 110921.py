import string
import random

list_=[]

def rnd_string (n):
    a = ''
    for i in range(n):
        a += random.choice(string.ascii_letters)
    return a

def char_count(n):
    length_ = len(n)
    count_up = 0
    count_down = 0
    for i in range(length_):
        if n[i] in string.ascii_lowercase:
            count_up += 1
        else:
            count_down += 1
    if count_up == count_down:
        return -1
    elif count_up > count_down:
        return 1
    else:
        return 0

def masslal(n,k):
    massslala = []
    for i in range(k):
        b = rnd_string(n)
        massslala.append(b)
    return massslala

def procent(mas, n):
    count_masslal = len(masslal(n,k))
    ko = 0
    for i in range(count_masslal):
        if char_count(masslal(n, k)[i]) == 1:
            ko += 1
    return (ko/count_masslal*100)


print('Введите кол-во символов в строке')
n = int(input())
print('Введите кол-во строк')
k = int(input())

massiv_strings = (masslal(n,k))
print(massiv_strings)
print('Количество строк с бОльшим количеством букв в верхнем регистре = ', procent(massiv_strings, n), '%', sep='') 
