from website_architect.catalog.profiles import PROFILES
from website_architect.domain.enums import NodeType, SiteMode, SiteType
from website_architect.generator.generator import ArchitectureGenerator


def test_generated_architecture_contains_templates() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    assert architecture.templates


def test_generated_templates_are_not_nodes() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    node_ids = {
        node.id
        for node in architecture.nodes
    }

    template_ids = {
        template.id
        for template in architecture.templates
    }

    assert node_ids.isdisjoint(template_ids)


def test_generated_templates_are_repeatable() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    assert all(
        template.repeatable
        for template in architecture.templates
    )


def test_collection_resolves_to_generated_template() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    template_ids = {
        template.id
        for template in architecture.templates
    }

    collections = [
        node
        for node in architecture.nodes
        if node.node_type is NodeType.COLLECTION
    ]

    assert collections

    for collection in collections:
        assert collection.item_template in template_ids


def test_entry_point_resolves_to_generated_template() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    template_ids = {
        template.id
        for template in architecture.templates
    }

    entry_points = [
        node
        for node in architecture.nodes
        if node.node_type is NodeType.ENTRY_POINT
    ]

    for entry_point in entry_points:
        assert entry_point.target_template in template_ids


def test_generated_templates_match_profile_templates() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    profile = PROFILES[SiteType.ECOMMERCE]

    expected_ids = {
        template.name.strip().lower().replace(" ", "-")
        for template in profile.templates
    }

    actual_ids = {
        template.id
        for template in architecture.templates
    }

    assert actual_ids == expected_ids