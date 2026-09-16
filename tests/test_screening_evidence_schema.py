import copy
import json
from pathlib import Path
from typing import Protocol, cast
from unittest import TestCase

from jsonschema import Draft202012Validator, FormatChecker, ValidationError

SCHEMA_PATH = Path("schemas/screening-evidence.schema.json")
FIXTURE_PATH = Path("tests/fixtures/screening-evidence-v1.json")


class Validator(Protocol):
    def validate(self, instance: object) -> None: ...


def load_object(path: Path) -> dict[str, object]:
    return cast(dict[str, object], json.loads(path.read_text(encoding="utf-8")))


class ScreeningEvidenceSchemaTests(TestCase):
    def setUp(self) -> None:
        self.schema = load_object(SCHEMA_PATH)
        self.fixture = load_object(FIXTURE_PATH)
        Draft202012Validator.check_schema(self.schema)
        self.validator = cast(
            Validator,
            Draft202012Validator(self.schema, format_checker=FormatChecker()),
        )

    def test_contract_fixture_is_valid(self) -> None:
        self.validator.validate(self.fixture)

    def test_candidate_history_is_mandatory(self) -> None:
        invalid = copy.deepcopy(self.fixture)
        invalid.pop("candidate_history")

        with self.assertRaisesRegex(ValidationError, "candidate_history"):
            self.validator.validate(invalid)

    def test_revision_must_be_a_full_lowercase_git_sha(self) -> None:
        invalid = copy.deepcopy(self.fixture)
        analysis = cast(dict[str, object], invalid["analysis"])
        analysis["code_revision"] = "not-a-revision"

        with self.assertRaisesRegex(ValidationError, "does not match"):
            self.validator.validate(invalid)
