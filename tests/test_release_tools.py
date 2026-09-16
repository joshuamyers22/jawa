import tempfile
from pathlib import Path
from unittest import TestCase

from tools.checksums import parse_manifest, verify_manifest, write_manifest
from tools.verify_release import project_version, verify_tag


class ChecksumTests(TestCase):
    def test_manifest_is_sorted_complete_and_verifiable(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory / "z.tar.gz").write_bytes(b"source")
            (directory / "a.whl").write_bytes(b"wheel")
            (directory / ".gitignore").write_text("*", encoding="utf-8")

            manifest = write_manifest(directory)

            self.assertEqual(
                [name for _, name in parse_manifest(manifest)],
                ["a.whl", "z.tar.gz"],
            )
            verify_manifest(directory)

    def test_tampered_artifact_fails_verification(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            artifact = directory / "jawa.whl"
            artifact.write_bytes(b"original")
            write_manifest(directory)
            artifact.write_bytes(b"tampered")

            with self.assertRaisesRegex(ValueError, "checksum mismatch"):
                verify_manifest(directory)

    def test_unlisted_artifact_fails_verification(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory / "jawa.whl").write_bytes(b"wheel")
            write_manifest(directory)
            (directory / "unexpected.txt").write_text("unexpected", encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "cover.*exactly"):
                verify_manifest(directory)


class ReleaseIdentityTests(TestCase):
    def test_project_version_is_the_release_identity_source(self) -> None:
        version = project_version(Path("pyproject.toml"))

        verify_tag(version, f"v{version}")
        with self.assertRaisesRegex(ValueError, "does not match"):
            verify_tag(version, "v999.0.0")
