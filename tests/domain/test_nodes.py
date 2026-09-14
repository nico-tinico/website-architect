import pytest

from structio.domain.enums import NodeType
from structio.domain.nodes import Node
from structio.domain.nodes import PageDefinition


def make_node(
    node_type: NodeType,
    *,
    repeatable: bool = False,
    item_template: str | None = None,
    target_template: str | None = None,
) -> PageDefinition:
    return PageDefinition(
        name="Test",
        node_type=node_type,
        required=True,
        repeatable=repeatable,
        purpose="Test node purpose.",
        children=(),
        item_template=item_template,
        target_template=target_template,
    )


def test_template_must_be_repeatable() -> None:
    with pytest.raises(
        ValueError,
        match="Template nodes must be repeatable",
    ):
        make_node(
            NodeType.TEMPLATE,
            repeatable=False,
        )


def test_template_is_repeatable() -> None:
    node = make_node(
        NodeType.TEMPLATE,
        repeatable=True,
    )

    assert node.repeatable is True


def test_page_cannot_be_repeatable() -> None:
    with pytest.raises(
        ValueError,
        match="page nodes cannot be repeatable",
    ):
        make_node(
            NodeType.PAGE,
            repeatable=True,
        )


def test_collection_must_define_item_template() -> None:
    with pytest.raises(
        ValueError,
        match="Collection nodes must define item_template",
    ):
        make_node(
            NodeType.COLLECTION,
        )


def test_collection_accepts_item_template() -> None:
    node = make_node(
        NodeType.COLLECTION,
        item_template="Product",
    )

    assert node.item_template == "Product"
    assert node.repeatable is False


def test_collection_cannot_define_target_template() -> None:
    with pytest.raises(
        ValueError,
        match="Collection nodes cannot define target_template",
    ):
        make_node(
            NodeType.COLLECTION,
            item_template="Product",
            target_template="Product",
        )


def test_entry_point_must_define_target_template() -> None:
    with pytest.raises(
        ValueError,
        match="Entry point nodes must define target_template",
    ):
        make_node(
            NodeType.ENTRY_POINT,
        )


def test_entry_point_accepts_target_template() -> None:
    node = make_node(
        NodeType.ENTRY_POINT,
        target_template="Product",
    )

    assert node.target_template == "Product"
    assert node.repeatable is False


def test_entry_point_cannot_define_item_template() -> None:
    with pytest.raises(
        ValueError,
        match="Entry point nodes cannot define item_template",
    ):
        make_node(
            NodeType.ENTRY_POINT,
            item_template="Product",
            target_template="Product",
        )


def test_page_cannot_define_item_template() -> None:
    with pytest.raises(
        ValueError,
        match="page nodes cannot define item_template",
    ):
        make_node(
            NodeType.PAGE,
            item_template="Product",
        )


def test_page_cannot_define_target_template() -> None:
    with pytest.raises(
        ValueError,
        match="page nodes cannot define target_template",
    ):
        make_node(
            NodeType.PAGE,
            target_template="Product",
        )


def test_purpose_cannot_be_empty() -> None:
    with pytest.raises(
        ValueError,
        match="Node purpose cannot be empty",
    ):
        PageDefinition(
            name="Test",
            node_type=NodeType.PAGE,
            required=True,
            repeatable=False,
            purpose="   ",
            children=(),
        )


def test_collection_requires_item_template() -> None:
    with pytest.raises(
        ValueError,
        match="item_template",
    ):
        Node(
            id="home.products",
            name="Products",
            node_type=NodeType.COLLECTION,
            required=True,
            repeatable=False,
            purpose="Groups products.",
            parent_id="home",
            position=0,
        )


def test_collection_accepts_item_template() -> None:
    node = Node(
        id="home.products",
        name="Products",
        node_type=NodeType.COLLECTION,
        required=True,
        repeatable=False,
        purpose="Groups products.",
        parent_id="home",
        position=0,
        item_template="product",
    )

    assert node.item_template == "product"
    assert node.target_template is None


def test_entry_point_requires_target_template() -> None:
    with pytest.raises(
        ValueError,
        match="target_template",
    ):
        Node(
            id="home.product",
            name="Product",
            node_type=NodeType.ENTRY_POINT,
            required=True,
            repeatable=False,
            purpose="Provides access to a product.",
            parent_id="home",
            position=0,
        )


def test_entry_point_accepts_target_template() -> None:
    node = Node(
        id="home.product",
        name="Product",
        node_type=NodeType.ENTRY_POINT,
        required=True,
        repeatable=False,
        purpose="Provides access to a product.",
        parent_id="home",
        position=0,
        target_template="product",
    )

    assert node.target_template == "product"
    assert node.item_template is None


def test_regular_node_cannot_reference_template() -> None:
    with pytest.raises(
        ValueError,
        match="item_template",
    ):
        Node(
            id="home.products",
            name="Products",
            node_type=NodeType.PAGE,
            required=True,
            repeatable=False,
            purpose="Product listing page.",
            parent_id="home",
            position=0,
            item_template="product",
        )