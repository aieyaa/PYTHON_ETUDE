from app.data import * 
from app.stock import stock_info


def demande():
    while True:
        try:
            paires = int(input(f"Combien de paires de chaussettes souhaitez-vous acheter ? "))

            if paires <= 0:
                print(f"Le nombre de paires doit être positif.")
                continue

            if paires > quantite_stock:
                print(f"Désolé, nous n'avons que {quantite_stock} paires en stock.")
                continue

            return paires

        except ValueError:
            print("Entre un nombre valide.")

def achat():
    global compte_client, compte_boutique, quantite_stock

    nb_paires = demande()
## Calculs
    montant_ht = nb_paires * prix_unitaire
    montant_ttc = montant_ht * (1 + tva)

    if montant_ttc > compte_client:
        print("C'est la hess, ta pas les tunes ")
        return

    # Mise à jour des variables
    quantite_stock -= nb_paires
    compte_client -= montant_ttc
    compte_boutique += montant_ttc

    # IX. 
    montant_ttc_str = f"{montant_ttc:.2f} €"

    # VI. 
    # Récapitulatif 
    print("\nAchat effectué avec succès !")
    print(f"Montant HT : {montant_ht:.2f} €")
    print(f"Montant TTC : {montant_ttc:.2f} €")
    print(f"Stock restant : {quantite_stock} paires")
    print(f"Nouveau solde client : {compte_client:.2f} €")
    print(f"Nouveau solde boutique : {compte_boutique:.2f} €")

    return nb_paires, montant_ht, montant_ttc * tva, montant_ttc
    ## casse les pieds ce return mdr !? 

    # Vérifier le stock critique
    stock_info()