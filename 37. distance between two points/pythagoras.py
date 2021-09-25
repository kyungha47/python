import math
# sqrt 쓰기위함
class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p1 = Point2D(30, 20)
p2 = Point2D(60, 50)

a = abs(p2.x - p1.x)
b = abs(p2.y - p1.y)

c = math.sqrt((a**2 + b**2))
#다른방법
d = math.sqrt(math.pow(a,2)+math.pow(b,2))
print(c)
print(d)

