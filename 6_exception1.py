"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
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
    try:
        question = 0
        while question != 'пока': 
            question = ask_user_dict()
    except KeyboardInterrupt:
        print('Пока!')
    
if __name__ == "__main__":
    ask_user()
