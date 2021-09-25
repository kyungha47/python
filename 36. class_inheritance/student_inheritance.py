class Person:
    def greeting(self):
        print('hello')

class Student(Person):
    def study(self):
        print('과제하기싫어')

kyungha = Student()
kyungha.greeting()
kyungha.study()

#같은 종류에 동등한 관계일때 상속을 사용! Person클래스의 기능을 상속받은 Student클래스

class Personlist:
    def __init__(self):
        self.person_list = []

    def append_person(self, person):
        self.person_list.append(person)

# 상속을 사용하지 않고 속성에 인스턴스를 넣어 관리--> Personlist가 Person을 포함하고 있다