'''Fes una funció per sumar els dígits d’un nombre sencer positiu utilitzant recursivitat.'''

def suma_digits_sencer(n):
    assert n >= 0 and int(n) == n, 'El número debe ser un entero'
    if n < 10:
        return n
    else:
        last_num = n % 10
        n = int(n / 10)
        total = last_num + suma_digits_sencer(n)
        return total
    
print(f"Resultado de la primera versión: {suma_digits_sencer(12345)}")
       


    
def suma_digits_versio2(n):
    assert n >= 0 and int(n) == n, 'El número debe ser un entero'
    if n == 0:
        return n
    return (n % 10 + suma_digits_versio2(int(n / 10)))   

print(f"Resultado de la segunda versión: {suma_digits_versio2(1234)}")

