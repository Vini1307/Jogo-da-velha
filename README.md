# Jogo da Velha em Python

Este é um simples jogo da velha (tic-tac-toe) implementado em Python. Dois jogadores podem jogar o jogo no terminal, alternando entre 'X' e 'O' até que um ganhe ou o jogo termine em empate.

## Como jogar

1. **Iniciar o Jogo**:
    - O jogo começa com o tabuleiro vazio.
    - O jogador 'X' faz o primeiro movimento, seguido por 'O', e assim por diante.

2. **Entrar com os Movimentos**:
    - O jogador escolhe uma linha (0-2) e uma coluna (0-2) para colocar o símbolo (X ou O).
    - O jogo verifica se a posição é válida e se já foi ocupada. Se não for válida ou já ocupada, o jogador deve tentar novamente.

3. **Objetivo**:
    - O objetivo do jogo é alinhar três símbolos (X ou O) horizontalmente, verticalmente ou diagonalmente.
    - Se o tabuleiro estiver cheio e nenhum jogador tiver vencido, o jogo termina em empate.

4. **Fim do Jogo**:
    - O jogo termina quando um jogador vence ou o tabuleiro está cheio (empate).

## Como Rodar o Código

Para rodar o jogo, siga os passos abaixo:

### Requisitos
- Python 3.x instalado no seu sistema.

### Passos

1. Clone este repositório ou copie o código para um arquivo Python, por exemplo, `jogo_da_velha.py`.

2. Abra o terminal ou prompt de comando.

3. Navegue até o diretório onde o arquivo foi salvo.

4. Execute o código com o comando:

    ```bash
    python jogo_da_velha.py
    ```

5. Siga as instruções no terminal para jogar.

## Estrutura do Código

### Funções

- **`print_board(board)`**:
    - Exibe o tabuleiro atual do jogo.

- **`chegar_ganhador(board, jogador)`**:
    - Verifica se o jogador ganhou, checando linhas, colunas e diagonais.

- **`is_board_full(board)`**:
    - Verifica se o tabuleiro está cheio, indicando empate.

- **`play_game()`**:
    - Função principal que gerencia o jogo, alternando entre os jogadores e verificando as condições de vitória ou empate.

## Exemplo de Execução

```bash
Jogador X, escolha a linha(0-2): 1
Jogador X, escolha a coluna(0-2): 1
| | | |
-----
|X| | |
-----
| | | |
Jogador O, escolha a linha(0-2): 0
Jogador O, escolha a coluna(0-2): 2
| | |O|
-----
|X| | |
-----
| | | |

...
```
## Contribuições

Se você encontrar algum problema ou quiser melhorar o código, sinta-se à vontade para abrir um pull request ou enviar uma issue.

