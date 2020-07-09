""" NAME: ABHIRUP CHAKRAVARTY
    REGISTRATION NO: 17BCE7055
    CODE: TICTACTOE"""

import itertools

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in current_state:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} has won horizontally")
            return True

    # vertical
    for col in range(len(current_state[0])):
        check = []
        for row in current_state:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} has won vertically")
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(current_state)))):
        diags.append(current_state[idx][reverse_idx])

    if all_same(diags):
        print(f"Player {diags[0]} has won diagonally (/)")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(current_state)):
        diags.append(current_state[ix][ix])

    if all_same(diags):
        print(f"Player {diags[0]} has won diagonally (\\)")
        return True

    return False


def game_board(current_state, player=0, row=0, column=0, just_display=False):

    try:
        if current_state[row][column] != 0:
            print("Already put.")
            return False

        print("   "+"  ".join([str(i) for i in range(len(current_state))]))
        if not just_display:
            current_state[row][column] = player
        for count, row in enumerate(current_state):
               print(count, row)
        return current_state
    except IndexError:
        print("IndexError. Please input valid answer.")
        return False
    except Exception as e:
        print(str(e))
        return False


flag_pl = True
players = [1, 2]
while flag_pl:
    current_state = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_status = False
    player_cycle = itertools.cycle([1, 2])
    game_board(current_state, just_display=True)
    while not game_status:
        current_player = next(player_cycle)
        flag_done = False
        while not flag_done:
            print(f"Player: {current_player}")
            print("Input row and column separately. (Starts with 0, 2 is max.)")
            rC = int(input())
            cC = int(input())
            flag_done = game_board(current_state, player=current_player, row=rC, column=cC, just_display=False)

        if win(current_state):
            game_status = True
            flag_re = input("Play again? (y/n) ")
            if flag_re.lower() == "y":
                print("Restarting.")
            elif flag_re.lower() == "n":
                print("Exiting.")
                flag_pl = False
            else:
                print("Not a valid answer.")
                flag_pl = False


