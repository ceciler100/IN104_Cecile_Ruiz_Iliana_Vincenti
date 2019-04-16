
import random
from environments.Environment import Environment
import time

#On numerote la grille par ordre croissant des etats de gauche a droite puis de haut en bas 
#Cette grille contient des obstacles. Un obstacle est represente par une case noire: cet etat est inaccessible par l'agent

class EnvironnementGrille2DObs(Environment):

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
        
        c = self.c
        l = self.l
        
        #Liste des obstacles: un obstacle occupe un etat= (ligne-1)*c+colonne
        self.obstacle=[(int(2*l/10)-1)*c+1, (int(2*l/10)-1)*c+2, (int(2*l/10)-1)*c+3, (int(l/3)-1)*c+int(c/2), (int(l/2)-1)*c+int(c/2), (int(l/2)-1)*c+int(c/2)+1, (int(l/2)-1)*c+int(c/2)+2]
        for i in range (int(l/3), 2*int(l/3)):
            self.obstacle += [(i-1)*c+int(c/2)]

        
        self.viewer = None


    def step(self, action):
        """See documentation in the base class"""
        
        c = self.c
        l = self.l 
        
        #Variable qui indique si l'agent s'est cogne ou non
        cogne=False
        
        # Decrease agent_cell by 1 if you go left, but only if you are not
        # in the left-most cell already
        # Dans la grille definie plus haut, on ne peut pas aller a gauche si le numero de la case est egal a k*colonne+1 (k entier)
        if action==EnvironnementGrille2DObs.GAUCHE:
            if self.current_state % c != 1 :
                if self.current_state-1 in self.obstacle:
                    cogne=True
                else:
                    self.current_state -= 1
            else:
                cogne=True                                  #L'agent s'est cogne au bord gauche

        # Increase agent_cell by 1 if you go right, but only if you are not
        # in the right-most cell already
        # Dans la grille definie plus haut, on ne peut pas aller a droite si le numero de la case est agal a k*colonne (k entier)
        if action==EnvironnementGrille2DObs.DROITE:     
            if (self.current_state % c) != 0:
                if self.current_state+1 in self.obstacle:
                    cogne=True
                else:
                    self.current_state += 1
            else:
                cogne=True                                  #L'agent s'est cogne au bord droit
                
        # Pour aller en haut dans la grille, on enleve au numero de la case le nombre colonne
        # On ne peut pas aller en haut si le numero de la case est inferieur ou egal au nombre colonne
        if action==EnvironnementGrille2DObs.HAUT:     
            if self.current_state > c:
                if self.current_state-c in self.obstacle:
                    cogne=True
                else:
                    self.current_state -= c
            else:
                cogne=True                                  #L'agent s'est cogne en haut
        
        # Pour aller en bas dans la grille, on ajoute au numero de la case le nombre colonne
        # On ne peut pas aller en bas si le numero de la case est superieur strictement a (l-1)*c
        if action==EnvironnementGrille2DObs.BAS:     
            if self.current_state < c+(l-1):
                if self.current_state+c in self.obstacle:
                    cogne=True
                else:
                    self.current_state += c
            else:
                cogne=True                                  #L'agent s'est cogne en bas

        is_done = self.current_state == self.terminal_state
       
        if is_done:
            # If you are in the terminal state, you've found the exit: reward!
            reward = 100
        elif cogne:
            #L'agent s'est cogne dans un mur
            reward = -10
        else:
            # Still wandering around: -1 penalty for each move
            reward = -1
  
        next_state = self.current_state
      
        return [next_state,reward,is_done]
        

    def reset(self):
        """See documentation in the base class"""

        # Put agent at random position (but not in a terminal state)
        cell = random.randint(1,self.num_states)
        while cell == self.terminal_state or cell in self.obstacle:
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
            for o in self.obstacle:
                obx = ((o-1)%self.c)*cell_width
                oby = ((o-1)/self.l)*cell_height
                ob = rendering.FilledPolygon([(l+obx,b+oby), (l+obx,t+oby), (r+obx,t+oby), (r+obx,b+oby)])
                ob.set_color(0,0,0) # noir pour un obstacle
                self.viewer.add_geom(ob)
                
                

        if self.current_state is None: return None

        state = self.current_state
        cellx = ((state-1)%self.c)*cell_width
        celly = ((state-1)/self.l)*cell_height
        self.celltrans.set_translation(cellx,celly)
        
        time.sleep(0.1)


        return self.viewer.render()


    def close(self):
        if self.viewer: self.viewer.close()