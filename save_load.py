import json

def save_game(state, filename="save.json"):
    with open(filename, "w") as f:
        json.dump(state, f, indent=4)
    print("Game saved.")


def load_game(filename="save.json"):
    try:
        with open(filename, "r") as f:
            state = json.load(f)
        print("Game loaded.")
        return state
    except FileNotFoundError:
        print("No save file found.")
        return None