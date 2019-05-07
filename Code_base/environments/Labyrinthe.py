import random
from environments.Environment import Environment
import time

class Labyrinthe(Environment):

    GAUCHE = 0
    DROITE = 1
    HAUT=2
    BAS=3

    def __init__(self,params):
        
        self.l=int(params['ligne'])
        self.c=int(params['colonne'])
        l=self.l
        c=self.c

        self.num_states = l * c


        self.obstacle=[8, 10 ,15 ,20 ,23 ,27 ,28 ,29 ,30 ,31 ,37 ,40 ,42 ,44 ,45 ,48 ,56 ,60 ,67,73 ,75, 81 ,83 ,84 ,85 ,88 ,89 ,90 ,91 ,92 ,93 ,94 ,95 ,96 ,98 ,101,102,103,105, 106,110, 111, 113, 123, 124, 128, 131, 135, 138, 140, 141, 142, 143, 145, 146, 147, 148, 153, 156, 157, 158, 159, 160, 161, 163, 166, 168, 170, 173, 175, 176, 178, 179, 181, 188, 190, 191, 195, 196, 206, 208, 209, 210, 213, 216, 218, 221, 223, 224, 227, 228, 229, 230, 231, 233, 236, 238, 239, 241, 243, 246, 249, 256, 258, 262, 268, 269, 271, 272, 274, 276, 277, 279, 281, 283, 290, 293, 296, 304, 306, 308, 309, 310, 311, 312, 313, 314, 317, 318, 321, 323, 324, 327, 333, 340, 345, 346, 352, 353, 354, 355, 356, 358, 360, 371, 374, 375, 383, 385, 386, 387, 388, 389 , 390, 391, 392, 393, 399, 401, 402, 406, 410, 414, 416, 421, 427, 428, 431, 435, 437, 439, 441, 444, 447, 448, 449, 450, 452, 455, 456, 457, 458, 459, 460, 462, 466, 467, 469, 474, 477, 478 , 485, 487, 489,  491, 494, 499, 502, 505, 507, 512, 514, 518, 519, 520, 521, 524, 527, 529, 530, 533, 539, 546, 557, 560, 563, 564, 565, 566, 567, 568, 569, 571, 572, 574, 576, 577, 578, 579, 580, 582, 584, 585, 586, 593, 596, 607, 611, 613, 614, 615, 621, 624]


    
        # Check if there are enough cells 
        assert self.num_states>1, "Number of cells must be 2 or larger"
        
        # Number of actions is always 4 (GAUCHE DROITE HAUT BAS)
        self.num_actions = 4
  
        # Set to most right cell (will change in reset(...) anyway)
        self.current_state  =  1

        # end state
        self.terminal_state = 1 # arbitrary

        self.viewer = None


    def step(self, action):
        """See documentation in the base class"""
        
        l=self.l
        c=self.c
        
        cogne=False      #indique si l'agent se cogne contre un obstacle
         
        if action==Labyrinthe.GAUCHE:      
            if self.current_state % c != 1:      # si l agent n'est pas sur le bord gauche de labyrinthe
                if self.current_state-1 in self.obstacle:
                    cogne=True
                else:
                    self.current_state -= 1
            else:
                cogne=True


        if action==Labyrinthe.DROITE:     
            if (self.current_state % c) != 0:     # si l agent n'est pas sur le bord droit du labyrinthe
                if self.current_state+1 in self.obstacle:
                    cogne=True
                else:
                    self.current_state += 1
            else:
                cogne=True


        if action==Labyrinthe.HAUT:     
            if self.current_state > c:     # si l agent n'est pas sur le bord haut du labyrinthe
                if self.current_state-c in self.obstacle:
                    cogne=True
                else:
                    self.current_state -= c
            else:
                cogne=True
                
                
        if action==Labyrinthe.BAS:     
            if self.current_state <= (l-1)*c:     # si l agent n'est pas sur le bord bas du labyrinthe
                if self.current_state + c  in self.obstacle:
                    cogne=True
                else:
                    self.current_state += c 
            else:
                cogne=True






        is_done = self.current_state == self.terminal_state
       
        if is_done:
            # If you are in the terminal state, you've found the exit: reward!
            reward = 250
        elif cogne:
            reward=-10
        else:
            # Still wandering around: -1 penalty for each move
            reward = -1
  
        next_state = self.current_state
      
        return [next_state,reward,is_done]
        

    def reset(self):
        """See documentation in the base class"""
        l=self.l
        c=self.c

        # Put agent at random position (but not in a terminal state)
        cell = random.randint(1,self.num_states)
        while cell == self.terminal_state:
            cell = random.randint(1,self.num_states)
        self.current_state = cell
        
        # Return first observed state
        return self.current_state


    def render(self):
        l=self.l
        c=self.c
        
        screen_width = 1000
        screen_height = 1000
        cell_width = screen_width / c
        cell_height = screen_height/l

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
                oby=((o-1)//self.l)*cell_height
                ob= rendering.FilledPolygon([(l+obx,b+oby), (l+obx,t+oby), (r+obx,t+oby), (r+obx,b+oby)])
                ob.set_color(0,0,0) # black pour obstacle
                self.viewer.add_geom(ob)


                        

        if self.current_state is None: return None

        state = self.current_state
        cellx = ((state-1)%self.c)*cell_width
        celly=((state-1)//self.l)*cell_height
        self.celltrans.set_translation(cellx,celly)
        
        time.sleep(0.1)


        return self.viewer.render()


    def close(self):
        if self.viewer: self.viewer.close()