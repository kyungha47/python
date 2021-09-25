class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hi'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()
        # super()로 base class의 __init__ 메서드를 호출한다 그래야 hello 쓸 수 있음
        # 만약 subclass에서 init 메서드를 안쓰면 super가 없어도 base class의 init이 호출된다
        self.school = '고려대학교'

kyungha = Student()
print(kyungha.school)
print(kyungha.hello)