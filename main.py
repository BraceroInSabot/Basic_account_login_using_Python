from colorama import Fore
from UserInfo.userclass import Acc

print('Welcome to\n')
print(Fore.RED + 'Exemple Book Marks Market!')
print(Fore.RESET)
print('First of all you need to login on our server to buy something!\n')

# User Inputs
name1: str = str(input('username: '))
email1: str = str(input('e-mail: '))    
password1: str = str(input('password: '))

# Inputs Validation
userinfos: Acc = Acc(id, name1, email1, password1)

# Logged in confirmation
print(f"\nCongrats!\nYour are now logged as {userinfos.name} | #ID: {userinfos.id}, always check your email for offers!")
print("\nHave a good shop on EBM Market!")

# FF
print(Fore.YELLOW + f"\nFun fact: this is how your password is stocked: {userinfos.password}")