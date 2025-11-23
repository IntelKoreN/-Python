import random
import os
def create_stats():
    if not os.path.exists("game_stats"):
        os.makedirs("game_stats")

def sohron_game_result(winner, size):
    with open("game_stats/resultates.txt", "a", encoding="utf-8") as f:
        if winner == "X":
            f.write(f"Победитель X на поле {size}x{size}\n")
        elif winner == "O":
            f.write(f"Победитель O на поле {size}x{size}\n")
        else:
            f.write(f"Ничья на поле {size}x{size}\n")

def print_board(board, size):
    print("\n   ", end="")
    for i in range(size):
        print(f" {i + 1} ", end="")
    print()

    for i in range(size):
        print(f"{i + 1} |", end="")
        for j in range(size):
            print(f" {board[i][j]} ", end="")
        print("|")

def WW_winner(board, size):

    for i in range(size):
        if board[i][0] != ' ' and all(board[i][j] == board[i][0] for j in range(size)):
            return board[i][0]

    for j in range(size):
        if board[0][j] != ' ' and all(board[i][j] == board[0][j] for i in range(size)):
            return board[0][j]

    if board[0][0] != ' ' and all(board[i][i] == board[0][0] for i in range(size)):
        return board[0][0]

    if board[0][size - 1] != ' ' and all(board[i][size - 1 - i] == board[0][size - 1] for i in range(size)):
        return board[0][size - 1]

    return None

def is_board_full(board, size):
    for i in range(size):
        for j in range(size):
            if board[i][j] == ' ':
                return False
    return True

def player_go(board, size, player):
    while True:
        try:
            move = input(f"Игрок {player}, введите номер строки и столбеца (Прример: 1 2): ")
            parts = move.split()
            if len(parts) != 2:
                print("ОшибачкО, два числа должны вводиться через пробел!!!")
                continue

            row = int(parts[0]) - 1
            col = int(parts[1]) - 1

            if row < 0 or row >= size or col < 0 or col >= size:
                print(f"Чет нито (числа должны быть от 1 до {size})")
                continue

            if board[row][col] != ' ':
                print("Эта клетка немножечко не пустая")
                continue

            return row, col

        except ValueError:
            print("Тута нужно вводить только цифарки")
        except Exception as e:
            print(f"ОшибачкО: {e}")

def computer_go(board, size):
    for i in range(size):
        for j in range(size):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                if WW_winner(board, size) == 'O':
                    board[i][j] = ' '
                    return i, j
                board[i][j] = ' '

    for i in range(size):
        for j in range(size):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                if WW_winner(board, size) == 'X':
                    board[i][j] = ' '
                    return i, j
                board[i][j] = ' '

    center = size // 2
    if board[center][center] == ' ':
        return center, center

    empty_cells = []
    for i in range(size):
        for j in range(size):
            if board[i][j] == ' ':
                empty_cells.append((i, j))

    return random.choice(empty_cells)


def play_game():
    create_stats()

    while True:
        print("\n" + "=" * 40)
        print("       Крестики - Нолики")
        print("=" * 40)

        while True:
            print("\nВыбер режима игры:")
            print("1 - people VS people")
            print("2 - people VS PC")
            try:
                mode = int(input("Ваш выбор (1 или 2): "))
                if mode in [1, 2]:
                    break
                else:
                    print("ОшибачкО! Введите 1 или 2")
            except:
                print("ОшибачкО! Введите число...")

        while True:
            try:
                size = int(input("\nВведите размер поля (3-5): "))
                if 3 <= size <= 5:
                    break
                else:
                    print("ОшибвчкО! Размер должен быть от 3 до 5")
            except:
                print("Ошибачк! Введите числою...")

        board = [[' ' for _ in range(size)] for _ in range(size)]

        current_player = random.choice(['X', 'O'])
        print(f"\nПервый ход: {current_player}")

        while True:
            print_board(board, size)

            if mode == 1 or current_player == 'X':
                row, col = player_go(board, size, current_player)
            else:
                print("\nТостер в глубоких размышлениях")
                row, col = computer_go(board, size)
                print(f"Тостер сделал гениальный ход: {row + 1} {col + 1}")

            board[row][col] = current_player

            winner = WW_winner(board, size)
            if winner:
                print_board(board, size)
                print(f"\nПришел, Увидел, Победил! {winner}!")
                sohron_game_result(winner, size)
                break

            if is_board_full(board, size):
                print_board(board, size)
                print(f"\n Победила дружба)")
                sohron_game_result("Ничья", size)
                break

            current_player = 'O' if current_player == 'X' else 'X'

        while True:
            again = input("\nХотите сыграть еще? (да/нет): ").lower()
            if again in ['да', 'д', 'yes', 'y']:
                break
            elif again in ['нет', 'н', 'no', 'n']:
                print("Спасибо за игру, с нетерпением ждем вашего возращения!")
                return
            else:
                print("Здесь понимается либо 'да' либо 'нет'")
if __name__ == "__main__":
    play_game()