import Hamong_WithoutObjectivity.GUI.MainMenuGUI as menu_gui
from Hamong_WithoutObjectivity.Logic import GameSettingsLogic as game_logic
import Hamong_WithoutObjectivity.InputData as input_data

"""
8 chance
"""


def main_menu_logic():
    while True:
        menu_gui.main_menu_gui()
        answer = input_data.get_only_int_data()
        if answer:
            if answer == 1:
                game_logic.start_game()
            elif answer == 2:
                menu_gui.good_bye()
                exit(0)
            else:
                menu_gui.wrong_input_data()