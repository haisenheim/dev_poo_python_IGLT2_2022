import crypt

class User:
    def __init__(self,id,name,pwd):
        self.id =id
        self.name = name
        self.password = pwd
        self._salt = crypt.mksalt()
        self._password = self._crypt_pwd(pwd)

    def check_pwd(self,pwd):
        return self._password == self._crypt_pwd(pwd) 
   
    def _crypt_pwd(self, p):
        return crypt.crypt(p,self._salt)    

""" def user_check_password(user,pwd):
    return user.password == pwd   """  

john = User(7,"Johnny Depp", "joho")

v = User(9,"Jojo","secret")

print("Je suis {} et mon id est {}, mon mot de passe en clair est {} et mon mot crypte est {} . La clef utilisee est {}".format(john.name,john.id,john.password,john._password,john._salt))
#print("Je suis {} et mon id est {}.".format(v.name,v.id))
if(john.check_pwd("joho")):
    print("le mot de passe est correct !")
else:
    print("Le mot de passe n'est pas correct !") 
