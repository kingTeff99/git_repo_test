from tabulate import tabulate

class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie, force, intelligence):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence
    
    def afficher_info(self):
            print(tabulate([[self.nom, self.classe, self.niveau, self.points_de_vie, self.force, self.intelligence]],
                     headers=["Nom", "Classe", "Niveau", "Points de Vie", "Force", "Intelligence"],
                     tablefmt="grid"))

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom}!")
        degats = self.force * 2
        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.points_de_vie -= degats
        print(f"{self.nom} subit {degats} points de dégats!")
