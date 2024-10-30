print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practica de funciones.")
#definir funcion con argumentos
#Si se desconoce el número de argumentos de
# palabras clave, agregue un doble **antes del nombre del parámetro:
def mi_funcion(**alumno):
    print("Ultimo alumno en entrar: " + alumno["Persona"])

mi_funcion (al1="Alex", Persona="Sheccid")
