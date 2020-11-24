from environnement import Environment
from ia import Agent


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

    print("Nombres d'actions pour finir : " + str(count))


e = Environment(19, 21, 18, [1, 2])
hedonist_table2 = [[2, -2, -2], [2, -2, -2], [3, -1, 4]]
print("hedo  :" + str(hedonist_table2[2][2]))
_contexte = [e.get_tInt(), e.get_tVoulue(), e.get_tExt()]
a = Agent(hedonist_table2, 4, e)
# a.addcontexte(_contexte)
action_outcome = [0, 0]

x = 'n'

while (x == 'n'):
    x = input('Quitter ?')
    print("T interieur : " + str(e.get_tInt()) + " T voulue : " + str(e.get_tVoulue()) + " T exterieur : " + str(
        e.get_tExt()))
    action_outcome = world(a, e, action_outcome[1])
    print("L'action a effectuer : " + str(action_outcome))
    print("T interieur : " + str(e.get_tInt()) + " T voulue : " + str(e.get_tVoulue()) + " T exterieur : " + str(
        e.get_tExt()))
