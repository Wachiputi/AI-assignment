#imports the GoHomeAndSleepUntilRestedState class
from GoHomeAndSleepUntilRestedState import GoHomeAndSleepStateUntilRestedState

#an agent class that implements the state that an agent is in, sets it to another state based on user input and display the updtaed state
class Agent:
    def __init__(self):
        self.state = GoHomeAndSleepStateUntilRestedState(self)
    
    def set_state(self, state):
        self.state = state
    
    def output_status(self):
        self.state.output_status()
#end of the agent class