contacts = {}
while True:
        print(" Contact Book: ")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input(" Enter your choice: ")
        if choice == '1':

            # Get contact details from user
            name = input(" Enter Name: ")
            email = input(" Enter Email: ")
            phone = input(" Enter Phone Number: ")
            address = input(" Enter Address: ")
            #store contact details in dictionary
            contacts[name] = {
            "email": email, 
            "phone": phone,
            "address": address
                                                            }
            print(" Contact added successfully!")

        elif choice == "2":
            # Check if contact book is empty
             if not contacts:
              print(" No contacts found!")
             else:
               # Display all contacts
                for name, details in contacts.items():
                 print("\nName:", name)
                 print("Phone:", details["phone"])
                 print("Email:", details["email"])
                 print("Address:", details["address"])
        elif choice == "3":
                search_name = input(" Enter name to search:")
            # Check if contact exits
                if search_name in contacts:
                 details = contacts[search_name]
                 print("\nName:", search_name)
                 print("Phone:", contacts[search_name]["phone"])
                 print("Email:", contacts[search_name]["email"])
                 print("Address:", contacts[search_name]["address"])
                else:
                 print(" Contact not found!")
        elif choice == "4":

              # Update contact details
                name = input (" Enter contact name to update: ")

            # Check if contact exits

                if name in contacts:
            # Get new contact details from user
                    phone = input(" Enter new phone number: ")
                    email = input(" Enter new email: ")
                    address = input(" Enter new address: ")

            # Update contact details
                    contacts[name] = {
                                "email": email,
                                "phone": phone,
                                "address": address
                        }
                print(" Contact updated successfully!") 
        elif choice == "5":
            # delete contact name
            name = input(" Enter contact name yo delete:")

            # Check if contact exits

            if name in contacts:
            # Delete contact
             del contacts[name]
             print(" Contact deleted successfully!")
            else:
             print(" Contact not found!")
        elif choice == "6":
          print(" Thank you for using the contact book!")
          break             
