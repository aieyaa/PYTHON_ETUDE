from app.data import nom_boutique
from app.data import produit, prix_unitaire, quantite_stock, tva, compte_client, compte_boutique
from app.achat import achat
from app.stock import stock_info
from app.facture import affichage



def main(): 

    result = achat()
    if result:
        nb_paires, montant_ht, tva_montant, montant_ttc = result
        affichage(nb_paires, montant_ht, tva_montant, montant_ttc)

        stock_info()

        # Afficher le type des variables à la fin
        print("\nTypes des variables :")
        variables = {
            "nb_paires": nb_paires,
            "montant_ht": montant_ht,
            "tva_montant": tva_montant,
            "montant_ttc": montant_ttc,
        }
        for nom, valeur in variables.items():
            print(f"{nom} : {type(valeur)}")

if __name__ == "__main__":
    main()
