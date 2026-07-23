import random
players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
capitalized = [name.capitalize() for name in players]
already_capitalized = [name for name in players if name[0].isupper()]
scores = {name: random.randint(0, 1000) for name in capitalized}
total_scores = sum([scores[name] for name in scores])
average = round(total_scores / len(scores), 2)
high_scores = {name: scores[name] for name in scores if scores[name] > average}
print("=== Game Data Alchemist ===")
print(f"Initial list of players: {players}")
print(f"New list with all names capitalized: {capitalized}")
print(f"New list of capitalized names only: {already_capitalized}")
print(f"Score dict: {scores}")
print(f"Score average is {average}")
print(f"High scores: {high_scores}")