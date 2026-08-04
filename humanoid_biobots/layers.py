"""
Layer model for the Humanoid BioBot stack.

Each Layer wraps an Element with a thickness (in mm) and optional notes,
and exposes computed biomechanical properties.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .elements import Element, ELEMENT_STACK


@dataclass
class Layer:
    """A single layer in the BioBot physical stack."""

    element: Element
    thickness_mm: float
    notes: str = ""

    # ------------------------------------------------------------------
    # Derived properties
    # ------------------------------------------------------------------

    @property
    def is_reactive(self) -> bool:
        """Return True if the element is reactive with water/air."""
        return self.element.is_reactive_with_water

    @property
    def label(self) -> str:
        """Human-readable label for display."""
        return (
            f"[{self.element.atomic_number}] {self.element.name} "
            f"({self.element.symbol}) — {self.element.humanoid_role}"
        )

    def __repr__(self) -> str:
        return (
            f"Layer(element={self.element.symbol!r}, "
            f"thickness_mm={self.thickness_mm}, "
            f"reactive={self.is_reactive})"
        )


@dataclass
class LayerStack:
    """
    An ordered sequence of layers composing the BioBot body.

    Layers are stored from base/internal (index 0) to top/external (index -1).
    """

    layers: List[Layer] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Factory
    # ------------------------------------------------------------------

    @classmethod
    def from_default(cls, thickness_mm: float = 10.0) -> "LayerStack":
        """
        Build the canonical five-layer stack with a uniform thickness.

        Stack order (base → top):
          Mg(12) → In(49) → Yb(70) → Li(3) → Be(4)
        """
        return cls(
            layers=[Layer(element=el, thickness_mm=thickness_mm) for el in ELEMENT_STACK]
        )

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def total_thickness_mm(self) -> float:
        """Sum of all layer thicknesses in mm."""
        return sum(layer.thickness_mm for layer in self.layers)

    @property
    def has_reactive_layers(self) -> bool:
        """Return True if any layer contains a water-reactive element."""
        return any(layer.is_reactive for layer in self.layers)

    @property
    def reactive_layers(self) -> List[Layer]:
        """Return the subset of layers that are water-reactive."""
        return [layer for layer in self.layers if layer.is_reactive]

    @property
    def outer_layer(self) -> Layer:
        """The topmost (external/armored) layer."""
        return self.layers[-1]

    @property
    def inner_layer(self) -> Layer:
        """The bottommost (internal/skeletal) layer."""
        return self.layers[0]

    # ------------------------------------------------------------------
    # Display
    # ------------------------------------------------------------------

    def describe(self) -> str:
        """Return a human-readable description of the full stack."""
        lines = [
            "[ TOP CAP: OUTSIDE WORLD ]",
            "           │",
        ]
        for layer in reversed(self.layers):
            arrow = "──>" if not layer.is_reactive else "~~>"
            lines.append(
                f"           ├── {layer.element.name} ({layer.element.atomic_number})"
                f"   {arrow} {layer.element.humanoid_analog}"
            )
        lines += [
            "           │",
            "[ BASE CORE: INTERNAL ]",
        ]
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"LayerStack(layers={self.layers!r})"
