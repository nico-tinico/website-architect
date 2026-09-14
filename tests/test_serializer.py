import json

from structio.domain.enums import SiteMode, SiteType
from structio.generator.generator import ArchitectureGenerator
from structio.serializers.json import JsonSerializer


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


def test_serialize_includes_templates() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    serializer = JsonSerializer()
    data = json.loads(serializer.serialize(architecture))

    assert "templates" in data
    assert data["templates"]


def test_serialize_collection_includes_item_template() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    serializer = JsonSerializer()
    data = json.loads(serializer.serialize(architecture))

    templates = {
        template["id"]
        for template in data["templates"]
    }

    collections = [
        node
        for node in data["nodes"]
        if node["type"] == "collection"
    ]

    assert collections

    for node in collections:
        assert "item_template" in node
        assert node["item_template"] in templates


def test_serialize_entry_point_includes_target_template() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    serializer = JsonSerializer()
    data = json.loads(serializer.serialize(architecture))

    entry_points = [
        node
        for node in data["nodes"]
        if node["type"] == "entry_point"
    ]

    assert entry_points

    for node in entry_points:
        assert "target_template" in node
        assert node["target_template"] == "product"


def test_serialize_deserialize_round_trip() -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.ECOMMERCE,
        mode=SiteMode.MULTI_PAGE,
    )

    serializer = JsonSerializer()

    serialized = serializer.serialize(architecture)
    restored = serializer.deserialize(serialized)

    assert restored == architecture


def test_save_and_load_round_trip(
    tmp_path,
) -> None:
    generator = ArchitectureGenerator()

    architecture = generator.generate(
        site_type=SiteType.AGENCY,
        mode=SiteMode.MULTI_PAGE,
    )

    path = tmp_path / "architecture.json"

    serializer = JsonSerializer()

    serializer.save(
        architecture,
        str(path),
    )

    restored = serializer.load(
        str(path),
    )

    assert restored == architecture