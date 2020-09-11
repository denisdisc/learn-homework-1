"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

school = [{'school_class': '4a', 'scores': [5,4,5,5]},
          {'school_class': '4b', 'scores': [5,4,3,5,4]},
          {'school_class': '4c', 'scores': [4,3,4,4,2,3]}]

def asschool(school):
    a, n = 0, 0
    for i in school:
        for j in i:
            if j == 'scores':
                n += len(i[j])    
                a += sum(i[j])
    return round(a/n, 1)

def main(school):
    print('Средний балл по школе: ' + str(asschool(school)))
    for k in school:
        print('Средний балл класса ' + k['school_class'] + ': ' + str(round(sum(k['scores'])/len(k['scores']), 1)))
'''
А можно было добавить к каждому словарю(школьному классу): средний балл: значение,
и вывести на печать пары школьный класс - значение
'''
if __name__ == "__main__":
    main(school)
