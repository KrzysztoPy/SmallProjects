import Hamong_WithoutObjectivity.GUI.GameSettingsGUI as gameSettingGui
import Hamong_WithoutObjectivity.InputData as inputData

player_names = []
number_of_lives = 0
word_for_guesses = ""
parameters_word_for_guesses = {"length": 0}


def name_player(text, name=""):
    if not name:
        print(text)
        return input()
    else:
        return second_player_name(text, name)


def second_player_name(text, name):
    while True:
        print(text)
        sec_player_name = input()
        if name.lower() == sec_player_name.lower():
            print(gameSettingGui.error_repeat_player_name())
        else:
            return sec_player_name


def how_many_chance(question, too_less, too_many):
    while True:
        print(question)
        chance = inputData.get_only_int_data()
        if chance:
            if chance < 1:
                print(too_less)
            elif chance > 8:
                print(too_many)
            else:
                return chance
        else:
            print(gameSettingGui.input_wrong_data_gui())


def set_game_setting():
    player_names.append(name_player(gameSettingGui.entry_name_player_one_gui()))
    player_names.append(name_player(gameSettingGui.entry_name_player_two_gui(), player_names[0]))
    number_of_lives = how_many_chance(gameSettingGui.how_many_lives_gui(), gameSettingGui.lives_number_less_gui(),
                                      gameSettingGui.lives_number_higher_gui())
    number_of_guesses = how_many_chance(gameSettingGui.how_many_guesses_gui(),
                                        gameSettingGui.guesses_number_less_gui(),
                                        gameSettingGui.guesses_number_higher_gui())

    return player_names, number_of_lives, number_of_guesses
