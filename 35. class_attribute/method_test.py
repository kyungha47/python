class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second



    @staticmethod
    def is_time_valid(time):
        hour, minute, second = map(int, time.split(':'))
        return hour <= 24 and minute <= 59 and second <= 60


    @classmethod
    def from_string(cls,time):
        cls.hour, cls.minute, cls.second = map(int, time.split(':'))
        return cls

time_string = input()

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')