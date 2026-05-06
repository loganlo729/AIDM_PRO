import json

from prompts import build_narration_prompt
from save_load import load_game
from game_loop import game_loop

def ask_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def create_character():
    print("=== Create DnD Character ===")

    character = {
        "character_name": input("Character name: "),
        "player_name": input("Player name: "),
        "race": input("Race: "),
        "class": input("Class: "),
        "level": ask_int("Level: "),
        "background": input("Background: "),
        "alignment": input("Alignment: "),
        "experience_points": ask_int("Experience points: "),

        "ability_scores": {
            "strength": ask_int("Strength: "),
            "dexterity": ask_int("Dexterity: "),
            "constitution": ask_int("Constitution: "),
            "intelligence": ask_int("Intelligence: "),
            "wisdom": ask_int("Wisdom: "),
            "charisma": ask_int("Charisma: ")
        },

        "combat": {
            "max_hp": ask_int("Max HP: "),
            "current_hp": ask_int("Current HP: "),
            "armor_class": ask_int("Armor Class: "),
            "speed": ask_int("Speed: "),
            "proficiency_bonus": ask_int("Proficiency Bonus: ")
        }
    }

    return character

def save_character(character, filename="characters.json"):
    with open(filename, "w") as file:
        json.dump(character, file, indent=4)

def main():
    choice = input("Load previous game? (y/n): ")

    # Load game
    if choice.lower() == "y":
        state = load_game()

        if state:
            game_loop(state["character"], loaded_state=state)
            return
        else:
            print("No save found. Starting new game.")

    # New game
    character = create_character()
    game_loop(character)

if __name__ == "__main__":
    main()