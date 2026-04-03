from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    StrategyError
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print(f"*** Tournament ***\n{len(opponents)} opponents involved")

    # Round-robin: each opponent fights every other opponent exactly once
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            fac1, strat1 = opponents[i]
            fac2, strat2 = opponents[j]

            # Spawn the fighters
            fighter1 = fac1.create_base()
            fighter2 = fac2.create_base()

            print("* Battle *")
            print(fighter1.describe())
            print("VS.")
            print(fighter2.describe())
            print("now fight!")

            try:
                # Fighter 1 acts
                actions1 = strat1.act(fighter1)
                for action in actions1:
                    print(action)

                # Fighter 2 acts
                actions2 = strat2.act(fighter2)
                for action in actions2:
                    print(action)

            except StrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return  # Abort the entire tournament on error


def main() -> None:
    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("\nTournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ])

    print("\nTournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ])


if __name__ == "__main__":
    main()
