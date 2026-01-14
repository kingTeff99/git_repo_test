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
            print(f"Nom: {self.nom}\n")
            print(f"Classe: {self.classe}\n")
            print(f"Niveau: {self.niveau}\n")
            print(f"Points de Vie: {self.points_de_vie}\n")
            print(f"Force: {self.force}\n")
            print(f"Intelligence: {self.intelligence}\n")

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom}!")
        degats = self.force * 2
        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.points_de_vie -= degats
        print(f"{self.nom} subit {degats} points de dégats!")
