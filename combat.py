class Combatant:
    """Base class for all combatants.
    This interface is required to support combat.
    """
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
        # Defence is temporarily boosted by some moves
        self.defence = 0

    def boost_defence(self, amount: int) -> int:
        """Boosts the defence of the combatant."""
        self.defence += amount
        return amount

    def heal(self, amount: int) -> int:
        """Heal the combatant by the given amount.
        Returns the amount of health restored.
        """
        self.hp += amount
        return amount

    def is_dead(self) -> bool:
        """Returns True if the combatant is dead."""
        return self.hp <= 0

    def reset_defence(self):
        """Resets the defence of the combatant."""
        self.defence = 0

    def take_damage(self, damage: int) -> int:
        """Deal damage to the combatant.
        Returns the amount of damage taken.
        """
        # Damage is absorbed by defence first
        while self.defence > 0 and damage > 0:
            damage -= 1
            self.defence -= 1
        # Remaining damage is dealt to hp
        self.hp -= damage
        return damage
