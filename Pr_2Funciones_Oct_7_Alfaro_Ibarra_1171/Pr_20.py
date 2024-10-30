print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practica de funciones.")
#Recursión de funciones, significa que
#una función definida puede llamarse a sí misma.
#Definir funcion y argumento
def recursion(k):
  if(k > 0):
    result = k - recursion(k - 2)
    print(result)
  else:
    result = 0
  return result

print("Ejemplo de recursion:")
recursion(6)