  
# (poly with function)  
def add (a,b):
    return a + b
print(add("good","bad"))
print(add(2,7))
print(add([1,2,3],[1,3,4]))

# (overriding)
class birds:
    def over_sound(self):
        print("more sound birds")
class parrot(birds):
    def over_sound(self):
        print("yes more sound ")
class sparrow(birds):
    def over_sound(self):
        print("this more  powerfull")
class penguin(birds):
    def over_sound(self):
        print("less more sounds ")
birds = [parrot(),penguin(), sparrow()]
for birds in birds:
    birds.over_sound()  






    
