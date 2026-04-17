from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return 'Spell fizzled'
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequenced_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequenced_spell


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    def is_powerful(target: str, power: int) -> bool:
        return power > 20

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 20)
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original: 10, Amplified: 30")

    print("\nTesting conditional caster...")
    safe_cast = conditional_caster(is_powerful, fireball)
    print(f"Weak cast: {safe_cast('Goblin', 10)}")
    print(f"Strong cast: {safe_cast('Goblin', 30)}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    for result in sequence("Troll", 15):
        print(result)
