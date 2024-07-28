# bai 1
# class Employee:
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#     def say_hi(self):
#         print(f'Hi, my name is {self.name}')
#     def tell_position(self):
#         print(f'I am a {self.position}')
# john = Employee('John', 'Software Engineer')
# john.say_hi()
# john.tell_position()

# bai 2
# class Hinh:
#     def __init__(self,w,h,r):
#         self.w = w
#         self.h = h
#         self.r = r
#     def hcn(self):
#         p = (self.w + self.h)*2
#         s = self.w*self.h
#         print(f'Perimeter: {p}')
#         print(f'Area: {s}')
#     def ht(self):
#         p = 2*3.14*self.r
#         s = self.r*self.r*3.14
#         print(f'Perimeter: {p}')
#         print(f'Area: {s}')
# shape = str(input('Shape (rectangle | circle):\n'))
# if shape == 'rectangle':
#     w = int(input('Width: '))
#     h = int(input('Height: '))
#     chuvihcn = Hinh(w,h,None)
#     chuvihcn.hcn()
# elif shape == 'circle':
#     r = int(input('Radius: '))
#     hinhtron = Hinh(None, None, r)
#     hinhtron.ht()

# bai 3
# from datetime import datetime
# today =  datetime.today()
# class CustomDate:
#     # def __init__(self):
#         # self = self
#     def datet(self):
#         print(today.strftime('%d/%m/%Y'))
#     def  timet(self):
#         print(today.strftime('%H:%M:%S'))
# now = CustomDate()
# now.datet()
# now.timet()

# bai 4
# from datetime import datetime as dt
# start_date = dt(2021,1,1)
# end_date = dt(2022,1,1)
# class DateHandler:
#     def format_date(date):
#         return date.strftime("%d/%m/%Y")
#     def get_days_between(date1, date2):
#         return (date2 - date1).days
# print(f"Start: {DateHandler.format_date(start_date)}")
# print(f"End: {DateHandler.format_date(end_date)}" )
# print(f"Days between: {DateHandler.get_days_between(start_date, end_date)}")