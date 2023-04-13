'''Fes la funció de comprovació de palíndrom utilitzant recursivitat'''

def es_palindromo(candidato):
    # Comprueba que el argumento es una cadena
    assert isinstance(candidato, str), "El argumento debe ser un string"
   
    # Si el string mide 0 o 1, devuelve True
    if len(candidato) <= 1:
        return True
    
    # Si el primer y último carácter son iguales, llama recursivamente a la función con el string sin el primero ni el último carácter
    elif candidato[0] == candidato[-1]:
        return es_palindromo(candidato[1:-1])
    
    # Si el primer y último carácter no son iguales, devuelve False
    elif candidato[0] != candidato[-1]:
        return False

print(es_palindromo('luzazul'))

print(es_palindromo('luz'))