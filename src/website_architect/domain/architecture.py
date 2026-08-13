from dataclasses import dataclass

from .enums import SiteMode, SiteType, Topology
from .graph import SiteGraph
from .nodes import Node


@dataclass(frozen=True, slots=True)
class SiteArchitecture:
    version: str
    site_type: SiteType
    mode: SiteMode
    topology: Topology
    root_id: str
    nodes: tuple[Node, ...]
    graph: SiteGraph

    def validate(self) -> None:
        self._validate_root()
        self._validate_node_ids()
        self._validate_parents()
        self._validate_positions()
        self._validate_links()

    def _validate_root(self) -> None:
        node_ids = {node.id for node in self.nodes}

        if self.root_id not in node_ids:
            raise ValueError(
                f"Root node '{self.root_id}' does not exist."
            )

    def _validate_node_ids(self) -> None:
        node_ids = [node.id for node in self.nodes]

        if len(node_ids) != len(set(node_ids)):
            raise ValueError("Duplicate node IDs detected.")

    def _validate_parents(self) -> None:
        node_ids = {node.id for node in self.nodes}

        for node in self.nodes:
            if node.parent_id is None:
                continue

            if node.parent_id not in node_ids:
                raise ValueError(
                    f"Node '{node.id}' references "
                    f"unknown parent '{node.parent_id}'."
                )

            if node.parent_id == node.id:
                raise ValueError(
                    f"Node '{node.id}' cannot be its own parent."
                )

    def _validate_positions(self) -> None:
        siblings: dict[str | None, list[int]] = {}

        for node in self.nodes:
            siblings.setdefault(node.parent_id, []).append(
                node.position
            )

        for parent_id, positions in siblings.items():
            expected = list(range(len(positions)))

            if sorted(positions) != expected:
                raise ValueError(
                    f"Invalid positions for parent '{parent_id}'. "
                    f"Expected {expected}, got {sorted(positions)}."
                )

    def _validate_links(self) -> None:
        node_ids = {node.id for node in self.nodes}

        for link in self.graph.links:
            if link.source not in node_ids:
                raise ValueError(
                    f"Link source '{link.source}' does not exist."
                )

            if link.target not in node_ids:
                raise ValueError(
                    f"Link target '{link.target}' does not exist."
                )