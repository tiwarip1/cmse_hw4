import random
from mesa import Agent,Model
from random_walk import random_walk

class Wolverine(random_walk):
    
    def __init__(self,position=(0,0),model=Model,food=0):
        
        super().__init__(position,model)
        self.pos = position
        self.food = food
        self.alive = True
        self.moore = True
        
    def step(self):
        '''Move the wolverine in a random direction after a given step and do
        some things that step would require, like food and death'''
        self.food_function()
        self.old_age()
        self.random_move()
        #It should be noted that once the self.alive=False, the wolverine will
        #be killed in the next step, not the current step, but they can die 
        #from old age in the current step
        if not self.alive:
            self.wolverine_killed()
            
        if self.food>3:
            self.wolverine_reproduce()
        
    def wolverine_reproduce(self):
        '''If the wolverine survives enough steps, it will stop and take a step
        to birth another wolverine in the same cell'''
        self.food = self.food/2
        cub = Wolverine(self.pos, self.model)
        self.model.grid.place_agent(cub, cub.pos)
        self.model.schedule.add(cub)
        print("A wolverine was born")
        
    def food_function(self):
        '''The wolverine will keep having food and will add to it each
        iteration'''
        self.food+=1
        
    def wolverine_killed(self):
        '''Gets rid of the Wolverine from the grid'''
        self.model.grid._remove_agent(self.pos,self)
        self.model.schedule.remove(self)
        
    def old_age(self):
        '''There is a random chance the wolverine will die in this step'''
        is_alive = random.uniform(0,100)
        if is_alive>95:
            self.alive = False
            print("wolverine died of old age")
            
    def name(self):
        '''This is just here to identify what type of object this is'''
        return "Wolverine"
    
    def food_contents(self):
        '''This is here to tell how much food the spartan gets for killing the
        wolverine'''
        return self.food

class Spartan(random_walk):
    
    def __init__(self,position=(0,0),model=Model,food=0):
        
        super().__init__(position,model)
        self.pos = position
        self.moore = True
        self.food = food
        self.alive = True
        
    def step(self):
        '''If there is a wolverine nearby, it will choose a random one and
        chase after it, if there is nothing nearby, it will move in a random
        direction'''
        self.old_age()
        self.random_move()
        if not self.alive:
            self.spartan_killed()
            
        if self.food>1:
            self.spartan_reproduce()
            
    def spartan_killed(self):
        '''Gets rid of spartan from the grid'''
        self.model.grid._remove_agent(self.pos,self)
        self.model.schedule.remove(self)
        
    def food_function(self):
        '''If a spartan eats a wolverine, its food will increase'''
        self.food+=1
        
    def add_food_from_kill(self,eaten_food):
        '''This is here so that '''
        self.food+=eaten_food
        
    def spartan_reproduce(self):
        '''If a spartan eats enough wolverines, it will take a step to stop
        and produce another spartan in the same cell'''
        self.food = self.food/2
        cub = Spartan(self.pos, self.model)
        self.model.grid.place_agent(cub, cub.pos)
        self.model.schedule.add(cub)
        print("A Spartan was born")
        
    def kill_wolverine(self):
        '''If there is a wolverine nearby, there is a random chance the spartan
        will kill the wolverine and add that to the amount of food it has'''
        chance_kill = random.uniform(0,100)
        killed = False
        if chance_kill<75:
            self.food_function()
            killed = True
            
        return killed
        
    def old_age(self):
        '''There is a random chance the spartan will die in this step'''
        is_alive = random.uniform(0,100)
        if is_alive>95:
            self.alive = False
            print("spartan died of old age")
        
    def name(self):
        '''This is just here to identify what type of object this is'''
        return "Spartan"
