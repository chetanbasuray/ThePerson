"""Tests for hobby validation and the Person personal container."""

from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from theperson.goals import Goals
from theperson.hobbies import Hobbies, Hobby
from theperson.person import Personal, Person, Profile


def test_hobbies_accepts_only_hobby_objects() -> None:
    hobbies = Hobbies([Hobby("coding"), Hobby("reading")])
    assert [h.name for h in hobbies.list] == ["coding", "reading"]

    with pytest.raises(TypeError):
        Hobbies("coding")

    with pytest.raises(TypeError):
        Hobbies([Hobby("coding"), "reading"])


def test_person_uses_personal_dataclass() -> None:
    hobbies = Hobbies([Hobby("music")])
    goals = Goals()
    goals.add_goal("ship feature")

    person = Person(
        profile=Profile(name="Alex"),
        personal=Personal(hobbies=hobbies, goals=goals),
    )

    assert person.personal.hobbies is hobbies
    assert person.personal.goals is goals
    assert person.hobbies is hobbies
    assert person.goals is goals


def test_legacy_profile_hobbies_migrate_to_personal() -> None:
    profile = Profile(name="Legacy User")
    profile.hobbies = ["chess", "coding"]  # Backward compatibility path

    person = Person(profile=profile)

    assert person.hobbies.summary() == "chess, coding"
