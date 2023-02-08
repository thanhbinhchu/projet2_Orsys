def ATP():
    f = open(r"proprietaire.txt", "r")

    for ligne in f:
        l = ligne.split(";")
        print("Le nom du propriétaire est:", l[1])
    f.close()


def rec(x):
    f = open(r"compte.txt", "r")
    d = {}
    for ligne in f:
        l = ligne.split(";")
        if l[0].strip() == x:
            d['idProp'] = l[1]
            d['solde'] = l[2]
            d['Dte'] = l[3]
            d['Type'] = l[4]
            return d
        else:
            return "Compte n'existe pas"
    f.close()


def dernier():
    f = open(r"compte.txt", "r")
    lignes = f.readlines()
    # print(len(lignes))
    if (len(lignes)) == 0:
        print("fichier vide")
    else:
        last_line = lignes[-1].split(";")
    f.close()
    return last_line[0]


def sp():
    f = open(r"proprietaire.txt", "a")
    idp = input("donner l'identifiant du prop:")
    nom = input("donner le nom du prop:")
    cin = input("donner le numéro cin du prop:")
    tel = input("donner le num du tel du prop:")
    ad = input("donner l'adresse du prop:")
    ligne = idp + ";" + nom + ";" + cin + ";" + tel + ";" + ad + "\n"
    f.write(ligne)
    f.close()
    return ligne


def date():
    from datetime import datetime
    date_time = datetime.now()  # date actuelle
    return (date_time.strftime("%d-%m-%Y"))


def cc():
    f = open(r"compte.txt", "a")
    idc = int(dernier()) + 1
    dp = input("donner l'identifiant du prop:")
    solde = input("donner le solde:")
    d = date()
    b = ['True', 'False']
    while 1:
        typee = input("donner le type:(True/False)")
        if typee in b: break
    ligne = str(idc) + ";" + dp + ";" + str(solde) + ";" + d + ";" + typee + "\n"
    f.write(ligne)
    f.close()
    return ligne

