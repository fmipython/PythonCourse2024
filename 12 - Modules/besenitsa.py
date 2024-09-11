from game.players.input_player import InputPlayer
from game.engine import *
import game.level as level

DIFFICULTIES = [level.EASY, level.MEDIUM, level.HARD, level.PESHO_BAFTATA]

def main():
    print("Welcome to Besenitsa.")
    
    d = -1
    while d not in range(len(DIFFICULTIES)):
        try:
            d = int(input("Select level [0-3]: "))
        except ValueError:
            print("Please enter a valid number (0, 1, 2 or 3).")
    
    level = DIFFICULTIES[d]
    player = InputPlayer(level.failed_attempts)
    engine = BesenitsaEngine(level.word, player)

    outcome = GameState.ONGOING
    while outcome == GameState.ONGOING:
        print(f"Word: {engine.masked_word}\nFailed attempts left: {player.hp}")
        outcome = engine.guess()

    if outcome == GameState.LOST:
        print("Sorry, you lost.")
    elif outcome == GameState.WON:
        print("Congrats! You won.")

if __name__ == "__main__":
    main()
