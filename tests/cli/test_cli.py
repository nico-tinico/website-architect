import json
import pytest

from website_architect.cli import main
from website_architect.domain.enums import SiteMode, SiteType
from website_architect.serializers.json import JsonSerializer


def test_cli_generate_outputs_json(
    monkeypatch,
    capsys,
) -> None:
    monkeypatch.setattr(
        "sys.argv",
        [
            "website-architect",
            "generate",
            "--type",
            "ecommerce",
            "--mode",
            "multi_page",
        ],
    )

    exit_code = main()

    assert exit_code == 0

    captured = capsys.readouterr()
    data = json.loads(captured.out)

    assert data["site"]["type"] == "ecommerce"
    assert data["site"]["mode"] == "multi_page"
    assert data["root_id"] == "home"
    assert data["nodes"]
    assert data["templates"]
    assert data["links"]


def test_cli_generate_output_is_deserializable(
    monkeypatch,
    capsys,
) -> None:
    monkeypatch.setattr(
        "sys.argv",
        [
            "website-architect",
            "generate",
            "--type",
            "agency",
            "--mode",
            "multi_page",
        ],
    )

    exit_code = main()

    assert exit_code == 0

    captured = capsys.readouterr()

    serializer = JsonSerializer()
    architecture = serializer.deserialize(
        captured.out,
    )

    assert architecture.site_type is SiteType.AGENCY
    assert architecture.mode is SiteMode.MULTI_PAGE


def test_cli_generate_writes_output_file(
    monkeypatch,
    tmp_path,
    capsys,
) -> None:
    output_path = tmp_path / "architecture.json"

    monkeypatch.setattr(
        "sys.argv",
        [
            "website-architect",
            "generate",
            "--type",
            "portfolio",
            "--mode",
            "single_page",
            "--output",
            str(output_path),
        ],
    )

    exit_code = main()

    assert exit_code == 0
    assert output_path.exists()

    captured = capsys.readouterr()

    assert (
        f"Architecture written to {output_path}"
        in captured.out
    )

    serializer = JsonSerializer()
    architecture = serializer.load(
        str(output_path),
    )

    assert architecture.site_type is SiteType.PORTFOLIO
    assert architecture.mode is SiteMode.SINGLE_PAGE


def test_cli_generate_output_file_is_valid_json(
    monkeypatch,
    tmp_path,
) -> None:
    output_path = tmp_path / "architecture.json"

    monkeypatch.setattr(
        "sys.argv",
        [
            "website-architect",
            "generate",
            "--type",
            "travel",
            "--mode",
            "multi_page",
            "--output",
            str(output_path),
        ],
    )

    exit_code = main()

    assert exit_code == 0

    with output_path.open(
        "r",
        encoding="utf-8",
    ) as file:
        data = json.load(file)

    assert data["site"]["type"] == "travel"
    assert data["site"]["mode"] == "multi_page"


def test_cli_help(
    monkeypatch,
    capsys,
) -> None:
    monkeypatch.setattr(
        "sys.argv",
        [
            "website-architect",
            "--help",
        ],
    )

    try:
        main()
    except SystemExit as exc:
        assert exc.code == 0

    captured = capsys.readouterr()

    assert "generate" in captured.out
    assert "website-architect" in captured.out


def test_cli_generate_help(
    monkeypatch,
    capsys,
) -> None:
    monkeypatch.setattr(
        "sys.argv",
        [
            "website-architect",
            "generate",
            "--help",
        ],
    )

    try:
        main()
    except SystemExit as exc:
        assert exc.code == 0

    captured = capsys.readouterr()

    assert "--type" in captured.out
    assert "--mode" in captured.out
    assert "--output" in captured.out


@pytest.mark.parametrize(
    "site_type",
    list(SiteType),
)
@pytest.mark.parametrize(
    "mode",
    list(SiteMode),
)
def test_cli_supports_all_combinations(
    monkeypatch,
    capsys,
    site_type: SiteType,
    mode: SiteMode,
) -> None:
    from website_architect.cli import main

    monkeypatch.setattr(
        "sys.argv",
        [
            "website-architect",
            "generate",
            "--type",
            site_type.value,
            "--mode",
            mode.value,
        ],
    )

    exit_code = main()

    assert exit_code == 0

    output = capsys.readouterr().out

    serializer = JsonSerializer()
    architecture = serializer.deserialize(output)

    assert architecture.site_type is site_type
    assert architecture.mode is mode