import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    try:
        if not isinstance(spells, list) or not spells:
            return 0
        clean_spells = [int(s) for s in spells if isinstance(
            s, (int, float, str)) and str(s).isdigit()]
        if not clean_spells:
            return 0

        ops: dict[str, Callable[[int, int], int]] = {
            "add": operator.add,
            "multiply": operator.mul,
            "max": lambda a, b: max(a, b),
            "min": lambda a, b: min(a, b)
        }

        if operation not in ops:
            return 0

        return functools.reduce(ops[operation], clean_spells)
    except Exception:
        return 0


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    if not callable(base_enchantment):
        def failed_enchantment(*args: Any, **kwargs: Any) -> str:
            return "Enchantment failed: invalid base spell"
        return {
            "fire": failed_enchantment,
            "water": failed_enchantment,
            "earth": failed_enchantment
        }

    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "water": functools.partial(base_enchantment, 50, "water"),
        "earth": functools.partial(base_enchantment, 50, "earth")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    try:
        safe_n = int(n)
        if safe_n <= 0:
            return 0
        if safe_n == 1:
            return 1
        return memoized_fibonacci(safe_n - 1) + memoized_fibonacci(safe_n - 2)
    except (ValueError, TypeError):
        return 0


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast_spell(arg: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(arg: int) -> str:
        return f"Damage spell: {arg} damage"

    @cast_spell.register(str)
    def _(arg: str) -> str:
        return f"Enchantment: {arg}"

    @cast_spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-cast: {len(arg)} spells"

    return cast_spell


if __name__ == "__main__":
    print("--- Standard Data Tests ---")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"Enchanted {target} with {power} {element} power!"

    enchanters = partial_enchanter(base_enchant)
    print(enchanters["fire"]("Sword"))
    print(enchanters["water"]("Shield"))

    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")

    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch(["fireball", "heal", "shield"]))

    print("\n--- Malicious Peer Tests ---")
    print(f"Reducer (Unknown Op): {spell_reducer([10, 20], 'divide')}")

    bad_spells: Any = ['a', 'b']
    print(f"Reducer (String List): {spell_reducer(bad_spells, 'add')}")

    bad_base_enchant: Any = "not a function"
    bad_enchanters = partial_enchanter(bad_base_enchant)
    print(f"Partial (Bad Base): {bad_enchanters['fire']('Sword')}")

    bad_fib_str: Any = '10'
    print(f"Fibonacci (String): {memoized_fibonacci(bad_fib_str)}")
    
    bad_fib_none: Any = None
    print(f"Fibonacci (None): {memoized_fibonacci(bad_fib_none)}")