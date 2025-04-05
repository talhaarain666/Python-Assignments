def main():

    fruit_list = ["apple", "banana", "orange", "grape", "pineapple"]
    print("Length before mango: " , len(fruit_list))
    fruit_list.append("mango")

    for fruit in fruit_list:
        print(fruit)
    print("Length of fruit_list after adding mango: " , len(fruit_list))


if __name__ == "__main__":
    main()