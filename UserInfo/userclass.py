from random import randint
from passlib.hash import pbkdf2_sha256 as cryp

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