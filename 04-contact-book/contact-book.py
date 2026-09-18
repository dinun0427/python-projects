import json

try:
    with open("04-contact-book/contacts.json", "r") as f:
        contact_book = json.load(f)
    

except (FileNotFoundError, json.JSONDecodeError):
    contact_book = []



while True:
    try:
        user_input_menu = int(input("Enter '1' to Add a Contact\n      '2' to View All Contacts\n      '3' to Quit Contact Book\n      '4' to Search a Contact\n      '5' to Delete a Contact\n      '6' to Edit a Contact\n: "))
        
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
                print(f"{index}: (Name  - {contact['name']}\n    Phone - {contact['phone']}\n    Email - {contact['email']})\n")
                
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
        
        elif user_input_menu == 6:
            while True:
                try:
                    edit_index = int(input("Enter user index to edit : "))
                    if (edit_index - 1) >= 0 and edit_index <= len(contact_book):
                        break
                    else:
                        print("Out of range. Please enter a valid Index.")
                except ValueError:
                    print("Try Again. Enter a valid input.")

            # --- Edit name ---
            while True:
                try:
                    edit_name = input("Enter the new name for the contact : ").strip()
                    if edit_name.isdigit():
                        raise ValueError("Numeric Values are not allowed.")
                    elif not edit_name:
                        raise ValueError("Empty inputs are not allowed.")
                    elif edit_name == contact_book[edit_index - 1]['name']:
                        print("You have entered the same name. Use a different name.")
                    else:
                        old_name = contact_book[edit_index - 1]['name']
                        contact_book[edit_index - 1]['name'] = edit_name
                        print(f"Successfully edited the name from {old_name} to {edit_name}.")
                        break
                except ValueError as error:
                    print(f"Error: {error} Please try again.")

            # --- Edit phone ---
            while True:
                edit_phone = input("Enter the new phone for the contact : ").strip()
                if not edit_phone:
                    print("Empty inputs are not allowed. Please try again.")
                elif not edit_phone.isdigit():
                    print("Phone number must contain digits only. Please try again.")
                elif edit_phone == contact_book[edit_index - 1]['phone']:
                    print("You have entered the same phone number. Use a different one.")
                else:
                    old_phone = contact_book[edit_index - 1]['phone']
                    contact_book[edit_index - 1]['phone'] = edit_phone
                    print(f"Successfully edited the phone number from {old_phone} to {edit_phone}.")
                    break

            # --- Edit email ---
            while True:
                edit_email = input("Enter the new email for the contact : ").strip()
                if not edit_email:
                    print("Empty inputs are not allowed. Please try again.")
                elif edit_email.isdigit():
                    print("Numeric values are not allowed. Please try again.")
                elif edit_email == contact_book[edit_index - 1]['email']:
                    print("You have entered the same email. Use a different one.")
                elif '@' not in edit_email:
                    print("Invalid email. Please try again.")
                else:
                    old_email = contact_book[edit_index - 1]['email']
                    contact_book[edit_index - 1]['email'] = edit_email
                    print(f"Successfully edited the email from {old_email} to {edit_email}.")
                    break

            # --- Save once, after all three edits are done ---
            with open("04-contact-book/contacts.json", "w") as f:
                json.dump(contact_book, f)
            
                    
                            
    except ValueError:
        print("Please enter a valid input")