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

## Architecture Model

## Development

## Testing

## License
