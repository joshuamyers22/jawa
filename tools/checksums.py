"""Write or verify a deterministic SHA-256 release manifest."""

from __future__ import annotations

import argparse
import hashlib
import re
from collections.abc import Sequence
from pathlib import Path

DIGEST = re.compile(r"^[0-9a-f]{64}$")
DEFAULT_MANIFEST = "SHA256SUMS"


def release_files(directory: Path, manifest_name: str) -> list[Path]:
    if not directory.is_dir():
        raise ValueError(f"release directory does not exist: {directory}")
    files = sorted(
        (
            path
            for path in directory.iterdir()
            if path.is_file()
            and not path.is_symlink()
            and not path.name.startswith(".")
            and path.name != manifest_name
        ),
        key=lambda path: path.name,
    )
    if not files:
        raise ValueError(f"release directory has no files: {directory}")
    for path in files:
        if "\n" in path.name or "\r" in path.name:
            raise ValueError("release filenames cannot contain newlines")
    return files


def sha256(path: Path) -> str:
    with path.open("rb") as source:
        return hashlib.file_digest(source, "sha256").hexdigest()


def write_manifest(directory: Path, manifest_name: str = DEFAULT_MANIFEST) -> Path:
    manifest = directory / manifest_name
    content = "".join(
        f"{sha256(path)}  {path.name}\n"
        for path in release_files(directory, manifest_name)
    )
    temporary = manifest.with_name(f".{manifest.name}.tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(manifest)
    return manifest


def parse_manifest(manifest: Path) -> list[tuple[str, str]]:
    if not manifest.is_file() or manifest.is_symlink():
        raise ValueError(f"checksum manifest is not a regular file: {manifest}")
    entries: list[tuple[str, str]] = []
    names: set[str] = set()
    for number, line in enumerate(
        manifest.read_text(encoding="utf-8").splitlines(), start=1
    ):
        digest, separator, name = line.partition("  ")
        if not separator or not DIGEST.fullmatch(digest) or not name:
            raise ValueError(f"invalid checksum line {number}")
        if Path(name).name != name or name in names:
            raise ValueError(f"unsafe or duplicate checksum filename: {name!r}")
        names.add(name)
        entries.append((digest, name))
    if not entries:
        raise ValueError("checksum manifest is empty")
    if [name for _, name in entries] != sorted(names):
        raise ValueError("checksum manifest entries are not sorted")
    return entries


def verify_manifest(directory: Path, manifest_name: str = DEFAULT_MANIFEST) -> None:
    manifest = directory / manifest_name
    entries = parse_manifest(manifest)
    expected_names = [path.name for path in release_files(directory, manifest_name)]
    actual_names = [name for _, name in entries]
    if actual_names != expected_names:
        raise ValueError(
            "checksum manifest does not cover the release directory exactly"
        )
    for expected, name in entries:
        actual = sha256(directory / name)
        if actual != expected:
            raise ValueError(f"checksum mismatch: {name}")


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument("operation", choices=("write", "verify"))
    command.add_argument("directory", type=Path)
    command.add_argument("--manifest", default=DEFAULT_MANIFEST)
    return command


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    directory = Path(args.directory)
    manifest_name = str(args.manifest)
    if Path(manifest_name).name != manifest_name:
        raise ValueError("manifest must be a filename, not a path")
    if args.operation == "write":
        manifest = write_manifest(directory, manifest_name)
        print(f"wrote {manifest}")
    else:
        verify_manifest(directory, manifest_name)
        print(f"verified {directory / manifest_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
