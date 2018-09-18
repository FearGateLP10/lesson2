
# Напишите функцию get_summ(num_one, num_two), 
# которая принимает на вход два целых числа (int) 
# и складывает их
# Оба аргумента нужно приводить к целому числу 
# при помощи int() и перехватывать исключение ValueError 
# если приведение типов не сработало


def get_summ(num_one, num_two):
    try:
        summ = int(num_one) + int(num_two)
        return summ
    except ValueError as e:
        print('ValueError', e)


a = 1.3
b = '2'
print(get_summ(a, b))
