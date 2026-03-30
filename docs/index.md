# kotti_file

File attachment add-on for [Kotti CMS](https://github.com/disko/Kotti).

## Installation

```bash
uv add kotti_file
```

Add to your Kotti configuration:

```ini
kotti.configurators = kotti_file.includeme
```

## Development

```bash
git clone https://github.com/disko/kotti_file
cd kotti_file
uv sync --group test
uv run pytest
```
