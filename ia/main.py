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

    for x in range(10):
        outcome = 0
        change = False
        print("change")
        count = 0
        _contexte = [environment.get_tInt(),environment.get_tVoulue(),environment.get_tExt()]
        agent.addcontexte(_contexte)
        while abs(environment.get_tInt() - environment.get_tVoulue()) > 0:

            action = agent.action(outcome)
            outcome = environment.outcome(action)
            print(" Action: " + traduction(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)
                  + ", Satisfaction: " + str(agent.satisfaction(outcome)))
            print(" TEMP "+str(environment.get_tInt()) +" ("+ str(environment.get_lastdiff() - environment.get_diff())+")" )
            count +=1
            if environment.update():
                change = True
                break
        if change == False:
             agent.savebestactions()
             new_temp = input('Entrer la nouvelle temperature2:')
             environment.set_tVoulue(int(new_temp))

        environment.set_lastTemp(environment.get_tInt())


        print("Nombres d'actions pour finir : "+ str(count))
good_anticipe_count = 0

e = Environment(19,21,18)
e2 = Environment(28,21,17)
e3 = Environment(28,21,17)
e1 = Environment(19,26,18)
hedonist_table2=[[2,-2],[2,-2],[3,-1]]


a = Agent(hedonist_table2, 4)



world(a, e)
print(" |||||||||||||||||||| DEUXIEME ITERATION |||||||||||||")
#world(a, e2)
print(" |||||||||||||||||||| TROISIEME ITERATION |||||||||||||")
#world(a,e1)
print(" |||||||||||||||||||| QUATRIEME ITERATION |||||||||||||")
# PAS OUBLIER DE REMETTRE C DEUX VALEURS COMME DE BASE QUAND ON UPDATE LENVIRONNEMENT
#e2.lastTemp =0
#e2.temperatureInterieur = 28
#world(a, e2)