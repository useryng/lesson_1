list_A = ["Иванов", "Смирнова", "Петрова"]
list_B = ["Иванова", "Смирнов", "Петров"]
list_C = ["Кузнецова", "Бодрова", "Петрова"]

def my_generator(some_list):
    for name in some_list:
        if name.endswith('а'):
            yield f'Гражданка {name}'
        else:
            yield f'Гражданин {name}'

print('A')
for i in my_generator(list_A):
    print(i)
    
print('B')
for i in my_generator(list_B):
    print(i)

print('C')
for i in my_generator(list_C):
    print(i)