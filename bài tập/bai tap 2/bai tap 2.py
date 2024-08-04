# cau 1
# class Rectangle:
#     def __init__(self,h,w):
#         self.w = w
#         self.h = h

#     def __str__(self):
#         return f'Rectangle object with height = {self.h} and width = {self.w}'
    
# rect = Rectangle(2,1)
# print(rect)

# cau 2
# class MathList:
#     def __init__(self, values):
#         self.values = values
    
#     def __str__(self):
#         return str(self.values)
    
#     def __add__(self, number):
#         return [x + number for x in self.values]
    
#     def __sub__(self, number):
#         return [x - number for x in self.values]

# number_list= MathList([1, 2, 3, 4, 5])
# print(number_list)
# number_list += 2
# print(number_list)

# cau 3
# class Square:
#     def __init__(self,cdc):
#         self.cdc = cdc

#     def cal_area(self):
#         return self.cdc * self.cdc
# class Cube(Square):
#     def cal_area(self):
#         return self.cdc * self.cdc * 6
    
#     def cal_volume(self):
#         return self.cdc * self.cdc * self.cdc
    
# square = Square(2)
# print('Square area:', square.cal_area())
# cube = Cube(2)
# print('Cube area:', cube.cal_area())
# print('Cube volume:', cube.cal_volume())

# cau 4
from datetime import datetime as dt
class User:
    def __init__(self,username, password):
        self.usn = username
        self.pas = password

    def welcome(self):
        print(f'Welcome, {self.usn}')
    
    def check_password(self, ckpass):
        return self.pas == ckpass

class SubscribedUser(User):
    def __init__(self, username, password, nhh):
        super().__init__(username, password)
        self.nhh = nhh
    
    def is_expired(self):
        now = dt.now()
        now.strftime("%d/%m/%Y")
        return now > self.nhh
    
user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))
s_user = SubscribedUser('s_mindx', '1234', dt(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())