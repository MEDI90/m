from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability


class StrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this normal strategy"
            )
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )

        actions = []
        if isinstance(creature, TransformCapability):
            actions.append(creature.transform())
            actions.append(creature.attack())
            actions.append(creature.revert())
        return actions


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        if not self.is_valid(creature):
            raise StrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )

        actions = []
        actions.append(creature.attack())
        if isinstance(creature, HealCapability):
            actions.append(creature.heal())
        return actions
