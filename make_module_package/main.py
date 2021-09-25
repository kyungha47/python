import hello
# 해당 스크립츠 파일 한번 실행
print('main.py __name__:', __name__)
# name 변수 출력

from calcpkg.operation import *
from calcpkg.geometry import *
print(add(10,20))
print(mul(10,20))

print(triangle_area(30,40))
print(rectangle_area(30,40))

# __init__ 파일에서
# from . import operation
# from . import geometry
# 또는
# __all__ = ['add', 'triangle_area'] -> *를 가져올때 이 두개만 가져옴
# from .operation import *
# from .geometry import *



# 써놨다면 main 파일에서 import calcpkg 만 써도 다 가져오게됨
