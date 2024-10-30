print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practica de funciones.(combinacion)")
#Puede combinar los dos tipos de argumentos en la misma función.
#Definir funcion y argumentos
def my_function(lugar, fecha, /, *, nombre, Apellido):
  print("No estuve en "+lugar +" el " + fecha+". " + nombre +" " + Apellido)

my_function("Casa", "30 de octubre, 2024", nombre="Sheccid", Apellido = "Alfaro")
#Cualquier argumento antes de / es solo posicional
# y cualquier argumento después de * es solo de palabra clave.