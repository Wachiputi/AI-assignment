class State:
    def __init__(self, agent):
        self.agent = agent

    def output_status(self):
        pass

class GoHomeAndSleepUntilRestedState(State):
    def output_status(self):
        print("I`m at Home, sleeping")
    def get_transitions(self):
        return {
            '1':GoToWorkplaceAndMakeMoneyState(self.agent)
        }
class GoToTheBankAndDepositMoneyState(State):
    def output_status(self):
        print("I`m at The Bank, depositing money")

    def get_transitions(self):
        return {
            '1': GoHomeAndSleepUntilRestedState(self.agent),
            '2': GoToWorkPlaceAndMakeMoneyState(self.agent)
        }
class GoToWorkplaceAndMakeMoneyState(State):
    def output_status(self):
        print("I`m at Workplace, making money")
    def get_transitions(self):
        return {
            '1': GoToTheBankAndDepositMoneyState(self.agent),
            '2': SatisfyHungerState(self.agent)
        }
class SatisfyHungerState(State):
    #defines a method that states where the agent is at an instance
    def output_status(self):
        print("I`m at the Restaurant, satisfying hunger")
    def get_transitions(self):
        return {
            '1': GoToWorkplaceAndMakeMoneyState(self.agent)
        }