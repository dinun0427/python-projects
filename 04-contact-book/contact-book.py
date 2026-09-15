
contact_book = []

while True:
    try:
        user_input_menu = int(input("Enter '1' to Add a Contact\n      '2' to View All Contacts\n      '3' to Quit Contact Book\n      '4' to Search a Contact\n: "))
        
        if user_input_menu >4 or user_input_menu <1:
            print("Error: Enter Valid Inputs.")
        
        elif user_input_menu == 1:
            name = input("Enter Name: ")
            phone = (input("Enter Phone Number: "))
            email = input("Enter Email: ")
            
            new_contact = {"name": name, "phone": phone, "email": email}
            
            contact_book.append(new_contact)
            
        elif user_input_menu == 2:
            for index, contact in enumerate(contact_book, start=1):
                print(f"{index}: (Name - {contact['name']}\n    Phone - {contact['phone']}\n    Email - {contact['email']})\n")
                
        elif user_input_menu == 3:
            break
        
        elif user_input_menu == 4:
            search = input("Search by name: ")
            found = False
            for contact in contact_book:
                if search.lower() in contact['name'].lower():
                    print(f"The user you are searching is : \n(Name: {contact['name']}\n Phone: {contact['phone']}\n Email: {contact['email']})")
                    found = True
            if not found:
                print(f"No one named {search} found in contact book")                   
    except ValueError:
        print("Please enter a valid input")