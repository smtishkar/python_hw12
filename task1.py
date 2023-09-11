# Задание. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.


import csv


class Name:
    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value: str):
        if value.isalpha() == False:
            raise ValueError(f'Значение {value} не должно содержать цыфр')
        if value.istitle() == False:
            raise ValueError (f'Значение {value} должно начаинаться с заглавной буквы ')


class Marks:
    def __init__(self, min_mark: int, max_mark: int):
        self.min_mark = min_mark
        self.max_mark = max_mark

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value: int):
        if value < self.min_mark or value > self.max_mark:
            raise ValueError (f'Отметки {value} не существует')  




class Subject:

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value: str):
        subjects_list =[]
        with open('subjects.csv', 'r', encoding='utf-8', newline='') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                subjects_list.append(''.join(line))  
            if value not in subjects_list:
                raise ValueError (f'Такого предмета {value} нет')


class Student:

    first_name = Name()
    last_name = Name()
    mark = Marks(2,5)        
    test = Marks(0,100)
    subject = Subject()
    
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        subject = None
        mark = None
        test = None
        self.common_dict = {}

    def __repr__(self):
        return f'{self.first_name} {self.last_name}' 
    
    def set_mark(self,subject,mark):
        self.mark = mark
        self.subject = subject
        if self.subject not in self.common_dict:
            self.common_dict.update({self.subject : {'Marks' : [self.mark]}})
        elif 'Marks' in self.common_dict[subject]:
            self.common_dict[self.subject]['Marks'] .append(self.mark)
        else:
            self.common_dict[subject]['Marks'] = [self.mark]


    def set_tests(self,subject,test):
        self.test = test
        self.subject = subject
        if self.subject not in self.common_dict:
            self.common_dict.update({self.subject : {'Tests' : [self.test]}})
        elif 'Tests' in self.common_dict[subject]:
            self.common_dict[self.subject]['Tests'] .append(self.test)
        else:
            self.common_dict[subject]['Tests'] = [self.test]

    def test_average(self, subject):
        res = 0
        for key, value in self.common_dict.items():
            if key == subject:
                for k,v in value.items():
                    if k == 'Tests':
                        for i in range(len(v)):
                            res += v[i]
                        res /=len(v)
                return res

                
    def marks_average(self):
        res = 0
        count=0
        for key, value in self.common_dict.items():
            # if key == subject:
            for k,v in value.items():
                if k == 'Marks':
                    for i in range(len(v)):
                        res += v[i]
                        count+=1
        res /=count
        return res

if __name__ == '__main__':
    st1 = Student('Вася', 'Петров')
    st1.set_tests('English', 50)
    st1.set_tests('Math', 58)
    st1.set_tests('Math', 44)
    st1.set_tests('English', 88)
    st1.set_mark('Math', 4)
    st1.set_mark('Math', 5)
    st1.set_mark('Math', 3)
    st1.set_tests('Literature',95)
    st1.set_mark('Math', 5)
    st1.set_mark('English', 5)
    st1.set_mark('Literature',5)

    print(st1)
    print(st1.common_dict)
    print(f'Средний балл за тест составляет - {st1.test_average("Math")}')
    print(f'Средний балл за тест составляет - {st1.test_average("English")}')
    print(f'Средний балл за тест составляет - {st1.test_average("Literature")}')
    print(f'Средний бал во всем дисциплинам - {st1.marks_average()}')