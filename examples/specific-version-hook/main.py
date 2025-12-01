"""A simple example that uses a third-party dependency."""

from typing import Any

import requests


def fetch_data(url: str) -> dict[str, Any]:
    """Fetch JSON data from a URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def main() -> None:
    """Main entry point."""
    data = fetch_data("https://api.github.com/repos/facebook/pyrefly")
    print(f"Repository: {data['full_name']}")
    print(f"Stars: {data['stargazers_count']}")


if __name__ == "__main__":
    main()
