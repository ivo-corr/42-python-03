import random


class Player:
    def __init__(self, name: str, achievements: set) -> None:
        self.name = name.capitalize()
        self._achievements = achievements

    def set_achievements(self, achievements: set):
        self._achievements = achievements

    def get_achievements(self):
        return self._achievements


def gen_player_achievements(achievements: list) -> set:
    player_achievements = set()
    for i in range(0, random.randint(1, len(achievements) - 1)):
        player_achievements.add(
            achievements[random.randint(0, len(achievements) - 1)])
    return player_achievements


def get_intersection(achs: list):
    lower = [x.intersection(y) for x, y in zip(achs, achs[1:])]
    if (len(lower) == 1):
        return (lower)
    return (get_intersection(lower))


def get_diff(achs: list):
    lower = [x.difference(y) for x, y in zip(achs, achs[1:])]
    if (len(lower) == 1):
        return (lower)
    return (get_diff(lower))


if __name__ == "__main__":
    achievements = ["Crafting Genius", "Strategist", "World Savior",
                    "Speed Runner", "Survivor", "Master Explorer",
                    "Treasure Hunter", "Unstoppable", "First Steps",
                    "Collector Supreme", "Untouchable", "Sharp Mind",
                    "Boss Slayer"]

    players = [
        Player("Alice", gen_player_achievements(achievements)),
        Player("Bob", gen_player_achievements(achievements)),
        Player("Charlie", gen_player_achievements(achievements)),
        Player("Dylan", gen_player_achievements(achievements)),
        Player("Dina", gen_player_achievements(achievements)),
        Player("Jakob", gen_player_achievements(achievements)),
        Player("Gabriel", gen_player_achievements(achievements)),
        Player("Priya", gen_player_achievements(achievements)),
        Player("Zoja", gen_player_achievements(achievements)),
        Player("Achilles", gen_player_achievements(achievements))
    ]
    print("=== Achievement Tracker System ===\n")
    for i in range(len(players)):
        print(f"Player {players[i].name} :"
              f"{players[i].get_achievements()}")
    print(f"\nAll distinct achievements: {set(achievements)}\n")
    intersections = get_intersection([x.get_achievements() for x in players])
    print(f"Common achievements: {intersections}\n")
    for i in range(len(players)):
        diffs = get_diff(
            [x.get_achievements() for x in (players[i:] + players[:i])])
        print(f"Only {players[i].name} has: {diffs}")
    print()
    for player in players:
        print(f"{player.name} is missing "
              f"{set(achievements) - player.get_achievements()}")
    print()
