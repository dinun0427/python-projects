import json


def load_contacts():
    try:
        with open("04-contact-book/contacts.json", "r") as f:
            contacts = json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []

    return contacts


def save_contacts(contacts):
    with open("04-contact-book/contacts.json", "w") as f:
        json.dump(contacts, f)


def add_contact(contacts):
    while True:
        try:
            name = input("Enter Name: ").strip()
            if name.isdigit():
                raise ValueError("Numeric Values are not allowed.")
            elif not name:
                raise ValueError("Empty inputs are not allowed.")
            else:
                break

        except ValueError as error:
            print(f"Error: {error} Please try again.")

    while True:
        try:
            phone = (input("Enter Phone Number: ")).strip()
            if not phone:
                raise ValueError("Empty inputs are not allowed.")
            else:
                break

        except ValueError as error:
            print(f"Error: {error} Please try again.")

    while True:
        try:
            email = input("Enter Email: ").strip()
            if not email:
                raise ValueError("Empty inputs are not allowed.")
            elif email.isdigit():
                raise ValueError("Numeric values are not allowed.")
            elif "@" not in email:
                raise ValueError("Invalid email '@' is missing.")
            else:
                break

        except ValueError as error:
            print(f"Error: {error} Please try again.")

    new_contact = {"name": name, "phone": phone, "email": email}

    contacts.append(new_contact)

    save_contacts(contacts)


def view_contact(contacts):
    for index, contact in enumerate(contacts, start=1):
        print(
            f"{index}: (Name  - {contact['name']}\n    Phone - {contact['phone']}\n    Email - {contact['email']})\n"
        )


def search_contact(contacts):
    search = input("Search by name: ")
    found = False

    for contact in contacts:
        if search.lower() in contact["name"].lower():
            print(
                f"The contact you are searching is : \n(Name: {contact['name']}\n Phone: {contact['phone']}\n Email: {contact['email']})"
            )
            found = True

    if not found:
        print(f"No one named {search} found in contact book")


def delete_contacts(contacts):
    while True:
        try:
            user_delete = int(input("Enter Contact Index You want to DELETE: "))
            if (user_delete - 1) >= 0 and user_delete <= len(contacts):
                deleted_item = contacts.pop(user_delete - 1)
                print(f"You succesfully deleted {deleted_item}")

                save_contacts(contacts)

                break

            else:
                print("Enter an existing contact index.")

        except ValueError:
            print("Invalid Input. Try Again.")


def edit_contacts(contacts):
    while True:
        try:
            edit_index = int(input("Enter user index to edit : "))
            if (edit_index - 1) >= 0 and edit_index <= len(contacts):
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
            elif edit_name == contacts[edit_index - 1]["name"]:
                print("You have entered the same name. Use a different name.")
            else:
                old_name = contacts[edit_index - 1]["name"]
                contacts[edit_index - 1]["name"] = edit_name
                print(f"Successfully edited the name from {old_name} to {edit_name}.")

                break
        except ValueError as error:
            print(f"Error: {error} Please try again.")

    # --- Edit phone ---
    while True:
        try:
            edit_phone = input("Enter the new phone for the contact : ").strip()
            if not edit_phone:
                raise ValueError("Empty inputs are not allowed.")
            elif edit_phone == contacts[edit_index - 1]["phone"]:
                print("You have entered the same phone number. Use a different one.")
            else:
                old_phone = contacts[edit_index - 1]["phone"]
                contacts[edit_index - 1]["phone"] = edit_phone
                print(
                    f"Successfully edited the phone number from {old_phone} to {edit_phone}."
                )

                break

        except ValueError as error:
            print(f"Error: {error} Please try again.")

    # --- Edit email ---
    while True:
        try:
            edit_email = input("Enter the new email for the contact : ").strip()
            if not edit_email:
                raise ValueError("Empty inputs are not allowed.")
            elif edit_email.isdigit():
                raise ValueError("Numeric values are not allowed.")
            elif edit_email == contacts[edit_index - 1]["email"]:
                print("You have entered the same email. Use a different one.")
            elif "@" not in edit_email:
                raise ValueError("Invalid email '@' is missing.")
            else:
                old_email = contacts[edit_index - 1]["email"]
                contacts[edit_index - 1]["email"] = edit_email
                print(
                    f"Successfully edited the email from {old_email} to {edit_email}."
                )

                break

        except ValueError as error:
            print(f"Error: {error} Please try again.")

    # --- Save once, after all three edits are done ---
    save_contacts(contacts)


def main():

    contact_book = load_contacts()

    while True:
        try:
            user_input_menu = int(
                input(
                    "Enter '1' to Add a Contact\n      '2' to View All Contacts\n      '3' to Quit Contact Book\n      '4' to Search a Contact\n      '5' to Delete a Contact\n      '6' to Edit a Contact\n: "
                )
            )

            if user_input_menu > 6 or user_input_menu < 1:
                print("Error: Enter Valid Inputs.")

            elif user_input_menu == 1:
                add_contact(contact_book)

            elif user_input_menu == 2:
                view_contact(contact_book)

            elif user_input_menu == 3:
                break

            elif user_input_menu == 4:
                search_contact(contact_book)

            elif user_input_menu == 5:
                delete_contacts(contact_book)

            elif user_input_menu == 6:
                edit_contacts(contact_book)

        except ValueError:
            print("Please enter a valid input")


if __name__ == "__main__":
    main()
