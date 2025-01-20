days="monday"
match (days):
    case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
         print("weekday")
    case "saturday"|"sunday":
        print("weekend")
month=7
match(month):
    case 1|3|5|7|8|12:
      print("days of 31")
    case 4|6|11:
      print("days of 30")
    case 2:
         print("day of 28 or 29")
percentage=20
match(percentage):
    case p if(90<=p<100):
        print("grade A")
    case P if(80<=p<90):
        print("grade B")
    case p if(70<=p<80):
        print("grade c")
    case p if(60<=p<70):
        print("grade d")
    case p if(50<=p<60):
        print("pass")
    case p if(0<=p<50):
        print ("fail")
month="may"
match month:
    case "december"|"january"|"february":
        print(month+" season of winter ")
    case "march"|"april"|"may":
        print(month +"season of spring")
    case"june"|"july"| "august":
        print(month+"season of summer")
    case"september"| "october"|"november":
        print(month+"season of fall")
p=0
match(p):
    case p if(p>0):
        print("postive number")
    case p if(p<0):
        print("negative number")
    case p if(p==0): 
        print("zero")

a=input("enter a letter: ")
match a:
    case "a"|"e"|"i"|"o"|"u":
        print("vowel")
    case "b"|"c"|"f"|"g"|"h"|"j"|"k"|"l"|"m"|"n"|"p"|"q"|"r"|"s"|"t"|"v"|"w"|"x"|"y"|"z":
        print("consonant")    
y=29
match y:
    case y if(1<y<20):
        print(" 10 to 20 range")
    case y if(21<y<30):
        print("20 to 30 range")
    case y if(31<y<50):
        print("30 to 50 range")
       