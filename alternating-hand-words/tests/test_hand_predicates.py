import string
from itertools import chain
from alternating_hand_words.main import left_hand_char_p, right_hand_char_p, alternating_hand_word_p


def test_qwerty_left_hand():
    lh_chars = tuple("qwert" "asdfg" "zxcvb")
    # test both upper and lower case
    both_cases = "".join(tuple(chain.from_iterable([lh_chars, map(lambda c: c.upper(), lh_chars)])))
    assert left_hand_char_p(both_cases)
    assert left_hand_char_p("")


def test_qwerty_right_hand():
    rh_chars = tuple("yuiop" "hjkl" "nm")
    # test both upper and lower case
    both_cases = "".join(tuple(chain.from_iterable([rh_chars, map(lambda c: c.upper(), rh_chars)])))
    assert right_hand_char_p(both_cases)
    assert right_hand_char_p("")


def test_alt_hand_base_cases():
    # all length 1 words are alternating by definition
    for c in string.ascii_letters:
        assert alternating_hand_word_p(c), f"len 1 word: {c}"


def test_alt_hand_words():
    positives = tuple(
        (
            "flake",
            "torment",
        )
    )
    for w in positives:
        assert alternating_hand_word_p(w), f"positive case: {w}"

    negatives = tuple(
        (
            "every",
            "good",
            "boy",
            "does",
            "fine",
        )
    )
    for w in negatives:
        assert not alternating_hand_word_p(w), f"negative case: {w}"
