"""
Programme testant si une date, saisie par l'utilisateur, est valide ou non.
Données : Une date saisie par l'utilisateur
Indications:
        Pour pouvoir déterminer si une année est bissextile :       
        	- Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
        	- Si elle est multiple de 4, on regarde si elle est multiple de 100.
            	- Si c'est le cas, on regarde si elle est multiple de 400.
      		- Si c'est le cas, l'année est bissextile.
                        		- Sinon, elle n'est pas bissextile.
- Sinon, elle est bissextile.

Résultats : Un message spécifiant si la date entrée est valide.

"""

### Déclaration et initialisation des variables
jour: int = 0
mois: int = 0
date: int = 0

### Séquence d'opération
print("saisissez une date :")
print("")

jour = int(input("Jour:"))
mois = int(input("Mois:"))
date = int(input("Année:"))

if mois < 1 or mois > 12 or jour < 1 or jour > 31:
    print("")
    print("L'année n'est pas valifde!")

elif mois == 4 or mois == 6 or mois == 9 or mois == 11 and jour > 30:
    print("Cette date n'est pas valide.")

elif jour > 29 and mois == 2:
    print("")
    print("L'année n'est pas valide!")

elif date % 4 == 0 and date % 100 != 0 or date % 400 == 0:
    print("")
    print("L'année est valide!")

else:
    print("")
    print("L'année est valifde!")
        
