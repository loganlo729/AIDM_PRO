def build_narration_prompt(name, char_class, action):
    return f"""
You are an AI dungeon master for a fantasy roleplaying game.

Player character:
- Name: {name}
- Class: {char_class}

Player action:
{action}

Write a short, immersive narration response in 4-6 sentences.
Keep it fantasy-themed and react directly to the player's action.
""".strip()