
import random
from agents.Agent import Agent
import numpy as np



##
#Notre premier Agent qui va apprendre de ses erreurs, adapte pour la grille 1D
def position_max (Q, state):
    """Retourne la position du maximum de Q a la ligne state"""
    [a,b] = np.shape(Q)
    M = Q[state, 0]
    pm = 0
    for j in range (1,b):
        if Q[state, j] > M:
            M = Q[state, j]
            pm=j
    return (pm)
    
def valeur_max(Q, state):
    """Retourne le maximum de Q a la ligne state"""
    [a,b] = np.shape(Q)
    M = Q[state, 0]
    for j in range (1,b):
        if Q[state, j] > M:
            M = Q[state, j]
    return (M)

##

class Agent001(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        
        #strategie initiale (au depart l'agent ne connait pas les deplacements optimaux a effectuer)
        #tableau de taille nombre d'etat * nombre d'actions possibles
        self.Q = np.zeros((int(params['num_cells_grid1D']),2))
        
        #Probabilite d'exploration
        self.exploration = 0.05
        
        
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        return action


    def step(self, reward, state, ancien_state, action):
        """See documentation in the base class"""
        
        self.Q [ancien_state, action] = self.Q [ancien_state, action] + reward + valeur_max(self.Q, state) - self.Q[ancien_state, action]

        action = self.policy(state)
        return action
    
    def fin(self, total_reward):
        pass
      
        
    def policy(self, state):
        """See documentation in the base class"""
        #On determine si l'agent explore ou choisit le choix optimal
        r = random.random()
        
        if r < self.exploration :                       # Exploration
            return random.randint(0,self.num_actions-1) # Returns a random action
        else :                                          # Choix optimal
            return position_max(self.Q, state)

        
        
        
        
        
        