def main():
    ab_length = float(input("Enter the length AB: "))
    ac_length = float(input("Enter the length AC: "))
    bc_length = (ab_length ** 2 + ac_length ** 2) ** 0.5
    print(f"The length BC is: {bc_length}")
    
if __name__ == '__main__':
    main()