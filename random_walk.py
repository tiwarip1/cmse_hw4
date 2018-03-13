import random
from mesa import Agent

class random_walk(Agent):
    
    def __init__(self,position,model):
        
        super().__init__(position,model)
        self.position = position
        
    def random_move(self):
        '''
        Step one cell in any allowable direction.
        '''
        # Pick the next cell from the adjacent cells.
        next_moves = self.model.grid.get_neighborhood(self.pos, self.moore, True)
        next_move = random.choice(next_moves)
        # Now move:
        self.model.grid.move_agent(self, next_move)