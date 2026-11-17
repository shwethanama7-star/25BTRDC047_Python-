from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich import box
from rich.text import Text
from monitoring.system_monitor import get_system_snapshot, get_top_processes
from storage.scanner import scan_temp_files, find_large_files
from storage.cleaner import clean_selected
from agent.decision_engine import build_recommendations
from database.history import init_db, add_event, get_events
from utils import format_bytes, pause

console = Console()

def header():
    console.clear()
    console.print(Panel.fit(
        "[bold bright_green]OPTIMIND[/bold bright_green]\n"
        "[dim]LOCAL PC RESOURCE MANAGEMENT AGENT • V1.0[/dim]",
        border_style="bright_green"
    ))

def dashboard():
    data = get_system_snapshot()
    table = Table(title="LIVE SYSTEM OVERVIEW", box=box.ROUNDED)
    table.add_column("RESOURCE", style="cyan")
    table.add_column("USAGE", justify="right")
    table.add_column("DETAILS")
    table.add_row("CPU", f"{data['cpu']:.1f}%", "Current overall utilization")
    table.add_row("RAM", f"{data['ram_percent']:.1f}%",
                  f"{format_bytes(data['ram_used'])} used / {format_bytes(data['ram_total'])}")
    table.add_row("Disk", f"{data['disk_percent']:.1f}%",
                  f"{format_bytes(data['disk_used'])} used / {format_bytes(data['disk_total'])}")
    console.print(table)
    console.print("[dim]Health indicators are guidance, not a benchmark of PC speed.[/dim]")

def ram_analysis():
    console.print(Panel("[bold]RAM PROCESS ANALYSIS[/bold]", border_style="cyan"))
    procs = get_top_processes(15)
    table = Table(box=box.SIMPLE_HEAVY)
    table.add_column("PID", justify="right")
    table.add_column("PROCESS", style="cyan")
    table.add_column("MEMORY", justify="right")
    table.add_column("STATUS")
    for p in procs:
        table.add_row(str(p["pid"]), p["name"][:32],
                      format_bytes(p["memory"]), p["status"])
    console.print(table)
    console.print("[yellow]Note:[/yellow] High memory use does not automatically mean a process is safe to close.")
    if Confirm.ask("Would you like to review a process to terminate?", default=False):
        try:
            pid = int(Prompt.ask("Enter the PID shown above"))
            target = next((p for p in procs if p["pid"] == pid), None)
            if not target:
                console.print("[red]That PID is not in the displayed list. Run the scan again.[/red]")
                return
            console.print(f"Selected: [bold]{target['name']}[/bold] (PID {pid})")
            console.print("[yellow]Save your work in that application first.[/yellow]")
            if Confirm.ask("Request termination of this process?", default=False):
                import psutil
                proc = psutil.Process(pid)
                proc.terminate()
                try:
                    proc.wait(timeout=3)
                except psutil.TimeoutExpired:
                    console.print("[yellow]Process did not exit promptly. No forced kill was attempted.[/yellow]")
                add_event("PROCESS_TERMINATE_REQUEST", f"{target['name']} PID={pid}")
                console.print("[green]Termination request sent.[/green]")
        except (ValueError, PermissionError, ProcessLookupError) as exc:
            console.print(f"[red]Could not complete request: {exc}[/red]")
        except Exception as exc:
            console.print(f"[red]Unexpected error: {exc}[/red]")

def storage_analysis():
    console.print(Panel("[bold]STORAGE ANALYSIS[/bold]", border_style="cyan"))
    temp_items, total = scan_temp_files()
    console.print(f"Temporary files found: [bold]{len(temp_items)}[/bold]")
    console.print(f"Estimated reclaimable size: [bold green]{format_bytes(total)}[/bold green]")
    if temp_items:
        table = Table(box=box.SIMPLE)
        table.add_column("#", justify="right")
        table.add_column("FILE")
        table.add_column("SIZE", justify="right")
        for i, item in enumerate(temp_items[:20], 1):
            table.add_row(str(i), str(item["path"])[:75], format_bytes(item["size"]))
        console.print(table)
        if len(temp_items) > 20:
            console.print(f"[dim]Showing 20 of {len(temp_items)} discovered files.[/dim]")
    console.print("\n[bold]Largest files (selected user folders)[/bold]")
    large = find_large_files(limit=10)
    if large:
        t = Table(box=box.SIMPLE)
        t.add_column("FILE")
        t.add_column("SIZE", justify="right")
        for item in large:
            t.add_row(str(item["path"])[:85], format_bytes(item["size"]))
        console.print(t)
    else:
        console.print("[dim]No large files found in the scanned folders, or folders were inaccessible.[/dim]")
    if temp_items and Confirm.ask("Review and clean discovered temporary files?", default=False):
        chosen = temp_items[:]
        if Confirm.ask(f"Clean all {len(chosen)} discovered temporary files?", default=False):
            deleted, reclaimed = clean_selected(chosen)
            add_event("TEMP_CLEAN", f"Deleted {deleted} files; reclaimed {format_bytes(reclaimed)}")
            console.print(f"[green]Cleaned {deleted} files. Approximate reclaimed size: {format_bytes(reclaimed)}[/green]")

def recommendations():
    data = get_system_snapshot()
    recs = build_recommendations(data)
    console.print(Panel("[bold]OPTIMIND AGENT ANALYSIS[/bold]", border_style="bright_green"))
    console.print(f"RAM: [bold]{data['ram_percent']:.1f}%[/bold] | CPU: [bold]{data['cpu']:.1f}%[/bold] | Disk: [bold]{data['disk_percent']:.1f}%[/bold]")
    for level, title, detail in recs:
        color = {"HIGH": "red", "MEDIUM": "yellow", "INFO": "cyan"}.get(level, "white")
        console.print(f"[{color}][{level}][/{color}] [bold]{title}[/bold]\n  {detail}")
    add_event("AGENT_ANALYSIS", f"{len(recs)} recommendations generated")

def history():
    rows = get_events()
    table = Table(title="LOCAL OPTIMIZATION HISTORY", box=box.ROUNDED)
    table.add_column("TIME", style="dim")
    table.add_column("EVENT", style="cyan")
    table.add_column("DETAIL")
    for row in rows:
        table.add_row(row[0], row[1], row[2])
    if not rows:
        console.print("[dim]No activity recorded yet.[/dim]")
    else:
        console.print(table)

def main():
    init_db()
    while True:
        header()
        console.print("[bold]MAIN MENU[/bold]")
        console.print(" [cyan]1[/cyan]  System dashboard")
        console.print(" [cyan]2[/cyan]  Smart RAM analysis")
        console.print(" [cyan]3[/cyan]  Storage analysis")
        console.print(" [cyan]4[/cyan]  Agent recommendations")
        console.print(" [cyan]5[/cyan]  Optimization history")
        console.print(" [cyan]0[/cyan]  Exit")
        choice = Prompt.ask("\n[bright_green]optmind@local[/bright_green]", choices=["1","2","3","4","5","0"])
        console.clear()
        try:
            if choice == "1": dashboard()
            elif choice == "2": ram_analysis()
            elif choice == "3": storage_analysis()
            elif choice == "4": recommendations()
            elif choice == "5": history()
            elif choice == "0":
                console.print("[green]OPTIMIND closed. Your PC remains under your control.[/green]")
                break
        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled by user.[/yellow]")
        except Exception as exc:
            console.print(f"[red]An error occurred: {exc}[/red]")
        if choice != "0":
            pause()

if __name__ == "__main__":
    main()
