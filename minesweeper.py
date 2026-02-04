"""
Buscaminas sencillo 4x4 en Python
"""
import random

SIZE = 4
NUM_MINES = 3


def create_board():
    """Crea el tablero con minas y números."""
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    # Colocar minas aleatoriamente
    mines_placed = 0
    while mines_placed < NUM_MINES:
        row = random.randint(0, SIZE - 1)
        col = random.randint(0, SIZE - 1)
        if board[row][col] != -1:
            board[row][col] = -1
            mines_placed += 1

    # Calcular números adyacentes
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == -1:
                continue
            count = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < SIZE and 0 <= nc < SIZE and board[nr][nc] == -1:
                        count += 1
            board[row][col] = count

    return board


def print_board(board, revealed):
    """Muestra el tablero al jugador."""
    print("\n    " + " ".join(str(i) for i in range(SIZE)))
    print("   " + "-" * (SIZE * 2 + 1))
    for row in range(SIZE):
        print(f"{row} |", end=" ")
        for col in range(SIZE):
            if revealed[row][col]:
                if board[row][col] == -1:
                    print("*", end=" ")
                else:
                    print(board[row][col], end=" ")
            else:
                print(".", end=" ")
        print("|")
    print("   " + "-" * (SIZE * 2 + 1))


def play():
    """Bucle principal del juego."""
    board = create_board()
    revealed = [[False for _ in range(SIZE)] for _ in range(SIZE)]
    cells_to_reveal = SIZE * SIZE - NUM_MINES

    print("=== BUSCAMINAS 4x4 ===")
    print(f"Hay {NUM_MINES} minas ocultas.")
    print("Introduce fila y columna (ej: 0 1) para revelar una celda.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        print_board(board, revealed)

        try:
            user_input = input("\nCelda (fila columna): ").strip()
            if user_input.lower() == "salir":
                print("¡Hasta luego!")
                break

            row, col = map(int, user_input.split())

            if not (0 <= row < SIZE and 0 <= col < SIZE):
                print("Coordenadas fuera del tablero. Intenta de nuevo.")
                continue

            if revealed[row][col]:
                print("Esa celda ya está revelada.")
                continue

            revealed[row][col] = True

            if board[row][col] == -1:
                # Revelar todas las minas
                for r in range(SIZE):
                    for c in range(SIZE):
                        if board[r][c] == -1:
                            revealed[r][c] = True
                print_board(board, revealed)
                print("\n¡BOOM! Pisaste una mina. ¡Perdiste!")
                break

            cells_to_reveal -= 1
            if cells_to_reveal == 0:
                # Revelar todo
                revealed = [[True for _ in range(SIZE)] for _ in range(SIZE)]
                print_board(board, revealed)
                print("\n¡FELICIDADES! ¡Ganaste!")
                break

        except ValueError:
            print("Entrada inválida. Usa formato: fila columna (ej: 0 1)")


if __name__ == "__main__":
    play()
