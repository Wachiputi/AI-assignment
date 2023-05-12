#imports the GoHomeAndSleepUntilRestedState class
#import GoHomeAndSleepUntilRestedState

#an agent class that implements the state that an agent is in, sets it to another state based on user input and display the updtaed state
from State import GoHomeAndSleepUntilRestedState


class Agent:
    def __init__(self):
        self.state = GoHomeAndSleepUntilRestedState(self)
    
    def set_state(self, state):
        self.state = state
    
    def output_status(self):
        self.state.output_status()

    def get_available_transitions(self):
        return self.state.get_transitions()
#end of the agent class