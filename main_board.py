import random
import numpy as np
import matplotlib.pyplot as plt

from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid,Grid
from Entities import Spartan,Wolverine

'''
This model is derived from the scripts in the wolf-sheep model in the mesa
examples, but has been heavily modified, so we did do something
'''

class board(Model):
    
    def __init__(self,num_wolverines,num_spartans,height = 40, width = 40):
        '''Initializes the board and randomly puts spartans and wolverines in
        the board. This uses a multigrid and rolling boundary conditions'''
        self.num_wolverines = num_wolverines
        self.num_spartans = num_spartans
        self.height = height
        self.width = width
        
        self.grid = MultiGrid(self.height, self.width,torus = True)
        self.schedule = RandomActivation(self)
        
        #Creates Wolverines
        for i in range(self.num_wolverines):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            wolverine = Wolverine((x, y), self)
            self.grid.place_agent(wolverine, (x, y))
            self.schedule.add(wolverine)

        # Create Spartans
        for i in range(self.num_spartans):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            spartan = Spartan((x, y), self)
            self.grid.place_agent(spartan, (x, y))
            self.schedule.add(spartan)
            
        self.running = True
        
    def step(self):
        '''Goes through the step functions found in the agents'''
        
        self.schedule.step()
        
    def run_model(self,num_iterations):
        '''Just iterates over the step for a given number of times and shows
        the colormap, this is mostly just for testing and the final result
        should include animation'''
        
        for i in range(num_iterations):
            self.step()
            self.print_model()
            
    def print_model(self):
        '''This function prints and does some operations in the function,
        specifically it goes through each square and if a wolverine and
        spartan are in the same square, it initiates combat along with putting
        the concentration of entities on a colormap, which is from my
        jupyter notebook'''
        agent_counts = np.zeros((self.grid.width, self.grid.height))
        self.total_count = 0
        for cell in self.grid.coord_iter():
            cell_content, x, y = cell
            self.total_count+=len(cell_content)
            cell_cont = list(cell_content)
            #This is statement goes through each cell and sees if there is a 
            #spartan and wolverine in the same square, then initiates combat
            if cell_cont!=[]:
                #Have the class objects return their name and if it meets the 
                #criteria, moves to combat
                if any(x.name() == "Spartan" for x in cell_cont) and \
                any(x.name() == "Wolverine" for x in cell_cont):
                    killed = False
                    for j in cell_content:
                        if j.name()=="Spartan":
                            killed = j.kill_wolverine()
                            break
                    if killed:
                        for i in cell_content:
                            if i.name() == "Wolverine":
                                j.add_food_from_kill(i.food_contents())
                                i.wolverine_killed()
                                print('A wolverine has just been killed')
                                break
            agent_count = len(cell_content)
            agent_counts[x][y] = agent_count
        print(self.total_count)
        plt.imshow(agent_counts, interpolation='nearest')
        plt.colorbar()
    
        plt.show()
        
#This is here to make sure the model works by making a colormap of it
model = board(20,20,5,5)
model.run_model(5)
    
