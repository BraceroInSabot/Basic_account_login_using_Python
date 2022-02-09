from random import randint
from colorama import Fore
from passlib.hash import pbkdf2_sha256 as cryp

print('Welcome to\n')
print(Fore.RED + 'Exemple Book Marks Market!')
print(Fore.RESET)
print('First of all you need to login on our server to buy something!\n')

# User account infos
class Acc:

    def __init__(self, id, name, email, password):
        self.__id = randint(0, 9999999999)
        self.__name = name
        self.__email = email
        self.__password = cryp.hash(password, rounds=randint(0, 9999999), salt_size=32)

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def password(self):
        return self.__password

# User Inputs
name1 = input('username: ')
email1 = input('e-mail: ')    
password1 = input('password: ')

# Inputs Validation
userinfos = Acc(id, name1, email1, password1)

# Logged in confirmation
print(f"Congrats! your are logged as {userinfos.name} #ID: {userinfos.id}, always check your email for offers!")
print(f'Have a good shop on EBM Market!')

# FF
print(f"Fun fact: this is how your password is stocked: {userinfos.password}")