########################################################
# Title:  Assignment07 Contact Information
# Dev:  BSpadavecchia
# Date:  February 28, 2022
# Change log: (Who,When,What)
# BSpadavecchia, 02-28-2022, Created Script
#########################################################
# Description:  Demonstration of pickling and error handling in python.

# Pickling demo

import pickle

# Collect contact information to pickle
contact_last_name = str(input("Enter last name of contact:  "))
contact_first_name = str(input("Enter first name of contact  "))
contact_email = str(input("Enter contact email  "))
contact_cell = str(input("Enter cell number of contact  "))
contact_lst = [contact_last_name, contact_first_name, contact_email, contact_cell]
print(contact_lst)


# Save data to a text file using pickle.dump
print("Saving contact data to a file using pickle.dump")
myfile = open("contacts.txt", "ab")
pickle.dump(contact_lst, myfile)
myfile.close()
print("Contact data pickled and saved")

# Read and display saved data using pickle.load
print("Reading contact data to a list from a binary file using pickle.load")
myfile = open("contacts.txt", "rb")
mydata = pickle.load(myfile)
print(mydata)
myfile.close()

# Error Handling demo
print("Press Enter to continue to Error Handling Demo")
print()
# Using the Exception Class to hold information about an error
try:
    new_contact_lst = contact_last_name + contact_cell
    print(new_contact_lst)
except FileNotFoundError as e:
    print("\n" + "Contacts.txt file must exist prior to running this script.  Error report: "+"\n")
    print(e, e.__doc__, e.__str__, type(e), sep="\n")
except Exception as e:
    print("\n" + "An unspecified error occurred?  Error report:  " + "\n")
    print(e, e.__doc__, e.__str__, type(e), sep="\n")

#Error Handling Creating Custom Classes
print("Press Enter to re-run the program with error handling")
print()

class AlphaError(Exception):
    """  Error in not using alphabetical letters for name  """
    def _str_(self):
        return 'Please use alphabetical letter for name fields'
class EntryError(Exception):
    def _str_(self):
        return "Entry not accepted:  Please enter at least one character in contact_last_name"
class NumError(Exception):
    def _str_(self):
        return "Please use only numbers in cell_number field"
class CellNumError(Exception):
    def _str_(self):
        return "Please use 10 numbers in cell_number field"

try:
    contact_last_name = input("Enter your contact's last name:  ")
    if contact_last_name.isnumeric():
        raise AlphaError()
    elif len(contact_last_name) == 0:
        raise EntryError()
    try:
        cell_number = input("Enter your contact's cell phone number:  ")
        if cell_number.isalpha():
            raise NumError()
        elif len(cell_number)!=10:
            raise CellNumError()
        else:
        # Save data to a text file using pickle.dump
            new_contact_lst = [contact_last_name, contact_first_name, contact_email, cell_number]
            print("\n" "Entry complete.  Preparing to save to contacts.txt")
            myfile = open("contacts.txt", "ab")
            print("Saving contact data to a file using pickle.dump")
            pickle.dump(new_contact_lst, myfile)
            myfile.close()
            print("Contact data pickled and saved")
# Read and display saved data using pickle.load
            print("Reading contact data to a list from a binary file using pickle.load")
            myfile = open("contacts.txt", "rb")
            mydata = pickle.load(myfile)
            print(mydata)
            myfile.close()
            print("Program for Assignment07 is over")
    except Exception as e:
        print("\n" + "Error: " + "\n")
        print(e)
except Exception as e:
    print("\n" + "Error: " + "\n")
    print(e, e.__doc__, e.__str__, type(e), sep="\n")
