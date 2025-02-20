    #   (1.single methods)
# class father:
#     def father_methods(self):
#         print("father method useing")
# class baby(father):
#     def baby_methods(self):
#         print("father methods useing baby methods")
# obj=baby()
# obj.father_methods()
# obj.baby_methods()

# #         (2.multiple inheritance)
# class father:
#     def methods1(self):
#         print("father methods used")
# class mother:
#     def methods2(self):
#         print("mother methods useing")
# class baby(father,mother):
#     print ("both methods useing")
# obj=baby()
# obj.methods1()
# obj.methods2()

# #         (3.multilevel inheritances)
# class thatha():
#     def methods1(self):
#         print("thatha methods is very usefull")
# class father(thatha):
#     def methods2(self):
#         print("father methods used thatha methods ")
# class baby(father):
#     def methods3(self):
#         print("both methods are very usefull")
# obj=baby()
# obj.methods3()
# obj.methods2()
# obj.methods1()

# #       (4.hirarchical inheritance)
# class father():
#     def methods1(self):
#         print("father methods useing babys ")
# class baby1(father):
#       pass
# class baby2(father):
#      pass
# obj=baby2()
# obj=baby1()
# obj.methods1()

# #     (5.hybrid inheritances)
# class number1():
#     def methods1(self):
#         print("useing number 1")
# class number2(number1):
#     def methods2(self):
#         print("number2 useing number1 methods ")
# class number3(number1):
#     def methods3(self):
#         print("number3 useing number1 methods")
# class number4(number2,number3):
#     def methods4(self):
#         print("number4 useing number2 and number3 ")
# obj=number4()
# obj.methods4()
# obj.methods1()
# obj.methods2()
# obj.methods3()
    
# #           (6.overring in inheritances)
# class father():
#     def method(self):
#         print("father method usefull")
# class baby(father):
#     def method(self):
#         print("father methods not usefull")
# obj=baby()
# obj.method()

# #            (7.super() methods)
# class father():
#     def method(self):
#         print("father is most usefull")
# class baby(father):
#     def method(self):
#         super().method()
#         print("father and baby methods also using")
# obj=baby()
# obj.method()