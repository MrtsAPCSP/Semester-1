def attack(strength, weapon_damage):
    return strength + weapon_damage

def defend(armor, shield):
    return armor + shield

def damage_dealt(attack_value, defense_value):
    if attack_value > defense_value:
        return attack_value - defense_value
    else:
        return 0  # no damage if defense is stronger

# Example battle round
atk = attack(10, 5)       # character attacks
def_val = defend(6, 3)    # other character defends
print("Damage Taken:", damage_dealt(atk, def_val))
