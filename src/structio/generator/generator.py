from __future__ import annotations

from structio.catalog.definitions import (
    SiteProfile,
    TemplateDefinition,
)
from structio.catalog.profiles import PROFILES
from structio.domain.architecture import SiteArchitecture
from structio.domain.enums import NodeType, SiteMode, SiteType
from structio.domain.graph import SiteGraph
from structio.domain.nodes import Node, PageDefinition
from structio.domain.templates import Template
from structio.generator.graph_builder import GraphBuilder


class ArchitectureGenerator:
    """
    Generates a complete site architecture from a catalog profile.

    The generator is intentionally catalog-driven:
    site-specific structure, templates, and link rules are defined
    by SiteProfile instances and are not hard-coded here.
    """

    VERSION = "1.0"
    ROOT_ID = "home"
    ROOT_NAME = "Home"

    def __init__(self) -> None:
        self._graph_builder = GraphBuilder()

    def generate(
        self,
        site_type: SiteType,
        mode: SiteMode,
    ) -> SiteArchitecture:
        """
        Generate and validate a complete site architecture.

        The generation pipeline is:

        1. Resolve the site profile.
        2. Resolve definitions for the requested mode.
        3. Build architecture nodes.
        4. Build runtime templates.
        5. Build the navigation graph.
        6. Construct the SiteArchitecture.
        7. Validate the resulting architecture.
        """
        profile = self._resolve_profile(site_type)

        definitions = profile.nodes_for_mode(mode)

        nodes = self._build_nodes(definitions)

        templates = self._build_templates(
            profile.templates
        )

        graph = self._build_graph(
            profile=profile,
            mode=mode,
            nodes=nodes,
        )

        architecture = SiteArchitecture(
            version=self.VERSION,
            site_type=site_type,
            mode=mode,
            topology=profile.default_topology,
            root_id=self.ROOT_ID,
            nodes=tuple(nodes),
            templates=templates,
            graph=graph,
        )

        architecture.validate()

        return architecture

    @staticmethod
    def _resolve_profile(
        site_type: SiteType,
    ) -> SiteProfile:
        try:
            return PROFILES[site_type]
        except KeyError as exc:
            raise ValueError(
                f"Unsupported site type: {site_type}"
            ) from exc

    def _build_nodes(
        self,
        definitions: tuple[PageDefinition, ...],
    ) -> list[Node]:
        """
        Build the complete node hierarchy for a profile.

        The architecture always owns its root node directly.
        Catalog definitions describe the root's descendants.
        """
        nodes = [self._build_root_node()]

        child_position = 0

        for definition in definitions:
            if self._is_root_definition(definition):
                continue

            nodes.extend(
                self._build_node_tree(
                    definition,
                    parent_id=self.ROOT_ID,
                    path=self.ROOT_ID,
                    position=child_position,
                )
            )

            child_position += 1

        return nodes

    @staticmethod
    def _build_root_node() -> Node:
        return Node(
            id=ArchitectureGenerator.ROOT_ID,
            name=ArchitectureGenerator.ROOT_NAME,
            node_type=NodeType.PAGE,
            required=True,
            repeatable=False,
            purpose="Website home page.",
            parent_id=None,
            position=0,
        )

    def _build_node_tree(
        self,
        definition: PageDefinition,
        *,
        parent_id: str,
        path: str,
        position: int,
    ) -> list[Node]:
        """
        Recursively transform catalog definitions into domain nodes.
        """
        node_id = self._build_node_id(
            path=path,
            name=definition.name,
        )

        node = Node(
            id=node_id,
            name=definition.name,
            node_type=definition.node_type,
            required=definition.required,
            repeatable=definition.repeatable,
            purpose=definition.purpose,
            parent_id=parent_id,
            position=position,
            item_template=self._normalize_template_reference(
                definition.item_template
            ),
            target_template=self._normalize_template_reference(
                definition.target_template
            ),
        )

        nodes = [node]

        for child_position, child in enumerate(
            definition.children
        ):
            nodes.extend(
                self._build_node_tree(
                    child,
                    parent_id=node_id,
                    path=node_id,
                    position=child_position,
                )
            )

        return nodes

    def _build_templates(
        self,
        definitions: tuple[TemplateDefinition, ...],
    ) -> tuple[Template, ...]:
        """
        Transform catalog template definitions into runtime templates.
        """
        return tuple(
            self._build_template(definition)
            for definition in definitions
        )

    @staticmethod
    def _build_template(
        definition: TemplateDefinition,
    ) -> Template:
        """
        Transform a catalog TemplateDefinition into a runtime Template.
        """
        return Template(
            id=ArchitectureGenerator._slugify(
                definition.name
            ),
            name=definition.name,
            required=definition.required,
            repeatable=definition.repeatable,
            purpose=definition.purpose,
        )

    def _build_graph(
        self,
        *,
        profile: SiteProfile,
        mode: SiteMode,
        nodes: list[Node],
    ) -> SiteGraph:
        """
        Build the navigation graph from catalog link rules.
        """
        node_ids = {
            node.id
            for node in nodes
        }

        rules = profile.links_for_mode(mode)

        return self._graph_builder.build(
            rules=rules,
            node_ids=node_ids,
        )

    @staticmethod
    def _build_node_id(
        *,
        path: str,
        name: str,
    ) -> str:
        return f"{path}.{ArchitectureGenerator._slugify(name)}"

    @staticmethod
    def _normalize_template_reference(
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        return ArchitectureGenerator._slugify(value)

    @staticmethod
    def _is_root_definition(
        definition: PageDefinition,
    ) -> bool:
        """
        Identify the catalog definition representing the architecture root.

        Home is a structural root owned by SiteArchitecture itself and must
        not be materialized as a second node.
        """
        return (
            definition.name.strip().lower()
            == ArchitectureGenerator.ROOT_NAME.lower()
        )

    @staticmethod
    def _slugify(value: str) -> str:
        return (
            value
            .strip()
            .lower()
            .replace(" ", "-")
        )