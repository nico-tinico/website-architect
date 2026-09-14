from __future__ import annotations

from structio.catalog.definitions import LinkRule
from structio.domain.graph import SiteGraph
from structio.domain.links import Link


class GraphBuilder:
    ROOT_ID = "home"

    def build(
        self,
        rules: tuple[LinkRule, ...],
        node_ids: set[str],
    ) -> SiteGraph:
        links: list[Link] = []

        for rule in rules:
            source_id = self._resolve_node_id(
                rule.source,
                node_ids,
            )

            if source_id is None:
                raise ValueError(
                    f"Unable to resolve link source: "
                    f"'{rule.source}'."
                )

            target_id = self._resolve_node_id(
                rule.target,
                node_ids,
            )

            if target_id is None:
                raise ValueError(
                    f"Unable to resolve link target: "
                    f"'{rule.target}'."
                )

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

    @classmethod
    def _resolve_node_id(
        cls,
        reference: str,
        node_ids: set[str],
    ) -> str | None:
        normalized = cls._normalize_reference(reference)

        if normalized == cls.ROOT_ID:
            return cls.ROOT_ID

        candidate = f"{cls.ROOT_ID}.{normalized}"

        if candidate in node_ids:
            return candidate

        return None

    @staticmethod
    def _normalize_reference(reference: str) -> str:
        parts = reference.strip().split(".")

        normalized_parts = [
            part.strip().lower().replace(" ", "-")
            for part in parts
            if part.strip()
        ]

        return ".".join(normalized_parts)