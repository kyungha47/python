try:
    x = int(input('나눌 숫자 입력:'))
    y = 10 / x
    print(y)

except:
    print('이 경우는 예외입나다.')

z = [10, 20, 30]

try:
    index, w = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(z[index] / w)
except ZeroDivisionError as e:  # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.', e)
except IndexError as e:  # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.', e)
# as 뒤 변수가 에러를 받아와서 저장된 에러메시지 출력
