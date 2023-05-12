
from State import State


class GoHomeAndSleepStateUntilRestedState(State):
    def output_status(self):
        print("I`m at Home, sleeping")