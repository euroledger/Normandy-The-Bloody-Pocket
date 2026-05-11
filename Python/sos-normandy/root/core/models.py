from dataclasses import dataclass, field
from typing import List, Optional, Union

from core.enums import *


# =========================================================
# CORE DOMAIN OBJECTS
# =========================================================

@dataclass
class AlliedArmy:
    name: str
    nation: Nation

    def __str__(self):
        return self.name


@dataclass
class GermanReinforcement:
    type: ReinforcementType
    name: Optional[str] = None

    def __str__(self):

        if self.name:
            return self.name

        return self.type.value


@dataclass
class Condition:
    text: str

    def is_met(self, game_state) -> bool:
        """
        Stub for future game logic.
        """
        return True


# =========================================================
# EFFECTS
# =========================================================

@dataclass
class Effect:

    modifier_type: ModifierType
    value: int

    target: Optional[Union[AlliedArmy, GermanReinforcement]] = None

    resource_type: Optional[ResourceType] = None

    condition: Optional[Condition] = None
    description: Optional[str] = None
    
    label: Optional[str] = None

    def apply(self, game_state):

        if self.condition and not self.condition.is_met(game_state):
            return

        print(f"Applying: {self}")

    def __str__(self):

        parts = []

        # =================================================
        # EFFECT NAME
        # =================================================

        effect_name = self.modifier_type.value

        # Special display names

        if self.modifier_type == ModifierType.AIR_POWER:
            effect_name = "Jabos"

        elif self.modifier_type == ModifierType.REINFORCEMENT:
            effect_name = "Reinforcement"

        elif self.modifier_type == ModifierType.DRM:
            effect_name = "DRM"
            
        elif self.modifier_type == ModifierType.COMMANDER:
            effect_name = self.label if self.label else "Commander"

        # Example:
        # +2 Attack Strength
        # -1 DRM
        # +1 Jabos

        parts.append(f"{self.value:+} {effect_name}")

        # =================================================
        # RESOURCE TYPE
        # =================================================

        # Example:
        # Supply
        # Transport
        # Hitler Approval

        if self.resource_type:
            parts.append(self.resource_type.value)

        # =================================================
        # TARGET
        # =================================================

        # Example:
        # 3rd US
        # Pz Lehr

        if self.target:
            parts.append(str(self.target))

        return " ".join(parts)


# =========================================================
# CARD SECTIONS
# =========================================================

@dataclass
class MilitarySection:
    formations: List[AlliedArmy] = field(default_factory=list)
    effects: List[Effect] = field(default_factory=list)
    text: List[str] = field(default_factory=list)


@dataclass
class AirPowerSection:
    effects: List[Effect] = field(default_factory=list)
    text: List[str] = field(default_factory=list)


@dataclass
class ResourceSection:
    effects: List[Effect] = field(default_factory=list)


@dataclass
class ActionSection:
    actions_available: int = 0
    effects: List[Effect] = field(default_factory=list)


# =========================================================
# CARD OBJECT
# =========================================================

@dataclass
class Card:

    card_id: int
    title: str

    military: MilitarySection = field(default_factory=MilitarySection)
    air_power: AirPowerSection = field(default_factory=AirPowerSection)
    resources: ResourceSection = field(default_factory=ResourceSection)
    actions: ActionSection = field(default_factory=ActionSection)

    # =====================================================
    # CARD SUMMARY
    # =====================================================

    def summary(self):

        print()
        print("=" * 60)
        print(f"CARD #{self.card_id} - {self.title}")
        print("=" * 60)

        # -------------------------------------------------
        # MILITARY
        # -------------------------------------------------

        print("\nMILITARY")

        if (
            not self.military.formations
            and not self.military.effects
            and not self.military.text
        ):
            print("  No Modifiers")

        # Formations

        for formation in self.military.formations:
            print(f"  {formation}")

        # Effects

        for effect in self.military.effects:
            print(f"  {effect}")

        # Text

        for text in self.military.text:
            print(f"  {text}")
            

        # -------------------------------------------------
        # AIR POWER
        # -------------------------------------------------

        print("\nAIR POWER")

        if not self.air_power.effects and not self.air_power.text:
            print("  No Modifiers")

        for effect in self.air_power.effects:
            print(f"  {effect}")

        for text in self.air_power.text:
            print(f"  {text}")

        # -------------------------------------------------
        # RESOURCES
        # -------------------------------------------------

        print("\nRESOURCES")

        if not self.resources.effects:
            print("  N/A")

        for effect in self.resources.effects:
            print(f"  {effect}")

        # -------------------------------------------------
        # ACTIONS
        # -------------------------------------------------

        print("\nACTIONS")
        print(f"  Actions Available: {self.actions.actions_available}")

        if not self.actions.effects:
            print("  No Modifiers")

        for effect in self.actions.effects:
            print(f"  {effect}")