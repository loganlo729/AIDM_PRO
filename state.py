def init_game_state(character):
    return {
        "character": character,
        "enemy_hp": 10,
        "player_hp": character["combat"]["current_hp"],
        "location": "tavern",
        "quest_progress": [],
        "history": [],
        "last_output": "",
        "current_npc": None
    }


def update_state(state, action, result):
    state["history"].append({
        "action": action,
        "result": result
    })


def apply_combat(state, roll):
    if roll >= 10:
        damage = roll // 2
        state["enemy_hp"] -= damage
        return f"Hit! Enemy takes {damage} damage. Enemy HP: {state['enemy_hp']}"
    else:
        enemy_damage = 2
        state["player_hp"] -= enemy_damage
        return f"Miss! Enemy hits you for {enemy_damage}. Your HP: {state['player_hp']}"