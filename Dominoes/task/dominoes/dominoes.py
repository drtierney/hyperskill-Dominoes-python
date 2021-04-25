import random

dominoes = [[a, b] for b in range(7) for a in range(7) if a <= b]
domino_snake = []
while True:
    random.shuffle(dominoes)
    stock = dominoes[0:14]
    computer = dominoes[14:21]
    player = dominoes[21:28]

    max_double = max(max(computer), max(player))
    if max_double[0] == max_double[1]:
        break

if max_double in computer:
    computer.remove(max_double)
    status = "player"
else:
    player.remove(max_double)
    status = "computer"

domino_snake.append(max_double)

print("=" * 70)
print(f"Stock size: {len(stock)}")
print(f"Computer pieces: {len(computer)}")
print()
for piece in domino_snake:
    print(piece)
print()
print("Your pieces:")
for idx, itm in enumerate(player):
    print(f"{idx + 1}:{itm}")
print()
if status == "player":
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print("Status: Computer is about to make a move. Press Enter to continue...")
