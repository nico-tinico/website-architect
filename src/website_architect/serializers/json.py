import json

from website_architect.domain.architecture import SiteArchitecture


class JsonSerializer:
    def serialize(
        self,
        architecture: SiteArchitecture,
    ) -> str:
        data = {
            "version": architecture.version,
            "site": {
                "type": architecture.site_type.value,
                "mode": architecture.mode.value,
                "topology": architecture.topology.value,
            },
            "root_id": architecture.root_id,
            "nodes": [
                {
                    "id": node.id,
                    "name": node.name,
                    "type": node.node_type.value,
                    "required": node.required,
                    "repeatable": node.repeatable,
                    "purpose": node.purpose,
                    "parent_id": node.parent_id,
                    "position": node.position,
                }
                for node in architecture.nodes
            ],
            "links": [
                {
                    "source": link.source,
                    "target": link.target,
                    "type": link.link_type.value,
                }
                for link in architecture.graph.links
            ],
        }

        return json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )

    def save(
        self,
        architecture: SiteArchitecture,
        path: str,
    ) -> None:
        content = self.serialize(architecture)

        with open(path, "w", encoding="utf-8") as file:
            file.write(content)
            file.write("\n")