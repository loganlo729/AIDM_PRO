from prompts import build_narration_prompt
from dice import roll_d20
from rag import generate_npc, retrieve_context
from llm import generate_response
from state import init_game_state, update_state, apply_combat
from rag import generate_npc
from save_load import save_game, load_game

def classify_action(action):
    action = action.lower()
    if "attack" in action:
        return "combat"
    elif "talk" in action:
        return "dialogue"
    elif "run" in action or "move" in action:
        return "movement"
    return "exploration"


def game_loop(character, loaded_state=None):
    if loaded_state:
        state = loaded_state
        print("\n=== Loaded Game ===")
    else:
        state = init_game_state(character)
        print("\n=== New Game Started ===")
    
    # Show last narration if it exists
    if state.get("last_output"):
        print("\n=== Previous Scene ===")
        print(state["last_output"])

    if "last_output" not in state:
        state["last_output"] = ""
    
    print("\n=== Game Started ===")

    while True:
        # Status
        print(f"\nHP: {state['player_hp']} | Location: {state['location']}")
        action = input("\nWhat do you do? (type 'save' or 'load' to save/load, 'quit' to quit): ")

        if action.lower() == "quit":
            print("Game ended.")
            break

        if action.lower() == "save":
            save_game(state)
            continue

        if action.lower() == "load":
            loaded = load_game()
            if loaded:
                state = loaded
            continue

        # --- REASONING STEPS ---
        print("\n[Processing Action]")
        print("1. Interpreting action...")

        scenario = classify_action(action)

        # Scenario-specific logic
        if scenario == "dialogue":
            npc = generate_npc()
            print(f"   You meet {npc}")

        elif scenario == "movement":
            state["location"] = "unknown area"
            print(f"   You move to a new location: {state['location']}")

        elif scenario == "exploration":
            print("   You carefully explore your surroundings...")

        if "quest" in action.lower():
            state["quest_progress"].append("New quest started")
            print("   Quest updated!")

        # Roll first
        roll = roll_d20()
        print(f"2. Rolled dice: {roll}")

        # Apply combat logic based on roll
        combat_result = ""
        if scenario == "combat":
            combat_result = apply_combat(state, roll)
            combat_result = "FINAL OUTCOME: " + combat_result

        # Game over condition
        if state["enemy_hp"] <= 0:
            print("\nEnemy defeated! You win!")
            break
        if state["player_hp"] <= 0:
            print("\nYou have been defeated. Game over.")
            break

        # Retrieve context (RAG)
        context = retrieve_context(action)
        print(f"3. Retrieved context: {context}")

        # Memory (last 3 actions)
        recent_history = state["history"][-3:]
        history_text = " ".join([h["action"] for h in recent_history])

        # Combine context + memory + combat info
        full_context = f"""
        Game Context:
        {context}

        Recent Actions:
        {history_text}

        Combat Result (FINAL):
        {combat_result}
        """

        print("4. Generating narration...\n")

        # Build prompt
        prompt = build_narration_prompt(
            character["character_name"],
            character["class"],
            action,
            full_context,
            roll
        )

        response = generate_response(prompt)
        print(response)
        state["last_output"] = response

        # Update state
        update_state(state, action, response)