__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]

class Environment:

	def __init__(self):

		pass

	def step(self, action):
		"""Project environment one step into the future.
        
         Given an action, compute the reward and next state, and whether next_state is terminal
            
         Args:
             action : The action the agent is performing
             
         Returns:
			next_state : an observation of the next state 
			reward : the reward the agent receives for performing action in the current state
			is_done = if the next_state is a terminal state
        """

		raise NotImplementedError('subclasses must override step()!')

	def render(self):
		""" Display the environment 
		"""

		raise NotImplementedError('subclasses must override render()!')


	def reset(self):
		"""Reset the environment.
        
         Args:
             
             
         Returns:
			first_state : the first state
        """
		raise NotImplementedError('subclasses must override render()!')


	def close(self):
		""" Close the environment 
		"""
		raise NotImplementedError('subclasses must override close()!')