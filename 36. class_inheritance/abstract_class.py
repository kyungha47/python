# 추상클래스: 메서드의 목록만 가진 클래스 -> 상속클래스에서 그 목록들을 모두 구현해야함
# abc: abstract base class

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass
#추상클래스는 호출할 일이 없기 때문에 pass만 넣어서 빈 메서드로 만든다

class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')

# 두 메서드 중 하나라도 안쓰면 오류남!

kyungha = Student()
kyungha.study()
kyungha.go_to_school()


