import random
from Agent import Agent
import numpy as np



##
#Notre troisieme Agent qui va apprendre de ses erreurs, adapte pour la grille 2D
def position_max (Q, state):
    """Retourne la position du maximum de Q a la ligne state"""
    [a,b] = np.shape(Q)
    M = Q[state-1, 0]
    pm =[0]
    for j in range (1,b):
        if Q[state-1, j] > M:
            M = Q[state-1, j]
            pm=[j]
        elif Q[state-1,j] ==M:
            pm.append(j)
    pr=random.choice(pm)
    return (pr)
    
def valeur_max(Q, state):
    """Retourne le maximum de Q a la ligne state"""
    [a,b] = np.shape(Q)
    M = Q[state-1, 0]
    for j in range (1,b):
        if Q[state-1, j] > M:
            M = Q[state-1, j]
    return (M)


def parcouru(state, action, liste):
    """renvoi vrai si la liste contient deja (state , action, ---) """
    for[e,a ,r] in liste:
        if e == state and a == action :
            return True
    return False
    
    
def moy(parcours , ns ,na):
    Q=np.zeros((ns,na))
    for i in range(ns):
        for j in range(na):
            n=len(parcours[i][j])
            m=0
            for k in range(n):
                m += (parcours[i][j][k]) 
            Q[i ,j]=m
    return Q
            
    
    
    
    
##

class Agent003(Agent):
#Qlearning monte carlo

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        
        self.l=int(params['ligne'])
        self.c=int(params['colonne'])
        
        #strategie initiale (au depart l'agent ne connait pas les deplacements optimaux a effectuer)
        #tableau de taille nombre d'etat * nombre d'actions possibles
        self.Q = np.zeros((self.l * self.c,4))
        
        
        self.Parcours=(self.c*self.l)*[4*[[]]]           #liste des recompenses obtenues
        
        #Probabilite d'exploration
        self.exploration = 0.05
        
        
        self.listeParcours=[]          #liste du parcours de l'episode
        
    def start(self, initial_state):
        """See documentation in the base class"""
        self.listeParcours=[]                         #on reinitialise la liste du parcours a chaque debut d'episode
        action = self.policy(initial_state)
        return action


    def step(self, reward, state, ancien_state, action):
        """See documentation in the base class"""
        
        p=parcouru(state , action ,self.listeParcours)
        if not p :
            self.listeParcours.append([state,action,0])
            
        for [e,a,r] in self.listeParcours:
            r += reward
        

        action = self.policy(state)
        
        # if reward == 100:  #fin de l'episode
        #     for [e,a ,r ] in self.listeParcours:
        #         self.Parcours[e][a].append(r)
        #         
        #     self.Q=moy(self.Parcours , self.c*self.l ,4)
        #         
                
        
        return action
        
    def fin():
        for [e,a ,r ] in self.listeParcours:
            self.Parcours[e][a].append(r)
            
        self.Q=moy(self.Parcours , self.c*self.l ,4)
        
      
        
    def policy(self, state):
        """See documentation in the base class"""
        #On determine si l'agent explore ou choisit le choix optimal
        r = random.random()
        
        if r < self.exploration :                       # Exploration
            return random.randint(0,self.num_actions-1) # Returns a random action
        else :                                          # Choix optimal
            return position_max(self.Q, state)
