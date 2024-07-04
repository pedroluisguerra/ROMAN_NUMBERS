# Tests

- Crear una funcion que pase de numero arabigo a romano (menor de 4000)
"""
to_roman(n: int) -> str
"""
- Test de unidades simples
- Test de numeros que suman de mayor a menor
Despues de la investigacion hemos decidido que un buen algoritmo es

1. Dividir el numero (siempre menor de 4000) en millares, centenas, decenas y unidades. Poner en una lista
2. Procesar cada item de la lista transformandolo en romano. Tendre que retocar el algoritmo que ya tengo
3. Concatenar de mayor a menor los simbolos romanos obtenidos

# Numeros mayores de 3999

1. Dividir el numero en miles (grupos de tres digitos) de derecha a izquierda. Si el ultimo es menor de 4 se añade ese digito al grupo de tres anterior, quedando como grupo de 4 menor de 4000

2. Los numeros los vamos a poner en una lista ordenada de derecha a izquierda

3. Iterar sobre la lista para conseguier el numero romano y añadirle "*" * posicion en la lista

concatenar en orden de menos a mas asteriscos cada uno de los romanos