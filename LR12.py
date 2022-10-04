a=1
while (a!=0):
    a=input()
    try:
                a = int(a)
                if a == 5:
                    print('Отлично')
                elif a == 4:
                    print('Хорошо')
                elif a == 3:
                    print('Удовлетворительно')
                elif a == 2:
                    print('Неудовлетворительно')
    except ValueError:
                if a=='Отлично':
                    print('5')
                elif a=='Хорошо':
                    print('4')
                elif a=='Удовлетворительно':
                    print('3')
                elif a=='Неудовлетворительно':
                    print('2')

