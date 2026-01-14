class Personnage:
    def __init__(self, nom, classe, niveau, points_de_vie, force, intelligence):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.points_de_vie = points_de_vie
        self.force = force
        self.intelligence = intelligence
    
    def afficher_info(self):
        info = (
            f"Nom: {self.nom}\n"
            f"Classe: {self.classe}\n"
            f"Niveau: {self.niveau}\n"
            f"Points de Vie: {self.points_de_vie}\n"
            f"Force: {self.force}\n"
            f"Intelligence: {self.intelligence}\n"
        )
        return info

    def attaquer(self, cible):
        print(f"{self.nom} attaque {cible.nom}!")
        degats = self.force * 2
        cible.subir_degats(degats)

    def subir_degats(self, degats):
        self.points_de_vie -= degats
        print(f"{self.nom} subit {degats} points de dégats!")
