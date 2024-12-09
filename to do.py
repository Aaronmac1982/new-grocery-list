def welcome_message():
    print("Welcome to my grocery list")
    
def add_item():
    item = input("Enter grocery item to add: ")
    grocery_list.append(item)
    print(f"Item '{item}' added sucessfully")
    
def view_items():
    if not grocery_list:
        print("Your grocery list is empty.")
    else:
        print("Grocery List :")
        for i, item in enumerate(grocery_list):
            print(f"{i+1}. {item}")
            
def delete_item():
    view_items()
    if not grocery_list:
        return
    index_to_delete = int(input("Enter the number of items to delete: ")) - 1
    del grocery_list[index_to_delete]
    print("Item deleted sucessfully")
    
def quit_app():
    Print("Exiting application. Goodbye")
    
grocery_list =[]

while True:
    welcome_message()
    print("\nMenu:")
    print("!. Add items")
    print("2. View items")
    print("3. Delete items")
    print("4. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_item()
    elif choice == "2":
        view_items()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        quit_app()
        break
    else:
        print("Invalid choice. Please try again.")