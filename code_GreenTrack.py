#unite=kg/km
voiture=0.195 
bus=0.105
train=0.041
avion=0.255
moto =0.103
velo=0.0
marche_a_pied=0.0
#unite=kg/repas
viande=7.0
poulet=2.0
poisson=3.0
vegetarien=1.5
vegan=1.0
print("bienvenue au test GreenTrack")
print("Info sur GreenTrack \n GreenTrack calcule votre empreinte de carbone quotidienne \n Et dans ce test choissisez les reponses devant les choix")
nom=input("Veuillez entrer votre nom")
date=input("Entrez la date auquelle vous faites ce test")
nbre_de_kilometres=input("Saisissez le nombre de kilometre que vous faites par jour")
nbre_de_kilometres=int(nbre_de_kilometres)
moyen_de_transport=input("Choississez par mi les moyens de transport \n 1- voiture \n -2 bus \n -3 train \n -4 avion \n -5 moto \n -6 velo \n -7 marche a pied \n choississez ")
arbre=input("Avez vous planter un arbre(oui/non)")
if arbre.lower() == "oui":
    nbre_arbre=input("combien d'arbre")
    nbre_arbre=int(nbre_arbre)
    quantite_produite_par_arbre=nbre_arbre*20
    print(f"vous avez compense {quantite_produite_par_arbre} kg")
elif arbre.lower() == "non":
    print("Vous n'avez pas planter d'arbre cett fois mais en planter pourrait compenser jusqu'a 20 kg")
    quantite_produite_par_arbre=0
else:
    print("incorrect")
if moyen_de_transport == '1' or "voiture":
    quantite_de_carbone_km=nbre_de_kilometres*voiture
    print(f"Vous consommez {quantite_de_carbone_km} kg/km de CO2")
    aliments=input("Votre nourriture parmi \n -1 viande rouge \n -2 poulet \n -3 poisson \n -4 vegetarien   \n -5 vegan \n choississez")
    nbre_de_fois=input("combien de fois manger vous cet aliments par jour")
    nbre_de_fois=int(nbre_de_fois)
    if aliments=='1':
        quantite_de_carbone_repas=nbre_de_fois*viande
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='2' :
        quantite_de_carbone_repas=nbre_de_fois*poulet
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='3':
        quantite_de_carbone_repas=nbre_de_fois*poisson
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='4':
        quantite_de_carbone_repas=nbre_de_fois*vegetarien
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='5':
        quantite_de_carbone_repas=nbre_de_fois*vegan
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    else:
        print("Incorrect")
    nbre_totale=quantite_de_carbone_repas+quantite_de_carbone_km
    seuil_journalier=5.5
    if nbre_totale <= seuil_journalier:
        statut="Positif"
    elif nbre_totale >= seuil_journalier:
        statut="Negatif par rapport au seuil journalier de 5.5 kg"
    
    print(f" Votre bilan est la suivante \n nom:{nom} \n date du GreenTrack:{date} \n Nombre de carbone de deplacement(kg) :{quantite_de_carbone_km} \n Nombre de carbone par rapport a la nourriture(kg):{quantite_de_carbone_repas}\n Nombre de carbone compensé:{quantite_produite_par_arbre} \n Nombre d'emission de carbone totale :{nbre_totale} \n Statut du bilan :{statut} ")
    with open("base.csv" , "a") as f :
        f.write(f"{nom},{date},{quantite_de_carbone_km},{quantite_de_carbone_repas},{quantite_produite_par_arbre},{nbre_totale},{statut} \n ")
elif moyen_de_transport == '2' or "bus":
    quantite_de_carbone_km=nbre_de_kilometres*bus
    print(f"Vous consommez {quantite_de_carbone_km} kg/km de CO2")
    aliments=input("Votre nourriture parmi \n -1 viande rouge \n -2 poulet \n -3 poisson \n -4 vegetarien   \n -5 vegan \n choississez")
    nbre_de_fois=input("combien de fois manger vous cet aliments par jour")
    nbre_de_fois=int(nbre_de_fois)
    if aliments=='1':
        quantite_de_carbone_repas=nbre_de_fois*viande
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='2':
        quantite_de_carbone_repas=nbre_de_fois*poulet
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='3':
        quantite_de_carbone_repas=nbre_de_fois*poisson
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='4' :
        quantite_de_carbone_repas=nbre_de_fois*vegetarien
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='5':
        quantite_de_carbone_repas=nbre_de_fois*vegan
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    else:
        print("Incorrect")
    nbre_totale=quantite_de_carbone_repas+quantite_de_carbone_km
    seuil_journalier=5.5
    if nbre_totale <= seuil_journalier:
        statut="Positif"
    elif nbre_totale >= seuil_journalier:
        statut="Negatif par rapport au seuil journalier de 5.5 kg"
    
    print(f" Votre bilan est la suivante \n nom:{nom} \n date du GreenTrack:{date} \n Nombre de carbone de deplacement(kg) :{quantite_de_carbone_km} \n Nombre de carbone par rapport a la nourriture(kg):{quantite_de_carbone_repas}\n Nombre de carbone compensé:{quantite_produite_par_arbre} \n Nombre d'emission de carbone totale :{nbre_totale} \n Statut du bilan :{statut} ")
    with open("base.csv" , "a") as f :
        f.write(f"{nom},{date},{quantite_de_carbone_km},{quantite_de_carbone_repas},{quantite_produite_par_arbre},{nbre_totale},{statut} \n ")
   
elif moyen_de_transport == '3' or "train":
    quantite_de_carbone_km=nbre_de_kilometres*train
    print(f"Vous consommez {quantite_de_carbone_km} kg/km de CO2")
    aliments=input("Votre nourriture parmi \n -1 viande rouge \n -2 poulet \n -3 poisson \n -4 vegetarien   \n -5 vegan \n choississez")
    nbre_de_fois=input("combien de fois manger vous cet aliments par jour")
    nbre_de_fois=int(nbre_de_fois)
    if aliments=='1' :
        quantite_de_carbone_repas=nbre_de_fois*viande
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='2':
        quantite_de_carbone_repas=nbre_de_fois*poulet
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='3':
        quantite_de_carbone_repas=nbre_de_fois*poisson
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='4':
        quantite_de_carbone_repas=nbre_de_fois*vegetarien
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='5':
        quantite_de_carbone_repas=nbre_de_fois*vegan
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    else:
        print("Incorrect")
    nbre_totale=quantite_de_carbone_repas+quantite_de_carbone_km
    seuil_journalier=5.5
    if nbre_totale <= seuil_journalier:
        statut="Positif"
    elif nbre_totale >= seuil_journalier:
        statut="Negatif par rapport au seuil journalier de 5.5 kg"
    
    print(f" Votre bilan est la suivante \n nom:{nom} \n date du GreenTrack:{date} \n Nombre de carbone de deplacement(kg) :{quantite_de_carbone_km} \n Nombre de carbone par rapport a la nourriture(kg):{quantite_de_carbone_repas}\n Nombre de carbone compensé:{quantite_produite_par_arbre} \n Nombre d'emission de carbone totale :{nbre_totale} \n Statut du bilan :{statut} ")
    with open("base.csv" , "a") as f :
        f.write(f"{nom},{date},{quantite_de_carbone_km},{quantite_de_carbone_repas},{quantite_produite_par_arbre},{nbre_totale},{statut} \n ")
   
elif moyen_de_transport == '4' or "avion":
    quantite_de_carbone_km=nbre_de_kilometres*avion
    print(f"Vous consommez {quantite_de_carbone_km} kg/km de CO2")
    aliments=input("Votre nourriture parmi \n -1 viande rouge \n -2 poulet \n -3 poisson \n -4 vegetarien   \n -5 vegan \n choississez")
    nbre_de_fois=input("combien de fois manger vous cet aliments par jour")
    nbre_de_fois=int(nbre_de_fois)
    if aliments=='1':
        quantite_de_carbone_repas=nbre_de_fois*viande
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='2':
        quantite_de_carbone_repas=nbre_de_fois*poulet
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='3':
        quantite_de_carbone_repas=nbre_de_fois*poisson
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='4':
        quantite_de_carbone_repas=nbre_de_fois*vegetarien
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='5':
        quantite_de_carbone_repas=nbre_de_fois*vegan
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    else:
        print("Incorrect")
    nbre_totale=quantite_de_carbone_repas+quantite_de_carbone_km
    seuil_journalier=5.5
    if nbre_totale <= seuil_journalier:
        statut="Positif"
    elif nbre_totale >= seuil_journalier:
        statut="Negatif par rapport au seuil journalier de 5.5 kg"
    
    print(f" Votre bilan est la suivante \n nom:{nom} \n date du GreenTrack:{date} \n Nombre de carbone de deplacement(kg) :{quantite_de_carbone_km} \n Nombre de carbone par rapport a la nourriture(kg):{quantite_de_carbone_repas}\n Nombre de carbone compensé:{quantite_produite_par_arbre} \n Nombre d'emission de carbone totale :{nbre_totale} \n Statut du bilan :{statut} ")
    with open("base.csv" , "a") as f :
        f.write(f"{nom},{date},{quantite_de_carbone_km},{quantite_de_carbone_repas},{quantite_produite_par_arbre},{nbre_totale},{statut} \n ")

   
elif moyen_de_transport == '5' or "moto":
    quantite_de_carbone_km=nbre_de_kilometres*moto
    print(f"Vous consommez {quantite_de_carbone_km} kg/km de CO2")
    aliments=input("Votre nourriture parmi \n -1 viande rouge \n -2 poulet \n -3 poisson \n -4 vegetarien   \n -5 vegan \n choississez")
    nbre_de_fois=input("combien de fois manger vous cet aliments par jour")
    nbre_de_fois=int(nbre_de_fois)
    if aliments=='1':
        quantite_de_carbone_repas=nbre_de_fois*viande
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='2':
        quantite_de_carbone_repas=nbre_de_fois*poulet
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='3' :
        quantite_de_carbone_repas=nbre_de_fois*poisson
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='4':
        quantite_de_carbone_repas=nbre_de_fois*vegetarien
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='5' :
        quantite_de_carbone_repas=nbre_de_fois*vegan
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    else:
        print("Incorrect")
    nbre_totale=quantite_de_carbone_repas+quantite_de_carbone_km
    seuil_journalier=5.5
    if nbre_totale <= seuil_journalier:
        statut="Positif"
    elif nbre_totale >= seuil_journalier:
        statut="Negatif par rapport au seuil journalier de 5.5 kg"
    
    print(f" Votre bilan est la suivante \n nom:{nom} \n date du GreenTrack:{date} \n Nombre de carbone de deplacement(kg) :{quantite_de_carbone_km} \n Nombre de carbone par rapport a la nourriture(kg):{quantite_de_carbone_repas}\n Nombre de carbone compensé:{quantite_produite_par_arbre} \n Nombre d'emission de carbone totale :{nbre_totale} \n Statut du bilan :{statut} ")
    with open("base.csv" , "a") as f :
        f.write(f"{nom},{date},{quantite_de_carbone_km},{quantite_de_carbone_repas},{quantite_produite_par_arbre},{nbre_totale},{statut} \n ")
   
elif moyen_de_transport == '6' or "velo":
    quantite_de_carbone_km=nbre_de_kilometres*velo
    print(f"Vous consommez {quantite_de_carbone_km} kg/km de CO2")
    aliments=input("Votre nourriture parmi \n -1 viande rouge \n -2 poulet \n -3 poisson \n -4 vegetarien   \n -5 vegan \n choississez")
    nbre_de_fois=input("combien de fois manger vous cet aliments par jour")
    nbre_de_fois=int(nbre_de_fois)
    if aliments=='1':
        quantite_de_carbone_repas=nbre_de_fois*viande
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='2':
        quantite_de_carbone_repas=nbre_de_fois*poulet
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='3':
        quantite_de_carbone_repas=nbre_de_fois*poisson
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='4':
        quantite_de_carbone_repas=nbre_de_fois*vegetarien
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='5':
        quantite_de_carbone_repas=nbre_de_fois*vegan
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    else:
        print("Incorrect")
    nbre_totale=quantite_de_carbone_repas+quantite_de_carbone_km
    seuil_journalier=5.5
    if nbre_totale <= seuil_journalier:
        statut="Positif"
    elif nbre_totale >= seuil_journalier:
        statut="Negatif par rapport au seuil journalier de 5.5 kg"
    
    print(f" Votre bilan est la suivante \n nom:{nom} \n date du GreenTrack:{date} \n Nombre de carbone de deplacement(kg) :{quantite_de_carbone_km} \n Nombre de carbone par rapport a la nourriture(kg):{quantite_de_carbone_repas}\n Nombre de carbone compensé:{quantite_produite_par_arbre} \n Nombre d'emission de carbone totale :{nbre_totale} \n Statut du bilan :{statut} ")
    with open("base.csv" , "a") as f :
        f.write(f"{nom},{date},{quantite_de_carbone_km},{quantite_de_carbone_repas},{quantite_produite_par_arbre},{nbre_totale},{statut} \n ")
   
elif moyen_de_transport == '7' or "marche_a_pied":
    quantite_de_carbone_km=nbre_de_kilometres*marche_a_pied
    print(f"Vous consommez {quantite_de_carbone_km} kg/km de CO2")
    aliments=input("Votre nourriture parmi \n -1 viande rouge \n -2 poulet \n -3 poisson \n -4 vegetarien   \n -5 vegan \n choississez")
    nbre_de_fois=input("combien de fois manger vous cet aliments par jour")
    nbre_de_fois=int(nbre_de_fois)
    if aliments=='1':
        quantite_de_carbone_repas=nbre_de_fois*viande
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='2' :
        quantite_de_carbone_repas=nbre_de_fois*poulet
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='3' :
        quantite_de_carbone_repas=nbre_de_fois*poisson
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='4' :
        quantite_de_carbone_repas=nbre_de_fois*vegetarien
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    elif aliments=='5':
        quantite_de_carbone_repas=nbre_de_fois*vegan
        print(f"Vous consommez {quantite_de_carbone_repas} kg/repas de CO2")
    else:
        print("Incorrect")

    nbre_totale=quantite_de_carbone_repas+quantite_de_carbone_km-quantite_produite_par_arbre
    seuil_journalier=5.5
    if nbre_totale <= seuil_journalier:
        statut="Positif"
    elif nbre_totale >= seuil_journalier:
        statut="Negatif par rapport au seuil journalier de 5.5 kg"
    
    print(f" Votre bilan est la suivante \n nom:{nom} \n date du GreenTrack:{date} \n Nombre de carbone de deplacement(kg) :{quantite_de_carbone_km} \n Nombre de carbone par rapport a la nourriture(kg):{quantite_de_carbone_repas} \n Nombre de carbone compensé:{quantite_produite_par_arbre} \n Nombre d'emission de carbone totale :{nbre_totale} \n Statut du bilan :{statut} ")
   

   
