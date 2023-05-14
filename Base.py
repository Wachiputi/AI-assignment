#create a base class State
class State:
    def __init__(self, agent):
        self.agent = agent

    def output_status(self):
        pass
#creates a GoHomeAndSleepUntilRestedState class that inherits from the base class State
class GoHomeAndSleepUntilRestedState(State):
    def output_status(self):
        #displays agents current location status and where they can possibly go
        print("I`m at Home, sleeping. can go to worrk if not fatigue")
    def get_transitions(self):
    #return transitions that an agent can go to
        return {
            '1':GoToWorkPlaceAndMakeMoneyState(self.agent)
        }
#creates a GoToTheBankAndDepositMoneyState class that inherit from base class State
class GoToTheBankAndDepositMoneyState(State):
    def output_status(self):
        #displays agents current location status and where they can possibly go
        print("I`m at The Bank, depositing money:\n can go home and sleep if satisfied with amount in the bank \n can go to work if not pleased with bank balance")

    def get_transitions(self):
        #return transitions that an agent can go to
        return {
            '1': GoHomeAndSleepUntilRestedState(self.agent),
            '2': GoToWorkPlaceAndMakeMoneyState(self.agent)
        }
#creates a GoToWorkPlaceandMakeMoneyState that inherits from base class State 
class GoToWorkPlaceAndMakeMoneyState(State):
    def output_status(self):
        #displays agents current location status and where they can possibly go
        print("I`m at Workplace, making money: \n can go the the bank if money made is enough\n can go to restaurant to satisfy hunger")
    def get_transitions(self):
        #return transitions that an agent can go to
        return {
            '1': GoToTheBankAndDepositMoneyState(self.agent),
            '2': SatisfyHungerState(self.agent)
        }
#creates a SatisfyHungerState that inherits from base class State
class SatisfyHungerState(State):
    #defines a method that states where the agent is at an instance
    def output_status(self):
        #displays agents current location status and where they can possibly go
        print("I`m at the Restaurant, satisfying hunger:\n can go to work and make more money if not hungry")
    def get_transitions(self): 
        #return transitions that an agent can go to
        return { 
            '1': GoToWorkPlaceAndMakeMoneyState(self.agent)
        }