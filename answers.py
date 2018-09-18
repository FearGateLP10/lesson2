import random


# Напишите функцию ask_user(), которая с помощью input() спрашивает пользователя “Как дела?”, 
# пока он не ответит “Хорошо”
# Создайте словарь типа "вопрос": "ответ", например: {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
# Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему 
# соотвествующий ответ. Например:
# Пользователь: Что делаешь?
# Программа: Программирую

# Перепишите функцию ask_user() из задания про while, чтобы она перехватывала KeyboardInterrupt, 
# писала пользователю "Пока!" и завершала работу при помощи оператора break


answers = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Привет": "Ну, здравствуй", 
			"Чем занимаешься?": "Играю", "Как ты?": "Норм", "Ясно": "Понятно (="
}

foo = ['Не понял ', "Пиши по-русски ", "Что? ", "Ты что-то хотел спросить у меня? ", "Повтори-ка "]


def get_answer(question, answers):
	return answers.get(question)


def ask_user(answers):
	print('Привет!')
	while True:
		user_input = input()
		answer = get_answer(user_input, answers)

		if user_input == 'пока':
			print('До скорого!')
			break
		elif answer:
			print(answer)
		else:
			print(random.choice(foo))


def main():
	try:
		ask_user(answers)
	except KeyboardInterrupt:
		print('лавно поговорили...')
	return None


if __name__ == '__main__':
	main()