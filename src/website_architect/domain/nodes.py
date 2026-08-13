from __future__ import annotations

from dataclasses import dataclass

from .enums import NodeType


@dataclass(frozen=True, slots=True)
class Node:
    id: str
    name: str
    node_type: NodeType
    required: bool
    repeatable: bool
    purpose: str | None
    parent_id: str | None
    position: int


@dataclass(frozen=True, slots=True)
class PageDefinition:
    name: str
    node_type: NodeType
    required: bool
    repeatable: bool
    purpose: str
    children: tuple["PageDefinition", ...]


def page(
    name: str,
    *,
    required: bool = True,
    repeatable: bool = False,
    purpose: str | None = None,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.PAGE,
        required=required,
        repeatable=repeatable,
        purpose=purpose,
        children=children,
    )


def section(
    name: str,
    *,
    required: bool = True,
    purpose: str | None = None,
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.SECTION,
        required=required,
        repeatable=False,
        purpose=purpose,
        children=(),
    )


def template(
    name: str,
    *,
    required: bool = True,
    purpose: str | None = None,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.TEMPLATE,
        required=required,
        repeatable=True,
        purpose=purpose,
        children=children,
    )


def collection(
    name: str,
    *,
    required: bool = True,
    purpose: str | None = None,
    children: tuple[PageDefinition, ...] = (),
) -> PageDefinition:
    return PageDefinition(
        name=name,
        node_type=NodeType.COLLECTION,
        required=required,
        repeatable=False,
        purpose=purpose,
        children=children,
    )