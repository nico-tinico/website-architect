from pathlib import Path

from website_architect.domain.enums import SiteMode, SiteType
from website_architect.generator.generator import ArchitectureGenerator
from website_architect.serializers.json import JsonSerializer


def main() -> None:
    print("Website Architect")
    print("=================")
    print()

    site_type = _ask_site_type()
    mode = _ask_mode()

    generator = ArchitectureGenerator()
    serializer = JsonSerializer()

    architecture = generator.generate(
        site_type=site_type,
        mode=mode,
    )

    output = serializer.serialize(architecture)

    output_path = Path("website-architecture.json")
    output_path.write_text(
        output,
        encoding="utf-8",
    )

    print()
    print("Architecture generated successfully.")
    print()
    print(f"Output: {output_path}")


def _ask_site_type() -> SiteType:
    types = list(SiteType)

    print("Select website type:")

    for index, site_type in enumerate(types, start=1):
        print(f"{index}. {site_type.value}")

    while True:
        try:
            choice = int(input("\nType: "))
            return types[choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Try again.")


def _ask_mode() -> SiteMode:
    print("\nSelect architecture mode:")
    print("1. Single Page")
    print("2. Multi Page")

    while True:
        choice = input("\nMode: ").strip()

        if choice == "1":
            return SiteMode.SINGLE_PAGE

        if choice == "2":
            return SiteMode.MULTI_PAGE

        print("Invalid choice. Try again.")