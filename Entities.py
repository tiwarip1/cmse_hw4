import random
from mesa import Agent
from move_wolverine import move_wolverine
from move_spartan import move_spartan

class Wolverine(move_wolverine):
    
    def __init__(self,position,model):
        
        super().__init__(position,model)
        
    def step(self):
        '''Move the wolverine in a random direction after a given step'''
        
    def wolverine_reproduce(self):
        '''If the wolverine survives enough steps, it will stop and take a step
        to birth another wolverine in the same cell'''
        
    def old_age(self):
        '''There is a random chance the wolverine will die in this step'''

class Spartan(move_spartan):
    
    def __init__(self,position,model):
        
        super().__init__(position,model)
        
    def step(self):
        '''Dependent on how we make move_spartan, we could make it such that
        spartan will follow their food supply if it's nearly, which is a 
        good idea'''
        
    def spartan_reproduce(self):
        '''If a spartan eats enough wolverines, it will take a step to stop
        and produce another spartan in the same cell'''
        
    def kill_wolverine(self):
        '''If there is a wolverine nearby, there is a random chance the spartan
        will kill the wolverine and add that to the amount of food it has'''
        
    def amount_food_eaten(self):
        '''Returns the amount of food the spartan has eaten since its last
        reproduction cycle'''
        
    def old_age(self):
        '''There is a random chance the spartan will die in this step'''