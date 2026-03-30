# kotti_file

File attachment add-on for [Kotti CMS](https://github.com/disko/Kotti).

## Overview

`kotti_file` extends Kotti with file attachment content types.

## Quickstart

Install as a dependency in your Kotti project:

```bash
uv add "kotti_file @ git+https://github.com/disko/kotti_file.git"
```

Then add to your `app.ini` / `development.ini`:

```ini
kotti.configurators =
    kotti_file.includeme
```

## Development

```bash
git clone https://github.com/disko/kotti_file
cd kotti_file
uv sync --group test
uv run pytest
```

## License

BSD-derived. See `LICENSE.txt`.
