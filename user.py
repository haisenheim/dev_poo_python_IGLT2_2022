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

 
