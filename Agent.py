#imports a finite state class 
#import the children class from their general class Base

from FiniteMachineState import FiniteMachineState
from Base import GoHomeAndSleepUntilRestedState, GoToTheBankAndDepositMoneyState, GoToWorkPlaceAndMakeMoneyState, SatisfyHungerState

#creates an instance agent, who is an employee of type FiniteMachineClass
agent = FiniteMachineState()

# declaies a list of transitions that a agent can go to base on the conditions 
transitions = {
    '1': GoHomeAndSleepUntilRestedState(agent),
    '2': GoToTheBankAndDepositMoneyState(agent),
    '3': GoToWorkPlaceAndMakeMoneyState(agent),
    '4': SatisfyHungerState(agent),
    'q': None # terminates the console program
}

#a while loop to keep the program running until user decides to stop it
while True:

    #prints the state that the agent is in 
    print("\nCurrent State:")

    agent.output_status()
    #displays the transitions that the agent can go to from the current transition
    print("Available Transitions:")
    transitions = agent.get_available_transitions()
    #checks user input if holds to the conditions below
    for key, value in transitions.items():
        if value:
            print(key, ": ", type(value).__name__)
    #prompt the user to enter a transition 
    user_input = input("Enter a transition key or \" q\" to quit: ")
    
    #kills the program if "q" is entered
    if user_input == 'q':
        break
    #transition to specified state if user input holds
    elif user_input in transitions:
        new_state = transitions[user_input]
        if new_state:
            agent.set_state(new_state)
#end of the Agent 



#end of this class