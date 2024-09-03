import game_art
import game_data


def show_game_board(board):
    separator = "----------------"
    for row in board:
        print(separator)
        line = ""
        for cell in row:
            line += f"  {cell}  |"
        print(line[:-1])
    print(separator)


def update_game_board(is_player_two, position):
    marker = "X"
    if is_player_two:
        marker = "O"

    global current_game_board

    board_index = game_data.game_board_position[position]

    if current_game_board[board_index] != " ":
        return False

    current_game_board[board_index] = marker
    return True


def get_player_name(is_player_two):
    if is_player_two:
        return "Player 2"
    return "Player 1"


def player_win_art(is_player_two):
    if is_player_two:
        return game_art.player_2_wins_art
    return game_art.player_1_wins_art


def is_there_a_winner():
    global current_game_board

    for row in game_data.winning_combination:
        if all(
            [
                current_game_board[row[0]] != " ",
                current_game_board[row[0]] == current_game_board[row[1]],
                current_game_board[row[0]] == current_game_board[row[2]],
            ]
        ):
            return True
    return False


def is_a_draw():
    global current_game_board

    for row in current_game_board:
        for cell in list(row):
            if cell == " ":
                return False
    return True


def end_current_game(draw=False):
    show_game_board(current_game_board)

    global current_player
    if not draw:
        print(f"{player_win_art(current_player)}")
    if draw:
        print(f"{game_art.draw_art}")

    global game_on
    game_on = False

    input("Press any key to continue ...")


# start game
current_game_board = game_data.game_board


while True:
    game_on = True
    current_player = False

    print(game_art.name_art)
    print("Please note the position numbering for the game")
    show_game_board(game_data.game_positions)

    answer = input("Press any key to play, q to quit: ")

    if answer.lower() == "q":
        break

    while game_on:
        while True:
            show_game_board(current_game_board)
            position = int(
                input(f"{get_player_name(current_player)}: Choose position: ")
            )

            success = update_game_board(current_player, position)

            if success:
                break
            print("Position already chosen !")

        if is_there_a_winner():
            end_current_game()
        elif is_a_draw():
            end_current_game(True)

        current_player = not current_player
