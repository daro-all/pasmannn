# PASMANNN 😎🔐
**Version:** 1.0.0
#### Video Demo: [link to video](https://youtu.be/bJDg3fXvAiA)
#### Description:

PASMANNN (Password Generator & Manager) is a **command-line application** written in Python that allows users to generate, analyze, store, and manage secure passwords locally.  
The program combines interactive features (using the `rich` library for colorful terminal UI), clipboard integration, and password management functionalities into a single, easy-to-use tool.

This project was built to address a common problem: many users still rely on weak or reused passwords, making their accounts vulnerable. PASMANNN offers a fun yet practical way to encourage better password hygiene by making strong password creation and management more accessible.  
The splash screen with a playful `cowsay` message and a stylized menu system is designed to make the tool engaging while remaining practical.

---

## Features

- 🔑 **Generate strong passwords** with customizable length, inclusion of symbols and numbers, and optional multiple outputs.
- 💪 **Check password strength and entropy**, with a simple classification (Weak, Medium, Strong, Very Strong).
- 💾 **Save passwords** locally associated with a service name.
- 📋 **Copy passwords to the clipboard** for easy pasting.
- 📜 **List saved passwords** in a styled table.
- 🗑️ **Delete individual service passwords** or clear the entire file.
- 📖 **Help menu** that loads from `HELP.md` for detailed usage instructions.
- 🎨 Rich terminal UI with tables, panels, and styled text.

---

## Project Structure

- **`project.py`**  
  The main application file. It contains the program’s logic, menu system, and all functionality:
  - `generate_password` → Creates random secure passwords.  
  - `is_strong` / `analyze_password` / `entropy` → Check strength and classify entropy.  
  - `save_password`, `list_passwords`, `delete_password`, `clear_passwords` → File-based password management.  
  - `copy_to_clipboard` → Integrates with the system clipboard via `pyperclip`.  
  - `main()` and others functions → User interface helpers and menu handling.
  
- **`HELP.md`**  
  Contains the **user guide**, loaded when the user selects option 6. It explains each menu option, program notes, and general recommendations.

- **`TODO.md`**  
  A list of pending improvements and ideas, such as moving from plain text storage to JSON, handling duplicates, exporting to CSV, and calculating real entropy.

- **`requirements.txt`**  
  Lists external dependencies:  
  - `pyperclip` → Clipboard functionality  
  - `rich` → Styled console output  
  - `pytest` → Testing framework  
  - `cowsay` → Fun splash screen text animation

- **`test_project.py`**  
  Unit tests for core functions. Covers password generation, strength checking, entropy classification, and clearing the password file. Tests ensure that edge cases are handled and that the program behaves as expected.

- **`passwords.txt`** (created at runtime)  
  Local plain-text storage of saved passwords in a simple `service: password` format.

- **`screenshots/`**  
  A folder containing example images of the application in use. They help readers quickly understand the look and feel of the project without running the code.

---

## Design Choices

- **Rich TUI**: Instead of plain text, the `rich` library provides colors, tables, and panels for a more modern CLI experience.  
- **File-based storage**: Simplicity and transparency; users can see and edit `passwords.txt` if needed. While not as secure as encrypted storage, it keeps the project beginner-friendly.  
- **Entropy estimation**: Implemented as a simple heuristic rather than mathematical entropy for clarity and speed. Future improvements aim at full entropy calculation.  
- **Clipboard integration**: Improves usability by letting users copy generated passwords directly.  
- **Splash screen**: Adds personality to the program and demonstrates external library usage.

---

## Testing

Testing is implemented using **pytest**.  
- The suite checks that generated passwords meet user specifications (length, symbols, numbers).  
- Validates that `is_strong` correctly classifies passwords.  
- Confirms entropy classification works as expected.  
- Ensures that clearing the password file (`clear_passwords`) empties it safely.  

These tests increase confidence in program correctness and make future refactoring safer.

---

## Future Work

Planned improvements (see `TODO.md`) include:  
- Switching from plain-text storage to **JSON** or encrypted formats.  
- Handling duplicates and malformed entries gracefully.  
- Adding search and update features for stored passwords.  
- Implementing **real entropy calculations** using logarithmic formulas.  
- Exporting data for integration with other password managers.  
- Improving visual consistency and giving users the option to skip the splash screen.

---

## Conclusion

PASMANNN is a playful yet practical password manager that demonstrates Python programming concepts, external library usage, file handling, and testing.  
It is fully functional in its current state but also leaves plenty of room for enhancement and learning. This project showcases both technical implementation and thoughtful design, blending usability, fun, and security awareness.
