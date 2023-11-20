nom = "PC"
prix = 1000
quantité = 10
print(f"nom: {nom} \n Prix : {prix} \n quantité {quantité}")
quantité_ajoutee = int(input("Entrez la quantité du produits à ajouter en stock  : "))
quantité += quantité_ajoutee
print(quantité)
prix *= 1.1
print("\nInformations mises à jour du produit après ajout en stock et augmentation de prix ")
print(f"Nom du produit : {nom}")
print(f"Prix unitaire : {prix:.2f} euros") 
print(f"Quantité: {quantité}")