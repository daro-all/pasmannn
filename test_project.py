import os
from project import SYMBOLS, generate_password, is_strong, entropy, clear_passwords


def test_generate_password():
    pw = generate_password(12, True, True)
    assert len(pw) == 12
    assert any(c.isalpha() for c in pw)
    assert any(c.isdigit() for c in pw)
    assert any(c in SYMBOLS for c in pw)


def test_is_strong():
    assert is_strong("Abc123!!") == True
    assert is_strong("pqr789()") == True
    assert is_strong("[]ASD456") == True
    assert is_strong("abc123") == False
    assert is_strong("abcdefg!") == False
    assert is_strong("12345678") == False


def test_entropy():
    assert entropy("abcDEF") == "Weak 🔴"
    assert entropy("abcdef73") == "Medium 🟡"
    assert entropy("abcdefghijk") == "Weak 🔴"
    assert entropy("abcdef%-RTVe") == "Strong 🟢"
    assert entropy("abcdef%-RTVe1793?") == "Very strong 🔵"


def test_clear_passwords():
    # Temporary file's name
    test_file = "test_pw.txt"

    # Create the file with initial content
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("gmail: test123\nmekka: 1$2%3kng\n")

    # Call the function to clear the file contents
    clear_passwords(test_file)

    # Verify that the file exists and is empty
    assert os.path.exists(test_file)
    with open(test_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ""

    # Remove the temporary file
    os.remove(test_file)
