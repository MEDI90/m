import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min,
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: '{operation}'")

    if operation in ('max', 'min'):
        return functools.reduce(ops[operation], spells)

    return functools.reduce(ops[operation], spells)


def partial_enchanter(
    base_enchantment: Callable
) -> dict[str, Callable]:
    return {
        'fire': functools.partial(base_enchantment, 50, 'fire'),
        'ice': functools.partial(base_enchantment, 50, 'ice'),
        'lightning': functools.partial(base_enchantment, 50, 'lightning'),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"{element} enchantment on {target} with power {power}"

    enchants = partial_enchanter(base_enchant)
    print(enchants['fire']('Sword'))
    print(enchants['ice']('Shield'))
    print(enchants['lightning']('Staff'))

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "lightning"]))
    print(dispatch(3.14))