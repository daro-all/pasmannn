import random
import string
import re
import pyperclip
import time
import cowsay
from rich.console import Console, Group
from rich.table import Table
from rich.prompt import Prompt
from rich.prompt import IntPrompt
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

__version__ = "1.0.0"

console = Console()

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?" # NOTE: empty character not included.
MIN_LENGTH = 6
MAX_LENGTH = 64
STRONG_MIN_LENGTH = 8
PASSWORD_FILE = "passwords.txt"


def main():
    while True:
        show_menu()
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5", "6", "7"])
        #Iterates until a valid option is selected. The ':'s are added automatically.
        #Prompt returns a pre-trimmed string.
        #If there are 'choices' or a default response, they are displayed to the user between [] or ().
        console.print()

        if choice == "1":
            passwords = get_passwords()

            console.print("\n[bold yellow]Generated Password(s):[/bold yellow]")
            for i, pw in enumerate(passwords, start=1):
                console.print(f"🔑 {i}. {pw} | 💪 Strong? {'✅' if is_strong(pw) else '❌'} | ⏳ Entropy: {entropy(pw)}")
            console.print()

            service = Prompt.ask("Enter service name to save (or press Enter to skip)", default="", show_default=False)
            if service:
                #We give the user the option to choose which password they want to save from among those generated.
                pw_count = len(passwords)
                if pw_count > 1:
                    idx = IntPrompt.ask(f"Which password do you want to save? (1-{pw_count})", default=1)
                    chosen = passwords[idx - 1]
                else:
                    chosen = passwords[0]

                save_password(service, chosen)
                console.print("[green]Password saved![/green]")

            console.print()
            if Prompt.ask("Copy first password to clipboard? (y/n)", default="n", case_sensitive=False).lower() == "y":
                if copy_to_clipboard(passwords[0]):
                    console.print("[blue]Password copied to clipboard![/blue]")

            wait_for_enter()

        elif choice == "2":
            pw = Prompt.ask("Enter password to check")
            console.print(f"💪 Strong? {'✅' if is_strong(pw) else '❌'} | ⏳ Entropy: {entropy(pw)}")

            wait_for_enter()

        elif choice == "3":
            saved = list_passwords()
            if saved is not None: #The file is valid (although it may be empty).
                if not saved: #Empty file.
                    console.print("[red]No saved passwords found.[/red]")
                else:
                    console.clear()
                    table = Table(title="\n💾 Saved Passwords")
                    table.add_column("Service", style="cyan")
                    # table.add_column("Password", style="magenta")
                    table.add_column("Password", style="bright_cyan")
                    for service, pw in saved.items():
                        table.add_row(service, pw)

                    console.print(table)

            wait_for_enter()

        elif choice == "4":
            service = Prompt.ask("Enter service to delete")
            delete_password(service)

            wait_for_enter()

        elif choice == "5":
            clear_passwords()
            wait_for_enter()

        elif choice == "6":
            show_help()
            wait_for_enter()

        elif choice == "7":
            console.print("[bold green]Goodbye! 👋\n[/bold green]")
            break


def splash_screen():
    console.clear()

    title = Text(f"Welcome to PASMANNN v{__version__} 😎🔐", style="bold magenta", justify="center")
    subtitle = Text("(a Password Generator & Manager)", style="italic cyan", justify="center")

    phrase = "It's time to use better passwords!\n...\nNa na na na na na na na Pasmannn !!!"
    animalsay = Text(cowsay.get_output_string("tux", phrase), style="yellow")

    content = Group(title, "\n", subtitle, "\n", animalsay)
    centered = Align.center(content)
    panel = Panel(centered, border_style="bright_blue", padding=(1, 4), width=100)

    console.print(panel)
    time.sleep(5)


def show_menu():
    """Display the main menu with available options."""
    console.clear()
    table = Table(title="\n🗝️ PASMANNN (Password Manager) 🗝️")
    table.add_column("Option", style="cyan", no_wrap=True)
    # table.add_column("Description", style="magenta")
    table.add_column("Description", style="bright_cyan")

    table.add_row("1", "Generate a password")
    table.add_row("2", "Check password strength")
    table.add_row("3", "List saved passwords")
    table.add_row("4", "Delete a password")
    table.add_row("5", "Clear password file")
    table.add_row("6", "Help")
    table.add_row("7", "Exit")

    console.print(table)


def get_passwords():
    """Handle user input for password generation parameters and return a list of generated passwords."""
    while True:
        try:
            length = IntPrompt.ask(f"Enter password length (between {MIN_LENGTH} and {MAX_LENGTH}, Enter for default)", default=STRONG_MIN_LENGTH)
            if length == STRONG_MIN_LENGTH:
                console.print(f"Using default length = {STRONG_MIN_LENGTH}")
                break
            else:
                if length < MIN_LENGTH or length > MAX_LENGTH:
                    raise ValueError
                else:
                    break

        # If user enters letters, IntPrompt handles it; if they enter an integer out of the allowed range, it enters here.
        except ValueError:
            console.print("[red]❗ Invalid input.[/red]")

    use_symbols = Prompt.ask("Include symbols?", choices=['y', 'n'], default='y', case_sensitive=False) == 'y'
    use_numbers = Prompt.ask("Include numbers?", choices=['y', 'n'], default='y', case_sensitive=False) == 'y'

    while True:
        try:
            count = IntPrompt.ask("How many passwords to generate? (max = 5)", default=1)
            if count < 1 or count > 5:
                raise ValueError
            break
        except ValueError:
            console.print("[red]❗ Invalid input.[/red]")

    passwords = [generate_password(length, use_symbols, use_numbers) for _ in range(count)]
    return passwords


def generate_password(length=STRONG_MIN_LENGTH, use_symbols=True, use_numbers=True):
    """
    Generate a random password with given options.
    The function ensures that there is at least one special character of those requested by the user.
    """
    base_chars = list(string.ascii_letters)  # A list is created with this initial content.
    # string.ascii_letters is a constant with this value: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    required = []

    if use_numbers:
        base_chars.extend(string.digits) # Another constant, containing digits 0-9
        required.append(random.choice(string.digits))
    if use_symbols:
        base_chars.extend(SYMBOLS)
        required.append(random.choice(SYMBOLS))

    remaining_length = length - len(required)
    password = required + random.choices(base_chars, k=remaining_length)

    # Shuffle to avoid required characters being at the beginning.
    random.shuffle(password)

    return "".join(password)


def analyze_password(password):
    """
    This function analyzes the composition of a given password and returns a dictionary indicating whether it contains specific character types.
    Each result is returned as a Boolean value.
    """
    return {
        "has_uppercase": bool(re.search(r"[A-Z]", password)),
        "has_lowercase": bool(re.search(r"[a-z]", password)),
        "has_number": bool(re.search(r"\d", password)),
        "has_symbol": bool(re.search(rf"[{re.escape(SYMBOLS)}]", password))
        # re.escape(SYMBOLS): escapes all special characters so they are not interpreted as regex commands.
    }


def is_strong(password):
    """
    Check if a password is strong:
    - At least STRONG_MIN_LENGTH characters (8 in general)
    - Includes numbers, symbols, uppercase OR lowercase (or maybe both)
    """
    if len(password) < STRONG_MIN_LENGTH:
        return False

    analysis = analyze_password(password)
    return analysis["has_number"] and analysis["has_symbol"] and (analysis["has_uppercase"] or analysis["has_lowercase"])


def entropy(password):
    """
    Password entropy measures how hard it is to guess or crack the password.
    This function estimate the strength of the password by its length and diversity of characters.
    Returns a simple classification: Weak, Medium, Strong, Very strong
    """
    length_pw = len(password)
    analysis = analyze_password(password)
    diversity_score = sum(analysis.values())

    if length_pw < 8 or diversity_score < 2:
        return "Weak 🔴"
    elif length_pw < 12 or diversity_score < 3:
        return "Medium 🟡"
    elif length_pw < 16 or diversity_score < 4:
        return "Strong 🟢"
    else:
        return "Very strong 🔵"


def save_password(service, password, filename=PASSWORD_FILE):
    """Save a password for a specific service into a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{service}: {password}\n")


def list_passwords(filename=PASSWORD_FILE):
    """Read and return all saved passwords from the storage file."""
    passwords = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if ": " in line:
                    service, pw = line.split(": ", 1) # maxsplit=1 for safety
                    passwords[service] = pw
                # else: skip malformed lines
        return passwords
    except FileNotFoundError:
        console.print("[red]File not found.[/red]")
        return None
    # except ValueError:
    #     console.print("[red]File corrupted.[/red]")
    #     return None


def copy_to_clipboard(password):
    """Copy the given password to the clipboard."""
    try:
        pyperclip.copy(password)
        return True #Serves to confirm that the function did its job.
    except Exception as e:
        console.print("[red]⚠️ Copy to clipboard failed[/red]")
        # console.print("[red]⚠️ Copy to clipboard failed[/red]", e)
        return False


def delete_password(service, filename=PASSWORD_FILE):
    """Delete a specific password by service name."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        found = False
        pattern = re.compile(rf"^{re.escape(service)}:\s.*$")

        with open(filename, "w", encoding="utf-8") as f:
            for line in lines:
                if pattern.match(line.strip()):
                    found = True
                else:
                    f.write(line)

        if found:
            console.print(f"\n[green]Password for '{service}' deleted.[/green]")
            return True
        else:
            console.print(f"\n[yellow]No password found for service: {service}[/yellow]")
            return False
    except FileNotFoundError:
        console.print("\n[red]Password file not found.[/red]")
        return False


def clear_passwords(filename=PASSWORD_FILE):
    """Delete all stored passwords by clearing the file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("")
        console.print("[green]All passwords cleared.[/green]")
        return True
    except Exception as e:
        console.print(f"[red]Error while clearing passwords: {e}[/red]")
        return False


def show_help():
    """Display help file content using rich."""
    try:
        console.clear()
        with open("HELP.md", "r", encoding="utf-8") as f:
            content = f.read()
        console.print("[bold cyan]\n📖 Help Guide[/bold cyan]\n")
        console.print(content, style="white")
    except FileNotFoundError:
        console.print("[red]HELP.md not found.[/red]")


def wait_for_enter():
    Prompt.ask("\nPress Enter to return to menu...", default="", show_default=False)


if __name__ == "__main__":
    splash_screen()
    main()
