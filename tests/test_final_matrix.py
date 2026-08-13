import json
import subprocess
import sys
from pathlib import Path

import pytest

from website_architect.domain.enums import SiteMode, SiteType
from website_architect.generator.generator import ArchitectureGenerator
from website_architect.serializers.json import JsonSerializer


SITE_TYPES = (
    SiteType.LANDING_PAGE,
    SiteType.SAAS,
    SiteType.AGENCY,
    SiteType.PORTFOLIO,
    SiteType.ECOMMERCE,
    SiteType.TRAVEL,
    SiteType.WELLNESS,
    SiteType.FINTECH,
    SiteType.TECHNOLOGY,
    SiteType.FASHION,
)

SITE_MODES = (
    SiteMode.SINGLE_PAGE,
    SiteMode.MULTI_PAGE,
)


COMBINATIONS = [
    (site_type, mode)
    for site_type in SITE_TYPES
    for mode in SITE_MODES
]


@pytest.fixture
def generator() -> ArchitectureGenerator:
    return ArchitectureGenerator()


@pytest.fixture
def serializer() -> JsonSerializer:
    return JsonSerializer()


@pytest.mark.parametrize(
    ("site_type", "mode"),
    COMBINATIONS,
)
def test_all_site_combinations_generate(
    generator: ArchitectureGenerator,
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    assert architecture.site_type is site_type
    assert architecture.mode is mode
    assert architecture.root_id == "home"
    assert architecture.nodes


@pytest.mark.parametrize(
    ("site_type", "mode"),
    COMBINATIONS,
)
def test_all_site_combinations_validate(
    generator: ArchitectureGenerator,
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    architecture.validate()


@pytest.mark.parametrize(
    ("site_type", "mode"),
    COMBINATIONS,
)
def test_all_site_combinations_have_valid_node_references(
    generator: ArchitectureGenerator,
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    node_ids = {
        node.id
        for node in architecture.nodes
    }

    template_ids = {
        template.id
        for template in architecture.templates
    }

    for node in architecture.nodes:
        if node.parent_id is not None:
            assert node.parent_id in node_ids

        if node.item_template is not None:
            assert node.item_template in template_ids

        if node.target_template is not None:
            assert node.target_template in template_ids

    for link in architecture.graph.links:
        assert link.source in node_ids
        assert link.target in node_ids


@pytest.mark.parametrize(
    ("site_type", "mode"),
    COMBINATIONS,
)
def test_all_site_combinations_serialize(
    generator: ArchitectureGenerator,
    serializer: JsonSerializer,
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    content = serializer.serialize(architecture)

    data = json.loads(content)

    assert data["version"] == architecture.version
    assert data["site"]["type"] == site_type.value
    assert data["site"]["mode"] == mode.value
    assert data["root_id"] == "home"
    assert data["nodes"]
    assert "templates" in data
    assert "links" in data


@pytest.mark.parametrize(
    ("site_type", "mode"),
    COMBINATIONS,
)
def test_all_site_combinations_have_consistent_templates(
    generator: ArchitectureGenerator,
    serializer: JsonSerializer,
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    data = json.loads(
        serializer.serialize(architecture)
    )

    template_ids = {
        template["id"]
        for template in data["templates"]
    }

    for node in data["nodes"]:
        if "item_template" in node:
            assert node["item_template"] in template_ids

        if "target_template" in node:
            assert node["target_template"] in template_ids


@pytest.mark.parametrize(
    ("site_type", "mode"),
    COMBINATIONS,
)
def test_all_site_combinations_round_trip(
    generator: ArchitectureGenerator,
    serializer: JsonSerializer,
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    original = serializer.serialize(architecture)

    restored = serializer.deserialize(original)

    restored.validate()

    result = serializer.serialize(restored)

    assert json.loads(result) == json.loads(original)


@pytest.mark.parametrize(
    ("site_type", "mode"),
    COMBINATIONS,
)
def test_all_site_combinations_cli(
    site_type: SiteType,
    mode: SiteMode,
    tmp_path: Path,
) -> None:
    output = tmp_path / (
        f"{site_type.value}-{mode.value}.json"
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "website_architect.cli",
            "generate",
            "--type",
            site_type.value,
            "--mode",
            mode.value,
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert output.exists()

    data = json.loads(
        output.read_text(encoding="utf-8")
    )

    assert data["site"]["type"] == site_type.value
    assert data["site"]["mode"] == mode.value
    assert data["root_id"] == "home"
    assert data["nodes"]


def test_final_matrix_contains_twenty_combinations() -> None:
    assert len(COMBINATIONS) == 20

    assert len(SITE_TYPES) == 10
    assert len(SITE_MODES) == 2

    assert len(set(COMBINATIONS)) == 20


@pytest.mark.parametrize("site_type", SITE_TYPES)
def test_every_site_type_supports_both_modes(
    generator: ArchitectureGenerator,
    site_type: SiteType,
) -> None:
    for mode in SITE_MODES:
        architecture = generator.generate(
            site_type=site_type,
            mode=mode,
        )

        assert architecture.site_type is site_type
        assert architecture.mode is mode
        architecture.validate()