"""
Programme de calcul du prix d'un billet de transport journalier selon plusieurs rabais possibles.
    Prix normal d'un billet : 10chf
    Rabais étudiant : 2chf
    Rabais demi-tarif : 5chf
    Rabais groupe : 2 chf par billet acheté à partir de 4.
    Carte mensuelle : Billet gratuit

Indications :
    - Il est possible de bénéficier d'un rabais demi-tarif et étudiant
    - Le rabais groupe n’est cumulable avec aucun autre rabais
    - Il est possible d'avoir une carte mensuelle permettant d’avoir ce billet gratuitement

Contrainte : 
- Si la personne possède la carte mensuelle, il ne faut pas lui demander
d'autres informations.

"""
### Déclaration et initialisation des variables
prix: int = 0
retu: int = 0
rdt: int = 0
rgroupe: int = 0

prix = 10
retu = 2
rdt = 5
rgroupe = 2





### Séquence d'opération
cm: str = str(input("Avez-vous la carte mensuel ?"))

if cm == "oui":
    print("")
    print("Votre billet de transport coute: 0chf")
elif cm == "non":
    rabaisetu: str = str(input("Êtes-vous étudiant ?"))

    rabaisdemi: str = str(input("Avez-vous une carte demi-tarif ?"))
    if rabaisetu == "oui" and rabaisdemi == "non":
        print("")
        print("Votre billet de transport coute: " + str(prix - retu) + "chf")

    if rabaisdemi == "oui" and rabaisetu == "non":
        print("")
        print("Votre billet de transport coute: " + str(prix - rdt) + "chf")

    if rabaisetu == "oui" and rabaisdemi == "oui":
        print("")
        print("Votre billet de transport coute: " + str(prix - retu - rdt)+ "chf")

    if rabaisetu == "non" and rabaisdemi == "non":
        print("")
        nbbillet: int = int(input("Nombre de billets ?"))

        if nbbillet > 3:
            print("")
            print("Votre billet de transport coute: " + str((prix - rgroupe) * nbbillet) + "chf")

        else:
            print("")
            print("Votre billet de transport coute: " + str(prix * nbbillet) + "chf")

