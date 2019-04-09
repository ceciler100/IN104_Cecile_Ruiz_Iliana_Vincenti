
import random
from agents.Agent import Agent
import numpy as np



##
#Notre deuxieme agent qui peut naviguer dans une grille 2D sans obstacles
def position_max (Q, state):
    """Retourne la position du maximum de Q a la ligne state"""
    [a,b] = np.shape(Q)
    M = Q[state-1, 0]
    pm=[0]
    for j in range (1,b):
        if Q[state-1, j] > M:
            M = Q[state-1, j]
            pm=[j]
        elif Q[state-1, j] == M:
            pm.append(j)
    p = random.choice(pm)
    return (p)
    
def valeur_max(Q, state):
    """Retourne le maximum de Q a la ligne state"""
    [a,b] = np.shape(Q)
    M = Q[state-1, 0]
    for j in range (1,b):
        if Q[state-1, j] > M:
            M = Q[state-1, j]
    return (M)

##

class Agent002(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        
        #Nombre de lignes
        self.l = int(params['ligne'])
        #Nombre de colonnes
        self.c = int(params['colonne'])
        
        #strategie initiale (au depart l'agent ne connait pas les deplacements optimaux a effectuer)
        #tableau de taille nombre d'etat * nombre d'actions possibles
        self.Q = np.zeros((self.c*self.l,4))
        
        #Probabilite d'exploration
        self.exploration = 0.05
        
        
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        return action


    def step(self, reward, state, ancien_state, action):
        """See documentation in the base class"""
        
        self.Q [ancien_state-1, action] = self.Q [ancien_state-1, action] + reward + valeur_max(self.Q, state) - self.Q[ancien_state-1, action]

        action = self.policy(state)
        return action
      
        
    def policy(self, state):
        """See documentation in the base class"""
        #On determine si l'agent explore ou choisit le choix optimal
        r = random.random()
        
        if r < self.exploration :                       # Exploration
            return random.randint(0,self.num_actions-1) # Returns a random action
        else :                                          # Choix optimal
            return position_max(self.Q, state)
            
            
            
            
            
            