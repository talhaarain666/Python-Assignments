C = 299792458

def main():
    m = float(input("Enter mass in kg: "))
    e = m * C**2
    print(f"Energy (E) = {e} joules of energy!")

if __name__ == '__main__':
    main()