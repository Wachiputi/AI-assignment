
import GoToTheBankAndDepositMoneyState
import SatisfyHungerState
import State


class GoToWorkplaceAndMakeMoneyState(State):
    def output_status(self):
        print("I`m at Workplace, making money")
    def get_transitions(self):
        return {
            '1': GoToTheBankAndDepositMoneyState(self.agent),
            '2': SatisfyHungerState(self.agent)
        }