# High level design

The goals of this tool are:
- produce words that are easy to type on a qwerty keyboard because they alternate right to left hand on the qwerty keyboard
- practice my [python typer](https://typer.tiangolo.com/) foo
- implement the idiom that multiple -v gives more logging output
- gain some experience with mypy to enforce typing all the way down
- practice my pytest foo
  - and maybe [pytest-fixture-typecheck](https://pypi.org/project/pytest-fixture-typecheck/)

# Use cases

## find all alternating words
- reading from the system dict words, which should be a parameter to every subcommand

```zsh
ahwords [-v] [--word-list file] search
```
