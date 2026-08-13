from dataclasses import dataclass

from .enums import LinkType


@dataclass(frozen=True, slots=True)
class Link:
    source: str
    target: str
    link_type: LinkType