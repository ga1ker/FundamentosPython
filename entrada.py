#function input ->retorna string

num_a=int(input("Ingresa un número: "))
num_b=int(input("Ingresa un número: "))

print(num_a+num_b)

name=input("Ingresa tu nombre: ")
age=int(input("Ingresa tu edad : "))
city=input("Ingresa tu ciudad: ")

#string format
"""
hola soy galker
jhj
"""
greeting="Hola soy {}, tengo {} años y vivo en {}"

print(greeting.format(name, age, city))

greeting2=f"Hola soy {name}, tengo {age} años y vivo en {city}"
print(greeting2)