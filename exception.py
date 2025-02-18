1
number= int(input("enter the number:"))
try: 
    a=1/number
    print(a)
except ZeroDivisionError:
    print("can't work this operation")
finally:
    print("process completed")
2
number= int(input("enter the number:"))
try: 
    result=1/number
    print(result)
except ZeroDivisionError:
    print("can't work this operation")
except ValueError:
    print("enter the value number:")
finally:
    print("process completed")
3

number= int(input("enter the number:"))
try: 
    square= number**2
    print(square)
except ZeroDivisionError:
    print("can't work this operation")
else: 
    print("square value:",square)
finally:
    print("process completed")

4
number= int(input("enter the number:"))
try: 
    square= number**2
    print(square)
except ZeroDivisionError:
    print("can't work this operation")
except ValueError:
    print("invalid number")
else: 
    print("square value:",square)
finally:
    print("process completed")

5
try: 
    n=int(input("enter the value"))
    if(n<0):
        print("negative number",n)      
except ValueError:
    print("invalid number")
finally:
    print("process completed")
