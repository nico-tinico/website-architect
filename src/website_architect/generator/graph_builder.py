from website_architect.catalog.definitions import LinkRule
from website_architect.domain.graph import SiteGraph
from website_architect.domain.links import Link


class GraphBuilder:
    def build(
        self,
        rules: tuple[LinkRule, ...],
        node_ids: set[str],
    ) -> SiteGraph:
        links: list[Link] = []

        for rule in rules:
            source_id = self._resolve_node_id(rule.source, node_ids)
            target_id = self._resolve_node_id(rule.target, node_ids)

            if source_id is None:
                continue

            if target_id is None:
                continue

            links.append(
                Link(
                    source=source_id,
                    target=target_id,
                    link_type=rule.link_type,
                )
            )

        return SiteGraph(
            links=tuple(links),
        )

    @staticmethod
    def _resolve_node_id(
        name: str,
        node_ids: set[str],
    ) -> str | None:
        normalized = name.lower().replace(" ", "-")

        if normalized in node_ids:
            return normalized

        matches = [
            node_id
            for node_id in node_ids
            if node_id.endswith(f".{normalized}")
        ]

        if len(matches) == 1:
            return matches[0]

        return None