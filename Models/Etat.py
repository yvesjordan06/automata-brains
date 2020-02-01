"""
Attribue:
valeur: string

Methode
modifier_valeur
hash
@operateur <comparaison>

Contrainte
• Une valeur est de type <<String<> ,
• #Une valeur peut etre de toute longeur
• #les fonctions doivent accepter uniquement les type <<String<> en parametre sinon on rejete
une erreur <<raise<>
• #Les etat qui ont le meme attribue sont considerer identique (donc ils on un hash similaire)
• #Surcharger l’operateur de comparaison “ <=” pour comparer 2 etat => retourne True si ils sont
identique sinon F alse
• les attributs et fonctions non accessiblent doivent etre proteges .__ pour les attibuts et __ pour les fonctions
"""
class Etat:
    "la class etat"

    def __init__(self,valeur,nom=None):
        self.__valeur=self.__verifier_type(valeur)
        self.nom = nom



    def __verifier_type(self, valeur):
        "cette fonction verifie si le type de l'etat est bien un 'str'"
        if isinstance(valeur, str) and  valeur.strip():
            return valeur
        else:
            raise TypeError("la valeur doit etre de type str")

    def definir_nom(self, nom):
        if not isinstance(nom, str):
            raise TypeError('Type invalide, <str> attendu')
        self.nom = nom

    def modifier_valeur(self, nouvelle_valeur):
        "cette fonction permet de modifier une valeur par une autre"
        self.__valeur = self.__verifier_type(nouvelle_valeur)

    # def surchage_hash():
    # "modifier la maniere avec laquelle le python comprend le hash"
    def __eq__(self, p):
        "modifier la manier avec laquelle le python comprend les operateurs '='"
        etat_self = self.__valeur
        try:
            etat1 = p.__valeur
        except:
            return False
        return etat_self == etat1

    def __repr__(self):
        return str(self.__valeur)

    def __hash__(self):
        return hash(self.__valeur)









