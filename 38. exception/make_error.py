class NotThreeMultipleError(Exception):  # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')


def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:  # x가 3의 배수가 아니면
            raise NotThreeMultipleError  # NotThreeMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)


three_multiple()

#다른방법
class NotThreeMultipleError(Exception):    # Exception만 상속받고
    pass                                   # 아무것도 구현하지 않음

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:  # x가 3의 배수가 아니면
            raise NotThreeMultipleError('3의 배수가 아닙니다.')
            # 예외를 발생시킬 때 에러 메시지를 넣음
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)

