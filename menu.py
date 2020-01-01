import main
import constants as c
import setup

class Menu(main._Mode):
    def __init__(self):
        super().__init__()
        self.background = None
        self.caption_font = None
        self.option_font = None
        self.option = None

    def startup(self):
        self.setup_background()
        self.setup_cursor()

    def setup_background(self):
        self.background = None
        self.caption_font = setup.FONTS[c.CAPTION_FONT]
        self.option_font = setup.FONTS[c.CAPTION_FONT]

    def setup_cursor(self):
        pass

    def get_event(self, event):
        if event.type == event.MOUSEMOTION:
            self.pos = event.pos
        elif event.type == event.MOUSEDOWN:
            self.switch = self.check_pos()

    def check_pos(self):
        return False

    def update(self, surface):
        # f1surf, rect = c.CAPTION_FONT.render(c.MENU_MODE, fgcolor=GOLD, size=20)
        self.update_cursor()
        surface.bilt(...)
        surface.bilt(...)

    def update_cursor(self):
        pass


