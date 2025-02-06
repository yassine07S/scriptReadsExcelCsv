employes=[]
developement=[]

def ajouter(n):
    developement=[]
    for i in range(n):
        information={
            "matricule":int(input("entrez le matricule d'employe "+str(i+1)+": ")),
            "nom":input("entrez le nom d'employe "+str(i+1)+": "),
            "prenom":input("entrez le prenom d'employe "+str(i+1)+": "),
            "j":int(input("entrez le jour de naissance d'employe "+str(i+1)+": ")),
            "m":int(input("entrez le mois de naissance d'employe "+str(i+1)+": ")),
            "a":int(input("entrez le annee de naissance d'employe "+str(i+1)+": ")),
            "je":int(input("entrez le jour de embauche d'employe "+str(i+1)+": ")),
            "me":int(input("entrez le mois de embauche d'employe "+str(i+1)+": ")),
            "ae":int(input("entrez le annee de embauche d'employe "+str(i+1)+": ")),
            "gsm":int(input("entrez le telephone d'employe "+str(i+1)+": ")),
            "salaire":float(input("entrez le salaire d'employe "+str(i+1)+": ")),
            "fonction":input("entrez fontion d'employe "+str(i+1)+": "),
            "eva":developement
        }        
        employes.append(information)


def modifier(matricule_rech):
    for i in range(n):
        if employes[i]["matricule"]==matricule_rech:
                employes[i]["matricule"]=int(input("entrez le neuveau matricule d'employe "+str(i+1)+": "))
                employes[i]["nom"]=input("entrez le neuveau nom d'employe "+str(i+1)+": ")
                employes[i]["prenom"]=input("entrez le neuveau prenom d'employe "+str(i+1)+": ")
                employes[i]["j"]=int(input("entrez le neuveau jour de naissance d'employe "+str(i+1)+": "))
                employes[i]["m"]=int(input("entrez le neuveau mois de naissance d'employe "+str(i+1)+": "))
                employes[i]["a"]=int(input("entrez le neuveau annee de naissance d'employe "+str(i+1)+": "))
                employes[i]["je"]=int(input("entrez le neuveau jour de embauche d'employe "+str(i+1)+": "))
                employes[i]["me"]=int(input("entrez le neuveau mois de embauche d'employe "+str(i+1)+": "))
                employes[i]["ae"]=int(input("entrez le neuveau annee de embauche d'employe "+str(i+1)+": "))
                employes[i]["gsm"]=int(input("entrez le neuveau telephone d'employe "+str(i+1)+": "))
                employes[i]["salaire"]=float(input("entrez le neuveau salaire d'employe "+str(i+1)+": "))
                employes[i]["fonction"]=input("entrez le neuveau fontion d'employe "+str(i+1)+": ")


def supprime(matricule_supp):
    for i in employes:
        if i["matricule"] == matricule_supp:
            employes.remove(i)



def ajouter_une_echelle_a_un_employe(matr_note):
    for i in employes:
        if i["matricule"]==matr_note:
            developement=[]
            for x in range(5):
                v={
                    "evalution":int(input("entrez l'echelle d'employe "+str(x+1)+": "))
                }
                developement.append(v)
            i["eva"]=developement


def affiche_un_employe(mat_rech):
    for i in employes:
        if i["matricule"]==mat_rech:
            print(f"Matricule: {i['matricule']}")
            print(f"Le nom: {i['nom']}")
            print(f"Le prénom: {i['prenom']}")
            print(f"La date de naissance: {i['j']}/{i['m']}/{i['a']}")
            print(f"La date d'embauche: {i['je']}/{i['me']}/{i['ae']}")
            print(f"Le Numéro de Téléphone: {i['gsm']}")
            print(f"Le salair: {i['salaire']}")
            print(f"La fonction: {i['fonction']}")
            print("evolution")
            for x in i["eva"]:
                print(x)


def affiche_tout_les_employes():
    for i in employes:
        print(f"Matricule: {i['matricule']}")
        print(f"Le nom: {i['nom']}")
        print(f"Le prénom: {i['prenom']}")
        print(f"La date de naissance: {i['j']}/{i['m']}/{i['a']}")
        print(f"La date d'embauche: {i['je']}/{i['me']}/{i['ae']}")
        print(f"Le Numéro de Téléphone: {i['gsm']}")
        print(f"Le salair: {i['salaire']}")
        print(f"La fonction: {i['fonction']}")
        print("evolution")
        for x in i["eva"]:
            print(x)


def  exporter(file):
    with open(file,"w") as f :
        for i in employes:
            f.write(f"Matricule: {i['matricule']}\n")
            f.write(f"Le nom: {i['nom']}\n")
            f.write(f"Le prénom: {i['prenom']}\n")
            f.write(f"La date de naissance: {i['j']}/{i['m']}/{i['a']}\n")
            f.write(f"La date d'embauche: {i['je']}/{i['me']}/{i['ae']}\n")
            f.write(f"Le Numéro de Téléphone: {i['gsm']}\n")
            f.write(f"Le salair: {i['salaire']}\n")
            f.write(f"La fonction: {i['fonction']}\n")
            f.write(f"Echelle: {i['eva']}\n")
    f.close



def importt(file):
    fh=open(file,"r") 
    data=fh.read()
    print(data)


def augmetation(mat_augmrtation,how_much):
    for i in employes:
        if i["matricule"]==mat_augmrtation:
            g=i["salaire"]*(how_much/100)
            i["salaire"]=i["salaire"]+g


def recherche(reche):
    if reche == "nom":
        nomm = input("entrez nom of employe : ")
        for i in employes:
            if i["nom"] == nomm:
                print(f"Matricule: {i['matricule']}")   
                print(f"Le nom: {i['nom']}")
                print(f"Le prénom: {i['prenom']}")
                print(f"La date de naissance: {i['j']}/{i['m']}/{i['a']}")
                print(f"La date d'embauche: {i['je']}/{i['me']}/{i['ae']}")
                print(f"Le Numéro de Téléphone: {i['gsm']}")
                print(f"Le salair: {i['salaire']}")
                print(f"La fonction: {i['fonction']}")
                print("evolution")
                for x in i["eva"]:
                    print(x)
                break
    elif reche == "date embauche":
        jee = int(input("entrez le jour de embauche d'employe "))
        mee = int(input("entrez le mois de embauche d'employe "))
        aee = int(input("entrez le annee de embauche d'employe "))
        for i in employes:
            if i["je"] == jee and i["me"] == mee and i["ae"] == aee:
                print(f"Matricule: {i['matricule']}")   
                print(f"Le nom: {i['nom']}")
                print(f"Le prénom: {i['prenom']}")
                print(f"La date de naissance: {i['j']}/{i['m']}/{i['a']}")
                print(f"La date d'embauche: {i['je']}/{i['me']}/{i['ae']}")
                print(f"Le Numéro de Téléphone: {i['gsm']}")
                print(f"Le salair: {i['salaire']}")
                print(f"La fonction: {i['fonction']}")
                print("evolution")
                for x in i["eva"]:
                    print(x)
                break
    elif reche == "fonction":
        fonctionn = input("entrez fonction of employe : ")
        for i in employes:
            if i["fonction"] == fonctionn:
                print(f"Matricule: {i['matricule']}")   
                print(f"Le nom: {i['nom']}")
                print(f"Le prénom: {i['prenom']}")
                print(f"La date de naissance: {i['j']}/{i['m']}/{i['a']}")
                print(f"La date d'embauche: {i['je']}/{i['me']}/{i['ae']}")
                print(f"Le Numéro de Téléphone: {i['gsm']}")
                print(f"Le salair: {i['salaire']}")
                print(f"La fonction: {i['fonction']}")
                print("evolution")
                for x in i["eva"]:
                    print(x)
                break
            
while True:
    print("________MENU________")
    print("a : ajouter un employe")
    print("b : modifier un employe")
    print("c : supprimer un employe")
    print("d : ajoutre une echelle a un employe")
    print("e : afficher un employe")
    print("f : afficher tous les employes ")
    print("g : exportre les données vers un fichier texte ")
    print("h : importer les données a partir d'un fichier texte ")
    print("i : augmenter un employe ")
    print("j : rechercher un employé (Par nom, par date embauche ou par fonction)")
    print("k : quitter")
    choix=input("entrez une lettre  ")
    match choix:
        case "a":
            n=int(input("entrez le nombre d'employes"))
            ajouter(n)
        case "b":
            matricule_rech=int(input("entrez le matricule  : "))
            modifier(matricule_rech)
        case "c":
            matricule_supp=int(input("entrez le matricule pour supprimer : "))
            supprime(matricule_supp)
        case "d":
            matr_note=int(input("saisir matricule pour ajouter l'echelle d'employe : "))
            ajouter_une_echelle_a_un_employe(matr_note)
        case "e":
            mat_rech=int(input("entrez matricule pour recherch : "))
            affiche_un_employe(mat_rech)
        case "f":
            affiche_tout_les_employes()
        case "g":
            namefile=input("name of file :")
            exporter(namefile)
        case "h":
            importt(namefile)
        case "i":
            mat_augmrtation=int(input("entrez matricule d'employe pour augmenter le salaire :"))
            how_much=int(input("Combien souhaitez-vous ajouter au salaire de votre employe ?(par %) : "))
            augmetation(mat_augmrtation,how_much)
        case "j":
            reche=input("Que voulez-vous utiliser pour rechercher (nom/data embauche/fonction) ? ")
            recherche(reche)
        case "k":
            print("quitte")
            break
        case _:
            print("entrez une lettre entre a et k")














            