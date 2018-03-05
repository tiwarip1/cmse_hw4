import random
from mesa import Agent

class move_spartan(Agent):
    
    def __init__(self,position,model):
        
        super().__init__(position,model)
        self.position = position
        
    def directed_move(self):
        '''If there is a wolverine nearby, it will choose a random one and
        chase after it, if there is nothing nearby, it will move in a random
        direction'''