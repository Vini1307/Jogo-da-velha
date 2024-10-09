def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*5)
        
def chegar_ganhador(board, jogador):
    for row in board:
        if all([spot == jogador for spot in row]):
            return True
    
    for col in range(3):
        if all([board[row][col]  == jogador for row in range(3)]):
            return True
    
    if all([board[i][i] == jogador for i in range(3)]) or all([board[i][2-i] == jogador for i in range(3)]):
        return True
    
    return False


def is_board_full(board):
    return all([spot != " " for row in board for spot in row])

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'


    while True:
        print_board(board)
        
        try:
            row = int(input(f'Jogador {jogador_atual}, escolha a linha(0-2): '))
            col = int(input(f'Jogador {jogador_atual}, escolha a coluna(0-2): '))
        except ValueError:
            print('Escolha inválida. Por favor, escolha um número inteiro entre')
            continue
        
        
        if row not in range(3) or col not in range(3):
            print('Posiçao invalida. Por favor escolha um numero de 0 a 2')
            continue
        if board[row][col] != ' ':
            print('Esse lugar ja foi escolhido, por favor escolha outro')
            continue
        
        board[row][col] = jogador_atual
        
        if chegar_ganhador(board, jogador_atual):
            print_board(board)
            print(f'Jogador {jogador_atual} ganhou!')
            break
        
        if is_board_full(board):
            print('Empate!')
            break
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        
if __name__ == '__main__':
    play_game()
        
    
    