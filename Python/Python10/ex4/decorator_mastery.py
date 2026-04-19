import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {getattr(func, '__name__', 'unknown')}...")
        start_time = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end_time = time.time()
            print(f"Spell completed in {end_time - start_time:.3f} seconds")

    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    try:
        safe_min_power = int(min_power)
    except (ValueError, TypeError):
        safe_min_power = 0

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power: Any = None

            if 'power' in kwargs:
                power = kwargs['power']
            elif len(args) >= 3:
                power = args[2]
            elif len(args) >= 1:
                power = args[0]

            try:
                if power is not None and int(power) >= safe_min_power:
                    return func(*args, **kwargs)
            except (ValueError, TypeError):
                pass

            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    try:
        safe_max = int(max_attempts)
    except (ValueError, TypeError):
        safe_max = 1

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, safe_max + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < safe_max:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{safe_max})"
                        )
            return f"Spell casting failed after {safe_max} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str):
            return False
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("--- Standard Data Tests ---")
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell")
    fail_count = 0

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        global fail_count
        fail_count += 1
        if fail_count <= 3:
            raise Exception("Fizzled")
        return "Waaaaaaagh spelled !"

    print(unstable_spell())

    @retry_spell(max_attempts=3)
    def stable_spell() -> str:
        return "Waaaaaaagh spelled !"

    print(stable_spell())

    print("\nTesting MageGuild...")
    print(f"Valid Name: {MageGuild.validate_mage_name('Valid Name')}")
    print(f"Invalid Name (A1): {MageGuild.validate_mage_name('A1')}")

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))

    print("\n--- Malicious Peer Tests ---")
    bad_name: Any = None
    print(f"Invalid Name (None): {MageGuild.validate_mage_name(bad_name)}")

    bad_int_name: Any = 123
    print(f"Invalid Name (int): {MageGuild.validate_mage_name(bad_int_name)}")

    bad_power: Any = "not an int"
    print(f"Corrupt Cast: {guild.cast_spell('Lightning', bad_power)}")
