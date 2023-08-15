from unittest.mock import patch

from code_challenges.advent_of_code.get_past_gaurd import (
    organize_schedule,
    track_each_gaurd,
    find_gaurd_asleep_most,
    when_to_sneak_in,
    gaurd_who_sleeps_most_on_same_hour,
)


@patch("code_challenges.advent_of_code.get_past_gaurd.get_gaurd_schedule")
def test_organize_schedule(mock_get_gaurd_schedule):
    mock_get_gaurd_schedule.return_value = [
        "1518-11-03 00:05 Guard #10 begins shift",
        "1518-11-03 00:24 falls asleep",
        "1518-11-01 00:00 Guard #10 begins shift",
        "1518-11-01 00:05 falls asleep",
        "1518-11-01 00:25 wakes up",
        "1518-11-02 00:50 wakes up",
        "1518-11-01 23:58 Guard #99 begins shift",
        "1518-11-01 00:30 falls asleep",
        "1518-11-01 00:55 wakes up",
        "1518-11-04 00:36 falls asleep",
        "1518-11-02 00:40 falls asleep",
        "1518-11-05 00:45 falls asleep",
        "1518-11-03 00:29 wakes up",
        "1518-11-04 00:02 Guard #99 begins shift",
        "1518-11-05 00:55 wakes up",
        "1518-11-04 00:46 wakes up",
        "1518-11-05 00:03 Guard #99 begins shift",
    ]
    actual = organize_schedule()
    expected = [
        ("1518-11-01 00:00", "Guard #10 begins shift"),
        ("1518-11-01 00:05", "falls asleep"),
        ("1518-11-01 00:25", "wakes up"),
        ("1518-11-01 00:30", "falls asleep"),
        ("1518-11-01 00:55", "wakes up"),
        ("1518-11-01 23:58", "Guard #99 begins shift"),
        ("1518-11-02 00:40", "falls asleep"),
        ("1518-11-02 00:50", "wakes up"),
        ("1518-11-03 00:05", "Guard #10 begins shift"),
        ("1518-11-03 00:24", "falls asleep"),
        ("1518-11-03 00:29", "wakes up"),
        ("1518-11-04 00:02", "Guard #99 begins shift"),
        ("1518-11-04 00:36", "falls asleep"),
        ("1518-11-04 00:46", "wakes up"),
        ("1518-11-05 00:03", "Guard #99 begins shift"),
        ("1518-11-05 00:45", "falls asleep"),
        ("1518-11-05 00:55", "wakes up"),
    ]

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.get_past_gaurd.get_gaurd_schedule")
def test_track_each_gaurd(mock_get_gaurd_schedule):
    mock_get_gaurd_schedule.return_value = [
        "1518-11-03 00:05 Guard #10 begins shift",
        "1518-11-03 00:24 falls asleep",
        "1518-11-01 00:00 Guard #10 begins shift",
        "1518-11-01 00:05 falls asleep",
        "1518-11-01 00:25 wakes up",
        "1518-11-02 00:50 wakes up",
        "1518-11-01 23:58 Guard #99 begins shift",
        "1518-11-01 00:30 falls asleep",
        "1518-11-01 00:55 wakes up",
        "1518-11-04 00:36 falls asleep",
        "1518-11-02 00:40 falls asleep",
        "1518-11-05 00:45 falls asleep",
        "1518-11-03 00:29 wakes up",
        "1518-11-04 00:02 Guard #99 begins shift",
        "1518-11-05 00:55 wakes up",
        "1518-11-04 00:46 wakes up",
        "1518-11-05 00:03 Guard #99 begins shift",
    ]
    actual = track_each_gaurd()
    expected = {"#10": [5, 25, 30, 55, 24, 29], "#99": [40, 50, 36, 46, 45, 55]}

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.get_past_gaurd.get_gaurd_schedule")
def test_find_gaurd_asleep_most(mock_get_gaurd_schedule):
    mock_get_gaurd_schedule.return_value = [
        "1518-11-03 00:05 Guard #10 begins shift",
        "1518-11-03 00:24 falls asleep",
        "1518-11-01 00:00 Guard #10 begins shift",
        "1518-11-01 00:05 falls asleep",
        "1518-11-01 00:25 wakes up",
        "1518-11-02 00:50 wakes up",
        "1518-11-01 23:58 Guard #99 begins shift",
        "1518-11-01 00:30 falls asleep",
        "1518-11-01 00:55 wakes up",
        "1518-11-04 00:36 falls asleep",
        "1518-11-02 00:40 falls asleep",
        "1518-11-05 00:45 falls asleep",
        "1518-11-03 00:29 wakes up",
        "1518-11-04 00:02 Guard #99 begins shift",
        "1518-11-05 00:55 wakes up",
        "1518-11-04 00:46 wakes up",
        "1518-11-05 00:03 Guard #99 begins shift",
    ]
    actual = find_gaurd_asleep_most()
    expected = ("#10", 50)

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.get_past_gaurd.get_gaurd_schedule")
def test_when_to_sneak_in(mock_get_gaurd_schedule):
    mock_get_gaurd_schedule.return_value = [
        "1518-11-03 00:05 Guard #10 begins shift",
        "1518-11-03 00:24 falls asleep",
        "1518-11-01 00:00 Guard #10 begins shift",
        "1518-11-01 00:05 falls asleep",
        "1518-11-01 00:25 wakes up",
        "1518-11-02 00:50 wakes up",
        "1518-11-01 23:58 Guard #99 begins shift",
        "1518-11-01 00:30 falls asleep",
        "1518-11-01 00:55 wakes up",
        "1518-11-04 00:36 falls asleep",
        "1518-11-02 00:40 falls asleep",
        "1518-11-05 00:45 falls asleep",
        "1518-11-03 00:29 wakes up",
        "1518-11-04 00:02 Guard #99 begins shift",
        "1518-11-05 00:55 wakes up",
        "1518-11-04 00:46 wakes up",
        "1518-11-05 00:03 Guard #99 begins shift",
    ]
    actual = when_to_sneak_in()
    expected = 240

    assert actual == expected, f"Returned {actual} instead of {expected}"


@patch("code_challenges.advent_of_code.get_past_gaurd.get_gaurd_schedule")
def test_gaurd_who_sleeps_mos_on_same_hour(mock_get_gaurd_schedule):
    mock_get_gaurd_schedule.return_value = [
        "1518-11-03 00:05 Guard #10 begins shift",
        "1518-11-03 00:24 falls asleep",
        "1518-11-01 00:00 Guard #10 begins shift",
        "1518-11-01 00:05 falls asleep",
        "1518-11-01 00:25 wakes up",
        "1518-11-02 00:50 wakes up",
        "1518-11-01 23:58 Guard #99 begins shift",
        "1518-11-01 00:30 falls asleep",
        "1518-11-01 00:55 wakes up",
        "1518-11-04 00:36 falls asleep",
        "1518-11-02 00:40 falls asleep",
        "1518-11-05 00:45 falls asleep",
        "1518-11-03 00:29 wakes up",
        "1518-11-04 00:02 Guard #99 begins shift",
        "1518-11-05 00:55 wakes up",
        "1518-11-04 00:46 wakes up",
        "1518-11-05 00:03 Guard #99 begins shift",
    ]
    actual = gaurd_who_sleeps_most_on_same_hour()
    expected = 4455

    assert actual == expected, f"Returned {actual} instead of {expected}"
