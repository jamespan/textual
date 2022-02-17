from tests.utilities.render import render
from textual.renderables.underline_bar import UnderlineBar

MAGENTA = "\x1b[35m"
GREY = "\x1b[38;5;59m"
STOP = "\x1b[0m"
GREEN = "\x1b[32m"
RED = "\x1b[31m"


def test_no_highlight():
    bar = UnderlineBar(width=6)
    assert render(bar) == f"{GREY}━━━━━━{STOP}"


def test_highlight_from_zero():
    bar = UnderlineBar(highlight_range=(0, 2.5), width=6)
    assert render(bar) == (
        f"{MAGENTA}━━{STOP}{MAGENTA}╸{STOP}{GREY}━━━{STOP}"
    )


def test_highlight_from_zero_point_five():
    bar = UnderlineBar(highlight_range=(0.5, 2), width=6)
    assert render(bar) == (
        f"{MAGENTA}╺━{STOP}{GREY}╺{STOP}{GREY}━━━{STOP}"
    )


def test_highlight_middle():
    bar = UnderlineBar(highlight_range=(2, 4), width=6)
    assert render(bar) == (
        f"{GREY}━{STOP}"
        f"{GREY}╸{STOP}"
        f"{MAGENTA}━━{STOP}"
        f"{GREY}╺{STOP}"
        f"{GREY}━{STOP}"
    )


def test_highlight_half_start():
    bar = UnderlineBar(highlight_range=(2.5, 4), width=6)
    assert render(bar) == (
        f"{GREY}━━{STOP}"
        f"{MAGENTA}╺━{STOP}"
        f"{GREY}╺{STOP}"
        f"{GREY}━{STOP}"
    )


def test_highlight_half_end():
    bar = UnderlineBar(highlight_range=(2, 4.5), width=6)
    assert render(bar) == (
        f"{GREY}━{STOP}"
        f"{GREY}╸{STOP}"
        f"{MAGENTA}━━{STOP}"
        f"{MAGENTA}╸{STOP}"
        f"{GREY}━{STOP}"
    )


def test_highlight_half_start_and_half_end():
    bar = UnderlineBar(highlight_range=(2.5, 4.5), width=6)
    assert render(bar) == (
        f"{GREY}━━{STOP}"
        f"{MAGENTA}╺━{STOP}"
        f"{MAGENTA}╸{STOP}"
        f"{GREY}━{STOP}"
    )


def test_highlight_to_near_end():
    bar = UnderlineBar(highlight_range=(3, 5.5), width=6)
    assert render(bar) == (
        f"{GREY}━━{STOP}"
        f"{GREY}╸{STOP}"
        f"{MAGENTA}━━{STOP}"
        f"{MAGENTA}╸{STOP}"
    )


def test_highlight_to_end():
    bar = UnderlineBar(highlight_range=(3, 6), width=6)
    assert render(bar) == (
        f"{GREY}━━{STOP}{GREY}╸{STOP}{MAGENTA}━━━{STOP}"
    )


def test_highlight_out_of_bounds_start():
    bar = UnderlineBar(highlight_range=(-2, 3), width=6)
    assert render(bar) == (
        f"{MAGENTA}━━━{STOP}{GREY}╺{STOP}{GREY}━━{STOP}"
    )


def test_highlight_out_of_bounds_end():
    bar = UnderlineBar(highlight_range=(3, 9), width=6)
    assert render(bar) == (
        f"{GREY}━━{STOP}{GREY}╸{STOP}{MAGENTA}━━━{STOP}"
    )


def test_highlight_full_range_out_of_bounds_end():
    bar = UnderlineBar(highlight_range=(9, 10), width=6)
    assert render(bar) == f"{GREY}━━━━━━{STOP}"


def test_highlight_full_range_out_of_bounds_start():
    bar = UnderlineBar(highlight_range=(-5, -2), width=6)
    assert render(bar) == f"{GREY}━━━━━━{STOP}"


def test_custom_styles():
    bar = UnderlineBar(highlight_range=(2, 4), highlight_style="red", background_style="green", width=6)
    assert render(bar) == (
        f"{GREEN}━{STOP}"
        f"{GREEN}╸{STOP}"
        f"{RED}━━{STOP}"
        f"{GREEN}╺{STOP}"
        f"{GREEN}━{STOP}"
    )
