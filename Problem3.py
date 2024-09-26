def makeDistinct(dials):
    actions = []  # Lista para almacenar las acciones
    seen = set()  # Conjunto para almacenar los dígitos ya vistos
    
    for i in range(len(dials)):
        # Si el dígito actual ya está en el conjunto "seen", necesitamos cambiarlo
        while dials[i] in seen:
            actions.append('+')  # Rotamos hacia arriba
            dials[i] = (dials[i] + 1) % 10  # Incrementamos el dígito con ciclo en 9 -> 0
        
        seen.add(dials[i])  # Añadimos el dígito actual al conjunto
        
        # Si no estamos en el último dial, movemos el dedo a la derecha
        if i < len(dials) - 1:
            actions.append('>')
    
    return ''.join(actions)  # Devolvemos las acciones como una cadena de texto

# Ejemplos
print("Solución de la primera secuencia:",makeDistinct([8, 8, 0, 9]))  # Salida esperada: ">+++"
print("Solución de la segunda secuencia:",makeDistinct([8, 9, 9, 1]))  # Salida esperada: "">>+>"
print("Solución de la tercera secuencia:",makeDistinct([0, 1, 0, 2, 0]))  # Salida esperada: ">>>>-<<<+++++"
print("Solución de la cuarta secuencia:",makeDistinct([9]))  # Salida esperada: ""
