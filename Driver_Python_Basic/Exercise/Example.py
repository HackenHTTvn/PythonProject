#!/usr/bin/python

from project import *
####################################################################################################

# Example
import requests
r = requests.get('https://www.python.org')
r.status_code
#'Python is a programming language' in r.content
# POST:
payload = dict(key1='value1', key2='value2')
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)



####################################################################################################
# MAIN FUNTION
####################################################################################################
P8_create_char_bar()
clear()
P6_encrypt_secret_message()
clear()
P5_create_dictionary_color_map()
clear()
P4_create_rando_team()
P3_turtle_racing()
clear()
P2_rock_paper_scissors()
P1_caculate_age_in_dog_year()
####################################################################################################
# P3_FUNCTION_DETAIL()
# P5_FUNCTION_DETAIL()
# P7_FUNCTION_DETAIL()




# import sys
# import keyword
# import math
# # a = keyword. __file__
# # print  (a)
# print(dir(keyword))
# print(dir(sys))
# print(dir(math))

# help(print)
####################################################################################################
# Using enter multi value and true type
# var1, var2 = [int(x) for x in input("Enter two number").split()]
####################################################################################################
# Xử lý ngoại lệ ( tức là check lỗi )
# https://vietjack.com/python/xu_ly_ngoai_le_trong_python.jsp
# try :
#     # Phép chia này có vấn đề, chia cho 0.
#     # Một lỗi được phát ra tại đây (ZeroDivisionError).
#     value = 10 / d
#     print ("value = ", value)
# except ZeroDivisionError as e :
#     print ("Error: ", str(e) )
#     print ("Ignore to continue ...")
# print ("Let's go!")

# 2, Finally.
# Nếu như trong khối lệnh try except bạn muốn sẽ có 1 đoạn lệnh chắc chắn sẽ được thực thi cho dù try đúng hay sai, thì bạn sẽ phải khai báo thêm khối lệnh finally vào cuối khối lệnh try except theo cú pháp sau:
# try:
#     # code
# except:
#     # code
# finally:
#     # code
# Finally trong Python thường được dùng để clear data mà trong quá trình try except tạo ra.

# VD:
# def sum(a, b):
#     return a / b
# try:
#     print(sum(6, 0))
# except ZeroDivisionError:
#     print('Co loi xay ra!')
# finally:
#     print('finally duoc goi!')

# Ket qua:
# Co loi xay ra!
# finally duoc goi!


# 3, Các exception có sẵn trong Python.
# Dưới đây là danh sách các exception mặc định trong Python.

# Exception Name  Chú Thích
# Exception   Đây là lớp cơ sở cho tất cả các exception, nó sẽ xuất hiện khi có bất cứ một lỗi nào xảy ra.
# StopIteration   Xuất hiện khi phương thức next() của interator không trỏ đến một đối tượng nào.
# SystemExit  Xuất hiện khi dùng phương thức sys.exit()
# StandardError   Lớp cơ sở cho tất cả các exception.
# ArithmeticError Xuất hiện khi có lỗi tính toán giữa các số với nhau
# OverflowError   Xuất hiện khi thực hiện tính toán và giá trị của nó vượt quá ngưỡng giới hạn cho phép của kiểu dữ liệu.
# FloatingPointError  Xuất hiện khi tính toán float thất bại.
# ZeroDivisonError    Xuất hiện khi thực hiện phép chia cho 0.
# AssertionError  Xuất hiện trong trường hợp lệnh assert thất bại.
# AttributeError  Xuất hiện khi không tồn tại thuộc tính này, hoặc thiếu tham số truyền vào nó.
# EOFError    Xuất hiện khi không có dữ liệu từ hàm input() hoặc cuối file.
# ImportError Xuất hiện khi lệnh import thất bại.
# KeyboardInterrupt   Xuất hiện khi ngắt trình biên dịch.
# LookupError Lớp cơ sở cho tất cả các lỗi về lookup.
# IndexError  Xuất hiện khi index không tồn tại trong list, string,...
# KeyError    Xuất hiện khi key không tồn tại trong dictionary.
# NameError   Xuất hiện khi một biến không tồn tại trong phạm vi bạn gọi nó.
# EnvironmentError    Xuất hiện khi có bất kỳ một lỗi nào ngoài phạm vị của Python.
# IOError Xuất hiện khi xử dụng input/ output thất bại, hoặc  mở file không thành công.
# OSError Xuất hiện khi có lỗi từ hệ điều hành.
# SyntaxError Xuất hiện khi chương trình có lỗi cú pháp.
# IndentationError    Xuất hiện khi bạn thụt dòng không đúng.
# SystemError Xuất hiện khi trình biên dịch có vấn đề nhưng mà nó lại không tự động exit.
# SystemExit  Xuất hiện khi trình biên dịch được thoát bởi sys.exit().
# TypeError   Xuất hiện khi thực thi toán tử hoặc hàm mà kiểu dữ liệu bị sai so với kiểu dữ liệu đã định nghĩa ban đầu.
# ValueError  Xuất hiện khi chúng ta build 1 function mà kiểu dữ liệu đúng nhưng khi chúng ta thiết lập ở tham số là khác so với khi truyền vào.
# RuntimeError    Xuất hiện khi lỗi được sinh ra không thuộc một danh mục nào.
# NotImplementedError Xuất hiện khi một phương thức trừu tượng cần được thực hiện trong lớp kế thừa chứ không phải là lớp thực thi
# UnboundLocalError   Xuất hiện khi chúng ta cố tình truy cập vào một biến trong hàm hoặc phương thức, nhưng không thiết lập giá trị cho nó.
# 4, Xây dựng một exception riêng.
# Do mình chưa giới thiệu với mọi người kiến thức hướng đối tượng trong Python, nên phần này những ai biết hướng đối tượng rồi thì xem, còn không thì khi khác xem lại cũng được :D.

# Để tạo một exception trong Python thì bắt buộc exception này phải kế thừa lớp Exception trong Python, và còn lại là bạn muốn xử lý như thế nào cũng được.

# VD: Mình sẽ viết một Exception có tên exceptionDemo.

# class ExceptionDemo(Exception):
#     def __init__(self, value):
#         print("Loi: " + value)
        
# Sau khi đã tạo ra được exception cho riêng mình rồi, thì khi thực hiện mà bạn muốn gọi ra gọi exception ra bạn chỉ cần sử dụng keyword raise theo cú pháp sau:

# raise exceptionName
# Trong đó, exceptionName là tên của exception bạn muốn gọi.

# VD:

# class ExceptionDemo(Exception):
#     def __init__(self, value):
#         print("Loi: " + value)

# def sum(a, b):
#     if (b == 0):
#         raise ExceptionDemo('b phai khac 0')
#     return a / b
# sum(6, 0)
####################################################################################################
# # Create new dictionary
# mydictionary = {
#     "tencongty": "Cong_Ty_A",
#     "soluongnhanhvien": 20,
#     "diachi": "Duong Hoang Van Thu"
# }

# print("Công ty:",mydictionary["tencongty"])
# print("Số lượng nhân viên:",mydictionary["soluongnhanhvien"])
# print("Địa chỉ:",mydictionary["diachi"])

# # Addition more items for dictionary
# mydictionary["ngayhoatdong"] = "20/03/2015"
# print("Ngày Hoạt Động:",mydictionary["ngayhoatdong"])

# # Delete one items from dictionary
# del mydictionary["ngayhoatdong"]
# print(mydictionary)

# # Delete all items from dictionary
# mydictionary.clear()
# print(mydictionary)

####################################################################################################
# list = ["tien","tung",["lk","kj"],"tuoi"]

# print(list[-1])
# list.append("ThanhPho")      # thêm phan tử dưới dạng string vào cuối list
# list.extend("quequan")    # extend chỉ có 1 tham số là list nên nếu viết "quequan" nó sẽ hiểu là nhận mỗi ký tự là 1 phân tử
# list.extend(["quequan","tuoi"])    # nếu thêm dạng ngoặc vuông tức là 1 list thì nó sẽ nhận các phần từ của list
# list.insert(0,"thienduong")
# b = list.index("tien",0,3)      # tìm kiếm trong khoảng index
# c = list.index("tien")
# a = "tien" in list  # tìm kiếm giá trị "tien" trong list ,trả về true or false
# print(list)
# print(len(list))

# print(a)
# print(b)

 ####################################################################################################
# print ("Python version: ", sys.version_info)
# print ("Python keywords: ", keyword.kwlist)

####################################################################################################
# program = 'a = 5\nb=10\nprint("Sum =", (a+b))'
# exec(program)
# c=5
# print(c)
# class Foo:
#     b = 5
# dummyFoo = Foo()
# print('id of dummyFoo =',id(program))
# print('id of dummyFoo =',id(dummyFoo))
# print('id of dummyFoo =',id(c))
# ccc = input('Enter a program:')
# exec(ccc)
####################################################################################################
# """
# A={"ten":"Nguyen","tuoi":35}
# print(A)
# A={"namsinh":1999}
# print(A)
# """
####################################################################################################

# if True:
#   print("Answer")
#   print("True")
# else:
#   print("false")
# def hi(name):
#   print("Hello ",name)
#   print("Have a good day!")
# hi("2")
# help(print)
# print("%d %d %s" %(2,3,"thienco"))
####################################################################################################



# var1="Python"
# def func1():
#   var1 = "PHP"
#   print("Inside func1() var1 :", var1)
# def func2():
#   global var1 #Call global variable
#   print("Inside func1() var1 :", var1)
# func1()
# func2()
####################################################################################################

# var=10.0
# print("%f" %(var**2))
# a=type(var)
# print(a)
# var='hello'
# a=type(var)
# print(a)
####################################################################################################
# z=(3+2j)
# t=(2-1j)
# print(z+t)
####################################################################################################
# x=7
# y=2
# print(x%y)
# print(int(x/y))
# print(str(x))
####################################################################################################
# s="Hello World"
# print(s[2:5])
# print(s[1:])
# print(s[-1])
# print(s[3]*2)
####################################################################################################
# a=3
# b=5.5
# if (a == 3):
#   print(a)
# elif (b == 5.5):
#   print(b)
# else:
#   print("False")

# while (a):
#   print(a)

# for i in range(0,10):     # i run from 0 to < 10
#   print(i)


####################################################################################################
# program=input("Enter program:")
# exec(program)
####################################################################################################
# from math import *
# exec('print(dir())')
# globalsParameter = {'__builtins__' : None}
# localsParameter = {'print': print, 'dir': dir}
# exec('print(dir())', globalsParameter, localsParameter)
####################################################################################################
# import os
# import random as rand
# from math import sqrt, cos, sin
# os.system('ls -l')
# r=rand.random()
# print(r)

# def caculate(a,b):
#   a*=3
#   b*=5
#   return (a,b)
# x,y = caculate(2,3)
# print(x,y)

# a="ThienCo.\nBatKhaLo"
# b="""Thien Co
# Bat Kha Lo"""
# print(a)
# print(b)


# print(eval('23*12'))
# a="Thien Co Bat Kha Lo"
# print(a[3:-1])
# print(a[-1])
# class Employee:
#   'Common base class for all employees'
#   empCount = 0

#   def __init__(self, name="a", salary=5000):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
#   def displayCount(self):
#       print("Total Employee %d" %Employee.empCount)
#   def displayEmployee(self):
#       print("Name: ", self.name, ", Salary: ",self.salary)

# emp1 = Employee("Toto", 2000)
# emp2 = Employee("Tutu", 5000)
# emp1 = Employee()
# emp2 = emp1
# emp3 = emp1
# del emp1
# del emp2
# del emp3 
# emp1.displayEmployee()
# emp2.displayEmployee()
# print("Total EMployee: %d" %Employee.empCount)
# emp3=emp2
# emp3.displayEmployee()
# emp1.age=7
# print(emp1.age)

# del emp1.age

# print(hasattr(emp1,'name'))
# setattr(emp1, 'age',8)
# getattr(emp1, 'age')

# print("Employee.__doc__:", Employee.__doc__)
# print("Employee.__name__:", Employee.__name__)
# print("Employee.__module__:", Employee.__module__)
# print("Employee.__bases__:", Employee.__bases__)
# print("Employee.__dict__:", Employee.__dict__)

# class Animal:
#   'Common base class for Animals'

#   def __init__(self, name='no-name'):
#       self.name = name
#   def say(self):
#       print("%s can't say" %self.name)

# class Bird(Animal):
#   def say(self):
#       print("%s twitter" %self.name)

# class Cat(Animal):
#   def say(self):
#       print("%s meow" %self.name)
# a = Animal('Dog')
# a.say()
# b = Bird('Flappy')
# b.say()
# c = Cat('Kitty')
# c.say()

# class Owl(Bird,Cat):
#   pass

# o = Owl('Chic')
# o.say()

# class Owlx(Bird,Cat):
#   "extra Owl"
#   def say(self):
#       print("owl...")
#       Cat.say(self)
# ox = Owlx('ChicX')
# ox.say()

