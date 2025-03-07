
# 1.pw search pattern
import re
pw_pattern=r"^[a-zA-z0-9]{8,}$"
pw=input("Enter the password:")
if re.match (pw_pattern,pw):
 print("valid pw")
else:
  print("Invalid pw")

# 2. number search pattern
import re
number_condition=r"^[5-9]\d{9}$"
num=input("Enter the mobile number:")
if re.match(number_condition,num):
    print("valid number")
else: 
    print("Invalid number")

# 3.gmail search pattern
import re
gmail=input("Enter gmail id:")
gmail_pattern=r"^[a-zA-Z0-9]+@gmail\.com$"
if re.match(gmail_pattern,gmail):
    print("valid gmail id")
else:
    print("Invalid gmail id")
