import Hamong_WithoutObjectivity.GUI.MainMenuGUI as menuGUI


def get_only_int_data():
    try:
        answer = int(input('Your choose: '))
        return answer
    except ValueError:
        return
