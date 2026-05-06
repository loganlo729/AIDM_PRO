import random

def roll_d20():
    return random.randint(1, 20)

def roll_damage(sides=6):
    return random.randint(1, sides)

def skill_check(modifier=0):
    roll = roll_d20()
    return roll + modifier, roll