def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = set(['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'])
    bob = set(['first_kill', 'level_10', 'boss_slayer', 'collector'])
    charlie = set(['level_10', 'treasure_hunter', 'boss_slayer',
                  'speed_demon', 'perfectionist'])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")

    all_unique = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")

    common_to_all = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_to_all}")

    shared_ab = alice.intersection(bob)
    shared_bc = bob.intersection(charlie)
    shared_ac = alice.intersection(charlie)

    all_shared = shared_ab.union(shared_bc).union(shared_ac)
    rare_achievements = all_unique.difference(all_shared)

    print(f"Rare achievements (1 player): {rare_achievements}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


if __name__ == "__main__":
    main()
