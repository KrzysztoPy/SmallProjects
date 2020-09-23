def give_word_to_guess_gui(player_name):
    return 'Give a word for guess: '


def pasue_press_enter_gui(player_name):
    return f'Press enter when player {player_name} been prepered.'


def give_hint_gui():
    return 'Give a hint: '


def word_of_guess_gui(word_of_guess):
    return f'Word for guess is: {word_of_guess} '


def hint_for_word_guess_gui(hint_for_word_guess):
    return f'\n\nHint: {hint_for_word_guess}'


def number_of_signs_gui(number):
    return '_ ' * number


def enter_a_sign_gui():
    return 'Enter a sign: '


def which_repeat_sign_gui():
    return "You can't choose again the same character! "


def whether_contains_sign_contains_gui(sign):
    return f"Congratulation! {sign} which you gave is in the word you are guessing."


def whether_contains_sign_not_contains_gui(sign):
    return f"Unfortunately! {sign} which you gave isn't in the word you are guessing."


def set_with_letters_already_used_gui(set_with_wrote_character):
    return f"Already used: {set_with_wrote_character} "


def give_word_to_guess_is_empty_gui():
    return "Guess is empty. Please try again!"


def player_win_gui(player_name):
    return f"Congratulation!!! Player {player_name} won."


def empty_input_gui():
    return "You didn't give any letter. Try again!"


def lives_counter_gui(number_of_lives):
    return f"Others lives: {number_of_lives}"
