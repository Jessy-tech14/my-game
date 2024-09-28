def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]], # top row
        [board[1][0], board[1][1], board[1][2]], # middle row
        [board[2][0], board[2][1], board[2][2]], # bottom row
        [board[0][0], board[1][0], board[2][0]], # left column
        [board[0][1], board[1][1], board[2][1]], # middle column
        [board[0][2], board[1][2], board[2][2]], # right column
        [board[0][0], board[1][1], board[2][2]], # diagonal
        [board[0][2], board[1][1], board[2][0]]  # other diagonal
    ]
    return [player, player, player] in win_conditions

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row) and not any(check_win(board, player) for player in ['X', 'O'])

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers.")
            continue
        
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid position. Please enter values between 0 and 2.")
            continue
        
        if board[row][col] != ' ':
            print("Position already taken. Choose another one.")
            continue
        
        board[row][col] = current_player
        
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if '_name_' == "_main_":
    play_game()