"""Minimal walking skeleton for a Hello World project."""


def greet(name: str = "World") -> str:
    """Return a friendly greeting for the provided name."""
    return f"Hello, {name}!"


def main() -> None:
    """Run the app entry point."""
    print(greet())


if __name__ == "__main__":
    main()
