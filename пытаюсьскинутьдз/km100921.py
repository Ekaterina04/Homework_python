from decorator import show
@show
def initials_PRO(names):
    b = len(names)
    new_names = []
    for i in range(b):
        a,b,c= names[i].split(' ')
        a +=' ' + b[0]+ ' ' + c[0]
        new_names.append(a)
    return new_names


spisok=['СТрыжак роберт андреевич','попов ростислав валерьевич','меняйло катерина андреевна','загребин керил максимович','герман стрыжак андреевич']

print(initials_PRO(spisok))