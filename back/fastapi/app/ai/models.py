
from datetime import datetime
import random

class Environment:
    def __init__ (self, Tint, Tvoulue, Text, agenda):
        self.temperatureExterieur = float(Text)
        self.temperatureInterieur = float(Tint)
        self.temperatureVoulue = float(Tvoulue)
        self._agenda = agenda
        self.lastTemp = 0
        self.diff = 0
        self.lastdiff = 0
        self.changeTvoulue = False
        self.pas_amelioration = False

    def outcome (self, action):
        print("Bool amelioration : " + str(self.pas_amelioration))
        # diff_ext_int = self.get_tExt() - self.get_tInt()
        self.set_lastTemp(self.get_tInt())

        # self.update()

        self.update_diff()
        if self.get_tInt() == self.get_lastTemp():
            self.pas_amelioration = True
        print("Bool amelioration 2 : " + str(self.pas_amelioration))

        if self.amelioration():
            #   print("Amelioration")
            return 0
        else:
            #  print("Pas d'amelioration ")
            return 1

    def user_in_house (self):

        # x = datetime.now()
        return False

    def update(self, interieur, voulue, exterieur):
        # interieur = input('Interieur ? ')
        # voulue = 21
        # exterieur = 18

        self.set_tInt(float(interieur))
        self.set_tExt(float(exterieur))
        if float(voulue) == self.get_tVoulue():
            self.changeTvoulue = False
        else:
            print("Avant : " + str(self.get_tVoulue()) + " Apres : " + str(voulue))
            self.set_t_voulue(float(voulue))
            self.changeTvoulue = True

    def update_test (self):
        interieur = input('Interieur ? ')
        voulue = input('Voulue ? ')
        exterieur = input('Exterieur ? ')
        self.set_tInt(float(interieur))
        self.set_tExt(float(exterieur))
        if float(voulue) == self.get_tVoulue():
            self.changeTvoulue = False
        else:
            print("Avant : " + str(self.get_tVoulue()) + " Apres : " + str(voulue))
            self.set_t_voulue(float(voulue))
            self.changeTvoulue = True

    def amelioration (self):
        # 26-22 26-23

        print(" AMELIORATION ? : " + str(self.lastdiff - self.diff))
        if self.get_lastdiff() > self.get_diff():
            return True
        else:
            if (self.get_lastTemp() > self.get_tVoulue() and self.get_tInt() < self.get_tVoulue()):
                return True
            if (self.get_lastTemp() < self.get_tVoulue() and self.get_tInt() > self.get_tVoulue()):
                return True

            return False

    def update_diff (self):
        self.set_diff(abs(self.get_tVoulue() - self.get_tInt()))
        self.set_lastdiff(abs(self.get_tVoulue() - self.get_lastTemp()))

    def get_tInt (self):
        return self.temperatureInterieur

    def set_tInt (self, t):
        self.temperatureInterieur = t

    def get_tExt (self):
        return self.temperatureExterieur

    def set_tExt (self, t):
        self.temperatureExterieur = t

    def get_tVoulue(self):
        return self.temperatureVoulue

    def set_t_voulue(self, t):
        self.temperatureVoulue = t

    def get_diff(self):
        return self.diff

    def set_diff(self, d):
        self.diff = d

    def get_lastdiff(self):
        return self.lastdiff

    def set_lastdiff (self, d):
        self.lastdiff = d

    def get_lastTemp (self):
        return self.lastTemp

    def set_lastTemp (self, t):
        self.lastTemp = t


class Agent:
    def __init__ (self, bored_limit, environnement):
        """ Creating our agent """
        self.hedonist_table = [[2, -2, -2], [2, -2, -2], [3, -1, 4]]
        self._action = 2
        self.env = environnement
        self.contexte = [self.env.get_tInt(), self.env.get_tVoulue(), self.env.get_tExt()]
        self._categorie = self.categorie(self.contexte)
        self.bored_limit = bored_limit
        self.bestactions = {}
        self.action_pref = 2
        self.outcome_pref = 0
        self.pref_action_count = 0
        self._lastactions = 2

    def add_contexte (self, _contexte):
        self.contexte = _contexte
        self._categorie = self.categorie(_contexte)
        self.pref_action_count = 0

        if not self.search_best_action():
            self.action_pref = 2
            self.outcome_pref = 0
            self._action = 2

    def search_best_action (self):

        if str(self.contexte) in self.bestactions:
            self.action_pref = self.bestactions[str(self.contexte)][0]
            self.outcome_pref = self.bestactions[str(self.contexte)][1]
            self._action = self.action_pref
            print("Contexte Trouver")
            return True
        else:
            for key, values in self.bestactions.items():
                if values[2] == self._categorie:
                    print(" Semblable trouver : " + str(key))
                    self.action_pref = self.bestactions[str(key)][0]
                    self.outcome_pref = self.bestactions[str(key)][1]
                    self._action = self.action_pref
                    return True
        return False

    def action (self, outcome):

        if self.env.pas_amelioration and not self.is_board():
            self.env.pas_amelioration = False
            self.count()
            return self._action

        print(str(self.hedonist_table[self._action][outcome]) + str(
            self.hedonist_table[self.action_pref][self.outcome_pref]))

        if self.hedonist_table[self._action][outcome] > self.hedonist_table[self.action_pref][self.outcome_pref]:
            self.action_pref = self._action
            print("Nouvelle action preferee :  " + str(self.action_pref))
            self.outcome_pref = outcome
            self.pref_action_count = 0
        else:
            if self._action != self.action_pref:
                self._action = self.action_pref
                outcome = self.outcome_pref

        if self.is_board() or self.hedonist_table[self._action][outcome] < 0:
            self.change_action(outcome)

        self.count()

        return self._action

    def change_action (self, outcome):
        print("HERE")
        print(str(self.is_board()) + "Ennuie")
        _temp = self._action

        if _temp == 2:
            _temp = random.randint(0, 1)
        else:
            if self.hedonist_table[_temp][outcome] > 0:
                _temp = 2
            else:
                if _temp == 0:
                    print("X")
                    _temp = random.randint(1, 2)
                elif _temp == 1:
                    while _temp == 1:
                        print("Y")
                        _temp = random.randint(0, 2)

        self._action = _temp
        if not self.is_board():
            print(str(self.is_board()) + "Ennuie")
            self.action_pref = self._action
        self.pref_action_count = 0

    def is_board (self):
        if self.pref_action_count >= self.bored_limit and self._action != 2 :
            print("Je m'ennuie")
            return True
        if self.pref_action_count >= self.bored_limit and self.env.pas_amelioration:
            return True
        else:
            return False

    def count (self):
        if self._lastactions == self._action:
            self.pref_action_count += 1
            print("Action count : " + str(self.pref_action_count))
        else:
            self._lastactions = self._action
            self.pref_action_count = 0

    def update_contexte (self):
        self.contexte = [self.env.get_tInt(), self.env.get_tVoulue(), self.env.get_tExt()]
        self._categorie = self.categorie(self.contexte)

    def categorie (self, _contexte):
        if _contexte[0] < _contexte[1]:
            if _contexte[0] >= _contexte[2]:
                return "A"
            else:
                return "B"
        elif _contexte[0] > _contexte[1]:
            if _contexte[0] <= _contexte[2]:
                return "C"
            else:
                return "D"

    def save_best_actions (self, action, outcome):
        if self.hedonist_table[action][outcome] > 0:

            if not str(self.contexte) in self.bestactions:
                print(" CATEGORIE : " + self.categorie(self.contexte))
                self.bestactions[str(self.contexte)] = [action, outcome, self._categorie]
                print(self.bestactions[str(self.contexte)])
            else:
                if self.hedonist_table[self.bestactions[str(self.contexte)][0]][
                    self.bestactions[str(self.contexte)][1]] > self.hedonist_table[action][outcome]:
                    print('Ne rien faire : ' + str(self.hedonist_table[self.bestactions[str(self.contexte)][0]][
                                                       self.bestactions[str(self.contexte)][1]]))
                else:
                    self.bestactions[str(self.contexte)] = [action, outcome, self._categorie]
                    print(self.bestactions[str(self.contexte)])


def objectif_atteint (e):
    if e.get_lastTemp() < e.get_tVoulue() <= e.get_tInt():
        return True
    if e.get_lastTemp() < e.get_tVoulue() <= e.get_tInt():
        return True
    else:
        return False


def world (agent, environment, outcome):
    # AJOUTER LE CONTEXTE A LA CREATION DE L'AGENT

    count = 0
    #  if e.changeTvoulue == True :
    #      print("change")
    #     _contexte = [environment.get_tInt(),environment.get_tVoulue(),environment.get_tExt()]
    #    agent.addcontexte(_contexte)
    agent.update_contexte()
    agent.search_best_action()  #
    action = agent.action(outcome)

    if objectif_atteint(environment):
        action = 2
    print("Action choisie : " + str(action))
    outcome = environment.outcome(action)
    # print(" TEMP "+str(environment.get_tInt()) +" ("+ str(environment.get_lastdiff() - environment.get_diff())+")" )
    agent.save_best_actions(action, outcome)

    #  new_temp = input('Entrer la nouvelle temperature2:')
    #  environment.set_tVoulue(int(new_temp))

    action_outcome = [action, outcome]

    return action_outcome

    # print("Nombres d'actions pour finir : " + str(count))
