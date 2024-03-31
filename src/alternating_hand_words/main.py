import typer  # type: ignore
from typing_extensions import Annotated
from pathlib import Path
import importlib.metadata
from loguru import logger

app = typer.Typer()


def left_hand_char_p(chars: str) -> bool:
    """
    Predicate for the characters of the qwerty keyboard
    indicating if all of the characters in chars
    are typically typed by the left hand.

    B is considered to be a left hand character.
    """
    qwerty_lh_chars = tuple("qwert" "asdfg" "zxcvb")
    return all((c.lower() in qwerty_lh_chars for c in chars))


def right_hand_char_p(chars: str) -> bool:
    """
    Same as left_hand_char_p, but for right hand qwerty characters.

    B is somewhat arbitrarily not true here.
    """
    qwerty_rh_chars = tuple("yuiop" "hjkl" "nm")
    return all((c.lower() in qwerty_rh_chars for c in chars))


def alternating_hand_word_p(word: str) -> bool:
    """
    Return True iff each sequential character in word
    would be typed by the alternate hand on a qwerty
    keyboard.

    >>> alternating_hand_word_p("flake")
    True
    """
    match len(word):
        case 0 | 1:
            return True

    is_right_hand: bool = right_hand_char_p(word[:1])
    if not is_right_hand:
        assert left_hand_char_p(word[:1])
    for c_index, c in enumerate(word[1:]):
        # choose the function for the next test
        f = left_hand_char_p if is_right_hand else right_hand_char_p
        # logger.debug(f"{c_index}: {c}: {t}: {word[1:1 + c_index + 1]}")
        if not f(c):
            # logger.debug(f"{word} failed at pos: {c_index + 1}: {word[:c_index + 2]}")
            return False
        is_right_hand = not is_right_hand

    return True


@app.command()
def search(
    word_dict: Annotated[
        Path,
        typer.Option(
            exists=True,
            file_okay=True,
            dir_okay=False,
            writable=False,
            readable=True,
            resolve_path=True,
        ),
    ] = Path("/usr/share/dict/words"),
    minimum_length: int = 3,
    maximum_length: int = 128,
    ignore_proper_names: bool = True,
) -> None:
    """
    Search WORD_DICT for alternating right and left hand words.
    Return an Iterable of matching words.
    """
    with word_dict.open() as wd:
        for w in map(lambda s: s.strip(), wd.readlines()):
            if len(w) < minimum_length:
                continue
            if len(w) > maximum_length:
                continue
            # ignore proper names
            if ignore_proper_names and w[0].isupper():
                continue
            if alternating_hand_word_p(w):
                print(f"{w}")


@app.command()
def version() -> None:
    """
    Report version.
    """
    package_name: str = "alternating-hand-words"
    v = importlib.metadata.version(package_name)
    print(f"{package_name}: {v}")
    typer.Exit()


def main():
    exit_code: int = app()
    return exit_code


if __name__ == "__main__":
    main()
