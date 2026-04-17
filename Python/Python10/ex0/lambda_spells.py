def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts,
                  key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    avg_power = round(
        sum(map(lambda mage: mage['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == "__main__":
    sample_artifacts = [{'name': 'Crystal Orb', 'power': 85}, {
        'name': 'Fire Staff', 'power': 92}]
    sample_mages = [{'name': 'Alex', 'power': 120},
                    {'name': 'Jordan', 'power': 90}]
    sample_spells = ['fireball', 'heal shield']

    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(sample_artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) comes "
          f"before {sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)")

    print("\nTesting spell transformer...")
    for spell in spell_transformer(sample_spells):
        print(spell)
