# TODO / Pending Improvements

## Password Manager Enhancements

- [ ] Handle passwords that include `: ` or `:` which may cause issues when reading the file.
- [ ] Use **JSON** instead of plain text for storing credentials.
- [ ] Improve handling of corrupted files or malformed entries.
- [ ] Detect common passwords (e.g., `123456`, `password`, `qwerty`, etc.) using a small dictionary.
- [ ] Calculate real mathematical entropy (log₂ of possible combinations).
- [ ] Implement password search by service name.
- [ ] Add ability to update an existing password for a given service.
- [ ] Export data to **CSV** or **JSON** for integration with other password managers.
- [ ] Hide passwords when listing: show only service names and reveal the password only if the user requests it.
- [ ] Prevent duplicate services or, if so, allow the option to delete only the first match or all matches when deleting.
- [ ] If the password file does not exist, avoid creating it automatically in `clear` mode? Instead warn the user?
- [ ] Handle potential errors that may occur when saving a password to the file.
- [ ] When generating more than one password and trying to copy it to the clipboard, provide the option to choose which one.
- [ ] Improve visual issues.
- [ ] Allow the user to skip the splashscreen.
