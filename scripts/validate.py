from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from scripts.resource_model import CatalogFormatError, load_resources, validate_resources

DATA_PATH = Path("data/resources.yaml")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the structured resource catalog")
    parser.parse_args(argv)

    try:
        resources = load_resources(DATA_PATH)
    except (CatalogFormatError, OSError) as error:
        print(f"Catalog error: {error}")
        return 1
    errors = validate_resources(resources)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"Validated {len(resources)} resources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
