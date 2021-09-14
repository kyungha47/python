class Person:
    def __init__(self, *person):
        print(person[0])
        print(person[1])
        print(person[2])


temp=["KH",24,"성북"]
kyungha=Person(*temp)




