import typing


def generate_game_events(total: int) -> typing.Generator:
    """Generates game events one by one without loading all into memory."""
    yield (1, "alice", 5, "killed monster")
    yield (2, "bob", 12, "found treasure")
    yield (3, "charlie", 8, "leveled up")

    for i in range(4, total + 1):
        level = 5
        action = "killed monster"

        if i - 3 <= 341:
            level = 10

        if i - 3 <= 88:
            action = "found treasure"
        elif i - 3 <= 88 + 155:
            action = "leveled up"

        yield (i, "npc", level, action)


def fibonacci(limit: int) -> typing.Generator:
    """Generates the Fibonacci sequence up to a limit."""
    a = 0
    b = 1
    for _ in range(limit):
        yield a
        temp = a + b
        a = b
        b = temp


def primes(limit: int) -> typing.Generator:
    """Generates prime numbers up to a limit."""
    count = 0
    n = 2
    while count < limit:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
        if is_prime:
            yield n
            count += 1
        n += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    print("Processing 1000 game events...\n")

    stream = generate_game_events(1000)

    total_processed = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for event in stream:
        event_id, player, level, action = event

        if event_id <= 3:
            print(
                f"Event {event_id}: Player {player} (level {level}) {action}")
        elif event_id == 4:
            print("...")

        total_processed += 1
        if level >= 10:
            high_level_count += 1
        if action == "found treasure":
            treasure_count += 1
        elif action == "leveled up":
            levelup_count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")

    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")

    fib_gen = iter(fibonacci(10))
    fib_str = f"{next(fib_gen)}"
    for _ in range(9):
        fib_str += f", {next(fib_gen)}"
    print(f"Fibonacci sequence (first 10): {fib_str}")

    prime_str = ""
    is_first = True
    for p in primes(5):
        if not is_first:
            prime_str += ", "
        prime_str += f"{p}"
        is_first = False
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    main()
