#imports one child class from base

from Base import GoHomeAndSleepUntilRestedState

#creates a class FiniteMachineState
class FiniteMachineState:
    #defines a method that initialise agent state to "GoHomeAndSleepUntilRestes"
    def __init__(self):
        self.state = GoHomeAndSleepUntilRestedState(self)
    #set the current state to next state
    def set_state(self, state):
        self.state = state
    #displays the state
    def output_status(self):
        self.state.output_status()
    #gets the available state from that transitioned-to state
    def get_available_transitions(self):
        return self.state.get_transitions()
#end of the finiteMachineState class