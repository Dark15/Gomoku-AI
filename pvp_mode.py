import main
import constants as c

class PvpMode(main._Mode):
    def __init__(self):
        super().__init__()
        self.now_play = c.BLACK

    def startup(self):
        pass
