# Script para verificar el rango de VLAN y permitir al usuario volver a intentarlo o salir

def verificar_rango_vlan(vlan):
    if 1 <= vlan <= 1000:
        print("La VLAN", vlan, "pertenece al rango normal.")
    elif 1002 <= vlan <= 4094:
        print("La VLAN", vlan, "pertenece al rango extendido.")
    else:
        print("El número de VLAN no es válido.")

def main():
    while True:
        try:
            vlan = int(input("Ingrese el número de VLAN: "))
            verificar_rango_vlan(vlan)
        except ValueError:
            print("Por favor, ingrese un número entero válido para la VLAN.")
        
        opcion = input("¿Quiere volver a intentarlo? (s/n): ").lower()
        if opcion != 's':
            break

if __name__ == "__main__":
    main()
