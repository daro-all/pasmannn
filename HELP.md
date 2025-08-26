# PASMANNN (Password Generator & Manager) - Help
*Version 1.0.0*

This program allows you to **generate**, **check**, **store**, and **manage** passwords locally.

---

## Features

- Generate strong passwords with customizable length, numbers, and symbols.
- Check password strength and entropy.
- Save passwords associated with services in a text file.
- List saved passwords in a table.
- Delete individual service passwords.
- Clear the entire password file.
- Copy a generated password to the clipboard.

---

## Menu Options

- **1) Generate a password**
  Create one or more random passwords. You can choose length, whether to include symbols and numbers, and optionally save one of them.

- **2) Check password strength**
  Enter a password to analyze its strength and entropy.

- **3) List saved passwords**
  Displays all saved services and their passwords in a table.

- **4) Delete a password**
  Remove a saved password for a specific service.

- **5) Clear password file**
  Permanently deletes all saved passwords.

- **6) Help**
  Show this help guide.

- **7) Exit**
  Close the program.

---

## Notes

- Passwords are stored locally in a plain text file (`passwords.txt`).
- If the file does not exist, it will be created automatically.
- Weak passwords such as `123456`, `password`, or `qwerty` are not recommended.
- The program estimates entropy but does not yet calculate mathematical entropy (`log₂` of combinations).

---
