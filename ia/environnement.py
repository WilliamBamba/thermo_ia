

class Environment:
    def __init__(self, Tint, Tvoulue , Text):
        self.temperatureExterieur = Text
        self.temperatureInterieur = Tint
        self.temperatureVoulue = Tvoulue
        self.lastTemp = 0
        self.diff = 0
        self.lastdiff = 0

    def outcome(self, action):
        diffExtInt = self.temperatureExterieur - self.temperatureInterieur
        self.lastTemp = self.temperatureInterieur
        if action == 0:
            self.temperatureInterieur+=0.5

        elif action == 1:
            self.temperatureInterieur-=0.5

        else :
            if diffExtInt > 0 : # Plus chaud dehors que dedans
                self.temperatureInterieur+=0.5
            elif diffExtInt < 0 :
                self.temperatureInterieur-=0.5
        if self.amelioration() :
            #   print("Amelioration")
            return 0
        else :
            #  print("Pas d'amelioration ")
            return 1


    def amelioration(self):
        #26-22 26-23
        self.update()
        # print(" AMELIORATION ? : " + str(self.lastdiff - self.diff))
        if self.lastdiff > self.diff :
            return True
        else:
            return False

    def update(self) :
        self.diff = abs(self.temperatureVoulue - self.temperatureInterieur)
        self.lastdiff = abs(self.temperatureVoulue - self.lastTemp)

