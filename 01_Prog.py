from random import randint

# DataTypes primitives
#    float    (float)
#    Integer  (int)
#    Boolean  (bool)
#    String§  (str)

# DataStructure to house DataTypes
#   my_list  [House any type of data and can mutate]
#   my_tuple (Same as list but data dont mutate)
#   my_set   {Can not have the same value twice}
#   my_dict  {House a keys with one and only one associate value}


# MathOperation
#   a*b multiplication    a**b power
#   a/b division          a%b  module
#   a+b addition          a//b absolute division
#   a-b subtration

#   from math import ceil, floor, sqrt 
#   (ceil()) 
#   (floor())
#   (sqrt())

# Metods class string
#     format
#         example edad = 40
#                 my_str = f'yo tengo {edad} años'
#     length
#         example len(my_str)

# Functions
#     def funtion_name(parameter):
#        print(parameter)

#     def pow_2(x):
#        return x*x

# Conditionals ?
#   ==
#   <=
#   >=
#   <
#   >
#   !=
#   is not and or in

#    if true:
#       print("hello world")
#    elif:
#       print("brrrrrr")
#    else:
#       print("byebye world")

# Loop
#   count = 0
#   while count < 5:
#       print(count)
#       count += 1

#   numeros = [1, 2, 3]
#   for i in numeros:
#       print(i)

my_list = [randint(0,6) for _ in range(7)]

menor_numero = 0

for elemento in my_list:
    if elemento <= menor_numero:    # selecccional el primer numro de la lista
        menor_numero = elemento     # compararlo con todos los demas y ver si es menor
                                    # en casió de serlo asignarlo a una variable

print(my_list)
print(menor_numero)
