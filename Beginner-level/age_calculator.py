import datetime

date_of_user  = (input('Enter Your DOB in DD-MM-YYYY format: '))
day,month,year = map(int,date_of_user.split('-'))
date1  = datetime.date(year,month,day)
def agecalculator(date1):
    today = datetime.datetime.now().date()
    your_age = int((today-date1).days/365.25)
    print(your_age)
agecalculator(date1)

