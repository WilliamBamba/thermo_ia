from random import *
from datetime import datetime 

class Agent:
    def __init__(self):
        """ Creating our agent """
    
        # dif(t voulue et t act ) dif(t voulue et t dehors ) decision et recompense
        self.memoire = []

    def evaluation_experience_precedente(self, tempData):
        # ajout de donnnees courantes 
        self.memoire.append([tempData[1] - tempData[0], tempData[1] - tempData[2], -1 , 0] )

        experience = []
        if len(self.memoire)> 1:
            experiencePrec = self.memoire[-2]
            experienceAct = self.memoire[-1]

            # if experienceAct[0] == 0:
            #     hey = 8

            if experienceAct[0] > experiencePrec[0] :
                self.memoire[-2][3] = -1
            elif experienceAct[0] == experiencePrec[0]:
                self.memoire[-2][3] = 0
            else:
                self.memoire[-2][3] = 1
            

    def cherche_pattern(self):
        exp_similiaire = []
        exp_val = []
        exp_act = self.memoire[-1]
        marge_erreur = 1

        for exp in self.memoire:
            if exp[0] == exp_act[0] or exp[0] + marge_erreur == exp_act[0] or exp[0] - marge_erreur == exp_act[0]:
                if exp[1] == exp_act[1] or exp[1] + marge_erreur == exp_act[1] or exp[1] - marge_erreur == exp_act[1]:
                    if exp[3] > 0:
                        diff = abs(exp[0] - exp_act[0]) + abs(exp[1] - exp_act[1])
                        exp_similiaire.append(exp)
                        exp_val.append(diff)

        if len(exp_similiaire) == 1:
            return exp_similiaire[0]
        elif len(exp_similiaire) == 1:
            return exp_val.index(min(exp_val.values()))

        return None
    
    def decision(self, tempData, agenda_utilisateur):
        recalcule = False
        nbAcceptable = 3
        dif_tVoulu_tAct = tempData[1] - tempData[0]
        dif_tVoulu_tDehors = tempData[1] - tempData[2]
        dif_hArrive_hCourante = agenda_utilisateur[1].hour - agenda_utilisateur[0].hour
        exp_similaire = self.cherche_pattern()

        if exp_similaire == None or dif_tVoulu_tAct + dif_tVoulu_tDehors == 0 or dif_tVoulu_tAct == 0:
            if len( self.memoire) >= 2:
                if self.memoire[-2][3] > 0:
                    decFinal = self.memoire[-2][2]
                    recalcule = True
                else:
                    decFinal = -1
                    recalcule = False
            
            if (len( self.memoire) >= 2 and self.memoire[-2][3] < 0 ) or (len( self.memoire) >= nbAcceptable and self.memoire[-2][-1] == self.memoire[-3][-1] == self.memoire[-4][-1] == 0):
                recalcule = False
            elif dif_tVoulu_tAct + dif_tVoulu_tDehors == 0 or dif_tVoulu_tAct == 0:
                    decFinal = 2
    
            # 0: chauffage on , clime off
            # 1: chauffage off , clime on
            # 2: chauffage off , clime offkj
            if len( self.memoire) <= 1 or not recalcule:
                if dif_tVoulu_tAct + dif_tVoulu_tDehors == 0 or dif_tVoulu_tAct == 0:
                    decFinal = 2
                elif dif_tVoulu_tAct > 0 and dif_tVoulu_tDehors < 0:
                    if dif_hArrive_hCourante <= 1:
                        decFinal = 0
                    else:
                        decFinal = 2
                elif dif_tVoulu_tAct < 0 and dif_tVoulu_tDehors > 0:
                    if dif_hArrive_hCourante <= 1:
                        decFinal = 1
                    else:
                        decFinal = 2
                elif dif_tVoulu_tAct > 0 and dif_tVoulu_tDehors > 0:
                    if dif_hArrive_hCourante <= 1 or dif_tVoulu_tAct >= 5:
                        decFinal = 0
                    else:
                        decFinal = 2
                elif dif_tVoulu_tAct < 0 and dif_tVoulu_tDehors < 0:
                    if dif_hArrive_hCourante <= 1 or dif_tVoulu_tAct >= 5:
                        decFinal = 1
                    else:
                        decFinal = 2

            self.memoire[-1][-2] = decFinal
        else:
            if dif_hArrive_hCourante <= 1 or dif_tVoulu_tAct >= 5:
                decFinal = exp_similaire[-2]
            else:
                decFinal = 2

            self.memoire[-1][-2] = decFinal

        return decFinal
    

# result_table[i] :
# 0: chauffage on , clime off
# 1: chauffage off , clime on
# 2: chauffage off , clime off

#temperature actuelle , temperature voulue , temperature dehors
temperature_data = [[10,23,17],[11,23,18],[11,23,19],[12,23,19],[12,23,19],[13,23,19],[14,23,19],[15,23,19],[17,23,19],[20,23,19],
                    [22,23,19],[23,23,19],[22,23,19],[22,23,20]]
# agenda va donner l'heure courante et l'heure de l'arrive de l'utilisateur
# datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31)
x = datetime.now()
y = datetime(2020,11, 12, 18, 14, 31)
agenda_utilisateur = [[x, y]]


a = Agent()

for sample in temperature_data:
    a.evaluation_experience_precedente(sample)

    res = a.decision(sample,agenda_utilisateur[0])

    # r0 = sample[0]
    print("Temperature actuelle: "+ str(sample[0])) 
    print("Temperature voulue: "+str(sample[1]))
    print("Temperature dehors: "+str(sample[2]))
    print("Temps restant: "+str(agenda_utilisateur[0][1].hour - agenda_utilisateur[0][0].hour))
    # print("Heure de l'arrive de l'utilisateur: "+str(agenda_utilisateur[0][1]))
    if res == 0:
        print("Action a faire: chauffage")
    elif res == 1:
        print("Action a faire: clime")
    elif res == 2:
        print("Action a faire: on eteint les 2")
    else:
        print("Action a faire: "+str(res))

    print("----------------------------------------------- ")



# sample = temperature_data[0]
# sample = temperature_data[1]
# sample = temperature_data[2]
# a = Agent(result_table,temperature_data[0], agenda_utilisateur)