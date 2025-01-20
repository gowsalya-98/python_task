# for number in range(1,11):
#  print(number)
# for number in range(1,10,2):
#     print( number)
# for w in "hello":
#     print(w)
# sum=0
# for i in range(1,11):
#     # print(i)
#     sum=sum+i
# print(sum)
# for i in range(10,1,-1):
#     print(i)
# for i in range(10,20,+2):
#     print(i)
# for i in range(20,50,+5):
#     print(i)
# a=15
# factorial=10
# for i in range(1,a+1):
#     factorial*=i
# print(factorial)
# for num in range(10,21):
#     is_prime=True
#     if num>1:
#      for i in range(2,num):
#       if(num %i==0):
#             is_prime=False
#       if(is_prime):
#           print(num)
# number=[1,800,73,43,67,80]
# large_number=number[0]
# for num in number:
#  if(num>large_number):
#   large_number=num
# print("large valu:",large_number)
# number=[12,4,456,800]
# greater_number=number[0]
# for num in number:
#     if(num>=greater_number):
#         greater_number=num
# print("greater than 10:",greater_number)
# product=1
# for i in range(1,6):
#     product*=i
# print(product)


# product=1
# while(True):
#     num=int(input("enter the number (enter  to stop):"))
#     if(num==0):
#      break
#     product*=num
# print("the product the all numbers is:" ,product)

# total_sum=0
# while(True):
#     num=int(input("enter the number:"))
    
#     if(num<0):
#        break
#     total_sum+=num
# print("the number sun:",total_sum)

# input_string=input("enter the vowels:")
# vowels=["a","i","o","e","u"]
# count=0
# for num in input_string:
#     if num in  vowels:
#         count+=1
# print("count the number of vowels:",count)

input_string="hello worlds in "
output_string=""
index=0
for char in input_string:
    if char!=" ":
        output_string+=char
print(" string without space:",output_string)


input_string="hello saravanamani "
output_string=""
index=0
while index < len(input_string):
    if input_string [index]!=" ":
        output_string+=input_string[index]
    index+=1    
print("string without space:",output_string)


