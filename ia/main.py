from environnement import Environment
from ia import Agent


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
e = Environment(19,23,18)
e2 = Environment(28,21,17)
e3 = Environment(28,21,17)
e1 = Environment(19,26,18)
hedonist_table2=[[2,-2],[2,-2],[3,-1]]

# TODO Choose an agent
a = Agent(hedonist_table2, 4)
# TODO Choose an environment
#e = Environment1()

#e = Environment()
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