"""Verify release tag, manifest version, and built distribution identity."""

from __future__ import annotations

import argparse
import tarfile
import tomllib
import zipfile
from collections.abc import Sequence
from email import policy
from email.parser import BytesParser
from pathlib import Path
from typing import cast

PROJECT_NAME = "jawa"


def project_version(manifest: Path) -> str:
    document = tomllib.loads(manifest.read_text(encoding="utf-8"))
    project_value: object = document.get("project")
    if not isinstance(project_value, dict):
        raise ValueError(f"{manifest} has no [project] table")
    project = cast(dict[str, object], project_value)
    version: object = project.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError(f"{manifest} has no valid project version")
    return version


def verify_tag(version: str, tag: str) -> None:
    expected = f"v{version}"
    if tag != expected:
        raise ValueError(f"release tag {tag!r} does not match {expected!r}")


def wheel_identity(wheel: Path) -> tuple[str, str]:
    with zipfile.ZipFile(wheel) as archive:
        metadata_names = [
            name for name in archive.namelist() if name.endswith(".dist-info/METADATA")
        ]
        if len(metadata_names) != 1:
            raise ValueError(f"{wheel} must contain exactly one METADATA file")
        message = BytesParser(policy=policy.default).parsebytes(
            archive.read(metadata_names[0])
        )
    name = str(message.get("Name", ""))
    version = str(message.get("Version", ""))
    return name, version


def sdist_version(sdist: Path) -> str:
    with tarfile.open(sdist, mode="r:gz") as archive:
        members = [
            member
            for member in archive.getmembers()
            if member.isfile() and member.name.endswith("/pyproject.toml")
        ]
        if len(members) != 1:
            raise ValueError(f"{sdist} must contain exactly one pyproject.toml")
        source = archive.extractfile(members[0])
        if source is None:
            raise ValueError(f"cannot read project metadata from {sdist}")
        document = tomllib.loads(source.read().decode("utf-8"))
    project_value: object = document.get("project")
    if not isinstance(project_value, dict):
        raise ValueError(f"{sdist} has no [project] table")
    version = cast(dict[str, object], project_value).get("version")
    if not isinstance(version, str) or not version:
        raise ValueError(f"{sdist} has no valid project version")
    return version


def verify_distributions(directory: Path, version: str) -> None:
    wheel = directory / f"{PROJECT_NAME}-{version}-py3-none-any.whl"
    sdist = directory / f"{PROJECT_NAME}-{version}.tar.gz"
    missing = [str(path) for path in (wheel, sdist) if not path.is_file()]
    if missing:
        raise ValueError(f"missing release distributions: {missing}")
    name, wheel_version = wheel_identity(wheel)
    if name != PROJECT_NAME or wheel_version != version:
        raise ValueError(
            f"wheel identity {(name, wheel_version)!r} does not match "
            f"{(PROJECT_NAME, version)!r}"
        )
    source_version = sdist_version(sdist)
    if source_version != version:
        raise ValueError(f"sdist version {source_version!r} does not match {version!r}")


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument("--tag")
    command.add_argument("--manifest", type=Path, default=Path("pyproject.toml"))
    command.add_argument("--dist-dir", type=Path)
    return command


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    manifest = cast(Path, args.manifest)
    version = project_version(manifest)
    if args.tag is not None:
        verify_tag(version, cast(str, args.tag))
        print(f"release tag {args.tag} matches project metadata")
    if args.dist_dir is not None:
        directory = cast(Path, args.dist_dir)
        verify_distributions(directory, version)
        print(f"distributions in {directory} match {PROJECT_NAME} {version}")
    if args.tag is None and args.dist_dir is None:
        parser().error("at least one of --tag or --dist-dir is required")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
