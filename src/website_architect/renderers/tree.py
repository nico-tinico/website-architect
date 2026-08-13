from __future__ import annotations

from website_architect.domain.architecture import SiteArchitecture
from website_architect.domain.nodes import Node


class TreeRenderer:
    def render(self, architecture: SiteArchitecture) -> str:
        lines = [
            "Website Architecture",
            "─" * 40,
            f"Type      : {architecture.site_type.value}",
            f"Mode      : {architecture.mode.value}",
            f"Topology  : {architecture.topology.value}",
            "",
            "/",
        ]

        children = architecture.root.children

        for index, child in enumerate(children):
            is_last = index == len(children) - 1
            self._render_node(
                child,
                lines,
                prefix="",
                is_last=is_last,
            )

        return "\n".join(lines)

    def _render_node(
        self,
        node: Node,
        lines: list[str],
        *,
        prefix: str,
        is_last: bool,
    ) -> None:
        connector = "└── " if is_last else "├── "

        suffix = ""

        if node.repeatable:
            suffix = " [repeatable]"

        if not node.required:
            suffix += " [optional]"

        lines.append(
            f"{prefix}{connector}{node.name}{suffix}"
        )

        child_prefix = prefix + ("    " if is_last else "│   ")

        for index, child in enumerate(node.children):
            child_is_last = index == len(node.children) - 1

            self._render_node(
                child,
                lines,
                prefix=child_prefix,
                is_last=child_is_last,
            )