import random
import typing

# Listes déduites de l'exemple de l'énoncé
PLAYERS = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS = ['run', 'eat', 'sleep', 'grab', 'move', 'climb', 'swim', 'use', 'release']

def gen_event() -> typing.Generator[tuple, None, None]:
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)

# --- PARTIE 1 : Flux infini de 1000 événements ---
print("=== Game Data Stream Processor ===")

stream = gen_event()
for i in range(1000):
    name, action = next(stream)
    print(f"Event {i}: Player {name} did action {action}")

# --- PARTIE 2 : Création de la liste de 10 événements ---
stream2 = gen_event()
event_list = []
for _ in range(10):
    event_list.append(next(stream2))

print(f"Built list of 10 events: {event_list}")

# --- PARTIE 3 : Consommation de la liste ---
def consume_event(lst) -> typing.Generator[tuple, None, None]:
    while len(lst) > 0:
        # On pick un index aléatoire
        idx = random.randrange(len(lst))
        # On récupère l'élément
        item = lst[idx]
        # On le supprime de la liste d'origine (mutation directe)
        del lst[idx]
        # On le yield
        yield item

# Utilisation directe dans le for .. in ..
for event in consume_event(event_list):
    print(f"Got event from list: {event}")
    print(f"Remains in list: {event_list}")
    