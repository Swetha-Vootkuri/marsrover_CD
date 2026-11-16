"""Minimal walking skeleton for a Hello World project."""


def greet() -> str:
    """Return a greeting which also serves as instructions for initialisation"""
    return f"Please enter initial X, Y coordinates and direction for rover"


def main() -> None:
    """Run the app entry point."""
    print(greet())


if __name__ == "__main__":
    main()
