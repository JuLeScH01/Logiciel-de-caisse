import ast

liste_argent = [10000,5000,5000,2000,2000,2000,2000,2000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000
                ,500,500,500,500,500,200,200,200,200,200,200,200,200,200,100,100,100,100,100,100,100,100,100
                ,50,50,50,50,50,50,50,50,50,50,20,20,20,20,20,20,20,20,5,5,5,5,5,5,5,5,5,5,2,2,2,2,2,2,2,2,2,
                2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1]


#glouton
client_donne = int(input('ce que le client donne/')) # a mettre avec bouton
liste_rendu = []
prix_a_payer = 1500 #le prix des articles selectionner par le client 
def algo_glouton(liste_argent,prix_a_payer,client_donne,liste_rendu):
    somme = 0
    val_a_rendre = client_donne - prix_a_payer

    for x in range(len(liste_argent)):
        if val_a_rendre != 0:
            if client_donne < prix_a_payer:
                    print('ce n est pas assez')
                    break
            if liste_argent[x] <= val_a_rendre:
                liste_rendu.append(liste_argent[x])
                val_a_rendre = val_a_rendre - liste_argent[x]
                
        else:
            return liste_rendu

print(algo_glouton(liste_argent,prix_a_payer,client_donne,liste_rendu))



try:
    with open("sauvegarder.txt","r") as f:
        texte = f.read()
        #ouvre la sauvegarde si elle existe
    if not texte or texte.strip() == "":
        raise ValueError("sauvegarde vide") #si la sauvegarde est vide ou que ya que dees espaces 
    #ça dit que ya pas et ça en crée une en bas 
    
    liste_argent = ast.literal_eval(texte) #passe la liste argent (string) en vrai liste

except Exception:
    print('aucune fichier ou nouvelle sauvegarde cree')

if len(liste_rendu) != 0:
    for valeur in liste_rendu:
        if valeur in liste_argent:
            liste_argent.remove(valeur)
        else: 
            print('pas assez de monnaie')
if client_donne != prix_a_payer:
    liste_argent.append(int(client_donne))
    liste_argent.sort(reverse=True)  # Tri décroissant pour le glouton ppour placer les rendues entre les bonnes valeur

with open("sauvegarder.txt", "w") as f:
    f.write(str(liste_argent))
print("donnees actualiser") #pour verifier si le code marche bien

print('Liste d\'argent restante:', liste_argent) #console pour verifier 



# + gerer le stack de billet 2X50 et tout ( pas fait )

#normalement tout marche avec la sauvergarde et tout faut juste que tu t arranges pour faire des 
# boutons pour convertir les 500 en billet de 5 etc et tu peux sup les messages consoles stv 
# c etait juste pour voir ce qui marche ou pas et que tu connectes avec les boutons la partie 
# client_donne et prix_a_payer (pour le rendu t as les valeurs que tu dois rendre et ça se fait auto 
# pour faire le rendu a la main affiche juste le rendu et le supprime pas dans la sauvegarde direct 
# l.46 a 49 comme ça tu rends a la main et t ajoute que ce que tu rends a la main c est ce qui est supp )
# / j ai par contre pas eu le temps de gerer le stack de billet jsp si ça vous sert ou pas 
# pour l affichage sur le site
#hesite pas a rajouter des billets parce que ya un message si on peut pas rendre mais c est plus sur de faire ça