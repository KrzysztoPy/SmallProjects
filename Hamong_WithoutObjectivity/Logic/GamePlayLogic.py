import Hamong_WithoutObjectivity.GUI.GamePlayGUI as gamePlayGUI
from sys import stdin
from os import system

'''
Zasady:
        1) Gracz numer_1 zaczyna od podania słowa do zgadnięcia
        2) Gracz numer_1 podaje podpowiedź
        3) Gracz numer_2 zgadnuje:
            a) Jeśli zganie dostaje 1 punkt
            b) Jeśli nie zgadnie dostaje 0 punktów

'''


def game_play(game_setting):
    player_name = game_setting[0]
    number_of_lives = game_setting[1]
    number_of_guesses = game_setting[2]
    player_score = [0, 0]
    word_to_guess = ""
    hint_for_word_guess = ""

    while True:
        for choose_player in range(0, player_name.__len__()):
            pause_press_enter(player_name[choose_player])
            word_to_guess = write_guess(player_name, choose_player)
            hint_for_word_guess = hint_for_the_puzzle()
            player_score[choose_player] += play_game(word_to_guess, hint_for_word_guess,
                                                     number_of_lives)
            if player_score[choose_player] == 8:
                print(gamePlayGUI.player_win_gui())


def write_guess(player_name, choose_player):
    while True:
        word_to_guess = give_word_to_guess(player_name[choose_player])
        if word_to_guess:
            return word_to_guess
        else:
            print(gamePlayGUI.give_word_to_guess_is_empty_gui())


def give_word_to_guess(player_name):
    print(gamePlayGUI.give_word_to_guess_gui(player_name[0]))
    return input().lower()


def hint_for_the_puzzle():
    print(gamePlayGUI.give_hint_gui())
    return input()


def pause_press_enter(player_name):
    input(gamePlayGUI.pasue_press_enter_gui(player_name))


def play_game(word_to_guess, hint_for_word_guess, number_of_lives):
    guessed_word = gamePlayGUI.number_of_signs_gui(len(word_to_guess))
    set_with_wrote_character = set()

    while True:
        print(gamePlayGUI.lives_counter_gui(number_of_lives))
        print(gamePlayGUI.hint_for_word_guess_gui(hint_for_word_guess))
        print(gamePlayGUI.set_with_letters_already_used_gui(set_with_wrote_character_to_str(set_with_wrote_character)))
        print(guessed_word)

        input_letter_and_is_repeat = which_repeat_or_empty_input(enter_a_sign(), set_with_wrote_character)
        if input_letter_and_is_repeat[0]:
            set_with_wrote_character.add(input_letter_and_is_repeat[0].lower())
            if not input_letter_and_is_repeat[1]:
                guessed_word, number_of_lives = whether_contains_sign(input_letter_and_is_repeat[0], word_to_guess,
                                                                      guessed_word, number_of_lives)
                if word_to_guess == guessed_word:
                    return 1
                if number_of_lives == 0:
                    return 0


def set_with_wrote_character_to_str(set_with_wrote_character):
    if set_with_wrote_character:
        return ""
    else:
        set_with_wrote_character_str = ""
        for counter in set_with_wrote_character:
            set_with_wrote_character_str += set_with_wrote_character[counter]
        return set_with_wrote_character_str


def enter_a_sign():
    print(gamePlayGUI.enter_a_sign_gui())
    return (stdin.read(1)).strip()


def which_repeat_or_empty_input(input_letter, set_with_wrote_character):
    repeat = False
    if input_letter:
        if input_letter.lower() in set_with_wrote_character:
            print(gamePlayGUI.which_repeat_sign_gui())
            repeat = True
        return input_letter, repeat
    else:
        print(gamePlayGUI.empty_input_gui())
        return input_letter, repeat


def whether_contains_sign(sign, word_to_guess, guessed_word, number_of_lives):
    if sign in word_to_guess:
        print(gamePlayGUI.whether_contains_sign_contains_gui(sign))
        return where_lies_input_letter(word_to_guess, sign), number_of_lives
    else:
        print(gamePlayGUI.whether_contains_sign_not_contains_gui(sign))
        return guessed_word, number_of_lives - 1


def where_lies_input_letter(word_to_guess, sign):
    new_guessed_word = ""
    for counter in range(0, word_to_guess.__len__()):
        if word_to_guess[counter].lower() == sign.lower():
            new_guessed_word += sign
        else:
            new_guessed_word += "_"
    return new_guessed_word

# def clear_screen():
#     return system('cls')
