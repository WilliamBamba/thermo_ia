import random


class Agent:
    def __init__ (self, _hedonist_table, bored_limit, environnement):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
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
