import Hamong_WithoutObjectivity.Logic.GamePlayLogic as GamePlayLogic
import Hamong_WithoutObjectivity.GUI.GamePlayGUI as GamePlayGUI


def which_repeat_sign_test():
    # input_sign = 'x'
    # list_with_wrote_character = ['a', 'v', 'x']
    #
    # result = GamePlayLogic.which_repeat_sign(input_sign, list_with_wrote_character)
    # # print(result)
    # assert result == input_sign
    # # print(result)
    # # print("You can't choose again the same character! ")
    # # print(result == "You can't choose again the same character! ")
    # input_sign = 'l'
    # guessed_word = "l_l__"
    # guessed_word_not = "_" * guessed_word.__len__()
    #
    # result = GamePlayLogic.where_lies_input_letter(guessed_word, input_sign)
    # assert result == guessed_word

    player_name = ["K", "L"]
    choose_player = 1

    result = GamePlayLogic.write_guess(player_name, choose_player)
    assert result == "mama"

which_repeat_sign_test()
