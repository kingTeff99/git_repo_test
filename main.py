from Personnage import Personnage

# Création de deux personnages
joueur1 = Personnage("Arragon", "Guerrier", 10, 100, 15, 5)
joueur2 = Personnage("Elandra", "Mage", 10, 80, 5, 15)

joueur1.afficher_info()
joueur2.afficher_info()

joueur1.attaquer(joueur2)
joueur2.afficher_info()