
import datetime
class Post:
    def __init__(self,auteur,message):
        self.author = auteur
        self.body = message
        self.created = datetime.datetime.now()
       
    def format(self):
        date =  self.created.strftime('le %d/%m/%Y a %H:%M:%S')
        return "<div><span>Par {} {}</span><p>{}</p></div>".format(self.author.name,date,self.body)
 
