import pytest

from website_architect.catalog.profiles import PROFILES
from website_architect.domain.enums import SiteMode, SiteType
from website_architect.generator.generator import ArchitectureGenerator


@pytest.mark.parametrize(
    "site_type",
    list(SiteType),
)
@pytest.mark.parametrize(
    "mode",
    list(SiteMode),
)
def test_all_site_type_and_mode_combinations(
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    architecture.validate()

    assert architecture.site_type is site_type
    assert architecture.mode is mode
    assert architecture.root_id == "home"
    assert architecture.nodes


@pytest.mark.parametrize(
    "site_type",
    list(SiteType),
)
@pytest.mark.parametrize(
    "mode",
    list(SiteMode),
)
def test_all_generated_nodes_have_purpose(
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    for node in architecture.nodes:
        assert node.purpose.strip(), (
            f"Node '{node.id}' has no purpose."
        )