import random
def generar_placas(cantidad=5):
    """
    Generar una muestra aleatorio de placas combinando letras y numeros.
    Se usa el concepto de producto cartesiano (permutaciones con repeticion).
    """
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'

    placas_generadas = []

    for _ in range(cantidad):
        letras_elegidas = "".join(random.choices(letras,k=3))
        numeros_elegidos = "".join(random.choices(numeros,k=3))
        placas_generadas.append(f"{letras_elegidas}-{numeros_elegidos}")

    return placas_generadas

print("=== ALGORITMO A: GENERADOR DE PLACAS ===")
lista_de_placas = generar_placas(5)

for i, placa in enumerate(lista_de_placas, 1):
    print(f"Placa {i}: {placa}")
