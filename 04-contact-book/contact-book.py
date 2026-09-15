import json

try:
    with open("04-contact-book/contacts.json", "r") as f:
        contact_book = json.load(f)
    

except (FileNotFoundError, json.JSONDecodeError):
    contact_book = []



while True:
    try:
        user_input_menu = int(input("Enter '1' to Add a Contact\n      '2' to View All Contacts\n      '3' to Quit Contact Book\n      '4' to Search a Contact\n      '5' to Delete a Contact\n: "))
        
        if user_input_menu >6 or user_input_menu <1:
            print("Error: Enter Valid Inputs.")
        
        elif user_input_menu == 1:
            name = input("Enter Name: ")
            phone = (input("Enter Phone Number: "))
            email = input("Enter Email: ")
            
            new_contact = {"name": name, "phone": phone, "email": email}
            
            contact_book.append(new_contact)
            
            with open("04-contact-book/contacts.json", "w") as f:
                json.dump(contact_book, f)
            
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
                
        elif user_input_menu == 5:
                try:
                    user_delete = int(input("Enter Contact Index You want to DELETE: "))
                    if (user_delete - 1) >= 0 and user_delete <= len(contact_book):
                        deleted_item = contact_book.pop(user_delete - 1)
                        print(f"You succesfully deleted {deleted_item}")
                        
                        with open("04-contact-book/contacts.json", "w") as f:
                            json.dump(contact_book, f)                        
                    
                    else:
                        print("Enter an existing contact index.")
                        
                except ValueError:
                    print("Invalid Input. Try Again.")
                
                            
    except ValueError:
        print("Please enter a valid input")