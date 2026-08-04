"""
Tests for the Humanoid BioBot elemental stack implementation.
"""

import pytest

from humanoid_biobots import (
    BERYLLIUM,
    ELEMENT_STACK,
    INDIUM,
    LITHIUM,
    MAGNESIUM,
    YTTERBIUM,
    EnvironmentStatus,
    HumanoidBioBot,
    Layer,
    LayerStack,
    build_default_biobot,
)


# ---------------------------------------------------------------------------
# Element tests
# ---------------------------------------------------------------------------


class TestElements:
    def test_element_stack_order(self):
        """Stack must follow the canonical Mg→In→Yb→Li→Be sequence."""
        expected = [12, 49, 70, 3, 4]
        actual = [el.atomic_number for el in ELEMENT_STACK]
        assert actual == expected

    def test_element_symbols(self):
        expected = ["Mg", "In", "Yb", "Li", "Be"]
        actual = [el.symbol for el in ELEMENT_STACK]
        assert actual == expected

    def test_magnesium_properties(self):
        assert MAGNESIUM.atomic_number == 12
        assert MAGNESIUM.symbol == "Mg"
        assert not MAGNESIUM.is_reactive_with_water
        assert MAGNESIUM.density < 2.0  # lightweight structural metal

    def test_indium_is_soft(self):
        assert INDIUM.atomic_number == 49
        assert INDIUM.hardness_mohs < 2.0  # very soft

    def test_ytterbium_is_heavy(self):
        assert YTTERBIUM.atomic_number == 70
        assert YTTERBIUM.atomic_weight > 150  # heavy rare-earth

    def test_lithium_is_least_dense(self):
        assert LITHIUM.atomic_number == 3
        assert LITHIUM.density < 1.0  # lighter than water
        assert LITHIUM.is_reactive_with_water

    def test_beryllium_is_hard(self):
        assert BERYLLIUM.atomic_number == 4
        assert BERYLLIUM.hardness_mohs > 5  # hard outer shell
        assert not BERYLLIUM.is_reactive_with_water


# ---------------------------------------------------------------------------
# LayerStack tests
# ---------------------------------------------------------------------------


class TestLayerStack:
    def test_default_stack_has_five_layers(self):
        stack = LayerStack.from_default()
        assert len(stack.layers) == 5

    def test_inner_layer_is_magnesium(self):
        stack = LayerStack.from_default()
        assert stack.inner_layer.element.symbol == "Mg"

    def test_outer_layer_is_beryllium(self):
        stack = LayerStack.from_default()
        assert stack.outer_layer.element.symbol == "Be"

    def test_total_thickness(self):
        stack = LayerStack.from_default(thickness_mm=5.0)
        assert stack.total_thickness_mm == pytest.approx(25.0)

    def test_has_reactive_layers(self):
        stack = LayerStack.from_default()
        assert stack.has_reactive_layers is True

    def test_reactive_layer_count(self):
        stack = LayerStack.from_default()
        reactive_symbols = {l.element.symbol for l in stack.reactive_layers}
        assert "Li" in reactive_symbols
        assert "Yb" in reactive_symbols

    def test_describe_contains_all_elements(self):
        stack = LayerStack.from_default()
        description = stack.describe()
        for el in ELEMENT_STACK:
            assert el.name in description


# ---------------------------------------------------------------------------
# HumanoidBioBot tests
# ---------------------------------------------------------------------------


class TestHumanoidBioBot:
    def test_build_default_biobot(self):
        bot = build_default_biobot("TestBot")
        assert bot.name == "TestBot"
        assert bot.environment == EnvironmentStatus.SEALED

    def test_sealed_is_operational(self):
        bot = build_default_biobot()
        assert bot.is_operational is True
        assert bot.is_at_risk is False

    def test_breached_not_operational(self):
        bot = HumanoidBioBot(environment=EnvironmentStatus.BREACHED)
        assert bot.is_operational is False
        assert bot.is_at_risk is True

    def test_degraded_not_operational(self):
        bot = HumanoidBioBot(environment=EnvironmentStatus.DEGRADED)
        assert bot.is_operational is False
        assert bot.is_at_risk is True

    def test_skeleton_is_magnesium(self):
        bot = build_default_biobot()
        assert bot.skeleton.element.symbol == "Mg"

    def test_armor_is_beryllium(self):
        bot = build_default_biobot()
        assert bot.armor.element.symbol == "Be"

    def test_status_report_contains_name(self):
        bot = build_default_biobot("MyBioBot")
        report = bot.status_report()
        assert "MyBioBot" in report

    def test_status_report_warning_when_breached(self):
        bot = HumanoidBioBot(environment=EnvironmentStatus.BREACHED)
        report = bot.status_report()
        assert "WARNING" in report

    def test_status_report_no_warning_when_sealed(self):
        bot = build_default_biobot()
        report = bot.status_report()
        assert "WARNING" not in report
