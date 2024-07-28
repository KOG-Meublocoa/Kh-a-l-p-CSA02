# class character:
#    def __init__(self, hair_color, age):
#       self.hair_color=hair_color
#       self.age=age
#       def inten(self):
#          print(inten)
# goku=character("black",20) 
# print(goku)   

# tham khảo:
#  def __init__(self, name):
#         self.name = name
#         self.employees = [] #Danh sach nhan vien

class Employee:
    def __init__(self,name,age): 
        self.name=name
        self.age=age
class Full_Time_Employee :
    # calculate_salary 
    def __init__(self,name,age,basic_salary,salary_multiplier):
        self.name=name
        self.age=age
        self.basic_salary=basic_salary
        self.salary_multiplier=salary_multiplier
    def luong(self):
        print("basic_salary" * "salary_multiplier")
class Part_Time_Employee:
    # calculate_salary 
    def __init__(self,name,age,hours_worked,hourly_rate):
        self.name=name
        self.age=age
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate
    def luong(self):
        print("hours_worked" * "hourly_rate")


class Department:
    def __init__(self,name):
        self.name=name
        self.employee_list=[]
    
    def add_employee(self,employee):
        self.employee_list.append(employee)
        self.employee_list.remove(employee)

    def listed (self,employee_list):    
        for i in employee_list:
            print(i.name)

name=("Jack",20,2000000)
name=("Adam",24,4000000)

