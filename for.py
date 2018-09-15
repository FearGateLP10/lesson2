
# Создать список из десяти целых чисел.
# Вывести на экран каждое число, увеличенное на 1.

my_list = [3, 1, 6, 4, 76, 213, 45, 32, 42, 57, 10]

for num in my_list:
	print(num + 1)


# Ввести с клавиатуры строку.
# Вывести эту же строку вертикально: по одному символу на строку консоли.

my_sting = input('Введите слово: ')
for letter in my_sting:
	print(letter)


# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.

score = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
		{'school_class': '4б', 'scores': [3,5,4,3,3,5]},
		{'school_class': '4в', 'scores': [5,4,5,5]},
		{'school_class': '4г', 'scores': [2,3,3,4,2,5,3,2]}
]

school_score_total = 0
total_score = 0

for class_ in score:
	class_score_total = 0

	for i in class_['scores']:
		class_score_total += i
		school_score_total += i
		total_score += 1

	average_score = round(class_score_total / len(class_['scores']), 1)
	print('Средний балл {} класса: {}'.format(class_['school_class'], average_score))

average_school_score = round(school_score_total / total_score, 1)
print('Средний балл по всей школе: {}'.format(average_school_score))
