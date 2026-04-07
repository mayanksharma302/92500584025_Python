lst = []

while True:
    print("\n1. Add element")
    print("2. Remove element")
    print("3. Display list")
    print("4. Search element")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        x = int(input("Enter element: "))
        lst.append(x)
    elif choice == 2:
        x = int(input("Enter element to remove: "))
        if x in lst:
            lst.remove(x)
        else:
            print("Element not found")
    elif choice == 3:
        print("List:", lst)
    elif choice == 4:
        x = int(input("Enter element to search: "))
        if x in lst:
            print("Element found")
        else:
            print("Element not found")
    elif choice == 5:
        break
    else:
        print("Invalid choice")
