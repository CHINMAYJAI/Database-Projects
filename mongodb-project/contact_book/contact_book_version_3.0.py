import os
from pymongo import MongoClient, TEXT
from bson import ObjectId  # Used to access the ObjectId which is used to delete unique documents from the database collection


class ContactBook:
    def __init__(self):
        # Initialize MongoDB connection and create database and collection
        mongodb_connection = os.environ.get("MongoDBLink")
        connection_establish = MongoClient(mongodb_connection)
        self.database = connection_establish["Contact-Book"]
        self.collection = self.database["Favouriate-Contacts"]
        # Create text indexes on important fields to enable full-text search capabilities
        self.collection.create_index([("Name", TEXT), ("Address", TEXT), ("Occupation", TEXT)])

    def add_new_contact(self):
        """This function is used to add the new contact in the contact book"""
        print("\n--- Add New Contact ---")  # Section header
        no_of_contacts = int(input("How many contacts do you want to save?\n"))
        encounter_variable = 0
        
        # Continue until the requested number of contacts are added
        while encounter_variable != no_of_contacts:
            # Get contact name and check if it already exists
            contact_name = str(input("Name: "))
            query1 = {"Name": contact_name.title()}
            tracked_name = self.collection.find_one(query1)
            
            if tracked_name:
                # Name already exists, notify user and repeat
                print("\nWARNING: Entered name is already present, please enter new name\n")
                continue
            else:
                # Name is unique, proceed to get phone number
                while True:
                    # Get phone number and check if it already exists
                    contact_phone_number = str(input("Phone Number (10 digits): "))
                    # Check if the phone number is valid
                    if len(contact_phone_number) != 10:
                        print("\nWARNING: Entered phone number is not valid, please enter a valid phone number.\n")
                        continue
                    else:
                        contact_phone_number = int(contact_phone_number)
                    query2 = {"Phone Number": contact_phone_number}
                    tracked_phone_number = self.collection.find_one(query2)
                    
                    if tracked_phone_number:
                        # Phone number already exists, notify user and repeat
                        print("\nWARNING: Entered phone number is already present, please enter new phone number.\n")
                        continue
                    else:
                        # Phone number is unique, get remaining contact details
                        contact_address = str(input("Address: "))
                        contact_occupation = str(input("Occupation: "))
                        
                        # Prepare document for insertion
                        keys = ["Name", "Phone Number", "Address", "Occupation"]
                        values = [
                            contact_name.title(),
                            contact_phone_number,
                            contact_address.title(),
                            contact_occupation.title(),
                        ]
                        document = {}
                        for i in range(4):
                            document.update({keys[i]: values[i]})
                        
                        # Insert document into database
                        document_id = self.collection.insert_one(document)
                        print("\n--- Contact Added Successfully ---")
                        print(f"Document ID: {document_id}\n")
                        encounter_variable += 1 # Increment the counter
                        break # Exit Inner loop

    def update_contact(self):
        """ReNaming the contact name, occupation, phone number, address in mongodb"""
        # Get search query from user for the contact to update
        print("\n--- Update Contact ---")  # Section header
        search_query = str(input("Enter the name or keyword of the person which you want to update: "))
        query = {"$text": {"$search": search_query}}  # Use text search
        
        # Check if any contacts match the search query
        matched_contacts = list(self.collection.find(query))
        
        if matched_contacts:
            print("\nMatch Found ✅")
            # If multiple contacts match, ask user to specify which one to update
            if len(matched_contacts) > 1:
                print(f"{len(matched_contacts)} contacts matched!")
                for i, contact in enumerate(matched_contacts):
                    print(f"{i + 1}: {contact}")
                contact_index = int(input("Select the contact number to update: ")) - 1
                contact_to_update = matched_contacts[contact_index]
            else:
                contact_to_update = matched_contacts[0]

            # Proceed to update the selected contact
            self._search_element_in_document(contact_to_update['Name'])
        else:
            print("\nMatch Not Found ❌")

    def _update_contact_name(self, edit_contact_name):
        """Updates the name of the contact entered by the user"""
        # Get new name for the contact
        new_name = str(input("New name: "))
        updated_query = {"$set": {"Name": new_name.title()}}
        old_query = {"Name": edit_contact_name.title()}
        
        # Update the name in database
        result = self.collection.update_one(old_query, updated_query)
        if result.modified_count > 0:
            print("Successful😊")
        else:
            # Update failed, retry
            print("Unsuccessful☹️, Something went wrong!")
            self._update_contact_name(edit_contact_name)

    def _update_contact_phone_number(self):
        """Updates the phone number of the contact entered by the user"""
        # Get old phone number to identify the contact
        old_phone_number = int(input("Old Phone Number: "))
        query = {"Phone Number": old_phone_number}
        
        # Check if contact with this phone number exists
        if self.collection.find_one(query):
            print("Match Found✅")
            new_phone_number = int(input("New Phone Number: "))
            updated_query = {"$set": {"Phone Number": new_phone_number}}
            self.collection.update_one(query, updated_query)
            print("Successful😊")
        else:
            # Phone number not found, retry
            print("Match Not Found❌\nPlease try again!")
            self._update_contact_phone_number()

    def _update_contact_address(self):
        """Updates the address of the contact entered by the user"""
        # Get old address to identify the contact
        old_contact_address = str(input("Old Contact Address: "))
        query = {"Address": old_contact_address.title()}
        
        # Check if contact with this address exists
        if self.collection.find_one(query):
            print("Match Found✅")
            new_contact_address = str(input("New Contact Address: "))
            updated_query = {"$set": {"Address": new_contact_address.title()}}
            self.collection.update_one(query, updated_query)
            print("Successful😊")
        else:
            # Address not found, retry
            print("Match Not Found❌\nPlease try again!")
            self._update_contact_address()

    def _update_contact_occupation(self):
        """Updates the occupation of the contact entered by the user"""
        # Get old occupation to identify the contact
        old_occupation = str(input("Old Occupation: "))
        query = {"Occupation": old_occupation.title()}
        
        # Check if contact with this occupation exists
        if self.collection.find_one(query):
            print("Match Found✅")
            new_occupation = str(input("New Occupation: "))
            updated_query = {"$set": {"Occupation": new_occupation.title()}}
            self.collection.update_one(query, updated_query)
            print("Successful😊")
        else:
            # Occupation not found, retry
            print("Match Not Found❌\nPlease try again!")
            self._update_contact_occupation()

    def _search_element_in_document(self, edit_contact_name):
        """This function is used to direct the program to their required functions to perform the task"""
        # Ask user which field they want to update
        ask_for_update = str(input("Which field do you want to update?\n(name, phone number, address, occupation)\n"))
        convert_ask_for_update = ask_for_update.lower()
        
        # Direct to appropriate update method based on user choice
        if "name" == convert_ask_for_update:
            self._update_contact_name(edit_contact_name)
        elif "phone number" == convert_ask_for_update:
            self._update_contact_phone_number()
        elif "address" == convert_ask_for_update:
            self._update_contact_address()
        elif "occupation" == convert_ask_for_update:
            self._update_contact_occupation()

    def delete_existing_contact(self):
        """Deleting the contact present in the mongodb database"""
        print("\n--- Delete Existing Contact ---")  # Section header
        search_query = str(input("Enter the name or keyword of the contact you want to delete:\n"))
        query = {"$text": {"$search": search_query}}  # Use text search
        
        # Check if any contacts match the search query
        matched_contacts = list(self.collection.find(query))
        
        if matched_contacts:
            print("\nMatch Found ✅")
            # Handle case where multiple contacts have the same name
            if len(matched_contacts) > 1:
                # Display all matching contacts
                for i, contact in enumerate(matched_contacts):
                    print(f"{i + 1}: {contact}")
                contact_index = int(input("Select the contact number to delete: ")) - 1
                contact_to_delete = matched_contacts[contact_index]
            else:
                contact_to_delete = matched_contacts[0]

            # Confirm deletion
            while True:
                confirmation = str(input(f"\nAre you sure you want to delete '{contact_to_delete['Name']}'? (yes/no): "))
                if "y" in confirmation.lower():
                    self.collection.delete_one({"_id": contact_to_delete["_id"]}) # Delete the specific contact
                    print("\nContact deleted successfully.")
                    break
                elif "n" in confirmation.lower():
                    print("Document is not deleted!")
                    break
                else:
                    print("Please enter a valid input.")
                    continue
        else:
            print("\nMatch Not Found ❌")

    def see_existing_contact(self):
        """This function is used to watch the contact details which the user wants to see"""
        # Get search query from user
        print("\n--- View Existing Contact ---")  # Section header
        search_query = str(input('Enter the name or keyword to search: '))
        # Use MongoDB's full-text search capabilities for more powerful searching
        query = {"$text": {"$search": search_query}}
        
        # Find all matching contacts
        tracked_persons = list(self.collection.find(query))
        
        # Display results
        if tracked_persons:
            print('\nMatches found ✅')
            for person in tracked_persons:
                print(person)
        else:
            print('\nMatch Not Found ❌')

    def run(self):
        """Main method to run the contact book application"""
        while True:
            # Display main menu and get user choice
            print("\n--- Main Menu ---")  # Section header
            user_choice = str(input("What do you want to do?\n1. Adding New Contact\n2. Update Contact\n3. Deleting Existing Contact\n4. Seeing the contact by person name\n**NOTE: Enter the number of the option which you want to perform**\n"))
            
            # Process user choice
            if "1" == user_choice:
                self.add_new_contact()
                self._exit_from_function()
                break
            elif "2" in user_choice:
                self.update_contact()
                self._exit_from_function()
                break
            elif "3" in user_choice:
                self.delete_existing_contact()
                self._exit_from_function()
                break
            elif "4" in user_choice:
                self.see_existing_contact()
                self._exit_from_function()
                break
            else:
                print("\nInvalid Input!")
                continue

    def _exit_from_function(self):
        """This function is used to exit from the program"""
        # Ask if user wants to exit
        ask_user = str(input("Do you want to exit?\nNOTE: Enter the 'y' for yes and 'n' for no\n"))
        if "y" in ask_user.lower():
            exit(0)  # Exit program
        elif "n" in ask_user.lower():
            self.run()  # Return to main menu
        else:
            self._exit_from_function()  # Invalid input, ask again


if __name__ == "__main__":
    # Create contact book instance and run the application
    contact_book = ContactBook()
    contact_book.run()