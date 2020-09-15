import GUI.GameGUI as game_gui

word_for_guesses = ""
parameters_word_for_guesses = {"length": 0}


def name_player(text):
    return input(text)


def how_many_chance():
    while True:
        chance = input(game_gui.how_much_lives_gui())
        if isinstance(chance, int):
            if chance < 1:
                game_gui.lives_number_gui()
            else:
                return chance
        else:
            game_gui.input_wrong_data_gui()


def start_game():
    player_one_name = name_player(game_gui.entry_name_player_one_gui())
    player_two_name = name_player(game_gui.entry_name_player_two_gui())
    lives = how_many_chance()

