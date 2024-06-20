import pytest
from tkinter import Tk, ttk
from unittest.mock import patch
import project  # Import the code from project.py

@pytest.fixture
def setup_app():
    project.root = Tk()
    project.root.title("Test Tic Tac Toe")
    project.root.geometry("600x600")
    project.grid_configure(project.root, 1, 1)
    project.frm = ttk.Frame(project.root, padding=10)
    project.frm.grid(sticky=(project.N, project.S, project.E, project.W))
    project.grid_configure(project.frm, 4, 1)
    project.game = project.PVP
    project.x_player = True
    project.combination = ["", "", "", "", "", "", "", "", ""]
    project.button_style = ttk.Style()
    project.button_style.configure("Large.TButton", font=("Arial", 16), padding=20)
    yield
    project.root.destroy()

def test_grid_configure(setup_app):
    project.grid_configure(project.frm, 4, 4)
    for i in range(4):
        assert project.frm.grid_rowconfigure(i)['weight'] == 1
        assert project.frm.grid_columnconfigure(i)['weight'] == 1

def test_clear_window(setup_app):
    ttk.Label(project.frm, text="Test").grid()
    assert len(project.frm.winfo_children()) > 0
    project.clear_window()
    assert len(project.frm.winfo_children()) == 0

def test_button_click(setup_app):
    button = ttk.Button(project.frm, text="")
    project.button_click(button, 0)
    assert button['text'] == "X"
    assert project.combination[0] == "X"

def test_win_condition_x(setup_app):
    with patch('project.win_screen') as mock_win_screen:
        project.combination = ["X", "X", "X", "", "", "", "", "", ""]
        project.win_condition(project.combination)
        mock_win_screen.assert_called_once_with("X", project.game)

def test_win_condition_o(setup_app):
    with patch('project.win_screen') as mock_win_screen:
        project.combination = ["O", "O", "O", "", "", "", "", "", ""]
        project.win_condition(project.combination)
        mock_win_screen.assert_called_once_with("O", project.game)

def test_tie_condition(setup_app):
    with patch('project.tie_screen') as mock_tie_screen:
        project.combination = ["X", "O", "X", "O", "X", "X", "O", "X", "O"]
        project.win_condition(project.combination)
        mock_tie_screen.assert_called_once_with(project.game)

def test_win_screen(setup_app):
    with patch('project.ttk.Label') as mock_label, patch('project.ttk.Button') as mock_button:
        project.win_screen("X", project.game)
        mock_label.assert_called_with(project.frm, text="Player X Wins", font=("Arial", 18), anchor="center")
        mock_button.assert_any_call(project.frm, text="Restart", command=project.game, style="Large.TButton")
        mock_button.assert_any_call(project.frm, text="Quit", command=project.root.destroy, style="Large.TButton")

def test_tie_screen(setup_app):
    with patch('project.ttk.Label') as mock_label, patch('project.ttk.Button') as mock_button:
        project.tie_screen(project.game)
        mock_label.assert_called_with(project.frm, text="Its a Tie", font=("Arial", 18), anchor="center")
        mock_button.assert_any_call(project.frm, text="Restart", command=project.game, style="Large.TButton")
        mock_button.assert_any_call(project.frm, text="Quit", command=project.root.destroy, style="Large.TButton")

def test_ai_move(setup_app):
    with patch('project.button1.invoke') as mock_invoke:
        project.combination[0] = ""
        project.ai_move()
        assert mock_invoke.called

def test_tic_tac_toe_grid(setup_app):
    project.tic_tac_toe_grid()
    assert isinstance(project.button1, ttk.Button)
    assert isinstance(project.button2, ttk.Button)
    assert isinstance(project.button3, ttk.Button)
    assert isinstance(project.button4, ttk.Button)
    assert isinstance(project.button5, ttk.Button)
    assert isinstance(project.button6, ttk.Button)
    assert isinstance(project.button7, ttk.Button)
    assert isinstance(project.button8, ttk.Button)
    assert isinstance(project.button9, ttk.Button)

def test_pvp(setup_app):
    with patch('project.ttk.Label') as mock_label:
        project.PVP()
        mock_label.assert_called()

def test_pva(setup_app):
    with patch('project.ttk.Label') as mock_label:
        project.PVA()
        mock_label.assert_called()

if __name__ == "__main__":
    pytest.main()
