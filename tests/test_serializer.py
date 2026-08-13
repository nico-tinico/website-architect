import json

from website_architect.domain.enums import SiteMode, SiteType
from website_architect.generator.generator import ArchitectureGenerator
from website_architect.serializers.json import JsonSerializer


def test_serialize_architecture() -> None:
    architecture = ArchitectureGenerator().generate(
        site_type=SiteType.SAAS,
        mode=SiteMode.MULTI_PAGE,
    )

    output = JsonSerializer().serialize(architecture)

    data = json.loads(output)

    assert data["version"] == "1.0"
    assert data["site"]["type"] == "saas"
    assert data["site"]["mode"] == "multi_page"
    assert data["site"]["topology"] == "hierarchical"

    assert data["root_id"] == "home"
    assert isinstance(data["nodes"], list)
    assert isinstance(data["links"], list)