import json
class Voiture(object):
    def __init__(self, marque, modele, transmission, couleur,
porte=4, accessoires = {}):
        self.marque = marque
        self.modele = modele
        self.transmission = transmission
        self.couleur = couleur
        self.porte = porte
        self.accessoires = accessoires


##instance

maVar = Voiture(marque="Nissan",
modele="Versa",
transmission="automatique",
couleur="orange",
porte=4,
accessoires={"toit_ouvrant": True}
)
print(maVar)
##utilisation de vars
print(vars(maVar))
## json
f =open('objvoiture.json','w')
json.dump(vars(maVar),f,indent=4)
f.close()


