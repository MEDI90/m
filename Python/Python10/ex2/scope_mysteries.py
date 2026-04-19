from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable[..., Any]:
    count = 0

    def counter() -> int | str:
        nonlocal count
        try:
            count += 1
            return count
        except Exception:
            return "Counter corrupted"
    return counter


def spell_accumulator(initial_power: int) -> Callable[..., Any]:
    try:
        total_power = int(initial_power)
    except (ValueError, TypeError):
        total_power = 0

    def accumulator(added_power: int) -> int | str:
        nonlocal total_power
        try:
            total_power += int(added_power)
            return total_power
        except (ValueError, TypeError):
            return "Invalid power input"
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[..., Any]:
    def enchanter(item_name: str) -> str:
        try:
            return f"{str(enchantment_type)} {str(item_name)}"
        except Exception:
            return "Enchantment failed"
    return enchanter


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[Any, Any] = {}

    def store(key: str, value: Any) -> None:
        try:
            memory[key] = value
        except TypeError:
            pass

    def recall(key: str) -> Any:
        try:
            return memory.get(key, "Memory not found")
        except TypeError:
            return "Memory not found"

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("--- Standard Data Tests ---")
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    flame_enchanter = enchantment_factory("Flaming")
    frost_enchanter = enchantment_factory("Frozen")
    print(flame_enchanter("Sword"))
    print(frost_enchanter("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")

    print("\n--- Malicious Peer Tests ---")
    
    bad_initial_power: Any = "100"
    bad_accumulator = spell_accumulator(bad_initial_power)
    print(f"Corrupt Acc Add int: {bad_accumulator(20)}")
    
    bad_added_power_str: Any = '30'
    print(f"Corrupt Acc Add str: {bad_accumulator(bad_added_power_str)}")
    
    bad_added_power_dict: Any = {'bad': 'data'}
    print(f"Corrupt Acc Add dict: {bad_accumulator(bad_added_power_dict)}")

    bad_unhashable_key: Any = ['unhashable', 'list']
    vault['store'](bad_unhashable_key, 'secret data')
    print(f"Recall unhashable key: {vault['recall'](bad_unhashable_key)}")