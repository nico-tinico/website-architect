import pytest

from structio.catalog.definitions import LinkRule
from structio.domain.enums import LinkType
from structio.generator.graph_builder import GraphBuilder


def test_graph_builder_resolves_root_nodes() -> None:
    builder = GraphBuilder()

    graph = builder.build(
        rules=(
            LinkRule(
                "Home",
                "Product",
                LinkType.NAVIGATION,
            ),
        ),
        node_ids={
            "home",
            "home.product",
        },
    )

    assert len(graph.links) == 1

    link = graph.links[0]

    assert link.source == "home"
    assert link.target == "home.product"


def test_graph_builder_rejects_unknown_source() -> None:
    builder = GraphBuilder()

    with pytest.raises(ValueError, match="source"):
        builder.build(
            rules=(
                LinkRule(
                    "Missing",
                    "Product",
                    LinkType.NAVIGATION,
                ),
            ),
            node_ids={
                "home",
                "home.product",
            },
        )


def test_graph_builder_resolves_nested_semantic_path() -> None:
    builder = GraphBuilder()

    graph = builder.build(
        rules=(
            LinkRule(
                "Product.Security",
                "Signup",
                LinkType.NAVIGATION,
            ),
        ),
        node_ids={
            "home",
            "home.product",
            "home.product.security",
            "home.signup",
        },
    )

    assert len(graph.links) == 1

    link = graph.links[0]

    assert link.source == "home.product.security"
    assert link.target == "home.signup"


def test_graph_builder_does_not_use_suffix_matching() -> None:
    builder = GraphBuilder()

    graph = builder.build(
        rules=(
            LinkRule(
                "Security",
                "Signup",
                LinkType.NAVIGATION,
            ),
        ),
        node_ids={
            "home",
            "home.security",
            "home.product.security",
            "home.signup",
        },
    )

    link = graph.links[0]

    assert link.source == "home.security"