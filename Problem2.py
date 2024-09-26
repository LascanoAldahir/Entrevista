# Importamos Counter para contar la frecuencia de caracteres en la cadena
from collections import Counter

class NearPalindromesDiv1:
    # Contamos cuántas veces aparece cada letra en la cadena S
    def solve(self, S: str) -> int:
        # Contamos cuántas letras tienen una frecuencia impar
        frequency = Counter(S)

        # Conteo de cuántas letras tienen una palabra impar
        odd_count = sum(1 for count in frequency.values() if count % 2 != 0)

        # Para que una cadena sea un "casi palíndromo", solo puede haber un carácter con frecuencia impar.
        # Si hay más de uno, necesitamos ajustar o eliminar caracteres hasta que solo quede uno con frecuencia impar.
        # El número mínimo de operaciones será ajustar todos los caracteres impares, excepto uno (si es que hay alguno).
        return max(0, odd_count - 1)

# Método principal para realizar pruebas con ejemplos
if __name__ == "__main__":
    # Creamos una instancia de la clase NearPalindromesDiv1
    solver = NearPalindromesDiv1()
    
     # Probamos con algunas palabras de ejemplo y esperamos los resultados
    print(solver.solve("cocoa"))      # Espera: 0 (ya es un casi palíndromo)
    print(solver.solve("daddy"))      # Espera: 2 (se requieren dos cambios para que sea un casi palíndromo)
    print(solver.solve("abcdefgh"))   # Espera: 4 (se requieren cuatro cambios para que sea un casi palíndromo)
