import entities

clement = entities.User(2,"Clement ESSOMBA","red")
junior = entities.User(1, "Junior malatou","123")
alain = entities.User(1, "Alain NGUIMBI","123")
jacq = entities.User(1, "Jacquemin moutoto","123")

post1 = entities.Post(jacq,"La date des rattrapages a été reportée au 13/06/2022")
commentaire1 = entities.Commentaire(clement,"Ok, C'est entendu")
post1.commenter(commentaire1)
post1.commenter(entities.Commentaire(jacq,"Preparez les sujets"))
post1.commenter(entities.Commentaire(alain,"Au besoin deposer les notes de classe"))

print(post1.format())

print(post1.getCommentaires())