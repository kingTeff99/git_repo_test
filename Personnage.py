from tabulate import tabulate

class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie, force, intelligence, arme= None):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence
        self.arme = arme
        self.en_vie = True
    
    def afficher_info(self):
            etat = "En vie" if self.en_vie else "Mort"

            print(tabulate([[self.nom, self.classe, self.niveau, self.points_de_vie, self.force, self.intelligence, self.arme.nom if self.arme else "Aucune arme équipée", self.en_vie]],
                     headers=["Nom", "Classe", "Niveau", "Points de Vie", "Force", "Intelligence", "Arme", "Etat"],
                     tablefmt="grid"))

    def attaquer(self, cible):
        if self.arme:
            print(f"{self.nom} attaque {cible.nom} avec {self.arme.nom}!")
            degats = self.force * 2 + self.arme.degats
        else:
            print(f"{self.nom} attaque {cible.nom} à mains nues!")
            degats = self.force * 2
        
        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.points_de_vie -= degats
        print(f"{self.nom} subit {degats} points de dégats!")

        if self.points_de_vie <= 0:
             self.en_vie = False
             print(f"{self.nom} est mort!")