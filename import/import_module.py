# import math as m -> m.sqrt() 처럼 줄여서 쓸 수 있음

from math import *
# *는 모든 변수, 함수, 클래스를 말한다 -> pi, sqrt 처럼 하나씩 쓸 수 있다.
print(pi)

del sqrt

import math
del math
# 해제한 모듈 다시 가져오기
import importlib
import math
importlib.reload(math)

print(math.sqrt(9.0))
