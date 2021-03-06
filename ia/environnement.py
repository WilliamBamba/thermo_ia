from datetime import datetime


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
        self.update()
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

        x = datetime.now()
        return False

    def update (self):
        interieur = input('Interieur ? ')
        voulue = 21
        exterieur = 18
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
