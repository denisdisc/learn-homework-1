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
    sum_scores, count_score = 0, 0
    for klass in school:
        count_score += len(klass['scores'])    
        sum_scores += sum(klass['scores'])
    return round(sum_scores/count_score, 1)

def main(school):
    print(f'Средний балл по школе: {str(asschool(school))}')
    for k in school:
        print(f'Средний балл класса {k["school_class"]}: {str(round(sum(k["scores"])/len(k["scores"]), 1))}')

if __name__ == "__main__":
    main(school)
