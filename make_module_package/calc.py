def add(a,b):
    return a+b

def mul(a,b):
    return a*b

if __name__ == '__main__':
# 프로그램의 시작점일 때만 !! 즉 다른 파일에서 import calc 하면 프린트안됨
    print(add(10,20))
    print(mul(10,20))