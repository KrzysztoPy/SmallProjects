import Hamong_WithoutObjectivity.GUI.GamePlayGUI as gamePlayGUI

'''
Zasady:
        1) Gracz numer_1 zaczyna od podania słowa do zgadnięcia
        2) Gracz numer_1 podaje podpowiedź
        3) Gracz numer_2 zgadnuje:
            a) Jeśli zganie dostaje 1 punkt
            b) Jeśli nie zgadnie dostaje 0 punktów

'''


def game_play(player_name=[], number_of_lives=0, number_of_guesses=0):
    player_name = player_name
    number_of_lives = number_of_lives
    number_of_guesses = number_of_guesses

    while True:
        pasue_press_enter()
        give_word_to_guess()
        hint_for_the_puzzle()
        pass


def give_word_to_guess(player_name):
    pasue_press_enter()
    print(gamePlayGUI.give_word_to_guess_gui())
    return input()

def hint_for_the_puzzle():


def pasue_press_enter(player_name):
    input(gamePlayGUI.pasue_press_enter_gui(player_name))
