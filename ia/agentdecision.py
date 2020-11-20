import random


class Agent:
    def __init__(self, _hedonist_table, bored_limit):
        """ Creating our agent """
        self.hedonist_table = _hedonist_table
        self._action = 2
        self.anticipated_outcome = 0
        self.contexte= [0,0,0]
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

        
            

        self._action = self.action_pref

        if self.is_board() or self.hedonist_table[self._action][outcome]<0:
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
        self.good_anticipe_count = 0
        self.pref_action_count = 0
        self.action_pref = self._action
        self.outcome_pref = outcome
        if self._action == 2 :
            self._action = random.randint(0, 1)
        else :
            if self.hedonist_table[self._action][outcome] > 0 :
                self._action = 2
            else :
                if self._action == 0 :
                    random.randint(1,2)
                if  self._action == 1 :
                        while self._action == 1:
                            random.randint(0,2)   
    def anticipation(self):
        self.anticipated_outcome = self.memoire[self._action]
        
        return self.anticipated_outcome

    def is_board(self):
        if self._action == 2 :
            return False
        else :    
            return self.good_anticipe_count >= self.bored_limit and self.pref_action_count >= self.bored_limit

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



class Environment2:
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
    

def traduction(action) :

    if action == 0 :
        return "0 Chauffage ON"
    elif action == 1 :
        return "1 Clim ON"
    elif action == 2 :
        return "2 All Off"        

def world(agent, environment):
    outcome = 0
    count = 0
    _contexte = [environment.temperatureInterieur,environment.temperatureVoulue,environment.temperatureExterieur]
    agent.addcontexte(_contexte)
    while abs(environment.temperatureInterieur - environment.temperatureVoulue) > 0:
        action = agent.action(outcome)
        outcome = environment.outcome(action)
        if not environment.amelioration :
            print('ACTION CHANGER')
            agent.changeaction(outcome)
            outcome = environment.outcome(action)
        print(" Action: " + traduction(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)
              + ", Satisfaction: " + str(agent.satisfaction(outcome)))
        print(" TEMP "+str(environment.temperatureInterieur) +" ("+ str(environment.lastdiff - environment.diff)+")" ) 
        count +=1  
    agent.savebestactions()
    print("Nombres d'actions pour finir : "+ str(count))
good_anticipe_count = 0
# TODO Define the hedonist values of interactions (action, outcome, outcome_souhaiter)
# Actions : 0 Chauffage , 1 Clim , 2 Rien 
# Outcome : 0 T Augmente , T Descend , T Inchanger
# Outcome souhaiter : 0 On veut que T augmente , 1 On veut que T descende
e = Environment2(19,23,18)
e2 = Environment2(28,21,17)
e3 = Environment2(28,21,17)
e1 = Environment2(19,26,18)
hedonist_table2=[[2,-2],[2,-2],[3,-1]]

# TODO Choose an agent
a = Agent(hedonist_table2, 4)
# TODO Choose an environment
#e = Environment1()

#e = Environment2()
# e = TurtleSimEnacter()

world(a, e)
print(" |||||||||||||||||||| DEUXIEME ITERATION |||||||||||||")
world(a, e2)
print(" |||||||||||||||||||| TROISIEME ITERATION |||||||||||||")
world(a,e1)
print(" |||||||||||||||||||| QUATRIEME ITERATION |||||||||||||")
# PAS OUBLIER DE REMETTRE C DEUX VALEURS COMME DE BASE QUAND ON UPDATE LENVIRONNEMENT
e2.lastTemp =0
e2.temperatureInterieur = 28
world(a, e2)