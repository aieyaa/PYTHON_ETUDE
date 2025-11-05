from app.data import quantite_stock, prix_unitaire

## VII.
def stock_info():
    if quantite_stock < 10:
        print("Stock bientôt épuisé !")

    ## VIII. 
    elif 10 < quantite_stock < 15 and prix_unitaire > 5:
        print("Attention produit presque en rupture !")