from Personnage import Personnage
from arme import Arme

# Création de deux personnages
epee_legendaire = Arme("Épée Légendaire", 25)
joueur1 = Personnage("Arragon", "Guerrier", 10, 100, 15, 5, epee_legendaire)
joueur2 = Personnage("Elandra", "Mage", 10, 80, 5, 15)

joueur1.afficher_info()
joueur2.afficher_info()

joueur1.attaquer(joueur2)
joueur2.afficher_info()