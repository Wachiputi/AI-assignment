#imports base class States
from State import State
#creates a child class that inherits from State
class SatisfyHungerState(State):
    #defines a method that states where the agent is at an instance
    def output_status(self):
        print("I`m at the Restaurant, satisfying hunger")
