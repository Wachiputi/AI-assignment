#imports all child classes of the base class State into Employee
import Agent
import GoHomeAndSleepUntilRestedState
import GoToTheBankAndDepositMoneyState
import GoToWorkPlaceAndMakeMoneyState
import SatisfyHungerState


agent = Agent()

transitions = {
    '1': GoHomeAndSleepUntilRestedState(agent),
    '2': GoToTheBankAndDepositMoneyState(agent),
    '3': GoToWorkPlaceAndMakeMoneyState(agent),
    '4': SatisfyHungerState(agent),
    'q': None
}

while True:


    print("\nCurrent State:")

    agent.output_status()

    print("Available Transitions:")
    transitions = agent.get_available_transitions()
    for key, value in transitions.items():
        if value:
            print(key, ": ", type(value).__name__)

    user_input = input("Enter a transition key: ")
    
    if user_input == 'q':
        break
    elif user_input in transitions:
        new_state = transitions[user_input]
        if new_state:
            agent.set_state(new_state)




#end of this class