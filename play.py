import constants as c
import main
import menu
import pvp_mode
import ai

if __name__ == '__main__':
    run = main.Main()
    modes_dict = {
        c.MENU_MODE: menu.Menu(),
        c.PVP_MODE: pvp_mode.PvpMode(),
        c.AI_MODE: ai.AiMode()
    }
    run.setup_modes(modes_dict, c.MENU_MODE)
    run.main()
