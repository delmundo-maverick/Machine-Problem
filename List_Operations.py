# Initialize an empty list
my_list = []

while True:
    print("Choose a number to perform operation on the list")
    print("1. Append")
    print("2. Insert")
    print("3. Remove")
    print("4. Pop")
    print("5. Clear")
    print("6. Index")
    print("7. Count")
    print("8. Sort")
    print("9. Reverse")
    print("10. View List")
    print("11. Exit")

    user_input = input("Enter choice to perform: ")
    try:
        choice = int(user_input)

    except ValueError:
        print("Invalid Input. Please enter a number.")
        continue

    # Append Operation
    if choice == 1:
        while True:
            number_of_input = input("How many elements would you like to store: ")
            print("-------------------------------------------------------------")

            try:
                number_of_input = int(number_of_input)

                for i in range(number_of_input):
                    while True:
                        data_type = input("What data type do you want to store: ").upper()

                        if data_type == "STRING":
                            try:
                                element_to_store = input("Enter the element you want to store: ")
                                my_list.append(element_to_store)
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a String.")

                        elif data_type == "INT":
                            try:
                                element_to_store = int(input("Enter the element you want to store: "))
                                my_list.append(element_to_store)
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a whole number.")

                        elif data_type == "FLOAT":
                            try:
                                element_to_store = float(input("Enter the element you want to store: "))
                                my_list.append(element_to_store)
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a decimal number.")

                        elif data_type == "BOOLEAN":
                            try:
                                bool_input = input("Enter the element you want to store (True/False): ").upper()
                                if bool_input == "TRUE":
                                    element_to_store = True
                                elif bool_input == "FALSE":
                                    element_to_store = False
                                else:
                                    raise ValueError("Invalid boolean input")
                                my_list.append(element_to_store)
                                element_stored = True
                                break
                            except ValueError:
                                print("Invalid Input. Please enter True or False.")

                        else:
                            print("Invalid data type. Please choose STRING, INT, FLOAT, or BOOLEAN.")
                break  

            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

    
    # Insert Operation
    elif choice == 2:
        while True:
            number_of_input = input("How many elements would you like to store: ")
            print("-------------------------------------------------------------")

            try:
                number_of_input = int(number_of_input)

                for i in range(number_of_input):
                    while True:
                        data_type = input("What data type do you want to store: ").upper()

                        if data_type == "STRING":
                            try:
                                element_to_store = input("Enter the element you want to store: ")
                                element_index_store = int(input("Enter the index number you want your element to be stored: "))
                                my_list.insert(element_index_store, element_to_store)
                                break 
                                
                            except ValueError:
                                print("Invalid Input. Please enter a whole number for the index number.")
                                continue

                        elif data_type == "INT":
                            try:
                                element_to_store = int(input("Enter the element you want to store: "))
                                element_index_store = int(input("Enter the index number you want your element to be stored: "))
                                my_list.insert(element_index_store, element_to_store)
                                break 
                                
                            except ValueError:
                                print("Invalid Input. Please enter a whole number.")
                                continue

                        elif data_type == "FLOAT":
                            try:
                                element_to_store = float(input("Enter the element you want to store: "))
                                element_index_store = int(input("Enter the index number you want your element to be stored: "))
                                my_list.insert(element_index_store, element_to_store)
                                break 
                                
                            except ValueError:
                                print("Invalid Input. Please enter a decimal.")
                                continue

                        elif data_type == "BOOLEAN":
                            try:
                                bool_input = input("Enter the element you want to store (True/False): ").upper()
                                if bool_input == "TRUE":
                                    element_to_store = True
                                elif bool_input == "FALSE":
                                    element_to_store = False
                                else:
                                    raise ValueError("Invalid boolean input")
                                element_index_store = int(input("Enter the index number you want your element to be stored: "))  # Added input()
                                my_list.insert(element_index_store, element_to_store)
                                element_stored = True
                                break 
                            except ValueError:
                                print("Invalid Input. Please enter True or False.")
                        else:
                            print("Invalid data type. Please enter STRING, INT, FLOAT, or BOOLEAN.")
                            continue
                
                break

            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

    # Remove Operation
    elif choice == 3:
        while True:
            number_of_input = input("How many elements would you like to remove: ")
            print("-------------------------------------------------------------")
            
            try:
                number_of_input = int(number_of_input)
                for i in range(number_of_input):
                    while True:
                        data_type = input("What data type do you want to remove: ").upper()

                        if data_type == "STRING":
                            try:
                                element_to_remove = input("Enter the element you want to remove: ")
                                if element_to_remove not in my_list:
                                    print(f"'{element_to_remove}' not found in the list")
                                    continue
                                else:
                                    my_list.remove(element_to_remove)
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a string.")
                                continue

                        elif data_type == "INT":
                            try:
                                element_to_remove = int(input("Enter the element you want to remove: "))
                                if element_to_remove not in my_list:
                                    print(f"'{element_to_remove}' not found in the list")
                                    continue
                                else:
                                    my_list.remove(element_to_remove)
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a whole number.")
                                continue

                        elif data_type == "FLOAT":
                            try:
                                element_to_remove = float(input("Enter the element you want to remove: "))
                                if element_to_remove not in my_list:
                                    print(f"'{element_to_remove}' not found in the list")
                                    continue
                                else:
                                    my_list.remove(element_to_remove)
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a decimal number.")
                                continue

                        elif data_type == "BOOLEAN":
                            try:
                                bool_input = input("Enter the element you want to remove (True/False): ").upper()
                                if bool_input == "TRUE":
                                    element_to_remove = True
                                elif bool_input == "FALSE":
                                    element_to_remove = False
                                else:
                                    raise ValueError("Invalid boolean input")
                                
                                if element_to_remove not in my_list:
                                    print(f"'{element_to_remove}' not found in the list")
                                    continue
                                else:
                                    my_list.remove(element_to_remove)
                                break
                            except ValueError:
                                print("Invalid Input. Please enter True or False.")
                                continue
                        
                        else:
                            print("Invalid data type. Please enter STRING, INT, FLOAT, or BOOLEAN.")
                            continue

                break
            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

    # Pop Operation
    elif choice == 4:
        while True:
            number_of_input = input("How many elements would you like to remove: ")
            print("-------------------------------------------------------------")
            
            try:
                number_of_input = int(number_of_input)
                for i in range(number_of_input):
                    while True:
                        try:
                            element_to_remove = int(input("Enter the index number of the element you want to remove: "))
                            poped_element = my_list.pop(element_to_remove)
                            print(f"{poped_element} removed.")
                            break
                        except IndexError:
                            print("Invalid Input. Index number out of scope. Please try again.")
                            continue
                        except ValueError:
                            print("Invalid Input. Please enter a whole number.")
                            continue

                break

            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

    # Clear Operation
    elif choice == 5:
        while True:
            my_list.clear()
            print("List successfully cleared")
            break

    # Index Operation
    elif choice == 6:
        while True:
            number_of_input = input("How many element do you want to know the position of: ")

            try:
                number_of_input = int(number_of_input)
                for i in range(number_of_input):
                    while True:
                        data_type = input("What data type do you want to know the position of: ").upper()

                        if data_type == "STRING":
                            try:
                                element_to_search = input("Enter the element you want to know the position of: ")
                                if element_to_search not in my_list:
                                    print(f"'{element_to_search}' not found in the list")
                                    continue
                                else:
                                    print(f"The position of {element_to_search} in the list is {my_list.index(element_to_search)}")
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a string.")
                                continue

                        elif data_type == "INT":
                            try:
                                element_to_search = int(input("Enter the element you want to know the position of: "))
                                if element_to_search not in my_list:
                                    print(f"'{element_to_search}' not found in the list")
                                    continue
                                else:
                                    print(f"The position of {element_to_search} in the list is {my_list.index(element_to_search)}")
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a whole numbers.")
                                continue

                        elif data_type == "FLOAT":
                            try:
                                element_to_search = float(input("Enter the element you want to know the position of: "))
                                if element_to_search not in my_list:
                                    print(f"'{element_to_search}' not found in the list")
                                    continue
                                else:
                                    print(f"The position of {element_to_search} in the list is {my_list.index(element_to_search)}")
                                break
                            except ValueError:
                                print("Invalid Input. Please enter an integer.")
                                continue

                        elif data_type == "BOOLEAN":
                            try:
                                element_to_search = input("Enter the element you want to know the position of (True/False): ")
                                if bool_input == "TRUE":
                                    element_to_remove = True
                                elif bool_input == "FALSE":
                                    element_to_remove = False
                                else:
                                    raise ValueError("Invalid boolean input")
                                
                                if element_to_search not in my_list:
                                    print(f"'{element_to_search}' not found in the list")
                                    continue
                                else:
                                    print(f"The position of {element_to_search} in the list is {my_list.index(element_to_search)}")
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a boolean type.")
                                continue
                break
            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

    # Count Operation
    elif choice == 7:
        while True:
            number_of_input = input("How many element do you want to know the count of: ")

            try:
                number_of_input = int(number_of_input)
                for i in range(number_of_input):
                    while True:
                        data_type = input("Enter the element you want to know the position of: ").upper()

                        if data_type == "STRING":
                            try:
                                element_to_search = input("Enter the element you want to know the position of: ")
                                if element_to_search not in my_list:
                                    print(f"'{element_to_search}' not found in the list")
                                    continue
                                else:
                                    print(f"The position of {element_to_search} in the list is {my_list.count(element_to_search)}")
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a string.")
                                continue

                        elif data_type == "INT":
                            try:
                                element_to_search = int(input("Enter the element you want to know the position of: "))
                                if element_to_search not in my_list:
                                    print(f"'{element_to_search}' not found in the list")
                                    continue
                                else:
                                    print(f"The position of {element_to_search} in the list is {my_list.count(element_to_search)}")
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a whole numbers.")
                                continue

                        elif data_type == "FLOAT":
                            try:
                                element_to_search = float(input("Enter the element you want to know the position of: "))
                                if element_to_search not in my_list:
                                    print(f"'{element_to_search}' not found in the list")
                                    continue
                                else:
                                    print(f"The position of {element_to_search} in the list is {my_list.count(element_to_search)}")
                                break
                            except ValueError:
                                print("Invalid Input. Please enter an integer.")
                                continue

                        elif data_type == "BOOLEAN":
                            try:
                                element_to_search = input("Enter the element you want to know the position of (True/False): ")
                                if bool_input == "TRUE":
                                    element_to_remove = True
                                elif bool_input == "FALSE":
                                    element_to_remove = False
                                else:
                                    raise ValueError("Invalid boolean input")

                                if element_to_search not in my_list:
                                    print(f"'{element_to_search}' not found in the list")
                                    continue
                                else:
                                    print(f"The position of {element_to_search} in the list is {my_list.count(element_to_search)}")
                                break
                            except ValueError:
                                print("Invalid Input. Please enter a boolean type.")
                                continue
                break
            except ValueError:
                print("Invalid Input. Please enter a number.")
                continue

    # Sort Operation
    elif choice == 8:
        while True:
            user_input = input("Are you sure you want to sort the list: [Y/N]").upper()
            if user_input == "Y":
                my_list.sort()
            else:
                break

    # Reverse Operation
    elif choice == 9:
        while True:
            user_input = input("Are you sure you want to reverse sort the list: [Y/N]").upper()
            if user_input == "Y":
                my_list.sort(reverse=True)
            else:
                break

    # Print List
    elif choice == 10:
        print(my_list)

    # Exit
    elif choice == 11:
        break

    else:
        print("Invalid Input. Only choose operations between 1-11.")
        continue