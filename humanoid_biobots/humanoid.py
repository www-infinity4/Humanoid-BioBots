"""
HumanoidBioBot — top-level assembly of the biomimetic elemental stack.

The HumanoidBioBot class represents a complete humanoid machine built from
the five-element stack (Mg → In → Yb → Li → Be) and exposes its mechanical
status and environmental constraints.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto

from .layers import Layer, LayerStack


class EnvironmentStatus(Enum):
    """Operational environment status of the BioBot."""

    SEALED = auto()       # Outer membrane intact; fully operational
    BREACHED = auto()     # Membrane breached; reactive layers exposed
    DEGRADED = auto()     # Partial membrane failure; limited operation


@dataclass
class HumanoidBioBot:
    """
    A biomimetic humanoid machine built from the elemental stack
    Mg(12) → In(49) → Yb(70) → Li(3) → Be(4).

    Physical anatomy analogy
    ------------------------
    Be  (4)  — Armored Skin / Exoskeleton
    Li  (3)  — Fast-twitch Muscle Groups
    Yb  (70) — Vital Organs / Radiation Shield
    In  (49) — Subcutaneous Fat / Soft Tissue
    Mg  (12) — Internal Skeleton / Bones
    """

    name: str = "BioBot-Alpha"
    stack: LayerStack = field(default_factory=LayerStack.from_default)
    environment: EnvironmentStatus = EnvironmentStatus.SEALED

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    @property
    def is_operational(self) -> bool:
        """
        The BioBot is fully operational only when its outer membrane is
        sealed, protecting the water-reactive interior layers.
        """
        return self.environment == EnvironmentStatus.SEALED

    @property
    def is_at_risk(self) -> bool:
        """
        Return True if reactive layers are potentially exposed.
        """
        return self.environment in (
            EnvironmentStatus.BREACHED,
            EnvironmentStatus.DEGRADED,
        )

    # ------------------------------------------------------------------
    # Skeletal / layer access
    # ------------------------------------------------------------------

    @property
    def skeleton(self) -> Layer:
        """The internal skeletal bone layer (Magnesium)."""
        return self.stack.inner_layer

    @property
    def armor(self) -> Layer:
        """The outer armored skin layer (Beryllium)."""
        return self.stack.outer_layer

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def status_report(self) -> str:
        """Return a formatted status report for this BioBot."""
        reactive_names = ", ".join(
            layer.element.name for layer in self.stack.reactive_layers
        )
        lines = [
            f"=== {self.name} — Status Report ===",
            f"Environment  : {self.environment.name}",
            f"Operational  : {self.is_operational}",
            f"At Risk      : {self.is_at_risk}",
            f"Total Layers : {len(self.stack.layers)}",
            f"Total Depth  : {self.stack.total_thickness_mm:.1f} mm",
            f"Reactive     : {reactive_names or 'none'}",
            "",
            "--- Anatomy ---",
            self.stack.describe(),
        ]
        if self.is_at_risk:
            lines += [
                "",
                "⚠️  WARNING: Reactive layers (Li, Yb) exposed to environment.",
                "   Immediate re-sealing required to prevent combustion/corrosion.",
            ]
        return "\n".join(lines)

    def __repr__(self) -> str:
        return (
            f"HumanoidBioBot(name={self.name!r}, "
            f"environment={self.environment.name})"
        )


# ---------------------------------------------------------------------------
# Convenience factory
# ---------------------------------------------------------------------------

def build_default_biobot(name: str = "BioBot-Alpha") -> HumanoidBioBot:
    """Return a ready-to-use HumanoidBioBot with the canonical element stack."""
    return HumanoidBioBot(
        name=name,
        stack=LayerStack.from_default(),
        environment=EnvironmentStatus.SEALED,
    )
