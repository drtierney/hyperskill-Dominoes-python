import random


domino_snake = []


def shuffle_pieces():
    while True:
        dominoes = [[a, b] for b in range(7) for a in range(7) if a <= b]
        random.shuffle(dominoes)
        stock_pieces = dominoes[0:14]
        computer_pieces = dominoes[14:21]
        player_pieces = dominoes[21:28]

        max_double = max(max(computer_pieces), max(player_pieces))
        if max_double[0] == max_double[1]:
            break

    if max_double in computer_pieces:
        computer_pieces.remove(max_double)
        status = "computer"
    else:
        player_pieces.remove(max_double)
        status = "player"

    domino_snake.append(max_double)
    return stock_pieces, computer_pieces, player_pieces, status


def show_field(snake):
    if len(snake) > 6:
        field = f"{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}"
    else:
        field = "".join(str(x) for x in snake)
    print(field)


def summary():
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(computer)}")
    print()
    show_field(domino_snake)
    print()
    print("Your pieces:")
    for idx, itm in enumerate(player):
        print(f"{idx + 1}:{itm}")
    print()


def is_valid_move(next_move):
    if p_move.strip("-").isnumeric():
        if abs(int(next_move)) - 1 < len(player):
            return True
    return False


def make_move(next_move, current_turn):
    if int(next_move) > 0:
        domino_snake.append(current_turn.pop(int(next_move) - 1))
    elif int(next_move) < 0:
        domino_snake.insert(0, current_turn.pop(int(next_move)))
    elif int(next_move) == 0:
        if len(stock):
            current_turn.append(stock.pop())


def check_game_state():
    state = None
    if domino_snake[0][0] == domino_snake[-1][-1] and \
            sum(x.count(domino_snake[0][0]) for x in domino_snake) == 8:
        state = "It's a draw"
    elif len(player) == 0:
        state = "You won"
    elif len(computer) == 0:
        state = "The computer won"
    elif len(stock) == 0 and (len(player) > len(computer)):
        state = "The computer won"
    return state


stock, player, computer, current_move = shuffle_pieces()
summary()
while True:
    game_state = check_game_state()
    if game_state is not None:
        print(f"Status: The game is over. {game_state}!")
        break

    if current_move == "computer":
        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()
        pieces = len(computer) - 1
        c_move = random.randint(pieces * -1, pieces)
        make_move(c_move, computer)
        summary()
        current_move = "player"

    if current_move == "player":
        print("Status: It's your turn to make a move. Enter your command.")
        p_move = input()
        while not is_valid_move(p_move):
            print("Invalid input. Please try again.")
            p_move = input()
            is_valid_move(p_move)
        make_move(p_move, player)
        summary()
        current_move = "computer"
