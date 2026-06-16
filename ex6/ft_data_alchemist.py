import random

players = ["Lukas", "Zoja", "Dina", "Alice", "bob", "emma", "gregory", "john"]
all_cap_players = [p.capitalize() for p in players]
only_cap_players = [p for p in players if p == p.capitalize()]
scores = {p: random.randint(1, 1000) for p in all_cap_players}
average = round(sum((x for x in scores.values()))/len(players), 2)
all_players_above_average = {p: s for p: s in scores if s > average}
print(players)
print(all_cap_players)
print(only_cap_players)
print(scores)
print(f"Score average: {average}")
print(f"High scores: {all_players_above_average}")
