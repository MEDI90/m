def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    try:
        return sorted(
            artifacts,
            key=lambda artifact: artifact.get('power', 0) if isinstance(artifact, dict) else 0,
            reverse=True
        )
    except TypeError:
        return []


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    try:
        return list(
            filter(
                lambda mage: isinstance(mage, dict) and mage.get('power', 0) >= min_power,
                mages
            )
        )
    except TypeError:
        return []


def spell_transformer(spells: list[str]) -> list[str]:
    try:
        return list(map(lambda spell: f"* {spell} *", spells))
    except TypeError:
        return []


def mage_stats(mages: list[dict]) -> dict:
    default_stats = {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    try:
        if not mages:
            return default_stats

        valid_mages = list(filter(lambda m: isinstance(m, dict) and 'power' in m, mages))
        
        if not valid_mages:
            return default_stats

        max_power = max(valid_mages, key=lambda mage: mage['power'])['power']
        min_power = min(valid_mages, key=lambda mage: mage['power'])['power']
        avg_power = round(
            sum(map(lambda mage: mage['power'], valid_mages)) / len(valid_mages), 2
        )

        return {
            'max_power': max_power,
            'min_power': min_power,
            'avg_power': avg_power
        }
    except (TypeError, ValueError, ZeroDivisionError):
        return default_stats


if __name__ == "__main__":
    sample_artifacts = [{'name': 'Crystal Orb', 'power': 85}, {'name': 'Fire Staff', 'power': 92}]
    sample_mages = [{'name': 'Alex', 'power': 120}, {'name': 'Jordan', 'power': 90}]
    sample_spells = ['fireball', 'heal shield']

    print("--- Standard Data Tests ---")
    sorted_arts = artifact_sorter(sample_artifacts)
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) comes "
          f"before {sorted_arts[1]['name']} ({sorted_arts[1]['power']} power)")

    for spell in spell_transformer(sample_spells):
        print(spell)

    print(mage_stats(sample_mages))

    print("\n--- Corrupted Data Tests ---")
    print(f"Artifact Sorter (None): {artifact_sorter(None)}")
    print(f"Power Filter (Malformed dicts): {power_filter([{'name': 'Novice'}], 50)}")
    print(f"Spell Transformer (Int list): {spell_transformer([1, 2, 3])}")
    print(f"Mage Stats (Mixed garbage): {mage_stats([{'power': 100}, 'not a mage', {'name': 'Bob'}])}")