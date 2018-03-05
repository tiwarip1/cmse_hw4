import random
from mesa import Agent

class move_wolverine(Agent):
    
    def __init__(self,position,model):
        
        super().__init__(position,model)
        self.position = position
        
    def randomly_move(self):
        #Chooses which direciton to move using mesa
        next_moves = self.model.grid.get_neighborhood(self.position,\
                                                      moore=True,\
                                                      include_center=True)
        
        next_move = random.choice(next_moves)
        #Actually does the moving
        self.model.grid.move_agent(self, next_move)