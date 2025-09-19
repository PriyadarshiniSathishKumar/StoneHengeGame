from stonehenge import Stonehenge
from strategy import interactive_strategy, recursive_minimax_strategy

def play_game():
    print("Welcome to Stonehenge!")

    # Ask board size
    side_length = int(input("Enter the board side length (1–5): "))

    # Create game
    game = Stonehenge(side_length)


    # Choose strategy for players
    p1_strategy = interactive_strategy  # human player
    p2_strategy = recursive_minimax_strategy  # AI opponent

    # Game loop
    while not game.is_over(game.current_state):
        print(game.current_state)
        current_player = game.current_state.get_current_player_name()

        if current_player == "p1":
            move = p1_strategy(game)
        else:
            move = p2_strategy(game)

        game.current_state = game.current_state.make_move(move)
        print(f"{current_player} chose move {move}\n")

    # End game
    print("Game over!")
    if game.is_winner("p1"):
        print("Player 1 wins!")
    elif game.is_winner("p2"):
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
