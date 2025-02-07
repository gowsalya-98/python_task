a=open("text","x")

# read text
a=open("text.txt","r")
print(a.read())


# write text
a=open("text.txt","a")
a.write("this is more usefull")
a.close()
a=open("text.txt","r")
print(a.read())

    # readline text
with open("text.txt") as file:
    content=file.readline()
print(content)


    #   cha text
with open ("text.txt") as file:
    content=file.read(15)
print(content)