#method overriding : subclass에서 base class의 메서드를 새로정의

class Person:
    def greeting(self):
        print('hi')

class Student(Person):
    def greeting(self):
        super().greeting()
        # base class의 메서드 호출하여 중복줄임
        print('nice to meet you')
        # 기능은 유지하면서 새 기능을 추가

kyungha = Student()
kyungha.greeting()