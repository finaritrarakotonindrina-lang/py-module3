import random

ALL_ACHIEVEMENTS = [
    'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme', 
    'Untouchable', 'Boss Slayer', 'Strategist', 'Unstoppable', 'Speed Runner', 
    'Survivor', 'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Hidden Path Finder'
]

def gen_player_achievements():
    return set(random.sample(ALL_ACHIEVEMENTS, random.randint(1, len(ALL_ACHIEVEMENTS))))

# On crée un dictionnaire de joueurs
players = {
    "Alice": gen_player_achievements(),
    "Bob": gen_player_achievements(),
    "Charlie": gen_player_achievements(),
    "Dylan": gen_player_achievements()
}

print("=== Achievement Tracker System ===")
for name, ach in players.items():
    print(f"Player {name}: {ach}")

# Union et Intersection dynamiques
all_sets = list(players.values())
all_distinct = all_sets[0].union(*all_sets[1:])
common = all_sets[0].intersection(*all_sets[1:])
print(f"All distinct achievements: {all_distinct}")
print(f"Common achievements: {common}")

master_set = set(ALL_ACHIEVEMENTS)

# Une seule boucle gère l'exclusivité et les manquants pour TOUS les joueurs
for name, ach in players.items():
    # On crée l'union de tous les AUTRES joueurs
    others = set()
    for other_name, other_ach in players.items():
        if other_name != name:
            others = others.union(other_ach)
            
    print(f"Only {name} has: {ach.difference(others)}")
    print(f"{name} is missing: {master_set.difference(ach)}")