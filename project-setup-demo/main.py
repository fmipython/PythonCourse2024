#!/usr/bin/env python3

from game.players.input_player import InputPlayer
from game.players.ai import AI
from game.engine import *
from game.level import Level

from config_parser.parser import ConfigParser

import sys
import os

def main():
    print("Welcome to Besenitsa.")
    
    config_name = sys.argv[1]

    path = os.path.join("configs", f"{config_name}.yaml")
    parser = ConfigParser(path)
    parser.parse()
    config_dict = parser.config
    
    is_ai = config_dict["ai_player"]
    level_props = config_dict["level"]
    level = Level(**level_props)
    
    if is_ai:
        player = AI(level.failed_attempts)
    else:
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
