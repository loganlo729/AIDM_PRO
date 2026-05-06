LORE_DB = {
    "goblin": "Goblins are small, cunning creatures that prefer ambush tactics.",
    "tavern": "Taverns are social hubs filled with rumors, drinks, and shady figures.",
    "attack": "Combat involves attack rolls versus armor class.",
    "run": "Fleeing may provoke opportunity attacks or require dexterity checks.",
    "castle": "Ancient castles often contain traps, secrets, and hidden enemies."
}

import random

def generate_npc():
    names = ["Thorin", "Elira", "Gorim", "Selene"]
    names = [
        "Lyra", "Drogath", "Fenric", "Isolde",
        "Varek", "Mira", "Brom", "Sylva", "Dain",
        "Nymera", "Rurik", "Alaric", "Seraphine", "Tiber",
        "Valka", "Eldrin", "Morwen", "Cedric", "Zarek",
        "Thorin", "Elira", "Gorim", "Selene", "Kael",
        "Aeliana", "Torvald", "Lunara", "Grimnar", "Faelyn",
        "Orin", "Kethra", "Baldric", "Velora", "Thalia",
        "Draven", "Rowan", "Eira", "Malgrim", "Cassian",
        "Freya", "Lucan", "Vesper", "Haldor", "Astrid",
        "Zephira", "Magnus", "Nerys", "Corwin", "Sylric",
        "Brynja", "Theron", "Ysara", "Kaida", "Leoric",
        "Ardyn", "Maeve", "Fenna", "Orrick", "Calista",
        "Varis", "Anwyn", "Darius", "Sigrid", "Jorund",
        "Ravena", "Talon", "Eldra", "Brenna", "Korin",
        "Zarina", "Ulric", "Naeris", "Torren", "Lilith",
        "Garrick", "Elowen", "Morthos", "Ilyana", "Rhogar",
        "Vaelin", "Selric", "Brakka", "Ophelia", "Tavric",
        "Mirabel", "Drogan", "Astra", "Fenlow", "Nyx",
        "Halric", "Celestra", "Vorstag", "Ember", "Roderic"
    ]
    roles = [
        "merchant", "guard", "mage", "thief",
        "blacksmith", "alchemist", "bounty hunter", "priest",
        "assassin", "bard", "ranger", "knight",
        "mercenary", "healer", "necromancer", "scholar",
        "innkeeper", "sailor", "farmer", "hunter",
        "paladin", "druid", "monk", "warlock",
        "enchanter", "smuggler", "spy", "gladiator",
        "captain", "stablemaster", "cook", "miner",
        "jeweler", "tailor", "fisherman", "herbalist",
        "cartographer", "sorcerer", "wizard", "archer",
        "duelist", "tavern owner", "gravekeeper", "executioner",
        "court advisor", "royal guard", "dragon hunter", "explorer",
        "witch", "shaman", "oracle", "beast tamer",
        "pirate", "cultist", "librarian", "messenger",
        "tax collector", "guild master", "engineer", "inventor",
        "apothecary", "tracker", "caravan leader", "soldier",
        "scribe", "artisan", "runesmith", "monster slayer",
        "treasure hunter", "town crier", "fletcher", "brewer",
        "locksmith", "spy master", "champion", "beekeeper",
        "shipwright", "fortune teller", "acrobat", "jailer",
        "executioner", "bodyguard", "diplomat", "archmage",
        "street performer", "gatekeeper", "grave robber", "nomad",
        "beast hunter", "quartermaster", "scout", "elder",
        "chieftain", "wandering trader", "artifact collector", "illusionist"
    ]

    return f"{random.choice(names)}, a {random.choice(roles)}"

def retrieve_context(action):
    action = action.lower()
    matches = []

    for key, value in LORE_DB.items():
        if key in action:
            matches.append(value)

    if matches:
        return " ".join(matches)

    return "General exploration. No specific lore found."