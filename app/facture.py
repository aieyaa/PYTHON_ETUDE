## Affichage Final dans le terminal pour la facture
#from app.data import nom_boutique, produit

#def affichage(nb_paires, montant_ht, tva_montant, montant_ttc):
#    montant_ht_str = f"{montant_ht:.2f} €"
#   tva_str = f"{tva_montant:.2f} €"
#    montant_ttc_str = f"{montant_ttc:.2f} €"

#   print("\n" + "-"*84)
#    print(f"{nom_boutique:^84}")
#   print("-"*84)
#    print(f"Produit{'':<35}Qté{'':<2}HT")
#    print(f"{produit:<40}{nb_paires:<4}{montant_ht_str:>10}")
#    print(f"{'Total HT :':>68} {montant_ht_str}")
#    print(f"{'TVA :':>68} {tva_str}")
#    print(f"{'Total TTC :':>68} {montant_ttc_str}")
#    print("-"*84)


from app.data import nom_boutique, produit

def affichage(nb_paires, montant_ht, tva_montant, montant_ttc):

    print("-" * 80)
    print(f"{nom_boutique:^84}")
    print("-" * 80)
    print(f"{'Produit':<20}{'qté':>10}{'HT':>20}")
    print(f"{produit:<20}{nb_paires:>10}{montant_ht:>20.2f}")
    print(f"{'':<50}{'-'*30}")
    print(f"{'Total HT :':>60} {montant_ht:>10.2f}")
    print(f"{'TVA :':>60} {tva_montant:>10.2f}")
    print(f"{'Total TTC :':>60} {montant_ttc:>10.2f}")
    print("-" * 80)
