from __future__ import annotations

import argparse
import sys

from structio.domain.enums import SiteMode, SiteType
from structio.generator.generator import ArchitectureGenerator
from structio.serializers.json import JsonSerializer


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "generate":
        return _generate(
            site_type=args.site_type,
            mode=args.mode,
            output=args.output,
        )

    parser.print_help()
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="structio",
        description=(
            "Generate website information architectures "
            "from reusable site profiles."
        ),
    )

    subparsers = parser.add_subparsers(
        dest="command",
    )

    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate a website architecture.",
    )

    generate_parser.add_argument(
        "--type",
        dest="site_type",
        required=True,
        choices=[site_type.value for site_type in SiteType],
        help="Website type.",
    )

    generate_parser.add_argument(
        "--mode",
        required=True,
        choices=[mode.value for mode in SiteMode],
        help="Structioure mode.",
    )

    generate_parser.add_argument(
        "--output",
        help="Write the generated JSON to a file.",
    )

    return parser


def _generate(
    *,
    site_type: str,
    mode: str,
    output: str | None,
) -> int:
    generator = ArchitectureGenerator()
    serializer = JsonSerializer()

    architecture = generator.generate(
        site_type=SiteType(site_type),
        mode=SiteMode(mode),
    )

    if output is None:
        print(serializer.serialize(architecture))
        return 0

    serializer.save(
        architecture,
        output,
    )

    print(f"Architecture written to {output}")

    return 0


if __name__ == "__main__":
    sys.exit(main())