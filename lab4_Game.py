
# Здесь создается двумерный список (матрица) размером 3x3,
# представляющий игровое поле. В начале все ячейки заполняются пробелами,
# обозначая, что они пусты.
def print_board(board):
    for row in board:
        print("-" * 10)
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board):
    # Функция check_winner проверяет,
    # есть ли победитель в текущей ситуации.
    # Она проверяет все строки, столбцы и диагонали на наличие
    # трех одинаковых символов (X или O).
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Проверка столбцов
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    # Проверка диагоналей
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(len(board))) or \
       all(board[i][len(board)-i-1] == board[0][len(board)-1] and board[i][len(board)-i-1] != ' ' for i in range(len(board))):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(len(board)) for j in range(len(board[0])))

# Функция is_board_full проверяет, заполнено ли поле.
# Если все клетки заняты и нет победителя, игра считается ничьей.


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input(f"Игрок {current_player}, выберите строку (0, 1, 2): "))
        col = int(input(f"Игрок {current_player}, выберите столбец (0, 1, 2): "))

        # Игроки вводят номер строки и столбца,
        #куда они хотят поставить свой символ.

        # Если выбранная клетка пуста, то в нее записывается
        #символ текущего игрока. После этого проверяется,
        #не завершилась ли игра.
        if board[row][col] == ' ':
            board[row][col] = current_player
            if check_winner(board):
                print_board(board)
                print(f"Игрок {current_player} победил!")
                break
            elif is_board_full(board):
                print_board(board)
                print("Ничья!")
                break
            # После каждого хода происходит проверка на наличие победителя или ничьей.
            # Если одно из условий выполняется, игра завершается.

            
            else:
                current_player = 'O' if current_player == 'X' else 'X'
                # Игроки ходят поочередно.
                # Эта строка кода обеспечивает смену текущего игрока после каждого хода.
        else:
            print("Эта клетка уже занята. Попробуйте снова.")

if __name__ == "__main__":
    tic_tac_toe()
