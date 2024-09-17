import math
def main():
    print("Ohmův zákon kalkulačka:")
    print("1. Výpočet odporu")
    print("2. Výpočet proužku")
    print("3. Výpočet napětí")
    print("4. Konec programu")

def ohms_law(voltage=None, current=None, resistance=None):
    if voltage is not None and current is not None:
        return calculate_resistance(voltage, current)
    elif resistance is not None and current is not None:
        return calculate_current(resistance, current)
    elif resistance is not None and voltage is not None:
        return calculate_voltage(resistance, voltage)
    else:
        raise ValueError("Neplatný vstup. Zadejte dvě hodnoty.")


def calculate_resistance(voltage, current):
    return voltage / current


def calculate_current(resistance, voltage):
    raise NotImplementedError("Výpočet proudu není implementován")


def calculate_voltage(resistance, current):
    raise NotImplementedError("Výpočet napětí není implementován")

    choice = input("Zvolte číslo operace: ")

    if choice == "1":
        voltage = float(input("Zadejte napětí (V): "))
        current = float(input("Zadejte proud (A): "))
        try:
            resistance = calculate_resistance(voltage, current)
            print(f"Odpor: {resistance:.2f} Ω")
        except ValueError as e:
            print(str(e))
    elif choice == "2":
        resistance = float(input("Zadejte odpor (Ω): "))
        current = float(input("Zadejte proud (A): "))
        try:
            voltage = calculate_voltage(resistance, current)
            print(f"Napětí: {voltage:.2f} V")
        except NotImplementedError:
            print("Výpočet napětí není zatím implementován.")
    elif choice == "3":
        resistance = float(input("Zadejte odpor (Ω): "))
        voltage = float(input("Zadejte napětí (V): "))
        try:
            current = calculate_current(resistance, voltage)
            print(f"Proud: {current:.2f} A")
        except NotImplementedError:
            print("Výpočet proudku není zatím implementován.")
    else:
        print("Konec programu.")


if __name__ == "__main__":
    main()