"""Tests for Buienradar timestamp parsing."""

from datetime import UTC, datetime
from zoneinfo import ZoneInfo

from buienradar.buienradar_json import __to_localdatetime


def test_utc_designator_is_parsed_as_utc():
    """Parse an ISO 8601 Z suffix as UTC rather than local time."""
    parsed_dt = __to_localdatetime("2026-10-15T12:30:00Z")

    assert parsed_dt == datetime(2026, 10, 15, 12, 30, tzinfo=UTC)
    assert parsed_dt.tzinfo is UTC


def test_explicit_offset_is_preserved():
    """Preserve an explicit ISO 8601 UTC offset."""
    parsed_dt = __to_localdatetime("2026-10-15T12:30:00+03:00")

    assert parsed_dt == datetime.fromisoformat("2026-10-15T12:30:00+03:00")
    assert parsed_dt.utcoffset().total_seconds() == 3 * 60 * 60


def test_timestamp_without_timezone_uses_amsterdam():
    """Interpret legacy naive timestamps in the Amsterdam timezone."""
    parsed_dt = __to_localdatetime("2026-10-15T12:30:00")

    assert parsed_dt == datetime(
        2026, 10, 15, 12, 30, tzinfo=ZoneInfo("Europe/Amsterdam")
    )


def test_invalid_timestamp_returns_none():
    """Return None for an invalid timestamp."""
    assert __to_localdatetime("not-a-timestamp") is None
