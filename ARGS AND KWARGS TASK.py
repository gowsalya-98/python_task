def my_sum(a,b):
  print(a + b)
my_sum(23, 23)


def my_sum(a,b):
  print(a * b)
my_sum(3, 3)




def my_Concatenate(kids,mummy):
  print("concatenate words "+ kids, mummy)
my_Concatenate("gowsalya","sudha")





def my_keywords(kids,mummy):
  print("keywords "+ mummy)
my_keywords(kids="gowsalya",mummy="sudha")


def display(**keyswords): 
 print("display dict:",keyswords)
 
items={
         "child1":"Emil", 
         "child2" : "Tobias", 
         "child3" :"Linus"
}
display(**items)
