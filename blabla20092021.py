def unique(a):
    
    return list(set(a))

def per(a,b):
    c = set(a) & set(b)
    return list(c)

a = {1,2,3,4,5,1,1,1,1,1}
b = {2,3,4,5,6}
print(list(per(a,b)))
print()
print(list(unique(a)))