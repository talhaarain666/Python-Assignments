def main():
    try:
        i = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return
    while i < 100:
        curr_value = i * 2
        print("The double of the number is:", curr_value)
        i = curr_value 

if __name__ == '__main__':
    main()


