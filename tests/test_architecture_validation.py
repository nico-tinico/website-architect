import pytest

from structio.domain.architecture import SiteArchitecture
from structio.domain.enums import (
    LinkType,
    NodeType,
    SiteMode,
    SiteType,
    Topology,
)
from structio.domain.graph import SiteGraph
from structio.domain.links import Link
from structio.domain.nodes import Node
from structio.domain.templates import Template


def make_architecture(
    *,
    nodes: tuple[Node, ...],
    links: tuple[Link, ...] = (),
    templates: tuple[Template, ...] = (),
) -> SiteArchitecture:
    return SiteArchitecture(
        version="1.0",
        site_type=SiteType.SAAS,
        mode=SiteMode.MULTI_PAGE,
        topology=Topology.HIERARCHICAL,
        root_id="home",
        nodes=nodes,
        templates=templates,
        graph=SiteGraph(
            links=links,
        ),
    )


def test_validation_rejects_missing_root() -> None:
    architecture = make_architecture(
        nodes=(
            Node(
                id="about",
                name="About",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose=None,
                parent_id=None,
                position=0,
            ),
        ),
    )

    with pytest.raises(ValueError, match="Root node"):
        architecture.validate()


def test_validation_rejects_unknown_parent() -> None:
    architecture = make_architecture(
        nodes=(
            Node(
                id="home",
                name="Home",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose=None,
                parent_id=None,
                position=0,
            ),
            Node(
                id="about",
                name="About",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose=None,
                parent_id="does-not-exist",
                position=0,
            ),
        ),
    )

    with pytest.raises(ValueError, match="unknown parent"):
        architecture.validate()


def test_validation_rejects_unknown_link_target() -> None:
    architecture = make_architecture(
        nodes=(
            Node(
                id="home",
                name="Home",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose=None,
                parent_id=None,
                position=0,
            ),
        ),
        links=(
            Link(
                source="home",
                target="missing",
                link_type=LinkType.NAVIGATION,
            ),
        ),
    )

    with pytest.raises(ValueError, match="Link target"):
        architecture.validate()


def test_template_ids_must_be_unique() -> None:
    template = Template(
        id="product",
        name="Product",
        required=True,
        repeatable=True,
        purpose="Defines a product.",
    )

    architecture = make_architecture(
        nodes=(
            Node(
                id="home",
                name="Home",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose="Website home page.",
                parent_id=None,
                position=0,
            ),
        ),
        templates=(template, template),
    )

    with pytest.raises(
        ValueError,
        match="Duplicate template IDs",
    ):
        architecture.validate()


def test_collection_item_template_must_exist() -> None:
    architecture = make_architecture(
        nodes=(
            Node(
                id="home",
                name="Home",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose="Website home page.",
                parent_id=None,
                position=0,
            ),
            Node(
                id="home.products",
                name="Products",
                node_type=NodeType.COLLECTION,
                required=True,
                repeatable=False,
                purpose="Groups products.",
                parent_id="home",
                position=0,
                item_template="product",
            ),
        ),
        templates=(),
    )

    with pytest.raises(
        ValueError,
        match="unknown item template",
    ):
        architecture.validate()


def test_collection_item_template_can_resolve() -> None:
    architecture = make_architecture(
        nodes=(
            Node(
                id="home",
                name="Home",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose="Website home page.",
                parent_id=None,
                position=0,
            ),
            Node(
                id="home.products",
                name="Products",
                node_type=NodeType.COLLECTION,
                required=True,
                repeatable=False,
                purpose="Groups products.",
                parent_id="home",
                position=0,
                item_template="product",
            ),
        ),
        templates=(
            Template(
                id="product",
                name="Product",
                required=True,
                repeatable=True,
                purpose="Defines a product.",
            ),
        ),
    )

    architecture.validate()


def test_entry_point_target_template_must_exist() -> None:
    architecture = make_architecture(
        nodes=(
            Node(
                id="home",
                name="Home",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose="Website home page.",
                parent_id=None,
                position=0,
            ),
            Node(
                id="home.product",
                name="Product",
                node_type=NodeType.ENTRY_POINT,
                required=True,
                repeatable=False,
                purpose="Provides access to products.",
                parent_id="home",
                position=0,
                target_template="product",
            ),
        ),
        templates=(),
    )

    with pytest.raises(
        ValueError,
        match="unknown target template",
    ):
        architecture.validate()