import Hamong_WithoutObjectivity.GUI.MainMenuGUI as mainMenuGUI
from Hamong_WithoutObjectivity.Logic import GameSettingsLogic as gameSettingsLogic
import Hamong_WithoutObjectivity.InputData as inputData

"""
8 chance
"""


def main_menu_logic():
    while True:
        print(mainMenuGUI.main_menu_gui())
        answer = inputData.get_only_int_data()

        if answer:
            if answer == 1:
                return (gameSettingsLogic.set_game_setting())
            elif answer == 2:
                print(mainMenuGUI.good_bye())
                exit(0)
            else:
                print(mainMenuGUI.wrong_input_data())
