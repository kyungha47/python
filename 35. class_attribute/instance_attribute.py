class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

kyungha = Person()
kyungha.put_bag('노트')

jeongeun = Person()
jeongeun.put_bag('아이패드')

print(kyungha.bag)
print(jeongeun.bag)

# 위의 두 경우 모두 [노트, 아이패드] : bag이 클래스 속성으로, 클래스에 속해있어 모든 인스턴스(경하/정은)에서 공유한다.

class Person2:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

kh = Person2()
kh.put_bag('노트')
je = Person2()
je.put_bag('아이패드')

print(kh.bag)
print(je.bag)

# bag을 인스턴스 속성으로 만들면 각자 넣은 물건만 출력된다 [노트], [아이패드]