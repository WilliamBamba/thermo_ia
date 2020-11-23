from environnement import Environment
from ia import Agent



def objectif_atteint(e) :

        if e.get_lastTemp() < e.get_tVoulue() and e.get_tInt() >= e.get_tVoulue():
            return True
        if e.get_lastTemp() < e.get_tVoulue() and e.get_tInt() >= e.get_tVoulue():
            return True
        else: return False


def world(agent, environment, outcome):

    # AJOUTER LE CONTEXTE A LA CREATION DE L'AGENT


    count = 0
    if e.changeTvoulue == True :
         print("change")
         _contexte = [environment.get_tInt(),environment.get_tVoulue(),environment.get_tExt()]
         agent.addcontexte(_contexte)
    agent.searchSemblable()  #
    action = agent.action(outcome)
    print("Action choisie : "+ str(action))
    if objectif_atteint(environment) :
        print("Objectif atteint")
        agent.savebestactions()
        action = 2
    outcome = environment.outcome(action)
    # print(" Action: " + traduction(action) + ", Anticipation: " + str(agent.anticipation()) + ", Outcome: " + str(outcome)              + ", Satisfaction: " + str(agent.satisfaction(outcome)))
    # print(" TEMP "+str(environment.get_tInt()) +" ("+ str(environment.get_lastdiff() - environment.get_diff())+")" )
    count +=1

         #  new_temp = input('Entrer la nouvelle temperature2:')
         #  environment.set_tVoulue(int(new_temp))

    action_outcome =[action,outcome]

    return action_outcome



    print("Nombres d'actions pour finir : "+ str(count))


e = Environment(19,21,18,[1,2])
#e2 = Environment(28,21,17)
#e3 = Environment(28,21,17)
#e1 = Environment(19,26,18)
hedonist_table2=[[2,-2,-2],[2,-2,-2],[3,-1,4]]
print("hedo  :" + str(hedonist_table2[2][2]))
_contexte = [e.get_tInt(),e.get_tVoulue(),e.get_tExt()]
a = Agent(hedonist_table2, 4)
a.addcontexte(_contexte)
action_outcome = [0,0]

x='n'

while(x == 'n'):
    x = input('Quitter ?')
    print("T interieur : "+str(e.get_tInt()) + " T voulue : "+ str(e.get_tVoulue()) + " T exterieur : "+ str(e.get_tExt()) )
    action_outcome=world(a,e,action_outcome[1])
    print("L'action a effectuer : "+ str(action_outcome))
    print("T interieur : "+str(e.get_tInt()) + " T voulue : "+ str(e.get_tVoulue()) + " T exterieur : "+ str(e.get_tExt()) )
    e.update()


#world(a, e)