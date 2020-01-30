class Alphabet:
    def __init__(self,alphabet):
        self.__alphabet = self.__verifie_aphabet(alphabet)

    def __repr__(self):
        return str(self.__alphabet)



    def __verifie_aphabet(self, alphabet):
        pile = set()
        if isinstance(alphabet, (list, tuple, set)):
            for i in alphabet:
                if (i != " ") or (i != ''):
                    pile.add(i)
            return pile
        elif isinstance(alphabet, str) and (alphabet != " "or alphabet !=''):
            return set(alphabet)
        else:
            raise TypeError("type non accepter")

    def __verifie_symbole(self,symbol):
        #verifie si le symbole entrée fait partier de l'aphabet
        if isinstance(symbol,str):
            return symbol
        else:
            raise TypeError("type non pris en charge")



    def ajouter_symbole(self,symbol):
        if isinstance(symbol,str) and (symbol != " " or symbol !=''):
            self.__alphabet.add(symbol)
        else:
            raise TypeError("symbole non accepter")

    def __contains__(self, item):
        return item in self.__alphabet

    def supprime_symbole(self,symbol):
        if symbol in self.__alphabet:
            self.__alphabet.remove(symbol)

    @property
    def list(self):
        return self.__alphabet