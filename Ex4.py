'''Passa un nombre sencer positiu a binari utilitzant recursivitat'''

def entero_a_binario(num):
    # Hacemos saltar un error si el argumento no es un entero positivo
    assert isinstance(num, int) and num >= 0, "El argumento debe ser un número entero positivo"
    # Si el número es 0, devuelve una cadena vacía.
    if num == 0:
        return ''
    # Devuelve el resultado de llamar a la función con el cociente de num entre 2 seguido del resto
    else:
        return entero_a_binario(num // 2) + str(num % 2)

    
print(entero_a_binario(8))
print(entero_a_binario('hola'))   