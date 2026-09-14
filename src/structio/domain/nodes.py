from __future__ import annotations

from dataclasses import dataclass

from structio.domain.enums import NodeType


@dataclass(frozen=True, slots=True)
class Node:
    """
    Represents a concrete node in a generated website architecture.

    Node is the runtime representation produced by the architecture
    generator from a PageDefinition.
    """

    id: str
    name: str
    node_type: NodeType
    required: bool
    repeatable: bool
    purpose: str | None
    parent_id: str | None
    position: int

    item_template: str | None = None
    target_template: str | None = None

    def __post_init__(self) -> None:
        self._validate_semantic_references()

    def _validate_semantic_references(self) -> None:
        if self.node_type == NodeType.COLLECTION:
            if self.item_template is None:
                raise ValueError(
                    "Collection nodes must define item_template."
                )

            if self.target_template is not None:
                raise ValueError(
                    "Collection nodes cannot define target_template."
                )

            return

        if self.node_type == NodeType.ENTRY_POINT:
            if self.target_template is None:
                raise ValueError(
                    "Entry point nodes must define target_template."
                )

            if self.item_template is not None:
                raise ValueError(
                    "Entry point nodes cannot define item_template."
                )

            return

        if self.item_template is not None:
            raise ValueError(
                f"{self.node_type.value} nodes cannot define item_template."
            )

        if self.target_template is not None:
            raise ValueError(
                f"{self.node_type.value} nodes cannot define target_template."
            )


@dataclass(frozen=True, slots=True)
class PageDefinition:
    """
    Defines a node in a website architecture profile.

    PageDefinition is the catalog-level definition used to describe
    pages, sections, collections, templates, and entry points.

    Collections reference the template used for their items through
    ``item_template``.

    Entry points reference the template they expose through
    ``target_template``.
    """

    name: str
    node_type: NodeType
    required: bool
    repeatable: bool
    purpose: str
    children: tuple[PageDefinition, ...]

    item_template: str | None = None
    target_template: str | None = None

    def __post_init__(self) -> None:
        self._validate_purpose()
        self._validate_repeatability()
        self._validate_semantic_references()

    def _validate_purpose(self) -> None:
        if not self.purpose.strip():
            raise ValueError(
                "Node purpose cannot be empty."
            )

    def _validate_repeatability(self) -> None:
        if self.node_type == NodeType.TEMPLATE:
            if not self.repeatable:
                raise ValueError(
                    "Template nodes must be repeatable."
                )

        elif self.node_type in {
            NodeType.PAGE,
            NodeType.SECTION,
            NodeType.COLLECTION,
            NodeType.ENTRY_POINT,
        }:
            if self.repeatable:
                raise ValueError(
                    f"{self.node_type.value} nodes cannot be repeatable."
                )

    def _validate_semantic_references(self) -> None:
        if self.node_type == NodeType.COLLECTION:
            if self.item_template is None:
                raise ValueError(
                    "Collection nodes must define item_template."
                )

            if self.target_template is not None:
                raise ValueError(
                    "Collection nodes cannot define target_template."
                )

            return

        if self.node_type == NodeType.ENTRY_POINT:
            if self.target_template is None:
                raise ValueError(
                    "Entry point nodes must define target_template."
                )

            if self.item_template is not None:
                raise ValueError(
                    "Entry point nodes cannot define item_template."
                )

            return

        if self.item_template is not None:
            raise ValueError(
                f"{self.node_type.value} nodes cannot define item_template."
            )

        if self.target_template is not None:
            raise ValueError(
                f"{self.node_type.value} nodes cannot define target_template."
            )