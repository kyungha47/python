class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
    # 클래스 메소드에서는 self대신 cls를 널어야함 cls() = Person()
            print(f'{cls.count}명 생성되었습니다')

kh = Person()
je = Person()
sy = Person()

Person.print_count()