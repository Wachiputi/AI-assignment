#imports all child classes of the base class State into Employee
from Agent import Agent
from GoHomeAndSleepUntilRestedState import GoHomeAndSleepStateUntilRestedState
from GoToTheBankAndDepositMoneyState import GoToTheBankAndDepositMoneyState
from GoToWorkPlaceAndMakeMoneyState import GoToWorkplaceAndMakeMoneyState
from SatisfyHungerState import SatisfyHungerState

#create an object "agent" of type Agent fro Agent class
agent = Agent()
# A list of transitions from which a user is prompted to chose from in order to make transitions
options = {
    '1': GoHomeAndSleepStateUntilRestedState(agent),
    '2': GoToTheBankAndDepositMoneyState(agent),
    '3': GoToWorkplaceAndMakeMoneyState(agent),
    '4': SatisfyHungerState(agent),
    'q': None #exits the execution when entered
}
# a while loop to keep the program executing until exit key is entered
while True:
    #displays the current state the user is at
    print("\nCurrent State:")
    #a function call to a method where transitions are implemented
    agent.output_status()

    print("Available Transitions:")
    # a for loop that checks if user input holds
    for key, value in options.items():
        if value:
            print(key, ": ", type(value).__name__)
    #prompt the user to enter transition
    user_input = input("Enter a transition key: ")
    #an if statement that checks user input and quit the program if the user enters a symbol "q"
    if user_input == 'q':
        break
    #checks if the user if within the range of options define above, if yes, it update the transition to the selected
    elif user_input in options:
        new_state = options[user_input]
        if new_state:
            agent.set_state(new_state)

#end of this class