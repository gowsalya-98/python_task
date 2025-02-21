# 
# (1.cls and object)
# class sbi_bank():
#     credit=2000
#     debit=4000
# #     loan=10000
# # sbi_bank1=sbi_bank()
# # print(sbi_bank1.debit)
# # a=sbi_bank1.debit=1500
# # print(a)
# # sbi_bank2=sbi_bank()
# # print(sbi_bank2.loan)

#     def cash(self):
#         print(" More amount transaction of sbi bank 1")
#     def loan1(self):
#         print("less transaction in loan devision")
#     def credit1(self):
#         print("people not ready to tranction" )
# bank1=sbi_bank()
# bank1.cash()
# bank2=sbi_bank()
# bank2.loan1()
# bank3=sbi_bank()
# bank3.credit1()


# # a=sbi_bank.credit1=("more tracsaction")
# # print(a)

# a=sbi_bank()
# b=a.credit1=("moe")
# print(b)

#  (2.cls and object with constructor)

class phone:
   def __init__(self ,a_call,b_call,c_call,d_call):
      self.a_call=a_call
      self.b_call=b_call
      self.c_call=c_call
      self.d_call=d_call
   def a(self):
      print(f"a_call is messages you {self.a_call}")
   def b(self):
      print(f"b_call is whatsapp msg you {self.b_call}")
   def c(self):
      print(f"look a instragram pages {self.c_call}")
   def d(self):
      print(f"using more times in mobile {self.d_call}")

obj=phone("ring1","ring2","ring3","ring4")
obj.a()
obj.b()
obj.c()
obj.d()  
     