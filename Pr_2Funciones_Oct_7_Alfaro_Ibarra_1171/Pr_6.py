print("")
print("Alfaro_Ibarra_Sheccid_1171_3w_Practica de funciones.")
#Si no sabe cuántos argumentos se pasarán a su función, 
#agregue un * antes del nombre del parámetro en la definición
#de la función.

def mi_funcion(*fruta):
    print("Fruta en oferta:" + fruta[2])
#De esta manera, la función recibirá una tupla de argumentos
# y podrá acceder a los elementos en consecuencia:
mi_funcion("Manzana", "Mango", "Uva")