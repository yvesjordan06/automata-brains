# automata-brains
TP INFO 304 - Les Automata

# Automate

### Definition
```
class Automate:
   # Attribut
    nom:str
    alpabet
    etats
    etat_initial
    etat_finaux
    transitions
```
### Initialisation
> 1 - Il doit etre possible d'initialiser l'automate avec les valeurs
NB Le nom ne doit pas initialiser

Example

```
a = Etat("a")
b = Etat("b")
c = Etat("c")

alphabet = Alphabet(['1','2','3'])

t1 = Transition(a,'1',a)
t2 = Transition(a,'1',b)
 
automata = Automate(alphabet, [a,b,c], a, [b], [t1,t2])
#ordre des parametre dans l'example 
# 1 = alphabet
# 2 = etats
# 3 = etat initial
# 4 = etats finaux
#5 = Transitions

```
### Initialisation
> 2 - Il doit etre possible d'ajouter des etat, transition a l'alphabet

Declaration `ajouter_etat(etat, est_initial = False, est_final = False)`

Example

```
#On considere l'automate de l'example precend
automate.ajouter_etat(Etat('d'),True,False) ou automate.ajouter_etat(Etat('d'),True) 
#Ajoute un etat d, Qui sera l'etat initial, et qui ne sera pas final
#NB Si un etat final existe deja il sera remplacer


automate.ajouter_etat(Etat('e'),False,True) 
#Ajoute un etat e, Qui fera partie des etat finaux, et qui ne sera pas initial


automate.ajouter_etat(Etat('d'),False,False) ou automate.ajouter_etat(Etat('d'))
#Ajoute un etat d, Qui ne fera partie des etat finaux, et ne sera pas initial

```

Declaration `definir_etat_initial(etat)`

> NB Si l'etat n'existe pas dans l'automate `raise`, Si l'etat est deja initial, Ne rien faire sinon faire que l'etat devien  initial
Si un etat initial existe, Le remplacer par le nouveau


Declaration `ajouter_etat_final(etat)`

>NB Si l'etat n'existe pas dans l'automate `raise`, Si l'etat est deja final, Ne rien faire sinon faire que l'etat devien final


Declaration `ajouter_transtion(transition)`

>NB Si la transition n'est pas valide (n'est pas de type transition ou etat introuvable, symbole qui n'existe pas , `raise` sinon Ajouter la transition
Si elle existe deja (l'utilite de la surcharge du hash et equivalence) Ne rien faire

> Pour ajouter l'alphabet on fera `automata.alphabet.ajouter_symbol()`


Declaration `definir_nom(nom:str)`

>Cette methode permet simplement de mettre la nom a l'automate Elle ne retourne rien et rejete une erreur si le type du nom n'est pas un str
