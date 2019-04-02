__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]

import random
from agents.Agent import Agent


class AgentRandom(Agent):

    def __init__(self, params):
        """See documentation in the base class"""
        Agent.__init__(self, params)
        
    def start(self, initial_state):
        """See documentation in the base class"""

        action = self.policy(initial_state)
        return action

    def step(self, reward, state):
        """See documentation in the base class"""

        action = self.policy(state)
        return action
        
    def policy(self, state):
        """See documentation in the base class"""

        return random.randint(0,self.num_actions-1) # Returns a random action
