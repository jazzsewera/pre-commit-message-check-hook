pre-commit-message-check-hook
=========================

A commit-msg hook for pre-commit.

See also: https://github.com/pre-commit/pre-commit
Credits for template: https://github.com/avilaton/add-msg-issue-prefix-hook


### Using with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
- repo: https://github.com/jazzsewera/pre-commit-message-check-hook
    rev: v0.2.0  # Use the ref you want to point at
    hooks:
    - id: commit-message-check
```

and install prepare-commit-msg hooks using
```
pre-commit install --hook-type commit-msg
```
