# AGENTS.md

## Project scope

This repository contains the `buienradar` Python library and command-line interface for retrieving and parsing Buienradar weather and precipitation data. Preserve the public Python API and existing output shapes unless a change explicitly requires otherwise.

## Instructions precedence

- Follow applicable system, developer, and user instructions first.
- Treat this file as repository-specific development guidance.
- Read `AI_POLICY.md` before making substantive changes with an AI coding agent.
- Inspect the implementation, related tests, and callers before changing behavior. Do not assume a file, workflow, dependency, or command exists without checking the repository.
- If instructions conflict, follow the higher-priority instruction and document material unresolved conflicts.

## Compatibility

- `setup.py` declares `python_requires=">=3.9"` and classifiers through Python 3.14. Keep production code compatible with Python 3.9 unless the project explicitly changes its supported Python floor.
- Do not use syntax or standard-library behavior unavailable in the minimum supported Python version. In particular, normalize an ISO 8601 trailing `Z` to `+00:00` before calling `datetime.fromisoformat()` when Python 3.9 compatibility is required.
- Preserve timezone semantics: an ISO 8601 `Z` suffix means UTC; an explicit numeric offset must be preserved; legacy timestamps without a timezone must retain the repository's established Europe/Amsterdam interpretation unless the task explicitly changes that contract.
- Avoid unrelated dependency upgrades and broad refactors when a focused fix is sufficient.
- Keep public function signatures, result dictionaries, command-line behavior, and documented behavior backward-compatible unless a breaking change is intended and explained.

## Python implementation

- Follow the style of the surrounding code and the existing `setup.cfg` lint configuration; the configured maximum line length is 100 characters.
- Add or update docstrings for changed public functions and non-obvious behavior.
- Add useful type annotations to new or changed code without introducing unsupported syntax for Python 3.9.
- Handle expected malformed or missing external data explicitly. Avoid broad exception handlers unless they are required by an established boundary and are documented.
- Do not silently change units, timestamp interpretation, missing-value behavior, or API payload structure.
- Do not compare floating-point values for exact equality when a tolerance or domain-specific comparison is appropriate.
- Keep network access, parsing, and conversion behavior deterministic and testable. Mock external HTTP calls in unit tests.

## Tests and validation

- Add regression tests for bug fixes and tests for changed behavior, including valid, invalid, and boundary inputs where relevant.
- Follow the existing pytest conventions and place tests under `tests/`.
- Run focused tests first, then the broader relevant suite. The repository's `tox.ini` defines `pytest`, `lint`, and `typing` environments; inspect the current configuration before relying on a command.
- Run lint and typing checks when the change affects code covered by those checks.
- Verify compatibility against the declared minimum Python version when possible. If a runtime or dependency is unavailable, state that validation was not run; never claim a test passed without executing it.
- Do not weaken, delete, or skip a test merely to make a change pass. Explain any necessary test adjustment.

## Changes and pull requests

- Keep changes narrowly scoped and explain the user-visible behavior being fixed.
- Review the final diff for regressions, accidental generated files, secrets, and unrelated edits.
- For behavior changes, describe the previous behavior, corrected behavior, and compatibility implications in the pull request.
- Report the exact validation commands and their outcomes. Clearly distinguish completed checks from checks that remain unrun.
