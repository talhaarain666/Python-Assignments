def access_fruit(fruit_list, index):
    try:
        return fruit_list[index]
    except IndexError:
        return "Index out of range"
    
def modify_fruit(fruit_list, index, new_fruit):
    try:
        fruit_list[index] = new_fruit
        return fruit_list 
    except IndexError:
        return "Index out of range"
    
def slice_list(fruit_list, firstInd, lastInd):
    try:
        return fruit_list[firstInd:lastInd]
    except IndexError:
        return "Index out of range"

def main():
    fruit_list = ["apple", "banana", "orange", "grape", "pineapple"]
    print("Fruits list:", fruit_list)
    user_input = input("Select an operation (1: Access, 2: Modify, 3: Slice): ")

    if user_input == "1":
        index = int(input("Enter the index of the fruit you want to access: "))
        result = access_fruit(fruit_list, index)
        print(result)
    elif user_input == "2":
        index = int(input("Enter the index of the fruit you want to modify: "))
        new_fruit = input("Enter the new fruit: ")
        result = modify_fruit(fruit_list, index, new_fruit)
        print(result)
    elif user_input == "3":
        firstInd = int(input("Enter the starting index for slicing: "))
        lastInd = int(input("Enter the ending index for slicing: "))
        result = slice_list(fruit_list, firstInd, lastInd)
        print(result)
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    main()