# 1 
# for i in range (1,11): 
#   if(i==5):
#    break
#   print(i)

# 4
# for i in range (1,11):
#   if(i==5):
#     continue
#   print(i)

# 10 
# for i in range(1,11):
#     if(i==5):
#      continue
#     if(i==8):
#       break
#     print(i)


# 5
# for i in range (1,11):
#     if(i%2!=0):
#         continue
#     print(i)
  
# 11
# for i in range(1,11):
#     if(i%2!=0):
#      pass
#     if(i%2==0):
#      continue
#     print(i)

# 8
# for i in range (1,20):
#     if(i%3!=0):
#         pass
#     if(i%3==0):
#         continue
#     print(i)


# 6
# list=[1,2,3,4,5,6,-7,8,-6,-4,]
# for i in list:
#     if(i>=0):
#         pass
#     if(i<=0):
#         continue
#     print(i)

# 3
# list=[10,3,0,4,3,3,9,4,96,9732,]
# for i in list:
#     if(i<=0):
#         continue
#     if(i==0):
#         break
#     print(i)


# 2

# list=[1,2,3,4,5,6,7,8,-2,-4]
# for i in list:
#     if(i<0):
#       print(i)

# 12  

# list=[1,-2,3,4,-5,6,7,8,0]
# for i in list:
#     if(i<=0):
#      continue
#     if(i==0):
#      break
#     print(i)

# 9
# list=[1,2,3,4,5,6,7,8,9,0]
# for i in list:
#     if(i==0):
#         pass
#     print(i)

# 7

# x="character"
# y="aieou"
# for character in x:
#     if character in y:
#         continue
#     print(character)

# 12

# list=[1,2,3,4,5,1,10,1]
# mid=len(list)//2
# for index,i in enumerate(list):
#     if(index<mid):
#         continue
#     print(i)    
    
# 13

# product=1
# while(True):
#     num=int(input("enter the number (enter  to stop):"))
#     if(num==0):
#      break
#     product*=num
# print("the product the all numbers is:" ,product)



# my_list = [1, 2, 3, 4, 5, 6, 0]
# midpoint = len(my_list) // 2
# for index in range(midpoint, len(my_list)):
#     element = my_list[index]
#     print(f"Processing element: {element}")