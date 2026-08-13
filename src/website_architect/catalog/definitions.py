from __future__ import annotations

from dataclasses import dataclass

from website_architect.domain.enums import (
    NodeType,
    SiteMode,
    SiteType,
    Topology,
)
from website_architect.domain.nodes import PageDefinition


@dataclass(frozen=True, slots=True)
class LinkRule:
    """
    Defines a relationship between two architecture nodes.
    """

    source: str
    target: str
    link_type: str


@dataclass(frozen=True, slots=True)
class SiteProfile:
    """
    Defines the reusable architecture profile of a website type.
    """

    site_type: SiteType
    default_topology: Topology

    single_page: tuple[PageDefinition, ...]
    multi_page: tuple[PageDefinition, ...]

    single_page_links: tuple[LinkRule, ...]
    multi_page_links: tuple[LinkRule, ...]

    templates: tuple[TemplateDefinition, ...] = ()

    def __post_init__(self) -> None:
        self._validate_templates()
        self._validate_template_references()

    def nodes_for_mode(
        self,
        mode: SiteMode,
    ) -> tuple[PageDefinition, ...]:
        if mode == SiteMode.SINGLE_PAGE:
            return self.single_page

        if mode == SiteMode.MULTI_PAGE:
            return self.multi_page

        raise ValueError(
            f"Unsupported site mode: {mode}"
        )

    def links_for_mode(
        self,
        mode: SiteMode,
    ) -> tuple[LinkRule, ...]:
        if mode == SiteMode.SINGLE_PAGE:
            return self.single_page_links

        if mode == SiteMode.MULTI_PAGE:
            return self.multi_page_links

        raise ValueError(
            f"Unsupported site mode: {mode}"
        )

    def _validate_templates(self) -> None:
        template_names = [
            template.name
            for template in self.templates
        ]

        if len(template_names) != len(set(template_names)):
            raise ValueError(
                "Template names must be unique within a site profile."
            )

        for template in self.templates:
            if not template.repeatable:
                raise ValueError(
                    f"Template '{template.name}' must be repeatable."
                )

    def _validate_template_references(self) -> None:
        template_names = {
            template.name
            for template in self.templates
        }

        for node in self._all_nodes():
            if node.node_type == NodeType.COLLECTION:
                if node.item_template not in template_names:
                    raise ValueError(
                        "Unknown item template: "
                        f"{node.item_template}"
                    )

            elif node.node_type == NodeType.ENTRY_POINT:
                if node.target_template not in template_names:
                    raise ValueError(
                        "Unknown target template: "
                        f"{node.target_template}"
                    )

    def _all_nodes(self) -> tuple[PageDefinition, ...]:
        nodes: list[PageDefinition] = []

        def visit(
            definitions: tuple[PageDefinition, ...],
        ) -> None:
            for definition in definitions:
                nodes.append(definition)
                visit(definition.children)

        visit(self.single_page)
        visit(self.multi_page)

        return tuple(nodes)


@dataclass(frozen=True, slots=True)
class TemplateDefinition:
    name: str
    required: bool
    purpose: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError(
                "Template definition name cannot be empty."
            )

        if not self.purpose.strip():
            raise ValueError(
                "Template definition purpose cannot be empty."
            )

    @property
    def repeatable(self) -> bool:
        return True
    

def profile(
    *,
    site_type: SiteType,
    default_topology: Topology,
    single_page: tuple[PageDefinition, ...],
    multi_page: tuple[PageDefinition, ...],
    single_page_links: tuple[LinkRule, ...],
    multi_page_links: tuple[LinkRule, ...],
    templates: tuple[TemplateDefinition, ...] = (),
) -> SiteProfile:
    return SiteProfile(
        site_type=site_type,
        default_topology=default_topology,
        single_page=single_page,
        multi_page=multi_page,
        single_page_links=single_page_links,
        multi_page_links=multi_page_links,
        templates=templates,
    )