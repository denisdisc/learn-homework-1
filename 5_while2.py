"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
import re

dialog = {"как дела": "хорошо!", "что делаешь?": "программирую"}

def ask_user_dict():
    question = input('Спрашивай! :)').lower()
    if re.search(r'пока', question) is not None:
        return 'пока'
    elif question in dialog:
        print(dialog[question].capitalize())
        return question
    else:
        answer = input('Я не знаю ответ.. :( Как мне ответить?')
        dialog[question] = answer
        return question

def ask_user():
    question = 0
    while question != 'пока': 
        question = ask_user_dict()
    
if __name__ == "__main__":
    ask_user()
