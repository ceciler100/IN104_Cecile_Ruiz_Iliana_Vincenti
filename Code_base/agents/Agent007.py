import random
from agents.Agent import Agent
import numpy as np



## fonctions utilisees dans les choix d'actions de l'agent


def position_max (Q, state):
    """Retourne la position du maximum de Q a la ligne state"""
    [a,b] = np.shape(Q)
    M = Q[state-1, 0]         #maximum
    pm =[0]                   #liste des positions du maximum
    for j in range (1,b):
        if Q[state-1, j] > M:
            M = Q[state-1, j]
            pm=[j]
        elif Q[state-1,j] ==M:
            pm.append(j)
    pr=random.choice(pm)      #si les actions sont equivalentes on en choisit une au hasard (position retournee)
    return (pr)
    
def valeur_max(Q, state):
    """Retourne le maximum de Q a la ligne state"""
    [a,b] = np.shape(Q)
    M = Q[state-1, 0]         #maximum
    for j in range (1,b):
        if Q[state-1, j] > M:
            M = Q[state-1, j]
    return (M)

## Notre 7eme Agent: apte pour les grilles 2D ,Q-learning , parametre alpha et gamma optimises , coefficient d' exploration variable en fonction de la recompense finale

class Agent007(Agent):

    def __init__(self, params):
        """initialisation de l'agent"""
        
        Agent.__init__(self, params)
        
        self.l=int(params['ligne'])
        self.c=int(params['colonne'])
        
        #strategie initiale (au depart l'agent ne connait pas les deplacements optimaux a effectuer)
        #tableau de taille nombre d'etat * nombre d'actions possibles
        self.Q = np.zeros((self.l * self.c,4))
        
        #Probabilite d'exploration
        self.exploration = 0.05
        
        
        self.alpha=0.6         #coefficient optimises
        self.gamma=1          


        
    def start(self, initial_state):
        """choisit la premiere action"""

        action = self.policy(initial_state)
        return action


    def step(self, reward, state, ancien_state, action):
        """calcule la prochaine action en fonction des differents parametres"""
        
        self.Q [ancien_state-1, action] = self.Q [ancien_state-1, action] + self.alpha*( reward + self.gamma*valeur_max(self.Q, state) - self.Q[ancien_state-1, action])

        action = self.policy(state)
        return action
        
    def fin(self,total_reward):
        #a la fin de l'episode on modifie le coefficient d'eploration en fonction de la recompense finale
        if total_reward < 50:
            self.exploration=0.08      #si la recompense est faible on doit s'ameliorer et donc explorer beaucoup
        elif total_reward < 0.04:
            self.exploration=0.04
        else :
            self.exploration=0     #si la recompense est tres haute on peut arreter d'explorer, on considere qu on a trouve la solution optimale
            
 

        
    def policy(self, state):
        """methode de calcul de l'action: exploration ou 'choix optimal' """
        #On determine si l'agent explore ou choisit le choix optimal
        r = random.random()
        
        if r < self.exploration :                       # Exploration
            return random.randint(0,self.num_actions-1) # Returns a random action
        else :                                          # Choix optimal
            return position_max(self.Q, state)