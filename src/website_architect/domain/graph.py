from dataclasses import dataclass

from .links import Link


@dataclass(frozen=True, slots=True)
class SiteGraph:
    links: tuple[Link, ...] = ()