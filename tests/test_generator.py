from structio.domain.enums import (
    SiteMode,
    SiteType,
    Topology,
)
from structio.generator.generator import ArchitectureGenerator


def test_generate_saas_multi_page() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.SAAS,
        mode=SiteMode.MULTI_PAGE,
    )

    assert architecture.version == "1.0"
    assert architecture.site_type is SiteType.SAAS
    assert architecture.mode is SiteMode.MULTI_PAGE
    assert architecture.topology is Topology.HIERARCHICAL
    assert architecture.root_id == "home"

    node_ids = {node.id for node in architecture.nodes}

    assert "home" in node_ids
    assert "home.product" in node_ids
    assert "home.pricing" in node_ids

    assert architecture.graph.links


def test_generate_landing_single_page() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.LANDING_PAGE,
        mode=SiteMode.SINGLE_PAGE,
    )

    assert architecture.topology is Topology.SEQUENTIAL

    node_ids = {node.id for node in architecture.nodes}

    assert "home" in node_ids
    assert "home.hero" in node_ids
    assert "home.cta" in node_ids