from __future__ import annotations

import json
from typing import Any

from website_architect.domain.architecture import SiteArchitecture
from website_architect.domain.enums import (
    LinkType,
    NodeType,
    SiteMode,
    SiteType,
    Topology,
)
from website_architect.domain.graph import SiteGraph
from website_architect.domain.links import Link
from website_architect.domain.nodes import Node
from website_architect.domain.templates import Template


class JsonSerializer:
    """
    Serialize and deserialize SiteArchitecture instances using JSON.

    The JSON representation is the external serialization contract of
    the architecture package.
    """

    def serialize(
        self,
        architecture: SiteArchitecture,
    ) -> str:
        """
        Serialize a SiteArchitecture into formatted JSON.
        """
        data = {
            "version": architecture.version,
            "site": {
                "type": architecture.site_type.value,
                "mode": architecture.mode.value,
                "topology": architecture.topology.value,
            },
            "root_id": architecture.root_id,
            "nodes": [
                self._serialize_node(node)
                for node in architecture.nodes
            ],
            "templates": [
                self._serialize_template(template)
                for template in architecture.templates
            ],
            "links": [
                self._serialize_link(link)
                for link in architecture.graph.links
            ],
        }

        return json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )

    def deserialize(
        self,
        content: str,
    ) -> SiteArchitecture:
        """
        Deserialize JSON into a validated SiteArchitecture.
        """
        data = self._load_json(content)

        site = self._require_mapping(
            data,
            "site",
        )

        nodes_data = self._require_list(
            data,
            "nodes",
        )

        templates_data = self._require_list(
            data,
            "templates",
        )

        links_data = self._require_list(
            data,
            "links",
        )

        nodes = tuple(
            self._deserialize_node(item)
            for item in nodes_data
        )

        templates = tuple(
            self._deserialize_template(item)
            for item in templates_data
        )

        links = tuple(
            self._deserialize_link(item)
            for item in links_data
        )

        architecture = SiteArchitecture(
            version=self._require_string(
                data,
                "version",
            ),
            site_type=self._deserialize_enum(
                SiteType,
                site,
                "type",
            ),
            mode=self._deserialize_enum(
                SiteMode,
                site,
                "mode",
            ),
            topology=self._deserialize_enum(
                Topology,
                site,
                "topology",
            ),
            root_id=self._require_string(
                data,
                "root_id",
            ),
            nodes=nodes,
            templates=templates,
            graph=SiteGraph(
                links=links,
            ),
        )

        architecture.validate()

        return architecture

    def save(
        self,
        architecture: SiteArchitecture,
        path: str,
    ) -> None:
        """
        Serialize an architecture and save it to a UTF-8 JSON file.
        """
        content = self.serialize(architecture)

        with open(
            path,
            "w",
            encoding="utf-8",
        ) as file:
            file.write(content)
            file.write("\n")

    def load(
        self,
        path: str,
    ) -> SiteArchitecture:
        """
        Load and deserialize an architecture from a JSON file.
        """
        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            return self.deserialize(file.read())

    @staticmethod
    def _serialize_node(
        node: Node,
    ) -> dict[str, Any]:
        data: dict[str, Any] = {
            "id": node.id,
            "name": node.name,
            "type": node.node_type.value,
            "required": node.required,
            "repeatable": node.repeatable,
            "purpose": node.purpose,
            "parent_id": node.parent_id,
            "position": node.position,
        }

        if node.item_template is not None:
            data["item_template"] = node.item_template

        if node.target_template is not None:
            data["target_template"] = node.target_template

        return data

    @staticmethod
    def _serialize_template(
        template: Template,
    ) -> dict[str, Any]:
        return {
            "id": template.id,
            "name": template.name,
            "type": NodeType.TEMPLATE.value,
            "required": template.required,
            "repeatable": template.repeatable,
            "purpose": template.purpose,
        }

    @staticmethod
    def _serialize_link(
        link: Link,
    ) -> dict[str, Any]:
        return {
            "source": link.source,
            "target": link.target,
            "type": link.link_type.value,
        }

    @classmethod
    def _deserialize_node(
        cls,
        data: Any,
    ) -> Node:
        mapping = cls._require_mapping_value(
            data,
            "node",
        )

        return Node(
            id=cls._require_string(
                mapping,
                "id",
            ),
            name=cls._require_string(
                mapping,
                "name",
            ),
            node_type=cls._deserialize_enum(
                NodeType,
                mapping,
                "type",
            ),
            required=cls._require_bool(
                mapping,
                "required",
            ),
            repeatable=cls._require_bool(
                mapping,
                "repeatable",
            ),
            purpose=cls._require_optional_string(
                mapping,
                "purpose",
            ),
            parent_id=cls._require_optional_string(
                mapping,
                "parent_id",
            ),
            position=cls._require_int(
                mapping,
                "position",
            ),
            item_template=cls._require_optional_string(
                mapping,
                "item_template",
            ),
            target_template=cls._require_optional_string(
                mapping,
                "target_template",
            ),
        )

    @classmethod
    def _deserialize_template(
        cls,
        data: Any,
    ) -> Template:
        mapping = cls._require_mapping_value(
            data,
            "template",
        )

        node_type = cls._deserialize_enum(
            NodeType,
            mapping,
            "type",
        )

        if node_type is not NodeType.TEMPLATE:
            raise ValueError(
                "Serialized template must have type 'template'."
            )

        return Template(
            id=cls._require_string(
                mapping,
                "id",
            ),
            name=cls._require_string(
                mapping,
                "name",
            ),
            required=cls._require_bool(
                mapping,
                "required",
            ),
            repeatable=cls._require_bool(
                mapping,
                "repeatable",
            ),
            purpose=cls._require_string(
                mapping,
                "purpose",
            ),
        )

    @classmethod
    def _deserialize_link(
        cls,
        data: Any,
    ) -> Link:
        mapping = cls._require_mapping_value(
            data,
            "link",
        )

        return Link(
            source=cls._require_string(
                mapping,
                "source",
            ),
            target=cls._require_string(
                mapping,
                "target",
            ),
            link_type=cls._deserialize_enum(
                LinkType,
                mapping,
                "type",
            ),
        )

    @staticmethod
    def _load_json(
        content: str,
    ) -> dict[str, Any]:
        try:
            data = json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError(
                "Invalid JSON content."
            ) from exc

        if not isinstance(data, dict):
            raise ValueError(
                "JSON root must be an object."
            )

        return data

    @staticmethod
    def _require_mapping(
        data: dict[str, Any],
        key: str,
    ) -> dict[str, Any]:
        value = data.get(key)

        if not isinstance(value, dict):
            raise ValueError(
                f"Field '{key}' must be an object."
            )

        return value

    @staticmethod
    def _require_mapping_value(
        value: Any,
        name: str,
    ) -> dict[str, Any]:
        if not isinstance(value, dict):
            raise ValueError(
                f"Serialized {name} must be an object."
            )

        return value

    @staticmethod
    def _require_list(
        data: dict[str, Any],
        key: str,
    ) -> list[Any]:
        value = data.get(key)

        if not isinstance(value, list):
            raise ValueError(
                f"Field '{key}' must be an array."
            )

        return value

    @staticmethod
    def _require_string(
        data: dict[str, Any],
        key: str,
    ) -> str:
        value = data.get(key)

        if not isinstance(value, str):
            raise ValueError(
                f"Field '{key}' must be a string."
            )

        return value

    @staticmethod
    def _require_optional_string(
        data: dict[str, Any],
        key: str,
    ) -> str | None:
        value = data.get(key)

        if value is None:
            return None

        if not isinstance(value, str):
            raise ValueError(
                f"Field '{key}' must be a string or null."
            )

        return value

    @staticmethod
    def _require_bool(
        data: dict[str, Any],
        key: str,
    ) -> bool:
        value = data.get(key)

        if not isinstance(value, bool):
            raise ValueError(
                f"Field '{key}' must be a boolean."
            )

        return value

    @staticmethod
    def _require_int(
        data: dict[str, Any],
        key: str,
    ) -> int:
        value = data.get(key)

        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(
                f"Field '{key}' must be an integer."
            )

        return value

    @staticmethod
    def _deserialize_enum(
        enum_type,
        data: dict[str, Any],
        key: str,
    ):
        value = JsonSerializer._require_string(
            data,
            key,
        )

        try:
            return enum_type(value)
        except ValueError as exc:
            raise ValueError(
                f"Invalid value '{value}' for field '{key}'."
            ) from exc