"""
Programme calculant le niveau de risque cardiovasculaire. 
  Données : - L'Age de l'utilisateur
            - Le sexe de l'utilisateur
            - Si l'utilisateur est un fumeur ou non
            - Si l'utilisateur pratique du sport
            - Si l’utilisateur possède une alimentation trop sucrée
  Indications :
            - Si l'utilisateur est fumeur, le niveau de risque augmente de 2
            - Si l'utilisateur fait du sport, le niveau de risque diminue de 1
            - Si l'utilisateur est un homme de plus de 50 ans,
              le niveau de risque augmente de 1
            - Si l'utilisateur est une femme de plus de 60ans,
              le niveau de risque augmente de 1
            - Si l’utilisateur consomme trop de sucre, le niveau de risque augmente de 2
            
  Résultats : Un message spécifiant le niveau de risque obtenu.
            - Si le niveau de risque est inférieur ou égal à 1, le niveau de risque est faible.
            - Si le niveau de risque est de 2 à 3, le niveau de risque est élevé
            - Sinon il est très élevé.

"""
### Déclaration et initialisation des variables
age: int = 0
sexe: str = 0
fumeur: str = 0
sport: str = 0
alim: str = 0

risque: int = 0

### Séquence d'opération
age = int(input("Quelle âge avez-vous ?"))
sexe = input("Quel est votre sexe ?")
fumeur = input("Êtes-vous fumeur ?")
sport = input("Pratiquez-vous du sport ?")
alim = input("Avez-vous une alimentation trop sucrée ?")


if fumeur == "oui":
    risque += 2
if sport == "oui":
    risque -= 1
if sexe == "homme" and age > 50:
    risque += 1
elif sexe == "femme" and age > 60:
    risque += 1
if alim == "oui":
    risque += 2
    print(" ")
    print("Niveau de risque obtenu: " + str(risque))
if risque <= 1:
    print("Niveau de risque: Faible!")
if risque == 2 or risque == 3:
    print("Niveau de risque: Elevé!")
else:
    print("Niveau de risque: Très élevé!")
