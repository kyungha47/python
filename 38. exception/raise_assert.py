try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴 raise 예외('에러메시지')
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)

# 현재 예외를 다시 발생
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:  # x가 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')  # 예외를 발생시킴
        print(x)
    except Exception as e:  # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise  # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김


try:
    three_multiple()
except Exception as e:  # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)

# assert
y = int(input('4의 배수를 입력하세요: '))
assert y % 4 == 0, '4의 배수가 아닙니다.'    # 4의 배수가 아니면 예외 발생, 4의 배수이면 그냥 넘어감
print(y)