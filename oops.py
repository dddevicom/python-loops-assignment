#Syntax
# class classname():
#     Attribute
#     methods


# class person_details():#class definition
#     user_name = "pythonlife" #attribute
#     emp_id = 1234 #attributes
#     def details(self): #methods
#         print(f"working at MNC company ",self.user_name)
#     def details2(self):#methods
#         print(f"he runs ABC company {self.emp_id}")
#         self.details()
#syntax
# objname = classname()
# raj_kumar = person_details()
# raj_kumar.details()
# raj_kumar.details2()
# print(raj_kumar.user_name)
# print(raj_kumar.emp_id)
# raj_kumar.details2()




# age = 35
# def details(a):
#     print(f"working at MNC company")
#     print(age)
# details()


# class mobilephone():#class definition
#     brand_name = "samsung" #attributes
#     color = "white" #attributes
#     model = 2025 #attributes
#     def calling(self,bn):
#         print(f"you are calling from {bn}")
#     def message(self,pn):
#         print(f"message sent successfully {pn}")
#     def camera(self,internal_storage):
#         print(f"photo captured...... internal storage {internal_storage}")
#     def browsing(self,nissue):
#         print(f"network issue .....{nissue}")
# #syntax
# # objname = classname()
# samsung = mobilephone()
# samsung.calling("samsung")
# samsung.message(12345678990)
# samsung.camera("128gb")
# samsung.browsing("samsung")
# oppo = mobilephone()
# oppo.calling("oppo")
# oppo.message(4567895644)
# oppo.camera("256gb")
# oppo.browsing("oppo")

# vivo = mobilephone()
# vivo.calling("vivo")
# vivo.message(9648949)
# vivo.camera("512gb")
# vivo.browsing("vivo")






# class laptop():
#     def __init__(self,bn,color,os,model):
#         self.bn = bn
#         self.color = color
#         self.os = os
#         self.model =model
#     def gaming(self,):
#         print(f"you are gaming biohazard4 on {self.bn}")
#     def browsing(self,browser):
#         print(f"you are browsing from {self.bn} on {browser}")
#     def movies(self,):
#         print(f"you are watching movies..{self.os} model {self.model}")
# lenova = laptop("lenova","white","windows",2025)
# lenova.gaming()
# lenova.browsing("chrome")
# lenova.movies()


# apple = laptop("apple","black","mac",2024)
# apple.gaming()
# apple.browsing("safari")



# class ATM():
#     balance = 1000
#     def __init__(self,bn,location,serial,):
#         self.bn = bn
#         # self.bn = bn
#         # self.bn = bn
#         pass
#     def deposit(self,amount):
#         pass
#     def withdraw(self):
#         pass
#     def balance(self):
#         pass

# sbin = ATM("sbin","hyd",1234)
# while True:

#     sbin.deposit(1000)















###################### sept 23 2025 ###################
# class feature_phone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def make_call(self,number):
#         print(f"calling {number} from {self.brand} {self.model}")
#     def send_message(self,message,number):
#         print(f"sending {message} from {number}")
# nokia = feature_phone("nokia",2002)
# nokia.make_call(1234568790)
# nokia.send_message("hello",12345678901)
# class smartphone(feature_phone):






# class feature_phone():
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def make_call(self,number):
#         print(f"calling {number} from {self.brand} {self.model}")
#     def send_message(self,message,number):
#         print(f"sending {message} from {number}")

# class smartphone(feature_phone):
#     def camera(self):
#         print(f"photo captured........")
#     def browsing(self):
#         print(f"internet browsing")
#     def gaming(self):
#         print(f"playing gta {self.brand}")
# nokia = smartphone("nokia",2025)
# nokia.camera()
# nokia.browsing()
# nokia.gaming()
# nokia.make_call(519564984984)
# nokia.send_message("hi",48156165495)






#one base class multiple derived classes
# class a():
#     def parent(self):
#         print("this is parent class")
# class b(a):
#     def child1(self):
#         print("this is child 1 class")
# class c(a):
#     def child2(self):
#         print("this is child 2 class")
# obj = b()
# obj.child1()
# obj.parent()

# obj1 = c()
# obj1.child2()
# obj1.parent()












#multiple base class one derieved class  --> multiple class
# class parent1():
#     def father(self):
#         print("this is father class")
# class parent2():
#     def mother(self):
#         print("this is mother class")
# class child(parent1,parent2,):
#     def child(self):
#         print("this is child class")
# obj = child()
# obj.child()
# obj.father()
# obj.mother()










# class gfather():
#     def output(self):
#         print(f"earned 100cr properties")
# class father(gfather):
#     def output1(self):
#         print(f"this is father class")
# class child(father):
#     def output2(self):
#         print(f"this is child class")
#     def sample(self):
#         print(f"started ABC company")

# obj = child()
# obj.output2()
# obj.output1()
# obj.output()
# obj.sample()













# polymorphism ---> implementing same thing in different forms
#two types
#1. overloading --> 1. operator overloading 2.method overloading
#2. method overriding


#operator overloading
# (+)
# a = 10
# b = 20
# print(a+b)


# a = "kiran"
# b = "raju"
# print(a+b)



# method overloading ---> 
# method name should be same
# arguments must be different ---> in the terms of length or type of arguments
# class calculator():
#     def add(self,a,b):
#         print(a,b)
#     def add(self,a,b,c):
#         print(a,b,c)
# obj = calculator()
# obj.add(20,20,20)
# obj.add(10,20)


# class calculator():
#     def add(self,a=50,b=1234566,c=25):
        # print(a,b,c)
#         print(a+b+c)
# obj = calculator()
# obj.add(10,10,10)
# obj.add(10,10,)
# obj.add(10,)
# obj.add()
# obj.add("vasu","frontend",1234)
# obj.add("raju","backend")
# obj.add("rakesh",)
# obj.add()





#2. method overriding
# # 2.method overriding--> method name should be same, arguments should be also same length

# class gfather():
#     def details(self,a):
#         print(f"this is gfather class",a)
# class father(gfather):
#     def details(self, a):
#         print(f"this is father class",a)
#         super().details("100cr")
# obj = father()
# obj.details("100cr")




# class gfather():
#     def output(self):
#         print(f"earned 100cr properties")
# class father(gfather):
#     def output(self):
#         print(f"this is father class")
#         super().output()
# class child(father):
#     def output(self):
#         print(f"this is child class")
#         super().output()
    # def sample(self):
    #     super().output()
# obj = child()
# obj.output()
# obj.sample()





# class ATM():
#     def __init__(self):
#         pass
#     def deposit(self):
#         pass
# class ATM2():
#     def withdraw(self):


# class ATM3(ATM2,ATM)
