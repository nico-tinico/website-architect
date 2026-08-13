# Website Architect

Website Architect is a Python package and CLI for generating
website information architectures from reusable, catalog-driven
site profiles.

It transforms a website type and architecture mode into a
validated structural model that can be serialized as JSON
and consumed by other systems.

## Features

- Catalog-driven architecture generation
- Reusable website profiles
- Single-page and multi-page architectures
- Hierarchical, sequential, and matrix topologies
- Runtime templates
- Collections and dynamic entry points
- Semantic architecture validation
- Graph-based navigation relationships
- JSON serialization and deserialization
- CLI interface
- Deterministic architecture generation

## Supported Website Types

Website Architect currently supports **10** website profiles

| Type         | Value          |
| ------------ | -------------- |
| Landing Page | `landing_page` |
| SaaS         | `saas`         |
| Agency       | `agency`       |
| Portfolio    | `portfolio`    |
| Ecommerce    | `ecommerce`    |
| Travel       | `travel`       |
| Wellness     | `wellness`     |
| Fintech      | `fintech`      |
| Technology   | `technology`   |
| Fashion      | `fashion`      |

## Architecture Modes

| Mode        | Value         |
| ----------- | ------------- |
| Single Page | `single_page` |
| Multi Page  | `multi_page`  |

## Installation

Website Architect requires **Python 3.11** or **later**.

### Install from source

Clone the repository and install the package in editable mode:

```
git clone <repository-url>
cd website-architect
python -m pip install -e .
```

This installs Website Architect together with its CLI command:

```
website-architect
```

Verify the installation:

```
website-architect --help
```

### Development installation

To install the development dependencies, including the test suite:

```
python -m pip install -e ".[dev]"
```

You can then run the complete test suite with:

```
python -m pytest
```

A successful installation should allow both the Python package and the `website-architect` CLI to be used directly from the environment.

## CLI

Website Architect provides a command-line interface for generating website architectures directly from the terminal.

The main command is:

```
website-architect
```

### Generate an architecture

Use the generate command:

```
website-architect generate --type ecommerce --mode multi_page
```

By default, the generated architecture is written to standard output.

To save the generated architecture as a JSON file, use `--output`:

```
website-architect generate \
    --type ecommerce \
    --mode multi_page \
    --output ecommerce.json
```

On Windows PowerShell, the same command can be written on a single line:

```
website-architect generate --type ecommerce --mode multi_page --output ecommerce.json
```

### Options

The `generate` command accepts the following options:

| Option     | Description                               |
| ---------- | ----------------------------------------- |
| `--type`   | Website type to generate                  |
| `--mode`   | Architecture mode                         |
| `--output` | Optional path for the generated JSON file |

### Supported website types

```
landing_page
saas
agency
portfolio
ecommerce
travel
wellness
fintech
technology
fashion
```

### Supported modes

```
single_page
multi_page
```

### Examples

Generate a single-page SaaS architecture:

```
website-architect generate --type saas --mode single_page
```

Generate a multi-page agency architecture:

```
website-architect generate --type agency --mode multi_page
```

Generate a multi-page portfolio and save it to a file:

```
website-architect generate \
    --type portfolio \
    --mode multi_page \
    --output portfolio.json
```

### Help

Display the available CLI commands:

```
website-architect --help
```

Display the options for the `generate` command:

```
website-architect generate --help
```

The CLI uses the same architecture generation pipeline as the Python API, ensuring that architectures generated from the terminal follow the same catalog definitions, validation rules, templates, graph relationships, and JSON serialization contract.

## Python API

Website Architect can also be used as a Python library, allowing generated architectures to be integrated directly into other applications and workflows.

### Generate an architecture

```
from website_architect.domain.enums import SiteMode, SiteType
from website_architect.generator.generator import ArchitectureGenerator


generator = ArchitectureGenerator()

architecture = generator.generate(
    site_type=SiteType.ECOMMERCE,
    mode=SiteMode.MULTI_PAGE,
)
```

The returned `SiteArchitecture` contains the complete generated architecture, including:

- website type and mode
- topology
- architecture nodes
- reusable templates
- graph relationships
- template references

### Validate an architecture

Generated architectures are validated automatically by the generator.

Validation can also be performed explicitly:

```
architecture.validate()
```

This verifies structural and semantic constraints, including node relationships, parent references, template references, positions, and graph links.

### Serialize an architecture

Use `JsonSerializer` to convert an architecture into the JSON representation:

```
from website_architect.serializer.json import JsonSerializer


serializer = JsonSerializer()

json_data = serializer.serialize(architecture)

print(json_data)
```

### Save an architecture

The serializer can write the generated architecture directly to a JSON file:

```
serializer.save(
    architecture,
    "ecommerce.json",
)
```

### Complete example

A complete generation workflow can therefore be written as:

```
from website_architect.domain.enums import SiteMode, SiteType
from website_architect.generator.generator import ArchitectureGenerator
from website_architect.serializer.json import JsonSerializer


generator = ArchitectureGenerator()
serializer = JsonSerializer()

architecture = generator.generate(
    site_type=SiteType.ECOMMERCE,
    mode=SiteMode.MULTI_PAGE,
)

serializer.save(
    architecture,
    "ecommerce.json",
)
```

The Python API and CLI use the same underlying generation pipeline. This means architectures generated programmatically follow the same catalog definitions, validation rules, template system, graph construction, and serialization contract as architectures generated through the command line.

## Output Format

Website Architect generates a structured JSON representation of the website architecture.

The output is designed to be deterministic, machine-readable, and suitable for consumption by other tools or systems.

A generated architecture follows this structure:

```
{
    "version": "1.0",
    "site": {
        "type": "ecommerce",
        "mode": "multi_page",
        "topology": "matrix"
    },
    "root_id": "home",
    "nodes": [],
    "templates": [],
    "links": []
}
```

### Top-level fields

| Field       | Description                                       |
| ----------- | ------------------------------------------------- |
| `version`   | Architecture schema version                       |
| `site`      | Website type, mode, and topology                  |
| `root_id`   | Identifier of the root architecture node          |
| `nodes`     | Concrete nodes composing the website architecture |
| `templates` | Reusable content templates                        |
| `links`     | Relationships between architecture nodes          |

### Site

The `site` object describes the high-level configuration:

```
{
    "type": "ecommerce",
    "mode": "multi_page",
    "topology": "matrix"
}
```

`type` identifies the website profile, while `mode` determines whether the architecture is single-page or multi-page. `topology` describes the structural organization of the generated architecture.

### Nodes

Each node represents a concrete element of the website information architecture:

```
{
    "id": "home.shop",
    "name": "Shop",
    "type": "page",
    "required": true,
    "repeatable": false,
    "purpose": "Provide the main product discovery and browsing experience for the store.",
    "parent_id": "home",
    "position": 0
}
```

Depending on the node type, a node can also contain a template reference:

```
{
    "id": "home.shop.category",
    "name": "Category",
    "type": "collection",
    "required": true,
    "repeatable": false,
    "purpose": "Organize products into meaningful categories for browsing and discovery.",
    "parent_id": "home.shop",
    "position": 0,
    "item_template": "product"
}
```

Entry points use `target_template` instead:

```
{
    "id": "home.product",
    "name": "Product",
    "type": "entry_point",
    "required": true,
    "repeatable": false,
    "purpose": "Provide direct access to individual product pages.",
    "parent_id": "home",
    "position": 1,
    "target_template": "product"
}
```

### Templates

Templates define reusable structures for repeatable content entities:

```
{
    "id": "product",
    "name": "Product",
    "type": "template",
    "required": true,
    "repeatable": true,
    "purpose": "Present an individual product and support product evaluation and purchase."
}
```

Collections reference templates through `item_template`, while entry points reference them through `target_template`.

### Links

Links describe relationships between architecture nodes:

```
{
    "source": "home.shop",
    "target": "home.product",
    "type": "navigation"
}
```

The supported link types are:

- `navigation`
- `cta`

Together, `nodes`, `templates`, and `links` provide a complete machine-readable representation of the generated website architecture.

## Architecture Model

Website Architect represents a website as a structured information architecture composed of **nodes**, **templates**, and **relationships**.

The model separates the reusable definitions stored in the catalog from the concrete architecture generated for a specific website type and mode.

Core concepts

```
Site Architecture
│
├── Site configuration
│   ├── Type
│   ├── Mode
│   └── Topology
│
├── Nodes
│   ├── Pages
│   ├── Sections
│   ├── Collections
│   └── Entry Points
│
├── Templates
│   └── Reusable content structures
│
└── Graph
    └── Relationships between nodes
```

### Site Architecture

The `SiteArchitecture` is the complete runtime representation produced by the generator.

It contains:

- the architecture version
- website type
- architecture mode
- topology
- root node
- concrete nodes
- reusable templates
- the architecture graph

```
SiteArchitecture(
    version="1.0",
    site_type=SiteType.ECOMMERCE,
    mode=SiteMode.MULTI_PAGE,
    topology=Topology.MATRIX,
    root_id="home",
    nodes=...,
    templates=...,
    graph=...,
)
```

The generated architecture is validated before being returned by the generator.

### Nodes

A `Node` represents a concrete element of the generated information architecture.

Website Architect supports the following node types:

| Type          | Purpose                                                |
| ------------- | ------------------------------------------------------ |
| `page`        | Represents a website page                              |
| `section`     | Represents a section within a single-page architecture |
| `collection`  | Represents a collection of repeatable entities         |
| `entry_point` | Provides access to an individual template instance     |

Nodes can form hierarchical relationships through `parent_id` and `position`.

For example:

```
home
└── shop
    └── category
```

A collection can reference the template used for its items:

```
Category
    └── item_template → product
```

An entry point can expose the corresponding individual template:

```
Product
    └── target_template → product
```

### Templates

Templates represent reusable structures for repeatable content entities.

They are intentionally separate from navigation nodes.

For example, an ecommerce architecture can define:

```
product
collection
```

The catalog defines these templates once, while generated collections and entry points reference them.

This allows the same architectural model to represent both static website structure and dynamic content entities.

### Graph

The architecture graph represents relationships between nodes.

Each relationship contains:

```
source
target
type
```

The supported relationship types are:

- `navigation`
- `cta`

For example:

```
home.shop
    │
    └── navigation → home.product
```

The graph is therefore complementary to the node hierarchy: `parent_id` describes structural containment, while graph links describe relationships and navigation flows.

### Catalog-driven generation

The architecture model is generated from reusable `SiteProfile` definitions.

The relationship between the catalog and runtime model is:

```
Site Profile
    │
    ├── Page Definitions
    ├── Template Definitions
    └── Link Rules
            │
            ▼
        Architecture Generator
            │
            ▼
        Site Architecture
              │
        ┌─────┼─────┐
        ▼     ▼     ▼
      Nodes Templates Graph
```

This separation allows website profiles to define **what an architecture should contain**, while the generator produces the concrete runtime representation.

### Validation

The architecture model enforces both structural and semantic constraints.

Validation covers:

- root node existence
- unique node IDs
- unique template IDs
- valid parent references
- valid node positions
- valid template references
- collection/entry-point semantics
- valid graph sources and targets
- repeatability constraints

As a result, a generated architecture is not merely a JSON structure: it is a **validated domain model** that can safely be serialized and consumed by downstream systems.

## Development

## Testing

## License
