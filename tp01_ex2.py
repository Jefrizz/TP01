"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Fanta orange à 2.90
           - Coca cola à 2.90
           - Coca cola light à 2.70
           - Henniez à 2.30
           - Ice Tea à 2.20
           - Limonade à 1.90
           
 Résultats : - Un message d’annulation de la transaction
                 (« Produit inconnu / Monnaie insuffisante »)
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant "santé"

"""

### Déclaration et initialisation des variables
fanta: float = 0
coca: float = 0
cocalight: float = 0
henniez: float = 0
icetea: float = 0
limonade: float = 0

fanta = 2.90
coca = 2.90
cocalight = 2.70
henniez = 2.30
icetea = 2.20
limonade = 1.90



### Séquence d'opération
print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Fanta Orange:     2.90")
print("2. Coca cola:        2.90")
print("3. Coca cola light:  2.70")
print("4. Henniez:          2.30")
print("5. Ice tea:          2.20")
print("6. Limonade:         1.90")
print(" ")
montant: float = float(input("Quelle montant ?"))
numarticle: int = int(input("Quel numéro d'article ?"))
print(" ")

if numarticle == 1:
    if montant < fanta:
        print("Monnaie insuffisante")
        print("Annulation de la transaction")

    elif montant >= fanta:
        print("Fanta: Santé!!")
        if montant > fanta:
            print("Monnaie rendu = " + str(format(montant - fanta, '.2f')))
elif numarticle == 2:
    if montant < coca:
        print("Monnaie insuffisante")
        print("Annulation de la transaction")

    elif montant >= coca:
        print("CocaCola: Santé!!")
        if montant > coca:
            print("Monnaie rendu = " + str(format(montant - coca, '.2f')))

elif numarticle == 3:
    if montant < cocalight:
        print("Monnaie insuffisante")
        print("Annulation de la transaction")

    elif montant >= cocalight:
        print("CocaCola Light: Santé!!")
        if montant > cocalight:
            print("Monnaie rendu = " + str(format(montant - cocalight, '.2f')))

elif numarticle == 4:
    if montant < henniez:
        print("Monnaie insuffisante")
        print("Annulation de la transaction")
    elif montant >= henniez:
        print("Henniez: Santé!!")
        if montant > henniez:
            print("Monnaie rendu = " + str(format(montant - henniez, '.2f')))

elif numarticle == 5:
    if montant < icetea:
        print("Monnaie insuffisante")
        print("Annulation de la transaction")
    elif montant >= icetea:
        print("IceTea: Santé!!")
        if montant > icetea:
            print("Monnaie rendu = " + str(format(montant - icetea, '.2f')))

elif numarticle == 6:
    if montant < limonade:
        print("Monnaie insuffisante")
        print("Annulation de la transaction")
    elif montant >= limonade:
        print("Limonda: Santé!!")
        if montant > limonade:
            print("Monnaie rendu = " + str(format(montant - limonade, '.2f')))

else:
    print("Produit inconnu !")

