def show(func):
    def new_func(*args, **kwargs):
        print('Running function: ', func.__name__)
        print('Positional arguments are: ', args)
        print('Keyword arguments are: ', kwargs)
        
    return new_func
@show
def initials_PRO(names):
    b = len(names)
    new_names = []
    for i in range(b):
        a,b,c= names[i].split(' ')
        a +=' ' + b[0]+ ' ' + c[0]
        new_names.append(a)
    return new_names


spisok=['Меняйло Екатерина Андреевна','Бабков Никита Алексеевич','Бухтиничева Ксения Геннадьвна','Загребин Кирилл Максимович','Лубянцев Дмитрий Андреевич']

print(initials_PRO(spisok))