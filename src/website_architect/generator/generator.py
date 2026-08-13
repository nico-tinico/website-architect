from website_architect.catalog.profiles import PROFILES
from website_architect.domain.architecture import SiteArchitecture
from website_architect.domain.enums import NodeType, SiteMode, SiteType
from website_architect.domain.nodes import Node
from website_architect.generator.graph_builder import GraphBuilder


class ArchitectureGenerator:
    VERSION = "1.0"

    def __init__(self) -> None:
        self._graph_builder = GraphBuilder()

    def generate(
        self,
        site_type: SiteType,
        mode: SiteMode,
    ) -> SiteArchitecture:
        profile = PROFILES[site_type]

        definitions = (
            profile.single_page
            if mode is SiteMode.SINGLE_PAGE
            else profile.multi_page
        )

        nodes: list[Node] = [
            Node(
                id="home",
                name="Home",
                node_type=NodeType.PAGE,
                required=True,
                repeatable=False,
                purpose="Website home page.",
                parent_id=None,
                position=0,
            )
        ]

        for index, definition in enumerate(definitions):
            if (
                mode is SiteMode.MULTI_PAGE
                and definition.name.lower() == "home"
            ):
                continue

            nodes.extend(
                self._build_nodes(
                    definition,
                    parent_id="home",
                    path="home",
                    position=index,
                )
            )

        node_ids = {node.id for node in nodes}

        rules = (
            profile.single_page_links
            if mode is SiteMode.SINGLE_PAGE
            else profile.multi_page_links
        )

        graph = self._graph_builder.build(
            rules=rules,
            node_ids=node_ids,
        )

        architecture = SiteArchitecture(
            version=self.VERSION,
            site_type=site_type,
            mode=mode,
            topology=profile.default_topology,
            root_id="home",
            nodes=tuple(nodes),
            graph=graph,
        )

        architecture.validate()

        return architecture

    def _build_nodes(
        self,
        definition,
        *,
        parent_id: str,
        path: str,
        position: int,
    ) -> list[Node]:
        node_id = f"{path}.{self._slugify(definition.name)}"

        node = Node(
            id=node_id,
            name=definition.name,
            node_type=definition.node_type,
            required=definition.required,
            repeatable=definition.repeatable,
            purpose=definition.purpose,
            parent_id=parent_id,
            position=position,
        )

        nodes = [node]

        for child_position, child in enumerate(definition.children):
            nodes.extend(
                self._build_nodes(
                    child,
                    parent_id=node_id,
                    path=node_id,
                    position=child_position,
                )
            )

        return nodes

    @staticmethod
    def _slugify(value: str) -> str:
        return (
            value
            .strip()
            .lower()
            .replace(" ", "-")
        )