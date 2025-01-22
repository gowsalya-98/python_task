1

list1=[1,2,3,4,5,6,7,8]
even_number=[]
odd_number=[]
for num in list1: 
 if(num%2==0):
      even_number.append(num)
 else:
    odd_number.append(num)
print(odd_number)
print(even_number)

2

list1=[1,2,3,4,5,6]
print(sum(list1))

3
list1=[1,2,3,0,4,5,6]
product=1
for i in list1:
   if(i!=0):
     product*=i
print(product)

6

books=["kids books","dad books", "mummy books"]
books.reverse()
print(books)

5

list1=[3,5,6,7,89,2,4,1,0]
largest=max(list1)
smallest=min(list1)
print("large value:",largest)
print("smallest value:",smallest)

4

list=[1,2,3,4,1,3]
y=set()
duplicate=[]
for i in list:
   if i in y:
     duplicate.append(i)
   else:
      y.add(i)
print(y)
print(duplicate)

