
contact_book = []

while True:
    try:
        user_input_menu = int(input("Enter '1' to Add a Contact\n      '2' to View All Contacts\n      '3' to Quit Contact Book\n: "))
        
        if user_input_menu >3 or user_input_menu <1:
            print("Error: Enter Valid Inputs.")
        
        if user_input_menu == 1:
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
                            
    except ValueError:
        print("Please enter a valid input")