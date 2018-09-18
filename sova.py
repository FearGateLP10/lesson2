def get_summ(num_one, num_two):
    try:
        print(int(num_one) + int(num_two))
    except ValueError:
        print('Цыц')

suming = get_summ([1, 2] , 5.3)