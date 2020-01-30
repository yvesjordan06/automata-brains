from Models.Etat import Etat
#####################################################################class Transistion ##########################################################################################
class Transition :
    def __init__(self,depart,symbole,arrive):
        self.depart= self.__verifie_etat(depart)
        self.symbole=self.__verifie_symbole(symbole)
        self.arrive= self.__verifie_etat(arrive)

    def __repr__(self):
        return '(' + str(self.depart) + ',' + str(self.symbole) + ',' + str(self.arrive) + ')'

    def __verifie_etat(self,etat):
        #verifie si les etats entrée font partir de la classe etat
        if isinstance(etat,Etat):
            return etat
        else:
            raise TypeError("type non pris en charge")

    def __verifie_symbole(self,symbol):
        #verifie si le symbole entrée fait partier de l'aphabet
        if isinstance(symbol,str):
            return symbol
        else:
            raise TypeError("type non pris en charge")

    def changer_etat_depart(self,newdepart):
        self.depart=self.__verifie_etat(newdepart)


    def changer_etat_arrive(self,newarrive):

        self.arrive=self.__verifie_etat(newarrive)


    def changer_symbole(self,newsymbol):
        #cette fonction permet de modifier le symbole d'une transition
        self.symbole=self.__verifie_symbole(newsymbol)

    def est_epsilon(self):
        if self.symbole == '' or self.symbole == '€':
            return True
        else:
           return False

    def __eq__(self, p):
         if not isinstance(p, Transition) : return  False
         return (self.depart, self.symbole, self.arrive) == (p.depart, p.symbole, p.arrive)
         c_self=Transition(self.__depart,self.__symbole,self.__arrive)
         c_p=Transition(p.__depart,p.__symbole,p.__arrive)
         return (c_p.depart == c_self.depart) and (c_p.symbole == c_self.symbole) and (c_p.arrive == c_self.arrive)


    def __hash__(self):
        return hash((self.depart, self.symbole, self.arrive))





