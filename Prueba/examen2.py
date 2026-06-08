import random

def generar_dni_peruano() -> str:
    """
    Generar el DNI de una persona (8 dígitos aleatorios).
    Cada posición toma un valor independiente del 0 al 9.
    """
    caracteres = '0123456789'
    # Selecciona exactamente 8 dígitos al azar y los une
    dni = "".join(random.choices(caracteres, k=8))
    return dni

def main() -> None:
    """
    Función principal: genera y muestra directamente el DNI de la persona.
    """
    print("\n" + "=" * 45)
    print("=== ALGORITMO B: GENERADOR DE DNI DE UNA PERSONA ===")
    print("=" * 45)
    
    # Generación directa del DNI solicitado
    dni_persona = generar_dni_peruano()
    
    print(f"El numero de DNI generado para la persona es: {dni_persona}")
    print("=" * 45 + "\n")

if __name__ == "__main__":
    main()