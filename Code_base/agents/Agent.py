__author__ = "Florence Carton"
__credits__ = ["Florence Carton", "Freek Stulp", "Antonin Raffin"]

class Agent:
    """ The interface an agent should conform to
    """
    
    def __init__(self, params):
        """Initializes a new agent.
        Args:
            num_states (int): Number of possible states the agent can make
            num_actions (int): Number of possible action the agent can perform
        """        

        self.num_states = params['num_states']
        self.num_actions = params['num_actions'] 

    def start(self, initial_state):
        """Start an episode with state 'initial_state', return first action
        Args: 
            initial_state (int): The first states the agent makes
        Returns:
            The first action the agent performs
        """
        raise NotImplementedError('subclasses must override agentStart()!')

    def step(self, reward, state):
        """One step of the agent in the reinforcement learning loop.
            
        Usually, this function will do two things:
        1) Use the reward to update values
        2) Call the agent's policy to determine the next action, given 
           the state
           
        Args: 
            reward (float): The reward recieved for performing the previous
                action in the previous state
            state : The state at the current time step
        Returns:
            The action returned for the state at the current time step
        """
        raise NotImplementedError('subclasses must override agentStep()!')

    def policy(self, state):
        """The policy of an agent.
        
        In reinforcement learning, the policy returns an action, given the
        current state.
        
        Args: 
            state : The state the agent is in.
        Returns:
            The action (int) the agent performs.
        """
        raise NotImplementedError('subclasses must override agentPolicy()!')