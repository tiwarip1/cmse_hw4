import random
import numpy as np
import matplotlib.pyplot as plt

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from Entities import Spartan,Wolverine

class board(Model):
    
    def __init__(self,num_wolverines,num_spartans,height = 40, width = 40):
        
        self.num_wolverines = num_wolverines
        self.num_spartans = num_spartans
        self.height = height
        self.width = width
        
        self.grid = MultiGrid(self.height, self.width,torus = True)
        self.schedule = RandomActivation(self)
        
        for i in range(self.num_wolverines):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            wolverine = Wolverine([x, y], self)
            self.grid.place_agent(wolverine, (x, y))
            self.schedule.add(wolverine)

        # Create wolves
        for i in range(self.num_spartans):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            spartan = Spartan([x, y], self)
            self.grid.place_agent(spartan, (x, y))
            self.schedule.add(spartan)
            
        self.running = True
        
        
# =============================================================================
# This is here to make sure the model works by making a colormap of it
# model = board(20,20,10,10)
# agent_counts = np.zeros((model.grid.width, model.grid.height))
# for cell in model.grid.coord_iter():
#     cell_content, x, y = cell
#     agent_count = len(cell_content)
#     agent_counts[x][y] = agent_count
# plt.imshow(agent_counts, interpolation='nearest')
# plt.colorbar()
# 
# plt.show()
# =============================================================================
