from __future__ import annotations

from dataclasses import dataclass

from website_architect.domain.enums import LinkType, SiteType, Topology
from website_architect.domain.nodes import PageDefinition


@dataclass(frozen=True, slots=True)
class LinkRule:
    """
    Defines a semantic relationship between two nodes.

    References are expressed as semantic paths relative to the website root.

    Examples:
        Product
        Product.Security
        Solutions.Enterprise
        Resources.Documentation
        Account.Wishlist
    """

    source: str
    target: str
    link_type: LinkType


@dataclass(frozen=True, slots=True)
class SiteProfile:
    site_type: SiteType
    default_topology: Topology
    single_page: tuple[PageDefinition, ...]
    multi_page: tuple[PageDefinition, ...]
    single_page_links: tuple[LinkRule, ...]
    multi_page_links: tuple[LinkRule, ...]


def profile(
    site_type: SiteType,
    topology: Topology,
    *,
    single_page: tuple[PageDefinition, ...],
    multi_page: tuple[PageDefinition, ...],
    single_page_links: tuple[LinkRule, ...] = (),
    multi_page_links: tuple[LinkRule, ...] = (),
) -> SiteProfile:
    return SiteProfile(
        site_type=site_type,
        default_topology=topology,
        single_page=single_page,
        multi_page=multi_page,
        single_page_links=single_page_links,
        multi_page_links=multi_page_links,
    )