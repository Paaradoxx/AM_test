from random import randint

liste_des_besoins = []
liste_des_cartes = [["givrali", 21.9],
                    ["pyroli", 23.5],
                    ["mentali", 25],
                    ["evoli", 23],
                    ["voltali", 23],
                    ["noctali", 69],
                    ["phyllali", 23],
                    ["aquali", 24],
                    ["nymphali", 25]]

prix = 0
for i in liste_des_cartes:
    prix += i[1]
    
nbr_essai = 10000

for nbr_booster in range(0, 20):
    moyenne = 0
    cartes_en_rab_en_moyenne = 0
    for i in range(nbr_essai):
        pioche = []
        for j in range(nbr_booster):
            pioche.append(randint(0, 8))
        
        collection = []
        for carte in pioche:
            if not carte in collection:
                collection.append(carte)
            
        cartes_manquantes = []
        for carte in range(9):
            if not carte in collection:
                cartes_manquantes.append(carte)
        
        prix = 0
        for carte in cartes_manquantes:
            prix += liste_des_cartes[carte][1]
            
        prix += 18*nbr_booster
        cartes_en_rab_en_moyenne += nbr_booster-len(collection)
        moyenne += prix        
            
            

    print("Il faut payer en moyenne ", moyenne/nbr_essai, " euro pour avoir le full set avec ", nbr_booster, " booster achete et il y aura ", cartes_en_rab_en_moyenne/nbr_essai, " cartes en rab")
    print(" ")






"""
for i in range(1000):
    collection = [randint(1, 9)]
    compteur = 1
    while len(collection) != 9:
        carte = randint(1, 9)
        if not carte in collection:
            collection.append(carte)
        compteur += 1  
    moyenne += compteur 
    liste_des_besoins.append(compteur)
    print(i+1, " /100")

liste_des_besoins.sort()
print("En moyenne il faut: ", moyenne/1000, " booster.")
print("En meddian il faut: ", liste_des_besoins[len(liste_des_besoins)//2], "booster")"""

    