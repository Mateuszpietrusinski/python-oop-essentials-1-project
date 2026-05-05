"""Tests for feeding schedule classes in the Zoo Garden system."""

from zoo import FeedingSchedule


# ---------------------------------------------------------------------------
# Test 14 — FeedingSchedule add/remove entries
# ---------------------------------------------------------------------------

def test_feeding_schedule_add_remove():
    """FeedingSchedule add_entry and remove_entry work correctly."""
    schedule = FeedingSchedule("Tuesday")
    assert len(schedule) == 0

    entry = schedule.add_entry("Savanna", "08:00", "meat", notes="fresh")
    assert len(schedule) == 1

    by_enc = schedule.get_by_enclosure("Savanna")
    assert len(by_enc) == 1
    assert by_enc[0].food_type == "meat"

    schedule.remove_entry(entry)
    assert len(schedule) == 0
