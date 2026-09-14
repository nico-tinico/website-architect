from dataclasses import dataclass

from .enums import SiteMode, SiteType, Topology, NodeType
from .graph import SiteGraph
from .nodes import Node
from .templates import Template


@dataclass(frozen=True, slots=True)
class SiteArchitecture:
    """
    Represents a complete generated website architecture.

    Nodes describe the information architecture.
    Templates describe reusable structures referenced by collections
    and entry points.
    The graph contains links between architecture nodes.
    """

    version: str
    site_type: SiteType
    mode: SiteMode
    topology: Topology
    root_id: str
    nodes: tuple[Node, ...]
    templates: tuple[Template, ...]
    graph: SiteGraph

    def validate(self) -> None:
        self._validate_root()
        self._validate_node_ids()
        self._validate_template_ids()
        self._validate_template_invariants()
        self._validate_parents()
        self._validate_positions()
        self._validate_template_references()
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
            raise ValueError(
                "Duplicate node IDs detected."
            )

    def _validate_template_ids(self) -> None:
        template_ids = [template.id for template in self.templates]

        if len(template_ids) != len(set(template_ids)):
            raise ValueError(
                "Duplicate template IDs detected."
            )

    def _validate_template_invariants(self) -> None:
        for template in self.templates:
            if not template.repeatable:
                raise ValueError(
                    f"Template '{template.id}' must be repeatable."
                )

            if not template.name.strip():
                raise ValueError(
                    f"Template '{template.id}' must have a name."
                )

            if not template.purpose.strip():
                raise ValueError(
                    f"Template '{template.id}' must have a purpose."
                )

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

    def _validate_template_references(self) -> None:
        template_ids = {
            template.id
            for template in self.templates
        }

        for node in self.nodes:
            if node.item_template is not None:
                if node.node_type is not NodeType.COLLECTION:
                    raise ValueError(
                        f"Node '{node.id}' defines item_template "
                        "but is not a collection."
                    )

                if node.item_template not in template_ids:
                    raise ValueError(
                        f"Node '{node.id}' references unknown "
                        f"item template '{node.item_template}'."
                    )

            if node.target_template is not None:
                if node.node_type is not NodeType.ENTRY_POINT:
                    raise ValueError(
                        f"Node '{node.id}' defines target_template "
                        "but is not an entry point."
                    )

                if node.target_template not in template_ids:
                    raise ValueError(
                        f"Node '{node.id}' references unknown "
                        f"target template '{node.target_template}'."
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