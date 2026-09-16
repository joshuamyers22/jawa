.PHONY: setup format lint typecheck test build verify-dist smoke package check audit
PYTHON ?=
UV_PYTHON = $(if $(PYTHON),--python $(PYTHON),)
UV_RUN = uv run $(UV_PYTHON)

setup:
	uv sync --frozen --dev $(UV_PYTHON)
format:
	$(UV_RUN) ruff format .
lint:
	$(UV_RUN) ruff check .
	$(UV_RUN) ruff format --check .
typecheck:
	$(UV_RUN) pyright
test:
	$(UV_RUN) python -m unittest discover -s tests
build:
	uv build
verify-dist: build
	$(UV_RUN) python tools/verify_release.py --dist-dir dist
smoke: verify-dist
	$(UV_RUN) python tools/smoke_dist.py --dist-dir dist
package: verify-dist smoke
check: lint typecheck test package
audit:
	uv audit --preview-features audit-command --locked --no-dev
	$(UV_RUN) python tools/check_licenses.py
