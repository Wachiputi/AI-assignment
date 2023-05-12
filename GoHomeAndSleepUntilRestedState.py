import GoToWorkPlaceAndMakeMoneyState
import State


class GoHomeAndSleepStateUntilRestedState(State):
    def output_status(self):
        print("I`m at Home, sleeping")
    def get_transitions(self):
        return {
            '1':GoToWorkPlaceAndMakeMoneyState(self.agent)
        }