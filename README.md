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

### Generate an architecture

### Options

## Python API

## Output Format

## Architecture Model

## Development

## Testing

## License
