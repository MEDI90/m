import time
from functools import wraps
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')

            if power is None:
                if args and isinstance(args[0], int):
                    power = args[0]
                elif len(args) >= 3 and isinstance(args[2], int):
                    power = args[2]

            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self: Any, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
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
    print(MageGuild.validate_mage_name("Valid Name"))
    print(MageGuild.validate_mage_name("A1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
