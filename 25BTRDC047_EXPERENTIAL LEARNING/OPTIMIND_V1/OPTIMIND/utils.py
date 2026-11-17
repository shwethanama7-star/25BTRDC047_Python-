from rich.prompt import Prompt

def format_bytes(value):
    value = float(value)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024 or unit == "TB":
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} TB"

def pause():
    Prompt.ask("\n[dim]Press Enter to return to the menu[/dim]", default="")
