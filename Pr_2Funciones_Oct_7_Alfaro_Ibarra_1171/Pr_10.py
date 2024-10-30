print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practica de funciones.(Lista, argumento)")
#Puede enviar cualquier tipo de datos de argumento a una función
# y se tratará como el mismo tipo de datos dentro de la función.

#Definir funcion y argumentos
def my_function(restaurantes):
  for x in restaurantes:
    print(x)

lugar = ["McDonalds", "BurgerKing", "KFC"]

my_function(lugar)