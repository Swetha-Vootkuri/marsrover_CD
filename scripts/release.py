"""Bump the project version, tag it, and push to trigger the release pipeline.

Usage: python scripts/release.py 0.2.0 [--yes]
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
VERSION_LINE = re.compile(r'^version = "([^"]*)"$', re.MULTILINE)
BRANCH = "main"
REMOTE = "origin"


def fail(message: str) -> None:
    sys.exit(f"error: {message}")


def git(*args: str) -> str:
    result = subprocess.run(["git", *args], capture_output=True, text=True)
    if result.returncode != 0:
        fail(f"git {' '.join(args)} failed:\n{result.stderr.strip()}")
    return result.stdout.strip()


def parse(version: str) -> tuple:
    match = SEMVER.match(version)
    if not match:
        fail(f"'{version}' is not a valid MAJOR.MINOR.PATCH version")
    return tuple(int(part) for part in match.groups())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("version", help="new version, e.g. 0.2.0 (a leading 'v' is accepted)")
    parser.add_argument("--yes", action="store_true", help="skip the confirmation prompt")
    args = parser.parse_args()

    new_version = args.version[1:] if args.version.startswith("v") else args.version
    new = parse(new_version)
    tag = f"v{new_version}"

    root = Path(git("rev-parse", "--show-toplevel"))
    pyproject = root / "pyproject.toml"

    if git("rev-parse", "--abbrev-ref", "HEAD") != BRANCH:
        fail(f"must be on '{BRANCH}'")
    if git("status", "--porcelain"):
        fail("working tree has uncommitted or untracked changes; commit or stash them first")

    git("fetch", REMOTE, BRANCH, "--tags")
    if git("rev-parse", "HEAD") != git("rev-parse", f"{REMOTE}/{BRANCH}"):
        fail(f"local '{BRANCH}' differs from '{REMOTE}/{BRANCH}'; pull/push first")

    text = pyproject.read_text(encoding="utf-8")
    matches = VERSION_LINE.findall(text)
    if len(matches) != 1:
        fail(f"expected exactly one 'version = \"...\"' line in pyproject.toml, found {len(matches)}")
    current_version = matches[0]
    if new <= parse(current_version):
        fail(f"{new_version} must be greater than current version {current_version}")

    existing = [t[1:] for t in git("tag", "--list", "v*").splitlines() if SEMVER.match(t[1:])]
    if existing:
        latest = max(existing, key=parse)
        if new <= parse(latest):
            fail(f"{new_version} must be greater than latest release tag v{latest}")
    if git("ls-remote", "--tags", REMOTE, f"refs/tags/{tag}"):
        fail(f"tag {tag} already exists on {REMOTE}")

    tests = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-q"], cwd=root)
    if tests.returncode != 0:
        fail("tests failed; not releasing")

    print(f"\nRelease {current_version} -> {new_version}: commit, tag {tag}, push to {REMOTE}/{BRANCH}")
    if not args.yes and input("Continue? [y/N] ").strip().lower() != "y":
        fail("aborted")

    pyproject.write_text(VERSION_LINE.sub(f'version = "{new_version}"', text), encoding="utf-8")
    git("add", str(pyproject))
    git("commit", "-m", f"Release {tag}")
    git("tag", "-a", tag, "-m", f"Release {tag}")

    push = subprocess.run(["git", "push", "--atomic", REMOTE, BRANCH, tag])
    if push.returncode != 0:
        git("tag", "-d", tag)
        git("reset", "--keep", "HEAD~1")
        fail("push failed; local release commit and tag were rolled back")

    print(f"\nPushed {tag}. Track the pipeline at https://github.com/Swetha-Vootkuri/marsrover_CD/actions")


if __name__ == "__main__":
    main()
