import pytest

from structio.domain.templates import Template


def test_template_is_repeatable() -> None:
    template = Template(
        id="product",
        name="Product",
        required=True,
        repeatable=True,
        purpose="Defines the structure of a product.",
    )

    assert template.repeatable is True


def test_template_requires_purpose() -> None:
    with pytest.raises(ValueError, match="purpose"):
        Template(
            id="product",
            name="Product",
            required=True,
            repeatable=True,
            purpose="",
        )


def test_template_must_be_repeatable() -> None:
    with pytest.raises(
        ValueError,
        match="repeatable",
    ):
        Template(
            id="product",
            name="Product",
            required=True,
            repeatable=False,
            purpose="Defines the structure of a product.",
        )


def test_template_requires_name() -> None:
    with pytest.raises(
        ValueError,
        match="name",
    ):
        Template(
            id="product",
            name="",
            required=True,
            repeatable=True,
            purpose="Defines the structure of a product.",
        )