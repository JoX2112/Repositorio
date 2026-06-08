import random

def permutacion_con_repeticion(n, r):
    return n ** r

def generar_placa():

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"

    total_letras = permutacion_con_repeticion(26, 3)
    total_numeros = permutacion_con_repeticion(10, 3)

    total_placas = total_letras * total_numeros

    parte_letras = ''.join(random.choices(letras, k=3))
    parte_numeros = ''.join(random.choices(numeros, k=3))

    placa = f"{parte_letras}-{parte_numeros}"

    return placa, total_letras, total_numeros, total_placas

def main():

    print("\n" + "=" * 50)
    print("=== ALGORITMO A: GENERADOR DE PLACAS ===")
    print("=" * 50)

    placa, total_letras, total_numeros, total_placas = generar_placa()

    print(f"\nPermutaciones de letras P(26,3): {total_letras}")
    print(f"Permutaciones de numeros P(10,3): {total_numeros}")
    print(f"Total de placas posibles: {total_placas}")

    print(f"\nPlaca generada: {placa}")

    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()