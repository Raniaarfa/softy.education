#external packages
from pyjokes import get_joke
from art import text2art

#internal packages
from calcul import add
from calcul import minus
from calcul import mult
from greeting import say_hi

say_hi("Rania!")
name = text2art("Rania")
print(name)

joke = get_joke('en','chuck')
print(joke)






# x = int(input ("Enter a number : "))
# y = int(input ("Enter a number : "))

# #result = add (x,y)
# #result = minus (x,y)

# result = mult(x,y)
# print(f"{x} x {y} = {result} ")

# #greeting.py
# #function say_hi
# #main.py --> say_hi