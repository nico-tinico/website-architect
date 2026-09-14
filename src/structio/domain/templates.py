from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Template:
    """
    Represents a reusable runtime template.

    A Template defines the structure of a repeatable content entity.
    It is intentionally separate from Node because templates are not
    part of the website navigation hierarchy.
    """

    id: str
    name: str
    required: bool
    repeatable: bool
    purpose: str

    def __post_init__(self) -> None:
        self._validate_name()
        self._validate_purpose()
        self._validate_repeatability()

    def _validate_name(self) -> None:
        if not self.name.strip():
            raise ValueError(
                "Template name cannot be empty."
            )

    def _validate_purpose(self) -> None:
        if not self.purpose.strip():
            raise ValueError(
                "Template purpose cannot be empty."
            )

    def _validate_repeatability(self) -> None:
        if not self.repeatable:
            raise ValueError(
                "Runtime templates must be repeatable."
            )