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

# Numeros mayores a 3999
1. 