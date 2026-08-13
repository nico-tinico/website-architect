import pytest

from website_architect.domain.architecture import SiteArchitecture
from website_architect.domain.enums import (
    LinkType,
    NodeType,
    SiteMode,
    SiteType,
    Topology,
)
from website_architect.domain.graph import SiteGraph
from website_architect.domain.links import Link
from website_architect.domain.nodes import Node


def make_architecture(
    nodes: tuple[Node, ...],
    links: tuple[Link, ...] = (),
) -> SiteArchitecture:
    return SiteArchitecture(
        version="1.0",
        site_type=SiteType.SAAS,
        mode=SiteMode.MULTI_PAGE,
        topology=Topology.HIERARCHICAL,
        root_id="home",
        nodes=nodes,
        graph=SiteGraph(links=links),
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
