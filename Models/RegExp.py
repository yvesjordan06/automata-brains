from Models.Alphabet import Alphabet
from Models.Automate import Automate
from Models.Etat import Etat
from Models.Transition import Transition


class ExpressionReguliere:
    def __init__(self, expression:str):
        if not isinstance(expression, str):
            raise TypeError('Une expression est de type str')
        self.expression = expression

    def convertir_en_afn(self):
        symbole_vers_automate = dict()
        expression_traite = list()

        index_suivant = 1;
        longeur_expression = len(self.expression)
        for symbole in self.expression:
            if symbole == '(':
                #TODO FAIRE CE CAS
                pass
            elif symbole in ['*','|',')','.']:
                if index_suivant == 1:
                    raise ValueError('Une Expression ne peux pas commencer par un operateur')
                else:
                    continue
            else:
                if index_suivant < longeur_expression:
                    symbole_suivant = self.expression[index_suivant]
                    operation_de_concatenation = True
                    operation_de_addition = False
                    operation_de_kleen = False
                    if symbole_suivant == '*':
                        operation_de_kleen = True
                    elif symbole_suivant == '|':
                        operation_de_addition = True

                    if operation_de_kleen:
                        automate_correspondant = GenerateurAutomate.a_partir_du_symbole(symbole)
                        automate_correspondant = GenerateurAutomate.faire_kleen(automate_correspondant)
                        symbole_vers_automate[f'{symbole}{index_suivant-1}'] = automate_correspondant
                        expression_traite.append(f'{symbole}{index_suivant-1}')
                    elif operation_de_addition:
                        automate1 = GenerateurAutomate.a_partir_du_symbole(symbole)
                        automate2 = GenerateurAutomate.a_partir_du_symbole(self.expression[index_suivant+1])
                        automate_correspondant = GenerateurAutomate.faire_union(automate1, automate2)
                        symbole_vers_automate[f'{symbole}{index_suivant - 1}'] = automate_correspondant
                        expression_traite.append(f'{symbole}{index_suivant - 1}')
                    else:
                        automate_correspondant = GenerateurAutomate.a_partir_du_symbole(symbole)
                        symbole_vers_automate[f'{symbole}{index_suivant - 1}'] = automate_correspondant
                        expression_traite.append(f'{symbole}{index_suivant - 1}')

class GenerateurAutomate:
    compteur_etat_initial = 0
    compteur_etat_final = 0
    compteur_etat = 0
    @staticmethod
    def a_partir_du_symbole(symbole):
        if not isinstance(symbole, str):
            raise TypeError('Un symbole dois etre de type str')
        alphabet = Alphabet([symbole])
        initial = GenerateurAutomate.etat_initial()
        final = GenerateurAutomate.etat_final()
        transition = Transition(initial,symbole,final)
        return Automate(alphabet,[initial,final],initial,[final],[transition])
    @staticmethod
    def faire_kleen(automate):
        if not isinstance(automate, Automate):
            raise TypeError('Kleen est possible uniquement sur un automate')
        initial = GenerateurAutomate.etat_initial()
        final = GenerateurAutomate.etat_final()

        ancien_initial = automate.etat_initial
        ancien_finaux = automate.etats_finaux.copy()
        print(initial)
        automate.ajouter_etats(initial)
        automate.ajouter_etats(final)
        automate.ajouter_initital(initial)

        for etat in ancien_finaux:
            automate.retirer_final(etat)

        automate.ajouter_final(final)

        transition_initial = Transition(initial,'',ancien_initial)
        automate.ajoute_transition(transition_initial)

        for etat in ancien_finaux:
            transition_final = Transition(etat,'',final)
            automate.ajoute_transition(transition_final)
            transition_boucle = Transition(etat,'',ancien_initial)
            automate.ajoute_transition(transition_boucle)

        transition_kleen = Transition(initial,'',final)
        automate.ajoute_transition(transition_kleen)

        return automate

    @staticmethod
    def faire_union(automate1:Automate, automate2:Automate):
        if not isinstance(automate1, Automate) or not isinstance(automate2, Automate):
            raise TypeError("L'addition se fais uniquement entre les automate")

        initial = GenerateurAutomate.etat_initial()
        final = GenerateurAutomate.etat_final()

        ancien_initial = [automate1.etat_initial, automate2.etat_initial]
        ancien_finaux = [*automate1.etats_finaux, *automate2.etats_finaux]

        nouveaux_etats = [*automate1.etats, *automate2.etats, initial, final]
        nouvelle_transition = [*automate1.transitions, *automate2.transitions]
        nouvel_alphabet = Alphabet([*automate1.alphabet.list, *automate2.alphabet.list])
        automate = Automate(nouvel_alphabet, nouveaux_etats, initial, [final], nouvelle_transition)



        for etat in ancien_initial:
            transition_initial = Transition(initial, '', etat)
            automate.ajoute_transition(transition_initial)

        for etat in ancien_finaux:
            transition_final = Transition(etat, '', final)
            automate.ajoute_transition(transition_final)

        return automate

    @staticmethod
    def faire_la_concatenation(automate1: Automate, automate2: Automate):
        initial = automate1.etat_initial
        final = list(automate2.etats_finaux)[-1]

        for etat in automate1.etats_finaux:
            automate2.remplacer_etat(automate2.etat_initial, list(automate1.etats_finaux)[-1])

        nouveaux_etats = [*automate1.etats, *automate2.etats]
        nouvelle_transition = [*automate1.transitions, *automate2.transitions]
        nouvel_alphabet = Alphabet([*automate1.alphabet.list, *automate2.alphabet.list])
        automate = Automate(nouvel_alphabet, nouveaux_etats, initial, [final], nouvelle_transition)

        return automate



    @staticmethod
    def etat():
        GenerateurAutomate.compteur_etat += 1
        return Etat(f'Q{GenerateurAutomate.compteur_etat}')

    @staticmethod
    def etat_initial():
        GenerateurAutomate.compteur_etat_initial += 1
        return Etat(f'I{GenerateurAutomate.compteur_etat_initial}')

    @staticmethod
    def etat_final():
        GenerateurAutomate.compteur_etat_final += 1
        return Etat(f'F{GenerateurAutomate.compteur_etat_final}')


if __name__ == '__main__':
    a = Automate(Alphabet(['1']), [Etat('a'), Etat('b')], Etat('a'), [Etat('b')], [Transition(Etat('a'),'1',Etat('b'))])
    b = Automate(Alphabet(['2']), [Etat('c'), Etat('d')], Etat('c'), [Etat('d')], [Transition(Etat('c'),'2',Etat('d'))])
    a.visualiser()
    b.visualiser()
    GenerateurAutomate.faire_kleen(a).visualiser()