import pytest

from structio.catalog.profiles import PROFILES
from structio.domain.enums import NodeType, SiteType


def collect_nodes(nodes):
    result = []

    def visit(definitions):
        for node in definitions:
            result.append(node)
            visit(node.children)

    visit(nodes)
    return result


@pytest.mark.parametrize("site_type", list(SiteType))
def test_profile_templates_are_unique(site_type: SiteType) -> None:
    profile = PROFILES[site_type]

    names = [
        template.name
        for template in profile.templates
    ]

    assert len(names) == len(set(names))


@pytest.mark.parametrize("site_type", list(SiteType))
def test_profile_templates_are_repeatable(site_type: SiteType) -> None:
    profile = PROFILES[site_type]

    for template in profile.templates:
        assert template.repeatable is True


@pytest.mark.parametrize("site_type", list(SiteType))
def test_collection_references_existing_template(
    site_type: SiteType,
) -> None:
    profile = PROFILES[site_type]

    template_names = {
        template.name
        for template in profile.templates
    }

    nodes = collect_nodes(profile.multi_page)

    for node in nodes:
        if node.node_type == NodeType.COLLECTION:
            assert node.item_template in template_names


@pytest.mark.parametrize("site_type", list(SiteType))
def test_entry_point_references_existing_template(
    site_type: SiteType,
) -> None:
    profile = PROFILES[site_type]

    template_names = {
        template.name
        for template in profile.templates
    }

    nodes = collect_nodes(profile.multi_page)

    for node in nodes:
        if node.node_type == NodeType.ENTRY_POINT:
            assert node.target_template in template_names


def test_ecommerce_product_template_is_defined_once() -> None:
    profile = PROFILES[SiteType.ECOMMERCE]

    product_templates = [
        template
        for template in profile.templates
        if template.name == "Product"
    ]

    assert len(product_templates) == 1


def test_ecommerce_category_references_product_template() -> None:
    profile = PROFILES[SiteType.ECOMMERCE]

    nodes = collect_nodes(profile.multi_page)

    category = next(
        node
        for node in nodes
        if node.name == "Category"
        and node.node_type == NodeType.COLLECTION
    )

    assert category.item_template == "Product"


def test_ecommerce_product_entry_point_targets_product_template() -> None:
    profile = PROFILES[SiteType.ECOMMERCE]

    nodes = collect_nodes(profile.multi_page)

    product = next(
        node
        for node in nodes
        if node.name == "Product"
        and node.node_type == NodeType.ENTRY_POINT
    )

    assert product.target_template == "Product"