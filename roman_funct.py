valors = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

def dividir_en_digitos(n:int):
    """
    TODO: evitar que entren numeros mayores de 3999. Lanzar ValueError
    """

    cad = f"{n:04d}"
    # millares = centenas = decenas = unidades = 0

    millares = int(cad[0]) * 1000
    centenas = int(cad[1]) * 100
    decenas = int(cad[2]) * 10
    unidades = int(cad[3]) * 1

    return [millares, centenas, decenas, unidades]

    
def divisor_n(n:int):

    len_n = len(str(n))    
    order = int(str(1).ljust(len_n,'0'))
    number = int(n/order)
    
    return (number, order)


def to_roman(n:int):

    a, b = divisor_n(n)
    
    if a <= 3:
        result = a * valors[b]
    elif a == 4:
        result = valors[1*b] + valors[5*b]
    elif a < 9:
        result = valors[5*b] + (a - 5) * valors[b]
    elif a == 9:
        result = valors[b] + valors[10*b]
    else:
        result = valors[b]        

    return result


def digitos_a_roman(lista):
    result = ""
    for numero in lista:
         result += to_roman(numero)
        
    return result

def arabigo_a_romano(n: int):
    lista = dividir_en_digitos(n)
    return digitos_a_roman(lista)