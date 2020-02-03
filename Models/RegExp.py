from Models.Alphabet import Alphabet
from Models.Automate import Automate
from Models.Etat import Etat
from Models.Transition import Transition


class ExpressionReguliere:
    def __init__(self, expression:str):
        if not isinstance(expression, str):
            raise TypeError('Une expression est de type str')
        self.expression = expression
        print(f"Expression {expression}")

    def convertir_en_afn(self):
        parenthese = False
        expression_entre__parenthese = str()
        symbole_vers_automate = dict()
        expression_traite = list()

        index_suivant = 0;
        longeur_expression = len(self.expression)
        sauter_le_prochain_symbole = False

        faire_loperation_sur_la_dernier_expression = False
        for symbole in self.expression:

            print(symbole)
            index_suivant += 1
            print(f"index suivant {index_suivant} total {longeur_expression}")
            if symbole == ')':
                if parenthese:
                    parenthese = False
                    automate_correspondant = ExpressionReguliere(expression_entre__parenthese).convertir_en_afn()
                    symbole_vers_automate[f'P{index_suivant - 1}'] = automate_correspondant
                    expression_traite.append(f'P{index_suivant - 1}')
                    faire_loperation_sur_la_dernier_expression = True
                    expression_entre__parenthese=str()
                else:
                    raise ValueError(f'Parenthese fermante pas approprie au symbole {index_suivant}')
            if parenthese:
                expression_entre__parenthese += symbole
            elif symbole == '(':
                parenthese = True
                continue
                #TODO FAIRE CE CAS
                pass


            else:
                if symbole in ['*', '|', '.', '+']:
                    if index_suivant == 1:
                        raise ValueError('Une Expression ne peux pas commencer par un operateur')

                    else:
                        if symbole == '.':
                            expression_traite.append('.')
                        elif symbole in ['|', '+']:
                            expression_traite.append('+')

                    continue

                if sauter_le_prochain_symbole:
                    sauter_le_prochain_symbole = False
                    continue
                if index_suivant <= longeur_expression:
                    try:
                        symbole_suivant = self.expression[index_suivant]
                    except:
                        symbole_suivant = None
                    operation_de_concatenation = True
                    operation_de_addition = False
                    operation_de_kleen = False
                    if symbole_suivant == '*':
                        operation_de_kleen = True
                    elif symbole_suivant in ['|','+']:
                        operation_de_addition = True

                    if operation_de_kleen:
                        if faire_loperation_sur_la_dernier_expression:
                            automate_correspondant = GenerateurAutomate.faire_kleen(symbole_vers_automate[expression_traite[-1]])
                            symbole_vers_automate[expression_traite[-1]] = automate_correspondant
                            faire_loperation_sur_la_dernier_expression = False
                        else:
                            automate_correspondant = GenerateurAutomate.a_partir_du_symbole(symbole)
                            automate_correspondant = GenerateurAutomate.faire_kleen(automate_correspondant)
                            symbole_vers_automate[f'{symbole}{index_suivant-1}'] = automate_correspondant
                            expression_traite.append(f'{symbole}{index_suivant-1}')
                        expression_traite.append('.')
                        print('Kleen a fait')
                        print(expression_traite)

                    elif operation_de_addition:
                        if faire_loperation_sur_la_dernier_expression:
                            expression_traite.append('+')
                            faire_loperation_sur_la_dernier_expression = False
                            continue
                        automate_correspondant = GenerateurAutomate.a_partir_du_symbole(symbole)
                        symbole_vers_automate[f'{symbole}{index_suivant - 1}'] = automate_correspondant
                        #automate_correspondant.visualiser()
                        expression_traite.append(f'{symbole}{index_suivant - 1}')
                        expression_traite.append('+')
                        print('addition a fait')
                        print(expression_traite)
                    else:
                        if faire_loperation_sur_la_dernier_expression:
                            expression_traite.append('.')
                            faire_loperation_sur_la_dernier_expression = False
                            continue
                        automate_correspondant = GenerateurAutomate.a_partir_du_symbole(symbole)
                        symbole_vers_automate[f'{symbole}{index_suivant - 1}'] = automate_correspondant
                        expression_traite.append(f'{symbole}{index_suivant - 1}')
                        expression_traite.append('.')
                        print('Concat a fais')
                        print(expression_traite)

            taken = False

        addition = False
        concat = False
        dernier_expression = None
        counter = -1
        expression_traite_normal = []

        exp_precedent = None
        for expression in expression_traite:
            if expression != exp_precedent:
                expression_traite_normal.append(expression)
            exp_precedent = expression

        #reduction des plus
        automate_precedent =None
        print(f"Expression normal = {expression_traite_normal}")
        automata_traite = []
        dois_additioner = False
        for expression in expression_traite_normal:

            if expression == '+':
                dois_additioner = True
                continue
            if expression == '.':
                continue
            elif dois_additioner:
                automata_traite[-1] = GenerateurAutomate.faire_union(automata_traite[-1], symbole_vers_automate[expression])
                dois_additioner = False
                continue
            else:
                automata_traite.append(Automate.a_partir_de(symbole_vers_automate[expression]))


        #Faire la concat
        taken = False
        for automate in automata_traite:
            if not taken:
                resultat = Automate.a_partir_de(automate)
                taken = True
            else:
                resultat = GenerateurAutomate.faire_la_concatenation(Automate.a_partir_de(resultat), automate)

        return resultat


        print(f"Expression normal = {expression_traite_normal}")
        for expression in expression_traite_normal:
            counter += 1
            #symbole_vers_automate[expression].visualiser()
            if expression == '.':
                concat = True
            elif expression == '+':
                addition = True
                concat = False
            elif not taken:
                resultat = symbole_vers_automate[expression]
                taken=True
                dernier_expression = Automate.a_partir_de(resultat)
            else:
                if concat :
                    concat = False
                    resultat = GenerateurAutomate.faire_la_concatenation(Automate.a_partir_de(resultat), symbole_vers_automate[expression])
                elif addition:
                    addition = False

                    resultat = GenerateurAutomate.faire_union(Automate.a_partir_de(resultat),
                                                                         symbole_vers_automate[expression])
            #resultat.visualiser()
        return resultat


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
            automate2.remplacer_etat(automate2.etat_initial, etat)

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
    #a = Automate(Alphabet(['1']), [Etat('a'), Etat('b')], Etat('a'), [Etat('b')], [Transition(Etat('a'),'1',Etat('b'))])
    #b = Automate(Alphabet(['2']), [Etat('c'), Etat('d')], Etat('c'), [Etat('d')], [Transition(Etat('c'),'2',Etat('d'))])
    #a.visualiser()
    #b.visualiser()
    #a.union_automate(b).determiniser().minimiser().visualiser()

    #alphabet = Alphabet(['a','b'])
    #a = Etat('1')
    #b = Etat('2')
    #c = Etat('3')
    #d = Etat('4')

    #t1 = Transition(a,'a',b)
    #t2 = Transition(a,'b',a)
    #t3 = Transition(b,'b',b)
    #t4 = Transition(b,'a',a)
    #t5 = Transition(c,'a',c)
    #t6 = Transition(c,'b',d)
    #t7 = Transition(d,'a',d)
    #t8 = Transition(d,'b',c)

    #automate1 = Automate(alphabet,[a,b], a, [a], [t1,t2,t3,t4])
    #automate1.definir_nom('pair de a')
    #automate2 = Automate(alphabet,[c,d], c, [c], [t5,t6,t7,t8])
    #automate2.definir_nom('pair de b')
    #automate1.visualiser()
    #automate2.visualiser()

    #automate1.union_automate(automate2).visualiser()
    #automate1.union_automate(automate2).determiniser().minimiser().visualiser()
    #automate1.union_automate(automate2).determiniser().visualiser()
    #automate1.union_automate(automate2).determiniser().visualiser()
    #GenerateurAutomate.faire_union(a,b).visualiser()
    #GenerateurAutomate.faire_kleen(a).visualiser()

     a = ExpressionReguliere('if').convertir_en_afn()
     b = ExpressionReguliere('else').convertir_en_afn()

     b.union_automate(a).visualiser()
