"""Install wheel and sdist independently and smoke-test public entry points."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import tempfile
import tomllib
from collections.abc import Sequence
from pathlib import Path
from typing import cast


def project_version(manifest: Path) -> str:
    document = tomllib.loads(manifest.read_text(encoding="utf-8"))
    project = cast(dict[str, object], document["project"])
    version = project.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError("project version is missing")
    return version


def python_in(environment: Path) -> Path:
    if os.name == "nt":
        return environment / "Scripts" / "python.exe"
    return environment / "bin" / "python"


def entry_point_in(environment: Path, name: str) -> Path:
    suffix = ".exe" if os.name == "nt" else ""
    directory = "Scripts" if os.name == "nt" else "bin"
    return environment / directory / f"{name}{suffix}"


def distribution_paths(directory: Path, version: str) -> list[Path]:
    expected = [
        directory / f"jawa-{version}-py3-none-any.whl",
        directory / f"jawa-{version}.tar.gz",
    ]
    missing = [str(path) for path in expected if not path.is_file()]
    if missing:
        raise ValueError(f"missing distributions: {missing}")
    return expected


def smoke_distribution(artifact: Path, version: str) -> None:
    with tempfile.TemporaryDirectory(prefix="jawa-dist-smoke-") as temporary:
        environment = Path(temporary) / "venv"
        subprocess.run(
            ["uv", "venv", "--python", sys.executable, str(environment)],
            check=True,
        )
        python = python_in(environment)
        subprocess.run(
            ["uv", "pip", "install", "--python", str(python), str(artifact)],
            check=True,
        )
        program = (
            "from importlib.metadata import version; "
            "import jawa; "
            f"assert version('jawa') == {version!r}; "
            "assert jawa.__doc__"
        )
        subprocess.run([str(python), "-c", program], check=True)
        for name in ("jawa", "jawa-regression", "jawa-validate", "jawa-dataset"):
            subprocess.run(
                [str(entry_point_in(environment, name)), "--help"],
                check=True,
                stdout=subprocess.DEVNULL,
            )


def parser() -> argparse.ArgumentParser:
    command = argparse.ArgumentParser(description=__doc__)
    command.add_argument("--dist-dir", type=Path, default=Path("dist"))
    command.add_argument("--manifest", type=Path, default=Path("pyproject.toml"))
    return command


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    version = project_version(cast(Path, args.manifest))
    artifacts = distribution_paths(cast(Path, args.dist_dir), version)
    for artifact in artifacts:
        smoke_distribution(artifact, version)
        print(f"smoke-tested {artifact}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
