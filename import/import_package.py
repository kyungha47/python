from urllib.request import Request as r, urlopen as u
# urllib 패키지의 request 모듈에서 Request 클래스를 r로 가져오고 urlopen 함수를 u로 가져옴

req = r('http://www.google.co.kr')
response = u(req)
response.status # url 열기에 성공하면 200값