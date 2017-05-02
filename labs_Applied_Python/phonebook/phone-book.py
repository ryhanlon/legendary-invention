# phonebook = {}
#
# cmd = None
# while cmd != 'quit':
#     print('Command? list or add or get or quit')
#     cmd = input()
#     if cmd == 'list':
#         for name in phonebook:
#             print(name)
#     elif cmd == 'add':
#         print('Name?')
#         name = input()
#         print('Phone number?')
#         number = input()
#         phonebook[name] = number
#     elif cmd == 'get':
#         print('Name?')
#         name = input()
#         number = phonebook.get(name, 'no entry')
#         print(name + ' -- ' + number)
#     else:
#         print('Unknown command: ' + cmd)


# create new contact

def show_menu():
    """
    
    :return: 
    """

    print("""
    Press 'A/add' to enter a contact.
    Press 'L/list' see list of contacts.
    Press 'F/find' to find a contact.
    Press "U/update' to update a contact.
    Press 'D/delete" to delete a contact.
    Press 'Q/quit' to exit contacts.
    """).lower()


def add_name_phone(name, mobile, phone_book):
    """
    
    >>> test_book = [{'name': 'Charlene', 'mobile': '7024561234'}, {'name': 'Ty', 'mobile': '8094561234'}, ]     
    >>> add_name_phone('Cherry', '8091239876', test_book)
    Cherry: 8091239876 is now in your Contacts.
    
    
    :param name: 
    :param phone_number: 
    :param phone_book: 
    :return: 
    """
    for name in phone_book:
        name.update({'name': 'mobile'})

    #contact = {'name': name, 'mobile': phone_number}

    print(f"{name} + 'is now in your Contacts.")



    # show list of contacts
def show_list(phone_book):
    """
    
    >>> test_book = [{'name': 'Charlene', 'mobile': '7024561234'}, {'name': 'Ty', 'mobile': '8094561234'}, ]  
    >>> show_list(test_book)
    Charlene
    name: Charlene
    mobile: 7024561234
    *----------------*
    Ty
    name: Ty
    mobile: 8094561234
    
    
    :param phone_book: 
    :return: 
    """

    for name in phone_book:

        print(f"""{name}
         'name:' {name}
         'mobile:' {phone_book[name], phone_number}
          *----------------*
          """)



# retrieve contact

def retrieve_contact(person, phone_book):
    """
    
    
    >>> test_book = [{'name': 'Charlene', 'mobile': '7024561234'}, {'name': 'Ty', 'mobile': '8094561234'}, ]
    >>> retrieve_contact(name, test_book)
    Ty
    name: Ty
    mobile: 8094561234
    *----------------*
    
    
    :param person: 
    :param phone_book: 
    :return: 
    
    """

    for contact in phone_book:
        if person in contact['name']:
            print(person)


# update existing contact, currently only name--expand to number later

def update_contacts(name, update_name, phone_book):
    """
    
    
    >>> test_book = [{'name': 'Charlene', 'mobile': '7024561234'}, {'name': 'Ty', 'mobile': '8094561234'}, ]
    >>> update_contacts('Ty', 'Tyler', test_book)
    Tyler
    name: Tyler
    mobile: 8094561234
    *----------------*
    
    
    :param up_date_name: 
    :param phone_book: 
    :return: 
    """

    for name in phone_book:
        if name == old_name:

            phone_book.remove(old_name)
            phone_book.append(update_name)


# delete contact

def delete_contact(del_name, phone_book):
    """
    
    >>> test_book = [{'name': 'Charlene', 'mobile': '7024561234'}, {'name': 'Ty', 'mobile': '8094561234'}, ]
    >>> delete_contact('Charlene', test_book)
    Contact is deleted.
    
    
    :param del_name: 
    :param phone_book: 
    :return: 
    """

    try:
        for del_name in phone_book:
            phone_book.remove(del_name)
            print("Contact is deleted.")

    except ValueError:
        print("Sorry, try again.")

    else:
        show_menu()



def menu_to_do(phone_book):

    phone_book = list()

    new_item = input("> ")

    while True:
        if new_item == 'A' or new_item == 'add':
            name = input("Enter contact name. ➙  ")
            phone_number = input("Enter phone number. ➙  ")
            add_name_phone(name, phone_number, phone_book)
            continue

        elif new_item == "L" or new_item == 'list':
            show_list(phone_book)
            continue

        elif new_item == "F" or new_item == "find":
            find_name = input("Enter the name to find.")
            retrieve_contact(person, phone_book)
            continue

        elif new_item == "U" or new_item == 'update':
            old_name = input('What name do you want to update?')
            up_date_name = input("What's the new name?")
            update_contacts(name, update_name, phone_book)
            continue

        elif new_item == "D" or new_item == 'delete':
            del_name = input("Enter the name you want to delete.")
            delete_contact(del_name, phone_book)
            continue

        elif new_item == "Q" or new_item == "quit":
            break

# show_menu()
# add_name_phone()
# retrieve_contact()
