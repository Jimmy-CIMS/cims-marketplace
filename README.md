# CIMS Marketplace

A marketplace for plugins and extensions that enhance the capabilities of CIMS products.

## Overview

CIMS Marketplace provides a curated collection of plugins developed by CIMS Global and its partners. Each plugin extends Claude Code with domain-specific commands, skills, and workflows tailored for clinical and biostatistical use cases.

## Available Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| `r-coding-guide` | Standard R coding style and refactoring tools | 1.0.0 |
| `clinical-validation` | Clinical data validation and quality checks | 1.0.0 |
| `oq-test-generator` | Generate OQ test cases for CRE system | 1.0.0 |

## Repository Structure

```
cims-marketplace/
├── .claude-plugin/
│   └── marketplace.json        # Marketplace registry
└── plugins/
    ├── r-coding-guide/         # R style guide and refactoring tools
    ├── clinical-validation/    # Clinical data validation
    └── oq-test-generator/      # OQ test case generation
```

## Usage

Each plugin is self-contained under `plugins/<plugin-name>/` and follows the Claude Code plugin structure:

- `plugin.json` — plugin metadata
- `commands/` — slash commands (`.md` files)
- `skills/` — skills invokable by Claude

Refer to each plugin's directory for plugin-specific documentation.

## License

Copyright © 2026 CIMS Global. All rights reserved.  
This software is proprietary. See [LICENSE](LICENSE) for details.
