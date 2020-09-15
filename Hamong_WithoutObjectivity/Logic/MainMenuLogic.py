
from Logic import GameLogic as game_logic
import GUI.MainMenuGUI as menu_gui

"""
8 chance
"""





def main_menu_logic():
    while True:
        menu_gui.main_menu_gui()
        answer = input('Your choose: ')
        if not isinstance(answer, int):
            menu_gui.wrong_input_data()
        else:
            if answer == 1:
                game_logic.start_game()
            elif answer == 2:
                menu_gui.good_bye()
                exit(0)
            else:
                menu_gui.wrong_input_data()

main_menu_logic()
