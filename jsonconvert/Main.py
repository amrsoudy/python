#lire
import json
f =open('voiture.json')
voiture = json.load(f)
print(voiture)
f.close()

voiture['voiturette']['couleur'] = 'noire'

#suvgarder
f = open('voiture.json','w')
json.dump(voiture,f)
f.close()