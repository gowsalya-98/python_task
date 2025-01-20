# pattern 3

# for i in range (1,6):
#     for j in range(1,6):
#         print(f"{j} ",end=" ")
#     print()    

# pattern 1

# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print() 

# pattern 2

# for i in range(1,6):
#     for j in range(1,6,):
#         print(f"{i}",end=" ")
#     print()

# pattern 3

# for i in range(1,6):
#     for j in range(1,6):
#         print(f"{j}",end=" ")
#     print()
 
# pattern  34

# for i in range(1,6):
#     for j in range (1,i+1):
#         print ("*", end="")
#     print()

# pattern 35

# for i in range(1,6):
#     for j in range(1,i+1):
#      print(f"{i}",end="")
#     print()



# pattern 25

# for i in range (1,6):
#     for j in range(1,6):
#         print(j%2,end=" ")
#     print()

# pattern 27

# row=5
# for i in range(1,6):
#     for j in range(1,6):                              
#       print(chr(64+j),end=" ")
#     print()

# pattern 26

# row=5
# for i in range(1,6):
#     for j in range(1,6):                                  
#         print(chr(64+i),end=" ")
#     print()


# pattern 31

# letters="ABCDEFGHIJKLMNOPQRSTUVWXY"
# row=5
# cols=5
# for i in range(row):                                             
#     for j in range(cols):
#         print(letters[(i+j)% len (letters)],end=" ")
#     print()

# pattern 29

# letters="EDCBA"
# for i in range(5):
#     for j in range(5):
#         print(letters[(j)%len (letters)],end=" ")
#     print()

# pattern 28

# letters="EDCBA"
# for i in range(5):
#     for j in range(5):
#         print(letters[(i)%len (letters)],end=" ")
#     print()

# pattern 32

# letters="ABCDEFGHIJKLMNOPQRSTUVWXY"
# row=5
# cols=5
# for i in range(row):                                             
#     for j in range(cols):
#         print(letters[(i*j)% len (letters)],end=" ")
#     print()

#  patters 30  

# letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# rows = 5
# cols = 5
# index = 0
# for i in range(rows):
#     for j in range(cols):
#         if index < len(letters):
#             print(letters[index], end=" ")
#             index += 1
#     print()

# patterns 23

# for i in range (1,6):
    # for j in range(1,6):
    #     print(i%2,end=" ")
    # print()
  

# patters 19

# rows = 5
# cols = 5
# for i in range(1, rows + 1):
#     value = i % 2  
#     for j in range(1, cols + 1):
#         print(value, end=" ")
#         value = 1 - value 
#     print()


# patters 24

# rows = 5
# cols = 5
# for i in range(1, rows + 1):
#     value = 0  
#     for j in range(1, cols + 1):
#         print(value, end=" ")
#         value = 1 - value 
#     print()



