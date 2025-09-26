import math

# Funktsiya 1: Obchislennya z = 1 / sqrt(m + sqrt(2))
def calculate_z():
    try:
        m = float(input("Vvedit chislo m: "))
        
        # Perevirka, shchob viraz pid korenem buv dodatinim
        if m + math.sqrt(2) <= 0:
            print("Pomylka: viraz pid korenem maye buty dodatnim")
            return None
        
        z = 1 / math.sqrt(m + math.sqrt(2))
        return z
    except ValueError:
        print("Pomylka: vvedit korektne chislo")
        return None
    except ZeroDivisionError:
        print("Pomylka: dilennya na nul")
        return None

# Funktsiya 2: Perevirka, chy ye chislo prostym
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Perevirka dilnykiv vid 5 do sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def check_prime_number():
    try:
        n = int(input("Vvedit chislo n dlya perevirky na prostotu: "))
        
        if is_prime(n):
            print(f"Chislo {n} ye prostym")
        else:
            print(f"Chislo {n} ne ye prostym")
        
        return is_prime(n)
    except ValueError:
        print("Pomylka: vvedit cile chislo")
        return False

# Golovna programa
def main():
    print("=== Programa z dvoma funktsiyamy ===")
    print()
    
    # Vikonannya pershoyi funktsiyi
    print("1. Obchislennya z = 1 / sqrt(m + sqrt(2))")
    result_z = calculate_z()
    if result_z is not None:
        print(f"Rezultat: z = {result_z:.6f}")
    print()
    
    # Vikonannya drugoyi funktsiyi
    print("2. Perevirka chisla na prostotu")
    check_prime_number()

# Zapusk programy
if __name__ == "__main__":
    main()