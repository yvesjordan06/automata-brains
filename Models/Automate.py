#from PyQt5.QtCore import QObject, pyqtSignal

from Models.Transition import Transition
from Models.Etat import Etat
from Models.Alphabet import Alphabet
#from graphviz import Digraph
import datetime


class Type:
    AFD = 'Automate Fini Deterministe'
    AFN = 'Automate Fini Non Deterministe'
    eAFN = f'Epsilon {AFN}'


#class Automate(QObject):
class Automate:
    # Signale de modification
    #automate_modifier = pyqtSignal()

    def __init__(self, alphabet, etats, etat_initial, etat_finaux, transition):
        super().__init__()
        self.__alphabet = self.__verifier_alphabet(alphabet)
        self.__etats = self.__verifier_etat(etats)
        self.__etat_initial = self.__verifier_initial(etat_initial)
        self.__etat_finaux = self.__verifier_finaux(etat_finaux)
        self.__transitions = self.__verifier_transition(transition)
        self.nom = str()

    def __verifier_alphabet(self, alphabet):
        if isinstance(alphabet, Alphabet):
            return alphabet
        else:
            return Alphabet(alphabet)

    def __verifier_etat(self, etats):
        pile = set()
        if isinstance(etats, (set, tuple, list)):
            for i in etats:
                if isinstance(i, Etat):
                    pile.add(i)
                else:
                    pile.add(Etat(i))
            return pile

    def __verifier_initial(self, initial):
        if isinstance(initial, Etat):
            if initial in self.__etats:
                return initial
            else:
                raise ValueError(initial, "ne se trouve pas dans self.__etats")
        else:
            raise TypeError("le type non prix en charge")

    def __verifier_finaux(self, finaux):
        pile = set()
        if isinstance(finaux, (set, list, tuple)):
            for i in finaux:
                if isinstance(i, Etat):
                    if i in self.__etats:
                        pile.add(i)
                    else:
                        raise ValueError(finaux, "ne se trouve pas dans self.__etats")

                else:
                    raise TypeError("le type non prix en charge")
            return pile
        elif isinstance(finaux, Etat):
            return set(finaux)
        else:
            raise TypeError("le type non prix en charge")

    def __verifier_transition(self, transitions):
        pile = set()
        if isinstance(transitions, (set, list, tuple)):
            for i in transitions:
                if isinstance(i, Transition):
                    if (i.depart in self.__etats) and (i.arrive in self.__etats) and (i.symbole in self.__alphabet or i.symbole in ['']):
                        pile.add(i)
                    else:
                        raise TypeError(f"transistion {i} mal defini")
                else:
                    raise TypeError("type Transition attendu")

            return pile
        elif isinstance(transitions, Transition):
            if (transitions.depart in self.__etats) and (transitions.arrive in self.__etats) and (
                    transitions.symbole in self.__alphabet):
                pile.add(transitions)
                return pile
        else:
            raise ("type non pris en charge")

    def ajouter_symbole(self, symbole):
        print(f"J'ajoute le symbole {symbole}")
        self.__alphabet.ajouter_symbole(symbole)
        print(self.alphabet)
        #self.automate_modifier.emit()

    """
             Cette fonction ajoute simplement un etat dans l'automate de type Etat
              Sinon elle rejet une erreur   
       """
    def ajouter_etats(self, etat):
        if isinstance(etat, Etat):
            self.__etats.add(etat)
            print(f"Etat Ajouter {etat}")
            #self.automate_modifier.emit()
        else:
            raise TypeError("type non prit en charge")

    """
             Cette fonction ajoute simplement un etat initial, l'etat dois etre present dans l'automate et etre de type Etat
              Sinon elle rejet une erruer   
       """
    def ajouter_initital(self, etat):
        if isinstance(etat, Etat):
            if etat in self.__etats:
                self.__etat_initial = etat
                print(f"Etat Initial {etat}")
                #self.automate_modifier.emit()
            else:
                raise ValueError("valeur non presente")
        else:
            raise TypeError("type non prit en charge")

    """
          Cette fonction ajoute simplement un etat final, l'etat dois etre present dans l'automate et etre de type Etat
           Sinon elle rejet une erruer   
    """
    def ajouter_final(self, etat):
        if isinstance(etat, Etat):
            if etat in self.__etats:
                self.__etat_finaux.add(etat)
                print(f"Etat Final {etat}")
                #self.automate_modifier.emit()
            else:
                raise ValueError("valeur non presente")
        else:
            raise TypeError("type non prit en charge")

    """
       Cette fonction ajoute simplement la transition passer en parametre
        Si le type du paremetre n'est pas Transition elle rejet une erruer   
    """
    def ajoute_transition(self, transition):
        if isinstance(transition, Transition):
            if (transition.depart in self.__etats) and (transition.arrive in self.__etats):
                if (transition.symbole in self.__alphabet) or transition.symbole in ('', "€"):
                    self.__transitions.add(transition)
                    print(f'Transtion Ajouter {transition}')
                    #self.automate_modifier.emit()
                else:
                    raise ValueError("symbole de la transtion non defini")
            else:
                raise ValueError("transition mal defini")
        else:
            raise TypeError("Type non prit en charge ")

    """
    Cette fonction supprime simplement la transition passer en parametre
    """
    def supprime_transition(self, transition):
        corbeille = []
        if isinstance(transition, Transition):
            for i in self.__transitions:
                if i == transition:
                    corbeille.append(i)
            for j in corbeille:
                self.__transitions.remove(j)

        else:
            raise TypeError("type non prit en charge")

    """
        Cette fonction se charge de supprimer un symbole de l'automate
        Si le symbol est absente elle ne fais rien

        Si le symbol est present, elle supprime aussi toute les transition qui lui sont associer
    """
    def supprime_symbole(self, symbole):
        corbielle = []
        if symbole in self.__alphabet:
            self.__alphabet.supprime_symbole(symbole)
            for i in self.__transitions:
                corbielle.append(i)
            for j in corbielle:
                self.__transitions.remove(j)

    """
    Cette fonction se charge de supprimer un etat de l'automate
    Si l'etat est absente elle ne fais rien
    
    Si l'etat est present, elle supprime aussi toute les transition qui lui sont associer
    """
    def supprime_etat(self, etat):
        corbeille = []
        if etat in self.__etats:
            self.__etats.remove(etat)
            if etat == self.__etat_initial:
                self.__etat_initial = None
            if etat in self.__etat_finaux:
                self.__etat_finaux.remove(etat)
            for i in self.__transitions:
                if etat in (i.depart, i.arrive):
                    corbeille.append(i)
            for j in corbeille:
                self.__transitions.remove(j)

    """
    Complementation
    
    Cette fonction retourne le complement de l'automate actuelle
    """
    def complementation_automate(self):
        new_transition = set()
        self.__etat_finaux.clear()
        self.__etat_finaux.add(self.__etat_initial)
        for i in self.__transitions:
            new_transition.add(Transition(i.arrive, i.symbole, i.depart))
        return Automate(self.__alphabet, self.__etats, self.__etat_initial, new_transition)

    """
    Intersection
    
    Cette fonction prend en parametre un autre automate et retourne un automate
    L'automate de retour est l'intersection entre les 2 automates
    """

    def intersection_automate(self, automate):
        if isinstance(automate, Automate):
            pass
        #TODO Terminer l'implementation de l'intersection

    def definir_nom(self, nom):
        if isinstance(nom, str):
            self.nom = nom
        else:
            self.nom = str(nom)
    """
    Permet de visualiser l'automate actuel
    Il faut au prealable avoir installer graphviz
    installation pip install graphviz
    sudo apt get install graphviz
    """
    def visualiser(self, **kwargs):
        # Si vous avez installer graphviz decommentez

        """kwargs.setdefault('filename', f'../diagrams/automate{datetime.datetime.now().time()}')
        kwargs.setdefault('format', f'png')

        f = Digraph('Test', filename=kwargs['filename'], format=kwargs['format'])
        # f.attr(label=f'Type: \n {self.check_type()}')
        f.attr(rankdir='LR', size='15,5')
        f.attr('node', shape='none', height='0', width='0')
        f.node('')
        f.attr('node', shape='doublecircle')
        for etat in self.etats_finaux:
            f.node(str(etat))
        f.attr('node', shape='circle')
        f.edge('', str(self.etat_initial))
        for t in self.transitions:
            f.edge(str(t.depart), str(t.arrive), label=t.symbole)
        return f.view()"""

        pass
    """
    Permet de visualiser l'image sans la stocker dans la memoire
    """
    def temp_view(self):
        return self.visualiser(filename='../diagrams/temp', format='png')

    """
    Permet d'enregistrer l'image sous le format et le nom du fichier passer en parametre
    Cette fonctionne retourne le lien ou se trouve l'image
    """
    def save_view(self, filename, _format):
        return self.visualiser(filename=filename, format=_format)

    '''
    Trouve les etat destinations pour un etat de depart sur la lecture d'une symbole
    Retourne un tableau d'etat
    '''
    def __etats_destination(self, depart: Etat, symbole: str) -> list:
        if not isinstance(depart, Etat) and not isinstance(symbole, str):
            raise TypeError('Type non pris en charge')
        destination = list()
        for transition in self.transitions:
            if transition.depart == depart and transition.symbole == symbole:
                destination.append(transition.arrive)
        return destination

    '''
    Cette fonctionne retourne tout un tableau d'etat accesible uniquement sur la lecture du symbole epsilon
    d'un etat en parametre
    '''
    def epsilon_fermeture(self, etat: Etat) -> list:
        if not isinstance(etat, Etat):
            raise TypeError('Type non pris en charge')

        # Un etat est dans sa fermeture elle meme
        fermeture = [etat]

        fermeture_verifier = list()

        for etat_a_verifier in fermeture:
            if etat_a_verifier in fermeture_verifier:
                continue
            else:
                etat_destination = list()
                try:

                    etat_destination = self.__etats_destination(etat_a_verifier, '')

                except Exception as error:
                    print("line 153", error)
                if etat_destination:
                    fermeture.extend(etat_destination)
            fermeture_verifier.append(etat_a_verifier)
        return list(set(fermeture_verifier))

    '''
    Cette fonction verifie si un mot est reconnu dans l'automate
    :return bool
    '''
    def reconnais_mot(self, mot:str)->bool:
        #TODO Determiniser d'abord avant de reconnaitre
        if not isinstance(mot, str):
            raise TypeError('Type str uniquement')

        suivant = self.etat_initial
        try:
            for symbole in mot:
                destinations = self.read(suivant, symbole)
                if destinations:
                    suivant = destinations[0]
                else:
                    return False
            if set(suivant).intersection(self.etats_finaux):
                return True
            else:
                return False
        except:
            return False

    """
    Cette fonction determinise l'automate actuelle
    Si l'automate est un AFD elle retourne l'automate
    Si l'automate est un AFN elle le minimise puis retourn l'automate minimiser
    Si l'automate est un epsilon AFN elle le transform en AFN puis la minimise et retourne l'automate minimiser
    """
    def determiniser(self):
        etats = [self.etat_initial]
        nouveau_vers_ancien_etat = {self.etat_initial : [self.etat_initial]}
        etats_finaux = set()
        transitions = set()

        etats_verifier = set()


        if self.type == Type.AFD:
            return self
        elif self.type == Type.AFN:
            if self.etat_initial in self.etats_finaux:
                etats_finaux.add(self.etat_initial)
            for etat in etats:
                print(f'je verifie {etat} => {nouveau_vers_ancien_etat[etat]}')
                if etat in etats_verifier:
                    continue
                for symbol in self.alphabet.list:
                    etats_destination = list()
                    for ancien_etat in nouveau_vers_ancien_etat[etat]:
                        etats_destination.extend(self.__etats_destination(ancien_etat,symbol))
                    print(f'etat destination {etats_destination}')
                    if etats_destination:
                        nouvelle_destination = Etat(''.join([str(x) for x in etats_destination]))
                        etats.append(nouvelle_destination)
                        nouveau_vers_ancien_etat[nouvelle_destination] = list(set(etats_destination))
                        if set(etats_destination).intersection(self.etats_finaux):
                            etats_finaux.add(nouvelle_destination)



                        nouvelle_transition = Transition(etat, symbol, nouvelle_destination)
                        transitions.add(nouvelle_transition)
                etats_verifier.add(etat)

            return Automate(self.__alphabet, etats_verifier, self.etat_initial, etats_finaux, list(transitions))

        else:
            return self.convertir_en_nfa().determiniser()

    """
    Cette fonction convertir l'automate actuelle en AFN
    a condition que l'automate sois epsilon AFN (contient des transition epsilon)
    Si l'automate n'est pas epsilon une erreur est retourner
    """

    def convertir_en_nfa(self):
        if self.type != Type.eAFN:
            raise TypeError(f'Conversion autorisee uniquement pour les {Type.eAFN} ')
        etat_initial = self.etat_initial
        etat_finaux = list()
        transition = list()
        fermeture_epsilon = {}

        for etat in self.etats:
            fermeture_epsilon[etat] = self.epsilon_fermeture(etat)

        for etat in self.etats:
            if self.etats_finaux.intersection(set(fermeture_epsilon[etat])):
                etat_finaux.append(etat)

            for symbole in self.alphabet.list:
                etats_destination = list()
                for etat_epsilon in fermeture_epsilon[etat]:
                    etats_destination.extend(self.__etats_destination(etat_epsilon,symbole))
                destination_resultat =  list()
                for etat_destination in set(etats_destination):
                    destination_resultat.extend(self.epsilon_fermeture(etat_destination))
                for destination in set(destination_resultat):
                    nouvelle_transition = Transition(etat,symbole,destination)
                    transition.append(nouvelle_transition)
        return Automate(self.alphabet, self.etats, self.etat_initial, etat_finaux, transition)

    """
    Determine si l'automate est complet
    Il verifie toute les paire symbole, alphabet
    Si une paire n'as pas de destination , L'automate n'est pas complet
    Si toute les paire on une destination, L'automate est complet
    """
    @property
    def est_complet(self):
        for etat in self.etats:
            for symbole in self.alphabet.list:
                if not self.__etats_destination(etat,symbole):
                    return False
        return True

    """
    Cette fonctionne complete l'automate actuelle en rajoutant un etat puit
    Si l'automate n'est pas AFD il le converti et retourne l'automate complet
    """
    def completer(self):
        if self.type != Type.AFD:
            return self.determiniser().completer()

        puit = Etat("PUIS")
        etats = self.etats
        etats.add(puit)
        transitions = self.transitions

        for etat in etats:
            for symbole in self.__alphabet.list:
                if not self.__etats_destination(etat, symbole):
                    self.transitions.add(Transition(etat, symbole, puit))

        return Automate(self.alphabet, etats, self.etat_initial, self.etats_finaux, transitions)

    """
    Cette fonction copie les propriete de l'automate en parameter sur l'automate actuelle
    """

    def copie_automate(self, autre):
        if isinstance(autre, Automate):
            self.__alphabet = autre.alphabet
            self.__etats = autre.etats
            self.__etat_initial = Automate.etat_initial
            self.__etat_finaux = autre.etat_finaux
            self.__transitions = autre.transition
            self.nom = autre.nom
        else:
            raise TypeError('Type Automate attendu ')

    '''
    Determine le type de l'automate
    
    Utilisation automate.type
    Valeur retour = Type.AFD, Type.AFN, Type.eAFN
    '''

    @property
    def type(self) -> str:
        epsilon = False
        nfa = False

        for transition in self.__transitions:
            if len(self.__etats_destination(transition.depart, transition.symbole)) > 1:
                nfa = True
            if transition.est_epsilon():
                epsilon = True
                nfa = True
            if epsilon and nfa:
                return Type.eAFN
        if nfa:
            return Type.AFN
        else:
            return Type.AFD

    @property
    def alphabet(self):
        return self.__alphabet

    @property
    def etats(self):
        return self.__etats

    @property
    def etat_initial(self):
        return self.__etat_initial

    @property
    def etats_finaux(self):
        return self.__etat_finaux

    @property
    def transitions(self):
        return self.__transitions


if __name__ == '__main__':
    alphabet = Alphabet(['1', '2', '3'])
    a = Etat('a')
    b = Etat('b')
    c = Etat('c')
    t1 = Transition(a, '1', b)
    t5 = Transition(b, '', c)
    t2 = Transition(a, '1', a)
    t6 = Transition(a, '', c)
    t3 = Transition(b, '2', b)
    t4 = Transition(b, '1', b)
    automate = Automate(alphabet, [a, b, c], a, [c], [t1, t5, t2, t6])
    print(automate.alphabet)
    automate.definir_nom('hiro')
    print(automate.nom)
    #automate.visualiser()
    #automate.convertir_en_nfa().visualiser()
    #automate.determiniser().visualiser()
    #automate.completer()
    #automate.visualiser()

# TODO Etat ne dois pas s'initialiser avec un symbole vide
# TODO Ajouter alphabet de dois pas prendre de symbole vide
# TODO Definir la fonction supprimer symbole
# TODO Definir la fonction supprimer etat
# TODO Ajouter etat dois prendre en parametre est initiale et est finale
