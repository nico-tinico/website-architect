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