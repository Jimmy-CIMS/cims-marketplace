# Contributing to CIMS Marketplace

Thank you for your interest in contributing. This document outlines the process for adding or updating plugins in the marketplace.

## Who Can Contribute

Contributions are accepted from CIMS Global team members and authorized partners only. External contributions require prior written approval from CIMS Global.

## Adding a New Plugin

1. **Create the plugin directory** under `plugins/<your-plugin-name>/`
2. **Follow the required structure:**
   ```
   plugins/<your-plugin-name>/
   ├── plugin.json
   ├── commands/        # optional
   │   └── *.md
   └── skills/          # optional
       └── <skill-name>/
           └── SKILL.md
   ```
3. **Fill in `plugin.json`** with the required fields:
   ```json
   {
     "name": "your-plugin-name",
     "version": "1.0.0",
     "owner": "Your Team",
     "validated": false
   }
   ```
4. **Register the plugin** in `.claude-plugin/marketplace.json` under the `plugins` array.

## Plugin Requirements

- Plugin names must be lowercase and hyphen-separated (e.g., `my-plugin`)
- Version must follow [Semantic Versioning](https://semver.org/) (`MAJOR.MINOR.PATCH`)
- All commands and skills must include clear descriptions
- `validated` must be `false` until reviewed and approved by CIMS Global

## Updating an Existing Plugin

- Increment the version in both `plugin.json` and `marketplace.json`
- Document what changed in your pull request description

## Pull Request Process

1. Branch off from `main` using the naming convention `feat/<plugin-name>` or `fix/<plugin-name>`
2. Ensure your plugin passes any applicable validation checks
3. Request review from at least one CIMS Global maintainer
4. Do not merge your own pull request

## Questions

Contact the maintainers at info@cims-global.com.
