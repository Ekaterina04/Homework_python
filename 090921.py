def gen_names(first_names):
    for i in range(first_names):
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
