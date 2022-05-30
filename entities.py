
import datetime
class User:
    def __init__(self,id,name,pwd):
        self.id =id
        self.name = name
        self.password = pwd


class Post:
    def __init__(self,auteur,message):
        self.author = auteur
        self.body = message
        self.created = datetime.datetime.now()
        self.commentaires = []
        self.votes = []
       
    def format(self):
        date =  self.created.strftime('le %d/%m/%Y a %H:%M:%S')
        """   return "<div><span>Par {} {}</span><p>{}</p></div>".format(self.author.name,date,self.body) """
        return "<div><span>Par "+  self.author.name +" "+ date +"</span>"
        +"<p>"+ self.body +"</p>"
        +self.getCommentaires()
        +"</div>"


    def getCommentaires(self):
        ret = '<ul>'
        for commentaire in self.commentaires:
            ret = ret+'<li>'+ commentaire.format() +'</li>'
        ret = ret +'</ul>'
        return ret

    def commenter(self, commentaire):
        self.commentaires.append(commentaire)

    def voter(self, vote):
        self.votes.append(vote)    

class Commentaire:
    def __init__(self,author,contenu):
        self.author = author
        self.contenu = contenu
        self.heure = datetime.datetime.now()

    def format(self):
        date =  self.heure.strftime('le %d/%m/%Y a %H:%M:%S')
        return "<div><span>Par {} {}</span><p>{}</p></div>".format(self.author.name,date,self.contenu)    

class Vote:
    def __init__(self,points,author):
        self.points = points
        self.author = author
        self.heure = datetime.datetime.now()
                
