import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Name(Field):
    pass


class Phone(Field):
    pass


class Record(Field):
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.add_phone(new_phone)
                self.phones.remove(phone)
                return True

    def delete_phone(self, new_phone):
        for phone in self.phones:
            if phone.value == new_phone:
                self.phones.remove(phone)
                return True




ADDRESSBOOK = AddressBook()
#CONTACTS={}
#CALENDAR={}




def input_error(func): #decorator
    
    def wrapper(*args, **kwargs):
        try:
            result=func(*args, **kwargs)
        
        except (KeyError, ValueError, IndexError) as e:
            print(f"Input data caused the error: {e}.")
            result="----Not result.----"
        return result
    return wrapper

    


    
#@input_error
#--------------------------------------------------------
@input_error
def hello_handler():
    print("How can i help you?")
#--------------------------------------------------------
#@input_error
def exit_handler():
    print("Good bye!")
    exit()
#--------------------------------------------------------
#@input_error
def show_contacts_handler():
    counter=0
    for name, phone in ADDRESSBOOK.data.items():
        counter+=1
        print(f"{counter}. Contact:{name}, phone number: {phone}")
#--------------------------------------------------------
#@input_error
def add_contact_handler(name,phone):
    cl_add_record= Record(name)
    cl_add_record.add_phone(phone)
    ADDRESSBOOK.add_record(cl_add_record)
    
    #CONTACTS[" ".join(name)]="".join(phone)
    print(f"Contact added {name} {phone}")
#--------------------------------------------------------
#@input_error
def change_handler(name,phone):
    
    new_phone = input("input new phone please:")

    record_change = ADDRESSBOOK.data[name]
    record_change.change_phone(old_phone=phone, new_phone=new_phone) 
    print("Changed.")
#--------------------------------------------------------
#@input_error
def phone_handler(name):
    if name in ADDRESSBOOK.data:
        print(ADDRESSBOOK.data[name])
    else:
        print("This person not defined in your contacts.")  

def delete_handler(name,phone):
    
    record_delete = ADDRESSBOOK.data[name]

    if record_delete.delete_phone(phone) is True:
        print("Deleated")

    else:
        return 'The phone number not exist'

#-------------------------------------------------------- нужно указать после всех используемых функций

COMMANDS={

    "hello":hello_handler, 
    "add":add_contact_handler,
    "change":change_handler,
    "phone":phone_handler,
    "deleat phone":delete_handler,
    "show all":show_contacts_handler,
    "good bye":exit_handler,
    "close":exit_handler,
    "exit":exit_handler,
    ".":exit_handler

    }

#--------------------------------------------------------
def command_parser(input_data):

    input_data=str(input_data.lower()) #register non-sensative

    name=[]
   
    phone=[]
   
        
    for key, value in COMMANDS.items():
        
        if input_data.startswith(key):

            if key in ["add", "change", "phone", "deleat phone"]:

                particles_input_data= (input_data.removeprefix(key)).strip()
                particles_input_data=particles_input_data.split(" ")
                
                for i in  particles_input_data:

                    if re.search('[a-z]+', i):
                        name.append(i)
                        
                    elif re.search('[\+0-9]+', i):
                        phone.append(i)
     
                command=COMMANDS[key]  
                phone="".join(phone)
                name=" ".join(name)
                out_func=command(name, phone)# Тут все еще передаются списки из компонентов составного имени и ряда телефонов введенных ранее одной строкой
                
            elif key not in ["add", "change", "phone", "deleat phone"]:
                   
                command=COMMANDS[key]
                out_func=command()

            return out_func

    if "out_func" not in locals(): #Проверяем находится ли доступная команда в инпут через конечный результат функции
        print("Command not definded ")


#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
def main():
    

    while True:

        input_variable= input("Please, input your command:")

        command_parser(input_variable)

        
        

if __name__ == '__main__':  
    exit(main())