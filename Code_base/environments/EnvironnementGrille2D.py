
import random
from environments.Environment import Environment
import time

#On numerote la grille par ordre croissant de gauche a droite puis de haut en bas 

class EnvironnementGrille2D(Environment):

    GAUCHE = 0
    DROITE = 1
    HAUT = 2
    BAS = 3

    def __init__(self,params):
        
        # En 2D, il y a ligne*colonne cases
        self.num_states = int(params['ligne'])* int(params['colonne'])

        # Check if there are enough cells 
        assert self.num_states>1, "Number of cells must be 2 or larger"
        
        # Number of actions is always 4 (GAUCHE, DROITE, HAUT, BAS)
        self.num_actions = 4 
  
        # Set to most right cell (will change in reset(...) anyway)
        self.current_state  =  1

        # end state
        self.terminal_state = 1 # arbitrary

        #Nombre de lignes
        self.l = int(params['ligne'])
        #Nombre de colonnes
        self.c = int(params['colonne'])
        #On regarde si l et c sont > 1:
        assert self.l>1, "On doit avoir plus d'une ligne"
        assert self.c>1, "On doit avoir plus d'une colonne"
        
        self.viewer = None


    def step(self, action):
        """See documentation in the base class"""
        
        c = self.c
        l = self.l 
        
        # Decrease agent_cell by 1 if you go left, but only if you are not
        # in the left-most cell already
        # Dans la grille definie plus haut, on ne peut pas aller a gauche si le numero de la case est egal a k*colonne+1 (k entier)
        if action==EnvironnementGrille2D.GAUCHE:
            if self.current_state % c != 1 :
                self.current_state -= 1

        # Increase agent_cell by 1 if you go right, but only if you are not
        # in the right-most cell already
        # Dans la grille definie plus haut, on ne peut pas aller a droite si le numero de la case est agal a k*colonne (k entier)
        if action==EnvironnementGrille2D.DROITE:     
            if (self.current_state % c) != 0:
                self.current_state += 1
                
        # Pour aller en haut dans la grille, on enleve au numero de la case le nombre colonne
        # On ne peut pas aller en haut si le numero de la case est inferieur ou egal au nombre colonne
        if action==EnvironnementGrille2D.HAUT:     
            if self.current_state > c:
                self.current_state -= c
        
        # Pour aller en bas dans la grille, on ajoute au numero de la case le nombre colonne
        # On ne peut pas aller en bas si le numero de la case est superieur strictement a (l-1)*c
        if action==EnvironnementGrille2D.BAS:     
            if self.current_state < c+(l-1):
                self.current_state += c

        is_done = self.current_state == self.terminal_state
       
        if is_done:
            # If you are in the terminal state, you've found the exit: reward!
            reward = 100
        else:
            # Still wandering around: -1 penalty for each move
            reward = -1
  
        next_state = self.current_state
      
        return [next_state,reward,is_done]
        

    def reset(self):
        """See documentation in the base class"""

        # Put agent at random position (but not in a terminal state)
        cell = random.randint(1,self.num_states)
        while cell == self.terminal_state:
            cell = random.randint(1,self.num_states)
        self.current_state = cell
        
        # Return first observed state
        return self.current_state


    def render(self):
        screen_width = 500
        screen_height = 500
        cell_width = screen_width / self.c
        cell_height = screen_height / self.l

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)

            l,r,t,b = 0, cell_width, cell_height, 0
            cell = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
            cell.set_color(0,0,1) # blue for current state
            end = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
            end.set_color(1,0,0) # red for end state (note : end state is 0)
            self.viewer.add_geom(end)
            self.celltrans = rendering.Transform()
            cell.add_attr(self.celltrans)
            self.viewer.add_geom(cell)

        if self.current_state is None: return None

        state = self.current_state
        cellx = ((state-1)%self.c)*cell_width
        celly = ((state-1)/self.l)*cell_height
        self.celltrans.set_translation(cellx,celly)
        
        time.sleep(0.1)


        return self.viewer.render()


    def close(self):
        if self.viewer: self.viewer.close()
