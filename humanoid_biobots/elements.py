"""
Elemental definitions for the Humanoid BioBot stack.

The five elements are selected for their unique mechanical, physical, and
electrochemical properties that together create a biomimetic analog for
human anatomy.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Element:
    """Represents a chemical element with relevant physical properties."""

    atomic_number: int
    symbol: str
    name: str
    atomic_weight: float          # g/mol
    density: float                # g/cm³
    hardness_mohs: Optional[float]  # Mohs scale (None if unmeasured)
    is_reactive_with_water: bool
    humanoid_role: str
    humanoid_analog: str
    description: str


# ---------------------------------------------------------------------------
# The five-element BioBot stack (listed from base/internal to top/external)
# ---------------------------------------------------------------------------

MAGNESIUM = Element(
    atomic_number=12,
    symbol="Mg",
    name="Magnesium",
    atomic_weight=24.305,
    density=1.738,
    hardness_mohs=2.5,
    is_reactive_with_water=False,
    humanoid_role="Internal Skeleton",
    humanoid_analog="Lightweight Internal Skeletal Bones",
    description=(
        "Magnesium has one of the highest strength-to-weight ratios of any "
        "structural metal. It is light, rigid, and absorbs vibrations "
        "incredibly well, mimicking the lightweight but strong nature of "
        "porous human bone."
    ),
)

INDIUM = Element(
    atomic_number=49,
    symbol="In",
    name="Indium",
    atomic_weight=114.818,
    density=7.31,
    hardness_mohs=1.2,
    is_reactive_with_water=False,
    humanoid_role="Soft Subcutaneous Tissue",
    humanoid_analog="Ultra-Soft Subcutaneous Fat",
    description=(
        "Indium is a post-transition metal so exceptionally soft it can be "
        "cut with a kitchen knife. It does not break under pressure; it "
        "slowly squishes and molds, acting like dense synthetic flesh or "
        "cartilage that absorbs heavy impacts without cracking."
    ),
)

YTTERBIUM = Element(
    atomic_number=70,
    symbol="Yb",
    name="Ytterbium",
    atomic_weight=173.045,
    density=6.90,
    hardness_mohs=None,
    is_reactive_with_water=True,
    humanoid_role="Dense Internal Core / Radiation Shield",
    humanoid_analog="High-Density Inner Core / Vital Organs",
    description=(
        "Ytterbium is a heavy rare-earth lanthanide. Its massive atomic "
        "weight gives it excellent radiation shielding properties, yet it "
        "remains soft and highly ductile, bending and flexing without "
        "snapping during movement."
    ),
)

LITHIUM = Element(
    atomic_number=3,
    symbol="Li",
    name="Lithium",
    atomic_weight=6.941,
    density=0.534,
    hardness_mohs=0.6,
    is_reactive_with_water=True,
    humanoid_role="Ultralight Actuator / Muscle Battery",
    humanoid_analog="Super-lightweight Muscle Tissue",
    description=(
        "Lithium is the least dense solid element on Earth — it literally "
        "floats on water. Used as a thick volumetric layer, the humanoid "
        "gains lifelike body mass without becoming heavy. Its massive "
        "electrochemical energy potential acts like a biological muscle "
        "battery."
    ),
)

BERYLLIUM = Element(
    atomic_number=4,
    symbol="Be",
    name="Beryllium",
    atomic_weight=9.0122,
    density=1.85,
    hardness_mohs=5.5,
    is_reactive_with_water=False,
    humanoid_role="Armored Outer Shell",
    humanoid_analog="Rigid Exoskeleton / Armored Skin",
    description=(
        "Beryllium is incredibly stiff, hard, lightweight, and resists "
        "bending or warping under extreme heat and stress. Placed at the "
        "outer layer, it provides a high-performance protective shell over "
        "the softer interior materials."
    ),
)

# Canonical stack order: base (internal) → top (external)
ELEMENT_STACK: tuple[Element, ...] = (
    MAGNESIUM,
    INDIUM,
    YTTERBIUM,
    LITHIUM,
    BERYLLIUM,
)
