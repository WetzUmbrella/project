import pytest
from project import grid_configure, button_click, win_condition, win_screen, tie_screen


def test_grid_configure():
    assert grid_configure(root, 1, 1) == pass