"""
Programme permettant de convertir une quantité en plusieurs unités d'énergie.

1J  =  0.738 ft-lb  =  0.239 cal  =  6.24*10^18 eV

Unités : joule, calorie, Ft-lb et eV
  Données : Une valeur et une unité
  Indications:
        Selon l'unité entrée par l'utilisateur, afficher la conversion
        dans les 3 autres unités.
  Résultats : Affichage des conversions
"""

### Déclaration et initialisation des variable
j: str = 0
ft: str = 0
cal: str = 0
ev: str = 0

qj: float = 0
qft: float = 0
qcal: float = 0
qev: float = 0

j = str("j")
ft = str("ft-lb")
cal = str("cal")
ev = str("ev")

qj = float(1)
qft = float(0.738)
qcal = float(0.239)
qev = float(6.24*10**18)

### Séquence d'opération
unite: str = input("Quelle unité ?")
quantite: float = float(input("Quelle quantite ?"))
print("")

if unite == j:
    print(str((quantite / qj) * qft) + " ft-lb")
    print(str((quantite / qj) * qcal) + " cal")
    print(str((quantite / qj) * qev) + " eV")

elif unite == ft:
    print(str((quantite / qft) * qj) + " J")
    print(str((quantite / qft) * qcal) + " cal")
    print(str((quantite / qft) * qev) + " eV")

elif unite == cal:
    print(str((quantite / qcal) * qj) + " J")
    print(str((quantite / qcal) * qft) + " ft-lb")
    print(str((quantite / qcal) * qev) + " eV")

elif unite == ev:
    print(str((quantite / qev) * qj) + " J")
    print(str((quantite / qev) * qcal) + " cal")
    print(str((quantite / qev) * qft) + " ft-lb")

else:
    print("Unité invalide!!")

