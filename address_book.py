import json



def create_address_book():
    n=int(input("Enter the number of enteries : "))
    for i in range(n):
        name_of_your_book=input("enter the name of your book: ")
        if address_book_dict1.get(name_of_your_book) is not None:
            print("Already exist")
            break
        else:
            address_book_dict1[name_of_your_book]={}
            First_name=input("enter the first name: ")
            address_book_dict1[name_of_your_book]['First name'] = First_name
            Second_name=input("Enter the second name: ")
            address_book_dict1[name_of_your_book]['second name'] = Second_name
            Mobile_number=input("Enter the Mobile Number: ")
            address_book_dict1[name_of_your_book]['mobile number'] = Mobile_number
            E_mail_address=input("Enter the E-mail_address: ")
            address_book_dict1[name_of_your_book]['E-mail address'] = E_mail_address
    print(address_book_dict1)

def edit_address_book():
    n=int(input("Enter the number of enteries : "))
    name_of_your_book=input("enter the name to change : ")
    for i in range(n):
        if address_book_dict1.get(name_of_your_book) is not None:
            print("1:Edit First name \n2:Edit Second name \n3:Edit Mobile number \n4:Edir E-mail address")
            option1 = int(input())
            if option1 == 1:
                First_name=input("enter the first name: ")
                address_book_dict1[name_of_your_book]['First name'] = First_name
            elif option1 == 2:
                Second_name=input("Enter the second name: ")
                address_book_dict1[name_of_your_book]['second name'] = Second_name
            elif option1 == 3:
                Mobile_number=input("Enter the Mobile Number: ")
                address_book_dict1[name_of_your_book]['mobile number'] = Mobile_number
            elif option1 == 4:
                E_mail_address=input("Enter the E-mail_address: ")
                address_book_dict1[name_of_your_book]['E-mail address'] = E_mail_address
        else:
            print("Does not exist")
            break
    print(address_book_dict1)

def delete_address_book():
    name_of_your_book=input("enter the name of book to del : ")
    if address_book_dict1.get(name_of_your_book) is not None:
        del address_book_dict1[name_of_your_book]
    else:
        print("Does not exist")
    print(address_book_dict1)

    
def display_address_book():
    print(address_book_dict1)
        

def write_to_json():
    a=json.dumps(address_book_dict1)
    file = open("address_book.json",'a')
    file.write(a)
    file.close()

def read_from_json():
    file1 = open('address_book.json','r')
    read_json_data=json.load(file1)
    file1.close()
    print(read_json_data)
            
if __name__ == "__main__":
    address_book_dict1={}
    while True:
        print("1:add values to address book \n2:Edit the address book \n3: To del \n4: To Display\n5:Write to json file\n6:Read from json\n7:to exit")
        option = int(input())
        if option == 1:
            create_address_book()
        elif option == 2:
            edit_address_book()
        elif option == 3:
            delete_address_book()
        elif option == 4:
            display_address_book()
        elif option == 5:    
            write_to_json()
        elif option == 6:
            read_from_json()
        elif option == 7:
            break
        





        #del nes_dict['dict1']