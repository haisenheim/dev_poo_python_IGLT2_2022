import crypt
import datetime
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

class Post:
    def __init__(self,auteur,message):
        self.author = auteur
        self.body = message
        self.created = datetime.datetime.now()
       
    def format(self):
        date =  self.created.strftime('le %d/%m/%Y a %H:%M:%S')
        return "<div><span>Par {} {}</span><p>{}</p></div>".format(self.author.name,date,self.body)

redacteur = User(2,"Clement","red")
post1 = Post(redacteur,"Ceci est le contenu du message") 

print(post1.format())