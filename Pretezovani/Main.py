from Zbozi import Zbozi
from ZlevneneZbozi import ZlevneneZbozi

def main():
    try:
        # Create an instance of Zbozi
        zbozi = Zbozi("Jablka", 100.0)
        print(f"Cena zbozi: {zbozi.get_cena()}")

        # Create an instance of ZlevneneZbozi
        zlevnene_zbozi = ZlevneneZbozi("Hrusky", 200.0, 0.25)
        print(f"Cena zlevneneho zbozi: {zlevnene_zbozi.get_cena()}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()