#import GoHomeAndSleepUntilRestedState
#import GoToWorkPlaceAndMakeMoneyState
#import State


from State import State


class GoToTheBankAndDepositMoneyState(State):
    def output_status(self):
        print("I`m at The Bank, depositing money")

    def get_transitions(self):
        return {
 #           '1': GoHomeAndSleepUntilRestedState(self.agent),
            #'2': GoToWorkPlaceAndMakeMoneyState(self.agent)
        }