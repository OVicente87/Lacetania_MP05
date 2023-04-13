'''Fes una funció per comptar totes les aparicions d’un caràcter específic en un string'''

def contar_caracter_recursivamente(cadena, caracter):
    
    # Verificamos si la cadena es un string
    assert isinstance(cadena, str), "La cadena debe ser un string."
    
    # Verificamos si el caracter es un string de longitud 1
    assert isinstance(caracter, str) and len(caracter) == 1, "El caracter debe ser un string de longitud 1."
    
    # Se ejecuta si la cadena está vacía 
    if len(cadena) == 0:
        return 0
    else:
        # Si el primer carácter de la cadena es el que estamos buscando,
        # retornamos 1 + la llamada recursiva con el resto de la cadena a partir del segundo carácter.
        if cadena[0] == caracter:
            return 1 + contar_caracter_recursivamente(cadena[1:], caracter)
        
        # Si el primer carácter de la cadena no es el caracter que estamos buscando,
        # simplemente retornamos la llamada recursiva con el resto de la cadena a partir del segundo carácter.
        elif cadena[0] != caracter:
            return contar_caracter_recursivamente(cadena[1:], caracter)
        
print(contar_caracter_recursivamente('programar te mantiene intelectualmente activo', 'm'))