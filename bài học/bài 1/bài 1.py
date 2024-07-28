# class Character:
# 	# Thuộc tính (attributes)
# 	def __init__(self, hair_color, age):
# 		self.hair_color = hair_color
# 		self.age = age
# 		self.genger = "Male"

# 	# Phương thức (methods)
# 	def punch(self):
# 		return "Mất 50 máu"

# 	def kick(self):
# 		print("Mất 30 máu")

# songoku = Character("black", 30)
# vegeta = Character("black", 27)

# songoku.punch()
# print(songoku.punch())

# Tạo class Rectangle yêu cầu người dùng nhập vào hai thuộc tính chiều dài, chiều rộng. Class sở hữu hai phương thức tính diện tích và chu vi.


# cd=input=("Nhập số :")
# cr=input=("Nhập số :")
# class Rectangle:

#     def __init__(self,cd,cr):
#      self.cd=cd
#      self.cr=cr

#     def dientich(self):
#      print("dientich",cd*cr)   

#     def chuvi(self):
#      print((self.cd+self.cr)*2)


#Bài tham khảo:
# class Rectangle:
#  def __init__(self, width, length):
#   self.width = width
#   self.length = length
# def perimeter(self):
#  return (self.width + self.length) * 2

# def area(self):
#  return self.width * self.length
# rectangle1 = Rectangle(5, 10)
# print(rectangle1.perimeter())