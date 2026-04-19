from collections.abc import Callable
from typing import Any


def spell_combiner(spell1: Callable[..., Any], spell2: Callable[..., Any]) -> Callable[..., Any]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        try:
            if not callable(spell1) or not callable(spell2):
                return ("Invalid spell", "Invalid spell")
            return (str(spell1(target, power)), str(spell2(target, power)))
        except Exception:
            return ("Spell failed", "Spell failed")
    return combined_spell


def power_amplifier(base_spell: Callable[..., Any], multiplier: int) -> Callable[..., Any]:
    def amplified_spell(target: str, power: int) -> str:
        try:
            if not callable(base_spell):
                return "Invalid spell"
            return str(base_spell(target, int(power) * int(multiplier)))
        except (ValueError, TypeError, Exception):
            return "Spell amplification failed"
    return amplified_spell


def conditional_caster(condition: Callable[..., Any], spell: Callable[..., Any]) -> Callable[..., Any]:
    def conditional_spell(target: str, power: int) -> str:
        try:
            if not callable(condition) or not callable(spell):
                return "Spell fizzled"

            if condition(target, power):
                return str(spell(target, power))
            return 'Spell fizzled'
        except Exception:
            return 'Spell fizzled'
    return conditional_spell


def spell_sequence(spells: list[Callable[..., Any]]) -> Callable[..., Any]:
    def sequenced_spell(target: str, power: int) -> list[str]:
        try:
            iter(spells)
            results = []
            for spell in spells:
                if callable(spell):
                    results.append(str(spell(target, power)))
                else:
                    results.append("Invalid spell in sequence")
            return results
        except TypeError:
            return ["Invalid sequence format"]
        except Exception:
            return ["Sequence casting failed"]
    return sequenced_spell


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heals {target} for {power} HP"

    def is_powerful(target: str, power: int) -> bool:
        return power > 20

    print("--- Standard Data Tests ---")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon", 20)
    print(f"Combined spell result: {res1}, {res2}")

    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: 10, Amplified: {mega_fireball('Dragon', 10)}")

    safe_cast = conditional_caster(is_powerful, fireball)
    print(f"Weak cast: {safe_cast('Goblin', 10)}")
    print(f"Strong cast: {safe_cast('Goblin', 30)}")

    sequence = spell_sequence([fireball, heal, fireball])
    for result in sequence("Troll", 15):
        print(result)

    print("\n--- Malicious Peer Tests ---")
    
    bad_spell: Any = "not a function"
    bad_combine = spell_combiner(bad_spell, heal)
    print(f"Corrupt Combiner: {bad_combine('Dragon', 20)}")

    bad_multiplier: Any = "three"
    bad_amp = power_amplifier(fireball, bad_multiplier)
    print(f"Corrupt Amplifier: {bad_amp('Dragon', 10)}")

    bad_seq_input: Any = None
    bad_seq = spell_sequence(bad_seq_input)
    print(f"Corrupt Sequence (None): {bad_seq('Troll', 15)}")