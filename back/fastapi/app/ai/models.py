
from datetime import datetime
import random

class Environment:
    def __init__(self, Tint, Tvoulue , Text, agenda):
        self.temperatureExterieur = Text
        self.temperatureInterieur = Tint
        self.temperatureVoulue = Tvoulue
        self._agenda = agenda
        self.lastTemp = 0
        self.diff = 0
        self.lastdiff = 0

    def outcome(self, action):
        diff_ext_int = self.get_tExt() - self.get_tInt()
        self.set_lastTemp(self.get_tInt())
        if action == 0:
            self.set_tInt(self.get_tInt()+0.5)

        elif action == 1:
            self.set_tInt(self.get_tInt()-0.5)

        else :
            if diff_ext_int > 0 : # Plus chaud dehors que dedans
                self.set_tInt(self.get_tInt()+0.5)
            elif diff_ext_int < 0 :
                self.set_tInt(self.get_tInt()-0.5)

        if(self.user_not_in_house()):
            return 2

        if self.amelioration() :
            #   print("Amelioration")

            return 0
        else :
            #  print("Pas d'amelioration ")
            return 1


    def user_not_in_house(self):

        x = datetime.now()

        return False

    def update(self):
        x = input('Changer temperature voulue ?')
        if x == 'oui' :
            new_temp = input('Entrer la nouvelle temperature:')
            self.set_tVoulue(int(new_temp))
            return True
        else :
            return False

    def amelioration(self):
        #26-22 26-23
        self.update_diff()
        # print(" AMELIORATION ? : " + str(self.lastdiff - self.diff))
        if self.get_lastdiff() > self.get_diff() :
            return True
        else:
            return False

    def update_diff(self) :
        self.set_diff(abs(self.get_tVoulue() - self.get_tInt()))
        self.set_lastdiff(abs(self.get_tVoulue() - self.get_lastTemp()))


    def get_tInt(self):
        return self.temperatureInterieur

    def set_tInt(self, t):
        self.temperatureInterieur = t

    def get_tExt(self):
        return self.temperatureExterieur

    def set_tExt(self, t):
        self.temperatureExterieur = t

    def get_tVoulue(self):
        return self.temperatureVoulue

    def set_tVoulue(self, t):
        self.temperatureVoulue = t

    def get_diff(self):
        return self.diff

    def set_diff(self, d):
        self.diff = d

    def get_lastdiff(self):
        return self.lastdiff

    def set_lastdiff(self, d):
        self.lastdiff = d

    def get_lastTemp(self):
        return self.lastTemp

    def set_lastTemp(self, t):
        self.lastTemp = t




class SmartAgent:
    def __init__(self, bored_limit: int = 5):
        """ Creating our agent """
        self.hedonist_table = [[2,-2,-2],[2,-2,-2],[3,-1,4]]
        self._action = 2
        self.anticipated_outcome = 0
        self.contexte = [0,0,0]
        self._categorie = " "
        self.bored_limit = bored_limit
        self.good_anticipe_count = 0
        self.memoire = {}
        self.bestactions = {}
        self.action_pref = 2
        self.outcome_pref = 0
        self.pref_action_count = 0


    def addcontexte(self,_contexte):
        self.contexte = _contexte
        self._categorie = self.categorie(_contexte)
        self.pref_action_count = 0
        if str(self.contexte) in self.bestactions :
            self.action_pref = self.bestactions[str(self.contexte)][0]
            self.outcome_pref = self.bestactions[str(self.contexte)][1]
            self._action = self.action_pref
        else :
            trouver = False
            for key, values in self.bestactions.items():
                if (values[2] == self._categorie) :
                    print(" Semblable trouver : "+ str(key))
                    self.action_pref = self.bestactions[str(key)][0]
                    self.outcome_pref = self.bestactions[str(key)][1]
                    self._action = self.action_pref
                    trouver = True

            if trouver == False :
                self.action_pref = 2
                self.outcome_pref = 0
                self._action = 2


    def action(self, outcome):
        print(str(self.hedonist_table[self._action][outcome]) + str(self.hedonist_table[self.action_pref][self.outcome_pref]))

        if self.hedonist_table[self._action][outcome] > self.hedonist_table[self.action_pref][self.outcome_pref]:
            self.action_pref = self._action
            print("Nouvelle action preferee :  " + str(self.action_pref))
            self.outcome_pref = outcome
            self.pref_action_count = 0
        else :
            if self._action != self.action_pref:
                self._action = self.action_pref
                outcome = self.outcome_pref

        if self.is_board() or self.hedonist_table[self._action][outcome] < 0:
            self.changeaction(outcome)

        if self._action not in self.memoire.keys():
            self.memoire[self._action] = outcome

        if self.anticipated_outcome != outcome:
            self.memoire[self._action] = outcome

        if self.anticipated_outcome == outcome:
            self.good_anticipe_count += 1

        if(self.action_pref == self._action):
            self.pref_action_count +=1


        return self._action

    def changeaction(self,outcome):
        print("HERE")
        print(str(self.is_board()) + "Ennuie")
        self._temp = self._action

        if self._temp == 2 :
            self._temp = random.randint(0, 1)
        else :
            if self.hedonist_table[self._temp][outcome] > 0 :
                self._temp = 2
            else :
                if self._temp == 0:
                    print("X")
                    self._temp = random.randint(1,2)
                elif  self._temp == 1 :
                    while self._temp == 1:
                        print("Y")
                        self._temp = random.randint(0,2)

        self._action = self._temp
        if self.is_board() == False :
                print(str(self.is_board()) + "Ennuie")
                self.action_pref = self._action
        self.good_anticipe_count = 0
        self.pref_action_count = 0

    def anticipation(self):
        self.anticipated_outcome = self.memoire[self._action]

        return self.anticipated_outcome

    def is_board(self):
        if self.pref_action_count >= self.bored_limit and self.good_anticipe_count >= self.bored_limit :
            print("Je m'ennuie")
            return True
        else:
            return False

    def satisfaction(self, new_outcome):

        anticipation_satisfaction = (self.anticipated_outcome == new_outcome)
        self.goodAnticipation = anticipation_satisfaction
        hedonist_satisfaction = self.hedonist_table[self._action][new_outcome]
        #print("YES "+  str(self.hedonist_table[0][1]) + "yes "+ str(self._action) + "yes "+ str(new_outcome))

        return anticipation_satisfaction, hedonist_satisfaction, self.is_board()


    def categorie(self,_contexte) :
        if (_contexte[0]<_contexte[1]):
            if (_contexte[0]>=_contexte[2]):
                return "A"
            else :
                return "B"
        elif (_contexte[0]>_contexte[1]):
            if(_contexte[0]<=_contexte[2]):
                return "C"
            else :
                return "D"

    def savebestactions(self) :
        if not str(self.contexte) in self.bestactions:
            print(" CATEGORIE : " + self.categorie(self.contexte))
            self.bestactions[str(self.contexte)]=[self.action_pref,self.outcome_pref,self._categorie]
        print(self.bestactions[str(self.contexte)])


