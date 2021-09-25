class Calc:
    @staticmethod
    def add(a, b):
        print(a+b)
# 정적메서드는 매개변수에 self를 지정하지 않는다

    @staticmethod
    def mul(a,b):
        print(a*b)

Calc.add(10,20)
Calc.mul(10,20)
# 정적메서드는 self를 받지 않아서 인스턴스 속성에 접근이 불가능하다! (필요없다)
# 정적메서드는 인스턴스의 상태를 변화시키지 않는 경우 사용한다

