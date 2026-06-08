import random

def permutacion_con_repeticion(n, r):
    return n ** r

def generar_dni_peruano():

    # El primer dígito no puede ser 0
    primer_digito = random.choice("123456789")

    # Los otros 7 dígitos pueden ser del 0 al 9
    restantes = ''.join(random.choices("0123456789", k=7))

    dni = primer_digito + restantes

    total_dnis = 9 * permutacion_con_repeticion(10, 7)

    return dni, total_dnis

def main():

    print("\n" + "=" * 60)
    print("=== ALGORITMO B: GENERADOR DE DNI DE UNA PERSONA ===")
    print("=" * 60)

    dni, total_dnis = generar_dni_peruano()

    print(f"\nCantidad de DNIs posibles: {total_dnis}")
    print(f"DNI generado para la persona: {dni}")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()