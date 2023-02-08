from datetime import date



def proprietaire(data):
    p =open('proprietaire.txt','w')
#    p.write("ID " + " NOM " + " NO-IDENTITY " + " TELEPHONE " + " ADRESSE " + "\n")

    new = "y"
    while new == "y":
        a = int(input("L’identifiant du propriétaire du compte: "))
        b = input("Le nom du propriétaire du compte: ")
        c = input("Le numéro de la carte d’identité nationale du propriétaire du compte: ")
        d = input("Le numéro de téléphone du propriétaire du compte: ")
        e = input("L’adresse du propriétaire du compte: ")

        f = str(a) + " ; " + b + " ; " + c + " ; " + d + " ; " + e + "\n"

        p.write(f)

        new = input("Nouveau Proprietaire? y/n")

    p.close()


def compte(data):
    c = open('compte.txt','w')
#    c.write("ID COMPTE " + " ID PROPRIETAIRE " + " SOLDE " + " DATE" + " TYPE ")

    new = "y"
    while new == "y":
        g = int(input("L’identifiant du compte: "))
        h = int(input("L'identifiant du proprietaire: "))
        i = float(input("Le montant du compte: "))
#        j = date(input("Date d'ouverture du compte: "))
#        k = bool(input("Compte courant ? Y/N "))

        m = str(g) +" ; " + str(h) +" ; " + str(i) +" ; " + "\n "
        c.write(m)

        new = input("Nouveau Compte ? y/n ")

    c.close()

def AfficherTousProprietaires():
    d = {}
    with open("proprietaire.txt") as p:
        d = [line.rstrip('\n') for line in p]

#    a = "Bonjour tout le monde"

 #   mots = a.split()
  #  for m in mots:

   #     d[m]=mots.count(m)

    print(d)

def RechercherCompte(idCompte):
    p = open('compte.txt', 'r')

    for line in p:
        l = line.split(";")
        list = {'idCompte': l[0] ,
                'idProprietaire' : l[1] ,
                'solde' : l[2]
#                'date' : l[3] ,
#                'type' : l[4]
                }
        if idCompte == l[0]:
            print(list)
    p.close()

def SaisirProprietaire(idProprietaire):
    p = open('proprietaire.txt', 'r')
    for ligne in p:
        l = ligne.split(";")

        ligne = {"idProprietaire" : l[0] ,
                 "Nom" : l[1],
                 "id Card" : l[2],
                 "Telephone " : l[3],
                 "Adresse" : l[4]
                 }
        if idProprietaire == l[0]:

            print(ligne)


    print(ligne)


def CreerCompte(data):
    c = open('compte.txt', 'a')
    #    c.write("ID COMPTE " + " ID PROPRIETAIRE " + " SOLDE " + " DATE" + " TYPE ")

    new = "y"

    for ligne in c:
        l = ligne.split(";")

        ligne = {"idCompte" : l[0] ,
                 "idProprietaire" : l[1],
                 "solde" : l[2],
                 "Date " : l[3],
                 "Type" : l[4]
                 }


        while new == "y":
                g = l[0] +1
                h = int(input("L'identifiant du proprietaire: "))
                i = float(input("Le montant du compte: "))
                j = date.now()
                k = bool("compte courant ...?")


                m = str(g) + " ; " + str(h) + " ; " + str(i) + " ; " + j + "\n "

                c.write(ligne[m])

                new = input("Nouveau Compte ? y/n ")

    c.close()









if __name__ == '__main__':
    data = [] ;
    proprietaire(data)
    compte(data)
    AfficherTousProprietaires()
    RechercherCompte('123')
    SaisirProprietaire(111)
    CreerCompte(data)

