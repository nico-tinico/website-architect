from __future__ import annotations

import argparse
import sys

from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.padding import Padding
from rich.console import Group

from structio.domain.enums import SiteMode, SiteType
from structio.generator.generator import ArchitectureGenerator
from structio.serializers.json import JsonSerializer


console = Console()


class StructioArgumentParser(argparse.ArgumentParser):
    """Argument parser with Structio's Rich-based help presentation."""

    def print_help(self, file=None) -> None:
        if self.prog == "structio":
            _render_main_help()
            return

        if self.prog.endswith(" generate"):
            _render_generate_help()
            return

        super().print_help(file)


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
    parser = StructioArgumentParser(
        prog="structio",
        description=(
            "Generate website information architectures "
            "from reusable site profiles."
        ),
    )

    subparsers = parser.add_subparsers(
        dest="command",
        parser_class=StructioArgumentParser,
    )

    generate_parser = subparsers.add_parser(
        "generate",
        help="Generate a website architecture.",
        description="Generate a website architecture.",
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
        help="Architecture mode.",
    )

    generate_parser.add_argument(
        "--output",
        help="Write the generated JSON to a file.",
    )

    return parser


_BLUE = "#3a96dd"
_RED = "#e74856"
_GREEN = "#00CF00"
_GRAY = "#7f7f7f"
_WHITE = "#FFFFFF"


def _render_main_help() -> None:
    version = _project_version()

    header = f"""[{_RED}]┏┓┏┳┓┳┓┳┳┏┓┏┳┓ ┳┏┓
┗┓ ┃ ┣┫┃┃┃  ┃  ┃┃┃
┗┛ ┻ ┛┗┗┛┗┛ ┻ •┻┗┛[/{_RED}]

[{_WHITE}]Structio — Web architecture engineering[/{_WHITE}]
[{_GRAY}]v{version} · https://github.com/nico-tinico/structio[/{_GRAY}]
"""

    table = Table(box=None, show_header=True, header_style=_WHITE, padding=0)
    
    table.add_column("Commands  ", style=_BLUE)
    table.add_column(style=_WHITE)

    rows = [
        ("", ""),
        (
            Padding("generate <type> <mode>", (0, 4, 0, 0)),
            "Generate a website architecture"
        ),
    ]

    for row in rows:

        table.add_row(*row)

    footer = f"""
[{_GRAY}][{_WHITE}]{len(SiteType)}[/{_WHITE}] website types · [{_WHITE}]{len(SiteMode)}[/{_WHITE}] architecture modes · deterministic output[/{_GRAY}]"""

    console.clear()
    console.print(
        Padding(
            Group(
                header,
                table,
                footer,
            ),
            (1, 2)
        )
    )


def _render_generate_help() -> None:
    console.print()

    header = Text()
    header.append("Structio", style="bold cyan")
    header.append(" — Generate architecture")
    console.print(header)
    console.print()

    console.print(Text("USAGE", style="bold"))
    console.print(Text("    structio generate --type <type> --mode <mode> [OPTIONS]", style="dim"))
    console.print()

    console.print(Text("OPTIONS", style="bold"))
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 2),
        collapse_padding=True,
    )
    table.add_column(style="bold cyan", no_wrap=True)
    table.add_column(style="default")
    table.add_row("--type <type>", "Website type")
    table.add_row("--mode <mode>", "Architecture mode")
    table.add_row("--output <file>", "Write the generated JSON to a file")
    table.add_row("-h, --help", "Show this help message")
    console.print(table)
    console.print()

    console.print(Text("EXAMPLES", style="bold"))
    console.print(Text("    structio generate --type ecommerce --mode multi_page", style="dim"))
    console.print(Text("    structio generate --type portfolio --mode single_page --output architecture.json", style="dim"))


def _project_version() -> str:
    try:
        from importlib.metadata import version

        return version("structio")
    except Exception:
        return "1.0.0"


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
        json = (serializer.serialize(architecture))

        result = f"""\n[{_GRAY}]{json}[/{_GRAY}]"""
    else:
        serializer.save(
            architecture,
            output,
        )

        result = f"""\nGenerating the structure...\n\n[{_GREEN}]✓ written to {output}[/{_GREEN}]"""

    header = f"""[{_RED}]┏┓┏┳┓┳┓┳┳┏┓┏┳┓ ┳┏┓
┗┓ ┃ ┣┫┃┃┃  ┃  ┃┃┃
┗┛ ┻ ┛┗┗┛┗┛ ┻ •┻┗┛[/{_RED}]
"""

    table = Table(box=None, show_header=True, header_style=_WHITE, padding=0)
    
    table.add_column("Configuration", style=_WHITE)
    table.add_column(style=_GRAY)

    rows = [
        ("", ""),
        (
            Padding(f"[{_GREEN}]✓[/{_GREEN}] Type", (0, 4, 0, 0)),
            f"← {site_type}"
        ),
        (
            Padding(f"[{_GREEN}]✓[/{_GREEN}] Mode", (0, 4, 0, 0)),
            f"← {mode}"
        ),
    ]

    for row in rows:

        table.add_row(*row)

    console.clear()
    console.print(
        Padding(
            Group(
                header,
                table,
                result
            ),
            (1, 2)
        )
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
