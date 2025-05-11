def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")


def check_winner(board, player):
    # Rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Row check
            return True
        if all([board[j][i] == player for j in range(3)]):  # Column check
            return True
    if all([board[i][i] == player for i in range(3)]):  # Diagonal \
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Diagonal /
        return True
    return False


def is_full(board):
    return all([cell != ' ' for row in board for cell in row])


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f"🎯 Player {current_player}'s turn.")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if board[row][col] != ' ':
                print("❗Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("❗Invalid input. Use numbers 0 to 2.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins!")
            show_win_image(current_player)
            break
        elif is_full(board):
            print_board(board)
            print("😲 It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'


def show_win_image(player):
    from PIL import Image
    import IPython.display as display

    if player == 'X':
        img = Image.open("player_x_win.jpg")  # Make sure this image exists
    else:
        img = Image.open("player_o_win.jpg")  # Make sure this image exists
    display.display(img)


# Run the game
play_game()
