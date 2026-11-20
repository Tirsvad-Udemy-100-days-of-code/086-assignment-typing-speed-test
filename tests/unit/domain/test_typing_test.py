"""@file test_typing_test.py
@brief Tests of TypingTest.
"""

from typing_speed_test.domain.enums import CharacterMark, TestState
from typing_speed_test.domain.sample_text import SampleText
from typing_speed_test.domain.typing_test import TypingTest

SAMPLE = SampleText("abc")
START = 100.0


def ready_test() -> TypingTest:
    return TypingTest(SAMPLE, 60)


def running_test(typed_text: str = "a") -> TypingTest:
    return ready_test().with_typed_text(typed_text, START)


def test_state_is_ready_without_times() -> None:
    assert TypingTest(SAMPLE, 60).state() is TestState.READY


def test_state_is_running_with_start_time() -> None:
    assert TypingTest(SAMPLE, 60, "a", started_at=1.0).state() is TestState.RUNNING


def test_state_is_finished_with_end_time() -> None:
    test = TypingTest(SAMPLE, 60, "abc", started_at=1.0, finished_at=5.0)
    assert test.state() is TestState.FINISHED


def test_new_test_has_empty_typed_text() -> None:
    assert TypingTest(SAMPLE, 60).typed_text == ""


def test_marks_are_all_pending_before_typing() -> None:
    assert ready_test().marks() == (CharacterMark.PENDING,) * 3


def test_marks_show_matching_characters_as_correct() -> None:
    marks = running_test("ab").marks()
    assert marks == (
        CharacterMark.CORRECT,
        CharacterMark.CORRECT,
        CharacterMark.PENDING,
    )


def test_marks_show_a_different_character_as_wrong() -> None:
    marks = running_test("ax").marks()
    assert marks == (
        CharacterMark.CORRECT,
        CharacterMark.WRONG,
        CharacterMark.PENDING,
    )


def test_counts_split_correct_and_wrong_characters() -> None:
    test = ready_test().with_typed_text("axc", START)
    assert test.correct_characters() == 2
    assert test.wrong_characters() == 1


def test_deleting_a_wrong_character_makes_it_pending_again() -> None:
    test = running_test("ax").with_typed_text("a", START + 1)
    assert test.wrong_characters() == 0
    assert test.marks()[1] is CharacterMark.PENDING
    assert test.state() is TestState.RUNNING


def test_empty_text_does_not_start_the_clock() -> None:
    test = ready_test().with_typed_text("", START)
    assert test.state() is TestState.READY
    assert test.started_at is None


def test_first_character_starts_the_clock() -> None:
    test = ready_test().with_typed_text("a", START)
    assert test.state() is TestState.RUNNING
    assert test.started_at == START


def test_later_input_keeps_the_start_time() -> None:
    test = running_test("a").with_typed_text("ab", START + 5)
    assert test.started_at == START


def test_deleting_everything_keeps_the_test_running() -> None:
    test = running_test("a").with_typed_text("", START + 5)
    assert test.state() is TestState.RUNNING
    assert test.started_at == START


def test_complete_text_finishes_the_test_at_that_moment() -> None:
    test = running_test("a").with_typed_text("abc", START + 12)
    assert test.state() is TestState.FINISHED
    assert test.finished_at == START + 12
    assert test.elapsed_seconds(START + 500) == 12


def test_complete_text_with_mistakes_also_finishes() -> None:
    assert running_test("a").with_typed_text("xyz", START + 3).state() is (
        TestState.FINISHED
    )


def test_text_longer_than_the_sample_is_cut() -> None:
    test = running_test("a").with_typed_text("abcdef", START + 3)
    assert test.typed_text == "abc"
    assert test.state() is TestState.FINISHED


def test_input_just_before_the_time_is_up_is_taken() -> None:
    test = running_test("a").with_typed_text("ab", START + 59.9)
    assert test.typed_text == "ab"
    assert test.state() is TestState.RUNNING


def test_input_at_sixty_seconds_is_refused_and_finishes_the_test() -> None:
    test = running_test("a").with_typed_text("ab", START + 60)
    assert test.typed_text == "a"
    assert test.state() is TestState.FINISHED
    assert test.finished_at == START + 60


def test_input_after_a_finished_test_changes_nothing() -> None:
    finished = running_test("a").with_typed_text("abc", START + 5)
    assert finished.with_typed_text("", START + 6) is finished


def test_check_time_keeps_a_running_test_before_the_time_is_up() -> None:
    test = running_test()
    assert test.check_time(START + 59.9) is test


def test_check_time_finishes_a_running_test_at_sixty_seconds() -> None:
    test = running_test().check_time(START + 60)
    assert test.state() is TestState.FINISHED
    assert test.finished_at == START + 60


def test_check_time_sets_the_end_at_the_limit_even_when_called_late() -> None:
    test = running_test().check_time(START + 75)
    assert test.finished_at == START + 60
    assert test.elapsed_seconds(START + 75) == 60


def test_check_time_leaves_a_ready_test_alone() -> None:
    test = ready_test()
    assert test.check_time(START + 1000) is test


def test_check_time_leaves_a_finished_test_alone() -> None:
    finished = running_test().check_time(START + 60)
    assert finished.check_time(START + 90) is finished


def test_elapsed_is_zero_before_the_first_key() -> None:
    assert ready_test().elapsed_seconds(START) == 0


def test_elapsed_counts_from_the_first_key() -> None:
    assert running_test().elapsed_seconds(START + 20) == 20


def test_remaining_is_the_full_time_before_the_first_key() -> None:
    assert ready_test().remaining_seconds(START) == 60


def test_remaining_counts_down_while_running() -> None:
    assert running_test().remaining_seconds(START + 20) == 40


def test_remaining_is_never_negative() -> None:
    assert running_test().remaining_seconds(START + 90) == 0
