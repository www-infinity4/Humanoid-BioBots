"""
Humanoid BioBots — biomimetic humanoid machine built from the elemental stack
Mg(12) → In(49) → Yb(70) → Li(3) → Be(4).
"""

from .elements import (  # noqa: F401
    Element,
    ELEMENT_STACK,
    MAGNESIUM,
    INDIUM,
    YTTERBIUM,
    LITHIUM,
    BERYLLIUM,
)
from .layers import Layer, LayerStack  # noqa: F401
from .humanoid import (  # noqa: F401
    EnvironmentStatus,
    HumanoidBioBot,
    build_default_biobot,
)

__all__ = [
    "Element",
    "ELEMENT_STACK",
    "MAGNESIUM",
    "INDIUM",
    "YTTERBIUM",
    "LITHIUM",
    "BERYLLIUM",
    "Layer",
    "LayerStack",
    "EnvironmentStatus",
    "HumanoidBioBot",
    "build_default_biobot",
]
