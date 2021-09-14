class Person:
    def __init__(self,**kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

    def hi(self):
        print(self.name)
        print(self.age)
        print(self.address)

if "__name__ = __main__":

    kyungha = Person(**{'name': '경하', 'age': 24, 'address' : '성북구'})
    kyungha.hi()