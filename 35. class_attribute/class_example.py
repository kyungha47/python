class Date:

    @staticmethod
    def is_date_valid(date):
        year, month, day = map(int, date.split('-'))

        if month <= 12 and day <= 31:
            return 1

if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')

else:
    print('잘못된 날짜 형식입니다.')